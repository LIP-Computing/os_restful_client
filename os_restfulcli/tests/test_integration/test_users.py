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


import os

import testtools

from os_restfulcli.client.controller import ControllerResource
from os_restfulcli.tests.credentials.session import KeySession


def configure_env(project_id):
    app = KeySession().create_keystone("admin", "stack1", project_id)
    token = app.auth_token # fixme(jorgesece): check what to do with auth ¿password or token?
    os.environ.data['OS_AUTH_URL'] = '127.0.0.23'
    os.environ.data['OS_PORT'] = '5000'
    os.environ.data['OS_VERSION'] = 'v3'
    os.environ.data['OS_TOKEN'] = token

class TestIntegrationUserController(testtools.TestCase):

    def setUp(self):
        super(TestIntegrationUserController, self).setUp()
        self.project_id = "484d3a7eeb4f4462b329c1d0463cf324"
        configure_env(self.project_id)
        self.controller = ControllerResource('projects')

    def test_index(self):
        result = self.controller.index()
        self.assertIsNotNone(result)

    # def test_show(self):
    #     result = self.controller.index()
    #     self.assertIsNotNone(result)

    def test_create_delete(self):
        list1 = self.controller.index()
        parameter = [{'name':'user_integration_11', 'email':'user1@integration1.es'}]
        result = self.controller.create(parameter)
        self.assertIsNotNone(result)
        self.assertIsNotNone(result[0])
        result_OK = result[0]
        self.assertIsInstance(result_OK, list)
        self.assertEqual(result_OK.__len__(), parameter.__len__())
        list2 = self.controller.index()
        self.assertEqual(list1.__len__() + parameter.__len__(), list2.__len__())
        #delete
        self.controller.delete([{'id':result_OK[0]['id']}])
        list3 = self.controller.index()
        self.assertEqual(list1.__len__(), list3.__len__())

    def test_bunch_create_delete(self):
        list1 = self.controller.index()
        parameter = [{'name':'user_integration_1', 'email':'user1@integration.es'},
                     {'name':'user_integration_2', 'email':'user2@integration.es'}
                     ]
        result = self.controller.create(parameter)
        self.assertIsNotNone(result)
        self.assertIsNotNone(result[0])
        result_OK = result[0]
        self.assertIsInstance(result_OK, list)
        self.assertEqual(result_OK.__len__(), parameter.__len__())
        list2 = self.controller.index()
        self.assertEqual(list1.__len__() + parameter.__len__(), list2.__len__())
        #delete
        param_delete = []
        for item in result_OK:
            param_delete.append({'id':item['id']})
        self.controller.delete(param_delete)
        list3 = self.controller.index()
        self.assertEqual(list1.__len__(), list3.__len__())

    def test_bunch_create_wrong_id(self):
        wrong_id= [{"id":"8903489034890234"}]
        result = self.controller.delete(wrong_id)
        self.assertIsNotNone(result)