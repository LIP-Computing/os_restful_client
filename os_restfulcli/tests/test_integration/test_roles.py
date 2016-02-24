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
from os_restfulcli.driver import parsers
from os_restfulcli.tests.test_integration import configure_env

import os_restfulcli.tests


class TestIntegrationRolesommand(os_restfulcli.tests.TestCaseCommandLine):

    def setUp(self):
        super(TestIntegrationRolesommand, self).setUp()
        self.user_id = "3a8b1c4387664d9488dee661df025b80"
        self.project_id = "484d3a7eeb4f4462b329c1d0463cf324"
        self.anotherrole = "e80fa7ab6cfa45d39be195878350853d"
        configure_env(self.project_id)

    def test_roles_list(self):
        result = self.runner.invoke(cli.grant_roles, ['list', self.project_id, self.user_id])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    def test_roles_link_unlink(self):
        result = self.runner.invoke(cli.grant_roles, ['create', self.project_id, self.user_id, self.anotherrole])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)
        result = self.runner.invoke(cli.grant_roles, ['delete', self.project_id, self.user_id, self.anotherrole])
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
            result_delete = self.runner.invoke(cli.users, ['delete', '--id=%s' % id])
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
            result_delete = self.runner.invoke(cli.users, ['delete', '--id=%s' % id])
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