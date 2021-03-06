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
#
import json
import webob

from os_restfulcli import exceptions
from os_restfulcli.driver import parsers


class OpenStackDriver(object):
    """Class to interact with the OS API."""

    def __init__(self, endpoint, token=None):
        self.endpoint = endpoint
        #self.version = version
        #self.port = port
        self.token = token

    @staticmethod
    def get_from_response(response, default):
        if response.status_int in [200, 201, 202]:
            exceptions.logger.debug('HTTP response: %s', response.status_int)
            return response.json_body #.get(element, default)
        elif response.status_int in [204]:
            return "Non Content"
        else:
            raise exceptions.exception_from_response(response)

    def _get_req(self, path, method,
                 content_type="application/json",
                 body=None,
                 query_string=""):
        """Return a new Request object to interact with OpenStack.

        This method will create a new request starting with the same WSGI
        environment as the original request, prepared to interact with
        OpenStack. Namely, it will override the script name to match the
        OpenStack version. It will also override the path, content_type and
        body of the request, if any of those keyword arguments are passed.

        :param path: new path for the request
        :param content_type: new content type for the request, defaults to
                             "application/json" if not specified
        :param body: new body for the request
        :param query_string: query string for the request, defaults to an empty
                             query if not specified
        :returns: a Request object
        """
        server = self.endpoint
        #port = self.port
        #base_url = "/%s" % self.version
        #kwargs = {"http_version": "HTTP/1.0", "server_name": server, "server_port": port}
        environ = {"HTTP_X-Auth-Token": self.token}

        new_req = webob.Request.blank(path=path, environ=environ,  base_url=server)#, **kwargs)
        #new_req.script_name = base_url
        new_req.query_string = query_string
        new_req.method = method
        if path is not None:
            new_req.path_info = path
        if content_type is not None:
            new_req.content_type = content_type
        if body is not None:
            new_req.body = parsers.utf8(body)


        return new_req

    def _make_get_request(self, path, parameters=None):
        """Create GET request
        This method create a GET Request instance
        :param path: path resource
        :param parameters: parameters to filter results
        """
        query_string = parsers.get_query_string(parameters)
        return self._get_req(path, query_string=query_string, method="GET")

    def _make_create_request(self, path, parameters):#TODO(jorgesece): Create unittest for it
        """Create CREATE request
        This method create a CREATE Request instance
        :param path: path resource
        :param parameters: parameters with values
        """
        resource = parsers.get_resource_from_path(path, True)
        body = parsers.make_body(resource, parameters)
        return self._get_req(path, content_type="application/json", body=json.dumps(body), method="POST")

    def _make_delete_request(self, path):
        """Create DELETE request
        This method create a DELETE Request instance
        :param req: the incoming request
        :param path: element location
        """
        return self._get_req(path, method="DELETE")

    def _make_put_request(self, path):
        """Create DELETE request
        This method create a DELETE Request instance
        :param req: the incoming request
        :param path: element location
        """
        return self._get_req(path, method="PUT")

    def index(self, path, parameters=None):
        """Get a list of networks.
        This method retrieve a list of network to which the tenant has access.
        :param req: the incoming request
        :param parameters: parameters to filter results
        """
        os_req = self._make_get_request(path, parameters)
        try:
            response = os_req.get_response(None)
        except Exception as e:
             response = webob.Response(status=500, body=str(e))
        json_response = self.get_from_response(response, {})
        return json_response

    def create(self, path, parameters):
        """Create a server.
        :param path: the incoming request
        :param parameters: parameters with values for the new resource
        """
        req = self._make_create_request(path, parameters)
        try:
            response = req.get_response(None)
        except Exception as e:
             response = webob.Response(status=500, body=str(e))
        json_response = self.get_from_response(response, {})
        return json_response

    def delete(self, path):
        """Delete network. It returns empty array
        :param path:
        """
        req = self._make_delete_request(path)
        try:
            response = req.get_response(None)
        except Exception as e:
             response = webob.Response(status=500, body=str(e))
        json_response = self.get_from_response(response, {})
        return json_response

    def show(self, path, parameters=None):
        """Get info from a resource. It returns json code from the server
        :param path: the incoming request
        :param parameters: parameters with values to filter
        """
        req = self._make_get_request(path, parameters)
        try:
            response = req.get_response(None)
        except Exception as e:
             response = webob.Response(status=500, body=str(e))
        json_response = self.get_from_response(response, {})
        return json_response

    def put(self, path):
        """Create a server.
        :param path: the incoming request
        """
        req = self._make_put_request(path)
        try:
            response = req.get_response(None)
        except Exception as e:
             response = webob.Response(status=500, body=str(e))
        json_response = self.get_from_response(response, {})
        return json_response

    #
    # def get_subnet(self, req, id):
    #     """Get information from a subnet.
    #     :param req: the incoming request
    #     :param id: subnet identification
    #     """
    #     path = "/subnets/%s" % id
    #     req = self._make_get_request(req, path)
    #     response = req.get_response(self.app)
    #
    #     return self.get_from_response(response, "subnet", {})
    #
    # def create_network(self, req, parameters):
    #     """Create a server.
    #     :param req: the incoming request
    #     :param parameters: parameters with values for the new network
    #     """
    #     req = self._make_create_request(req, "network", parameters)
    #     response = req.get_response(self.app)
    #     json_response = self.get_from_response(response, "network", {})
    #     #subnetattributes
    #     if "occi.networkinterface.address" in parameters:#TODO(jorgesece): Create unittest for it
    #         parameters["network_id"] = json_response["id"]
    #         req_subnet= self._make_create_request(req, "subnet", parameters)
    #         response_subnet = req_subnet.get_response(self.app)
    #         json_response["subnet_info"] = self.get_from_response(response_subnet, "subnet", {})
    #
    #     return json_response
    #

    #
    # def run_action(self, req, action, id):
    #     """Run an action on a network.
    #     :param req: the incoming request
    #     :param action: the action to run
    #     :param server_id: server id to delete
    #     """
    #     os_req = self._make_action_reques(req, action, id)
    #     response = os_req.get_response(self.app)
    #     if response.status_int != 202:
    #         raise helpers.exception_from_response(response)
