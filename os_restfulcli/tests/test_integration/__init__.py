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

import os
from os_restfulcli.tests.credentials.session import KeySession

def configure_env(project_id):
    token = "XX"
    app = KeySession().create_keystone("admin", "stack1", project_id)
    token = app.auth_token # fixme(jorgesece): check what to do with auth ¿password or token?
    os.environ.data['OS_AUTH_URL'] = '127.0.0.23'
    os.environ.data['OS_PORT'] = '5000'
    os.environ.data['OS_VERSION'] = 'v3'
    os.environ.data['OS_TOKEN'] = token