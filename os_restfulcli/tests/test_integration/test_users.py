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

import testtools

from os_restfulcli.client import cli
from os_restfulcli.client.controller import ControllerResource
from os_restfulcli.tests.test_integration import configure_env
from os_restfulcli.driver import parsers
import os_restfulcli.tests


class TestIntegrationProjectCommand(os_restfulcli.tests.TestCaseCommandLine):

    def setUp(self):
        super(TestIntegrationProjectCommand, self).setUp()
        self.user_id = "89c3bc64dd4e4436a67342383fd07d4e"
        self.project_id = "484d3a7eeb4f4462b329c1d0463cf324"
        configure_env(self.project_id)

    def test_user_list(self):
        result = self.runner.invoke(cli.users, ['list'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)


    def test_user_show(self):
        result = self.runner.invoke(cli.users, ['show', 'admin'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)


    def test_user_create_delete(self):
        result = self.runner.invoke(cli.users, ['create', '--attributes={"name":"name53"}'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)
        #delete
        #id = str(result.output_bytes).strip().split("\n")[2].split("|")[5].strip()
        ids = parsers.json_load_from_client(result.output_bytes)
        for id in ids:
            result_delete = self.runner.invoke(cli.users, ['delete', '--user_name=%s' % id])
            self.assertEqual(result_delete.exit_code,0)
            self.assertIsNone(result_delete.exception)

    def test_user_create_delete_bunch(self):
        result = self.runner.invoke(cli.users, ['create', '--file=../user_json_file_example.json'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)
        #delete
        ids = parsers.json_load_from_client(result.output_bytes)
        # var = "[{u'project': {u'description': u'', u'links': {u'self': u'http://localhost/v3/projects/e2b42b2aa5d5444f833b94d973571b63'}, u'enabled': True, u'id': u'e2b42b2aa5d5444f833b94d973571b63', u'parent_id': None, u'domain_id': u'default', u'name': u'name3'}}]"
        # result_dict = parsers.json_load_from_os_string(var)
        for id in ids:
            result_delete = self.runner.invoke(cli.users, ['delete', '--user_name=%s' % id])
            self.assertEqual(result_delete.exit_code,0)
            self.assertIsNone(result_delete.exception)


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