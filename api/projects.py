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
import exceptions

import api
from driver.openstack import OpenStackDriver


class Controller(object):
    def __init__(self, *args, **kwargs):
        if api.check_identity_variables():
            self.identity = api.get_identity_variables()
        else:
           # print "Error OS variables"
           # raise
            # fixme(jorgesece): manage properly
            self.identity = {'OS_AUTH_URL':'127.0.0.23','OS_PORT': '5000', "OS_VERSION": 'v3','OS_TOKEN':'1a83b395ee334b768f22e0811c44cf1b'}
        self.os_helper = OpenStackDriver(self.identity['OS_AUTH_URL'], self.identity['OS_PORT'], self.identity["OS_VERSION"],self.identity['OS_TOKEN'])

    def index(self, parameters=None):
        """List networks filtered by parameters
        :param parameters: request parameters
        """
        path = '/projects'
        r = self.os_helper.index(path, parameters) # todo(jorgesece): parse out, code...

        return r

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
    # def create(self, req, parameters, body=None): # todo(jorgesece): manage several creation
    #     """Create a network instance in the cloud
    #     :param: req: request object
    #     :param parameters: request parameters with the new network attributes
    #     :param body: body request (not used)
    #     """
    #     # FIXME(jorgesece): Body is coming from OOI resource class and is not used
    #     attributes = self._filter_attributes(parameters)
    #     net = self.os_helper.create_network(req, attributes)
    #     occi_network_resources = self._get_network_resources([net])
    #
    #     return occi_network_resources[0]
    #
    # def delete(self, req, parameters): # todo(jorgesece): manage several deletion
    #     """delete networks which satisfy the parameters
    #     :param parameters:
    #     """
    #     attributes = self._filter_attributes(parameters)
    #     network_id = self.os_helper.delete_network(req, attributes)
    #
    #     return []
    #
    # def run_action(self, req, id, body, parameters = None):
    #     raise exception.NotFound()
