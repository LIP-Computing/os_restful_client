# -*- coding: utf-8 -*-

# Copyright 2015 Spanish National Research Council
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

from keystoneclient import session
from keystoneclient.v2_0 import client
import webob

from keystoneclient.auth.identity import v3





class KeySession(object):

    def __init__(self, auth_url = 'http://localhost:5000/v2.0'):
        self.auth_url = auth_url

    def create_session(self, user, password, project):
        auth = v3.Password(auth_url=self.auth_url,
                           username=user,
                           password=password,
                           project_id=project)
        return session.Session(auth=auth)

    def create_keystone(self, user, password, project):
        #sess = self.create_session(user, password, project)

        #
        keystone = client.Client(auth_url=self.auth_url,
                                 username=user,
                                 password=password,
                                 project_id=project)

        return keystone.auth_ref # token in keystone.auth_ref.auth_token

    def create_request_conection1(self,user,password,project_id, path="/"):

        app = self.create_keystone(user,password,project_id)  #"dev", "passwd", "6271876e5bea4935a98cf10840f8dcb6")
        environ = {"HTTP_X_PROJECT_ID": project_id, "HTTP_X-Auth-Token": app.auth_token} #"4cf9e807516c450fa98f320f4a9f431a
        kwargs = {}
        kwargs["http_version"] = "HTTP/1.1"
        kwargs["server_name"] = "127.0.0.1"
        kwargs["server_port"] = "9696"

        return webob.Request.blank(path=path, environ=environ, base_url="/v2.0", **kwargs)

    def create_request_conection(self,user,password,project_id, path="/"):
        app = self.create_keystone(user,password,project_id)  #"dev", "passwd", "6271876e5bea4935a98cf10840f8dcb6")
        environ = {"HTTP_X_PROJECT_ID": project_id}

        return self.create_request(app, path=path, environ=environ)

    def create_request(self, app, path="/", environ={}, headers=None, **kwargs):
        environ ["HTTP_X-Auth-Token"]= app.auth_token #"4cf9e807516c450fa98f320f4a9f431a
        kwargs["http_version"] = "HTTP/1.1"
        kwargs["server_name"] = "127.0.0.1"
        kwargs["server_port"] = "9696"

        return webob.Request.blank(path=path, environ=environ, base_url="/v2.0", headers=headers, **kwargs)