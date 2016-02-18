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

from os_restfulcli.client import client_utils
from os_restfulcli.exceptions import ControllerException


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
        r = self.os_helper.index(path, parameters) # todo(jorgesece): parse out, code...

        return r[self.resource]

    def create(self, parameters):
        """Create a network instance in the cloud
        :param parameters: array of projects (containg their paramemters)
        """
        path = '/%s' % self.resource
        created = []
        for param in parameters:
            if 'name' not in param:
                raise ParseException(400, "Bad attribute definition for OS")
            try:
                result = self.os_helper.create(path, param) # todo(jorgesece): parse out, code...
            except Exception as e:
                result = '{"Error":{"name":"%s", "details": "%s"}}' % (param['name'], e.message)
            created.append(result)

        return created

    # def show(self,  id, parameters=None):
    #     """Get network details
    #     :param req: request object
    #     :param id: network identification
    #     :param parameters: request parameters
    #     """
    #     resp = self.os_helper.get_network(req, id)
    #     occi_network_resources = self._get_network_resources([resp])
    #     return occi_network_resources[0]
    #
    def delete(self, parameters):
        """delete networks which satisfy the parameters
        :param parameters:
        """
        deleted = []
        for param in parameters:
            try:
                path = "/%s/%s" % (self.resource, param['id'])
                result = self.os_helper.delete(path)
                result = {'status': 'OK', 'id':param['id'], 'description': result}
            except TypeError:
                result = '{"status": "Error", "description": "Bad attribute definition for OS"}'
            except Exception as e:
                result = '{"status": "Error", "id":"%s", "description": "%s"}' % (param['id'], e.message)
            deleted.append(result)
        return deleted


class ControllerClient(object):

    def __init__(self, resource):
        self.control = ControllerResource(resource)

    def index(self):
        result = self.control.index()
        return result

    def create(self, attributes, file, format ):
        resulting_message = "CREATED:\n ["
        if file:
            parameters = file
        elif attributes:
            parameters = [attributes]
        else:
            # click.get_current_context.get_help()
            raise TypeError('You need to specify either --attributes or --file')

        result = self.control.create(parameters)
        for item in result:
            resulting_message = '%s%s\n' % (resulting_message, item)
        resulting_message = '%s]' % resulting_message
        return resulting_message

    def delete(self, id, file, format):
        resulting_message = "DELETED:\n ["
        if file:
            parameters = file
        elif id:
            parameters = [{"id":id}]
        else:
            raise TypeError('You need to specify either --id or --file')

        result = self.control.delete(parameters=parameters)
        for item in result:
            resulting_message = '%s%s\n' % (resulting_message, item)
        resulting_message = '%s]' % resulting_message

        return resulting_message