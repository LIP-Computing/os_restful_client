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
        try:
            path = "/%s/%s" % (self.resource, id)
            result = self.os_helper.show(path)
        except TypeError:
            result = parsers.parse_controller_err("Undefined", "Bad attribute definition for OS")
        except Exception as e:
            result = parsers.parsers.parse_controller_err(id, e.message)
        return [result[self.resource[:-1]]]

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
                result = parsers.parse_controller_delete("ok", param['id'], result)
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
        self.control = ControllerResource(resource)

    def index(self):
        result = self.control.index()
        return result

    def show(self, id):
        parameters = {"id":id}
        result = self.control.show(parameters=parameters)
        return result

    def create(self, attributes, file, format ):
        if file:
            parameters = file
        elif attributes:
            parameters = [attributes]
        else:
            # click.get_current_context.get_help()
            raise TypeError('You need to specify either --attributes or --file')
        result = self.control.create(parameters)
        return result

    def delete(self, id, file, format):
        if file:
            parameters = file
        elif id:
            parameters = [{"id":id}]
        else:
            raise TypeError('You need to specify either --id or --file')
        result = self.control.delete(parameters=parameters)

        return result