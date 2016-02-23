# -*- coding: utf-8 -*-

# Copyright 2015 LIP - Lisbon
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
import click


from os_restfulcli.exceptions import ParseException
from os_restfulcli.driver.openstack import OpenStackDriver

from os_restfulcli.client import client_utils, parsers


class ControllerResource(object):
    resource = None

    def __init__(self, resource):
        self.resource = resource
        if client_utils.check_identity_variables():
            self.identity = client_utils.get_identity_variables()
        else:
            raise ParseException(401
                                 , 'Environmet variables are need: OS_AUTH_URL=127.0.0.23,'
                                   ' OS_PORT=5000, OS_VERSION=v3, OS_TOKEN=948473890234890')

            #self.identity = {'OS_AUTH_URL':'127.0.0.23','OS_PORT': '5000', "OS_VERSION": 'v3','OS_TOKEN':'cb6ec577f8a340f7bf49812aada2cfde'}
        self.os_helper = OpenStackDriver(self.identity['OS_AUTH_URL'], self.identity['OS_PORT'], self.identity["OS_VERSION"],self.identity['OS_TOKEN'])

    def index(self, parameters=None):
        """List networks filtered by parameters
        :param parameters: request parameters
        """
        path = '/%s' % self.resource
        r = self.os_helper.index(path, parameters)

        return r[self.resource]

    def create(self, parameters):
        """Create a network instance in the cloud
        :param parameters: array of projects (containg their paramemters)
        """
        path = '/%s' % self.resource
        created = []
        error_creation = []
        for param in parameters:
            if 'name' not in param:
                raise ParseException(400, "Bad attribute definition for OS")
            try:
                result = self.os_helper.create(path, param)
                created.append(result[self.resource[:-1]])
            except Exception as e:
                result = parsers.parse_controller_err(param['name'], e.message)
                error_creation.append(result)
        return created, error_creation

    def show(self, id):
        """Get network details
        :param id: identificator
        """
        showed = []
        showed_err = []
        try:
            path = "/%s/%s" % (self.resource, id)
            result = self.os_helper.show(path)
            showed.append(result[self.resource[:-1]])
        except TypeError:
            result = parsers.parse_controller_err("Undefined", "Bad attribute definition for OS")
            showed_err.append(result)
        except Exception as e:
            result = parsers.parse_controller_err(id, e.message)
            showed_err.append(result)
        return showed, showed_err

    def delete(self, parameters):
        """delete networks which satisfy the parameters
        :param parameters:
        """
        deleted = []
        deleted_err = []
        for param in parameters:
            try:
                path = "/%s/%s" % (self.resource, param['id'])
                result = self.os_helper.delete(path)
                result = parsers.parse_controller_delete("statisfully deleted", param['id'], result)
                deleted.append(result)
            except TypeError:
                result = parsers.parse_controller_delete("ERROR", "Undefined", "Bad attribute definition for OS")
                deleted_err.append(result)
            except Exception as e:
                result = parsers.parse_controller_delete("ERROR",param['id'], e.message)
                deleted_err.append(result)
        return deleted, deleted_err


class ControllerClient(object):

    def __init__(self, resource):
        try:
            self.resource = resource
            self.control = ControllerResource(resource)
        except Exception as e:
            raise click.ClickException(e.message)

    def index(self, out_format):
        try:
            result = self.control.index()
            client_utils.print_data(self.resource, result, out_format)
        except Exception as e:
            raise click.ClickException(e.message)

    def show(self, id, out_format):
        try:
            result, errors = self.control.show(id)
            client_utils.print_data(self.resource, result, out_format)
            client_utils.print_data(self.resource, errors, out_format, 'FAIL')
        except TypeError as e:
            raise click.BadArgumentUsage(e.message)
        except Exception as e:
            raise click.ClickException(e.message)

    def create(self, attributes, file, out_format):
        try:
            if file:
                parameters = file
            elif attributes:
                parameters = [attributes]
            else:
                # click.get_current_context.get_help()
                raise TypeError('You need to specify either --attributes or --file')
            result, errors = self.control.create(parameters)
            client_utils.print_data(self.resource, result, out_format)
            client_utils.print_data(self.resource, errors, out_format, 'FAIL')
        except TypeError as e:
            raise click.BadArgumentUsage(e.message)
        except Exception as e:
                raise click.ClickException(e.message)

    def delete(self, id, file, out_format):
        try:
            if file:
                parameters = file
            elif id:
                parameters = [{"id":id}]
            else:
                raise TypeError('You need to specify either --id or --file')
            result, errors =  self.control.delete(parameters=parameters)
            client_utils.print_data(self.resource, result, out_format)
            client_utils.print_data(self.resource, errors, out_format, 'FAIL')
        except TypeError as e:
            raise click.BadArgumentUsage(e.message)
        except Exception as e:
            raise click.ClickException(e.message)