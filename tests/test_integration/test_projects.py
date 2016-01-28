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
import testtools
import os

from client import cli
from api.controller import Controller
from credentials.session import KeySession
import tests
from driver import parsers


def configure_env(project_id):
    app = KeySession().create_keystone("admin", "stack1", project_id)
    token = app.auth_token # fixme(jorgesece): check what to do with auth ¿password or token?
    os.environ.data['OS_AUTH_URL'] = '127.0.0.23'
    os.environ.data['OS_PORT'] = '5000'
    os.environ.data['OS_VERSION'] = 'v3'
    os.environ.data['OS_TOKEN'] = token


class TestIntegrationProjectCommand(tests.TestCaseCommandLine):

    def setUp(self):
        super(TestIntegrationProjectCommand, self).setUp()
        self.project_id = "484d3a7eeb4f4462b329c1d0463cf324"
        configure_env(self.project_id)

    def test_project_list(self):
        result = self.runner.invoke(cli.project, ['list'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    def test_project_create_delete(self):
        result = self.runner.invoke(cli.project, ['create','--name=name1'])
        #json.loads(result.output_bytes.replace ("u\'", "\"").replace ("\'", "\"").replace("True","\"True\"").replace("None","\"None\""))[0]['project']['id']
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)
        #delete
        result_dict = parsers.json_load_from_client(result.output_bytes)
        # var = "[{u'project': {u'description': u'', u'links': {u'self': u'http://localhost/v3/projects/e2b42b2aa5d5444f833b94d973571b63'}, u'enabled': True, u'id': u'e2b42b2aa5d5444f833b94d973571b63', u'parent_id': None, u'domain_id': u'default', u'name': u'name3'}}]"
        # result_dict = parsers.json_load_from_os_string(var)
        for item in result_dict:
            id = item['project']['id']
            result_delete = self.runner.invoke(cli.project, ['delete','--id=%s' % id])
            self.assertEqual(result_delete.exit_code,0)
            self.assertIsNone(result_delete.exception)

    def test_project_create_delete_bunch(self):
        result = self.runner.invoke(cli.project, ['create','--file=../json_file_example.json'])
        #json.loads(result.output_bytes.replace ("u\'", "\"").replace ("\'", "\"").replace("True","\"True\"").replace("None","\"None\""))[0]['project']['id']
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)
        #delete
        #
        #var = "CREATED PROJECTS: \n {u'project': {u'description': u'description lip 1', u'links': {u'self': u'http://localhost/v3/projects/7bf753af62454620bb71aa939c4c4d04'}, u'enabled': True, u'id': u'7bf753af62454620bb71aa939c4c4d04', u'parent_id': None, u'domain_id': u'default', u'name': u'lipjson1'}} \n {u'project': {u'description': u'description lip 1', u'links': {u'self': u'http://localhost/v3/projects/f86ae5fdc3fb427ca31c493282ae1dc8'}, u'enabled': True, u'id': u'f86ae5fdc3fb427ca31c493282ae1dc8', u'parent_id': None, u'domain_id': u'default', u'name': u'lipjson2'}}"

        result_dict = parsers.json_load_from_client(result.output_bytes)
        # var = "[{u'project': {u'description': u'', u'links': {u'self': u'http://localhost/v3/projects/e2b42b2aa5d5444f833b94d973571b63'}, u'enabled': True, u'id': u'e2b42b2aa5d5444f833b94d973571b63', u'parent_id': None, u'domain_id': u'default', u'name': u'name3'}}]"
        # result_dict = parsers.json_load_from_os_string(var)
        for item in result_dict:
            id = item['project']['id']
            result_delete = self.runner.invoke(cli.project, ['delete','--id=%s' % id])
            self.assertEqual(result_delete.exit_code,0)
            self.assertIsNone(result_delete.exception)

    # def test_project_create_bunch_yaml_ok(self, m_create):
    #     result = self.runner.invoke(cli.project, ['createBunch','yaml_file_example.yml','--content_format=yaml'])
    #     self.assertEqual(result.exit_code,0)
    #     self.assertIsNone(result.exception)
    #
    #
    # def test_project_create_bunch_json_ok(self, m_create):
    #     result = self.runner.invoke(cli.project, ['createBunch','json_file_example.json','--content_format=json'])
    #     self.assertEqual(result.exit_code,0)
    #    self.assertIsNone(result.exception)

class TestIntegrationProjectController(testtools.TestCase):

    def setUp(self):
        super(TestIntegrationProjectController, self).setUp()
        self.project_id = "484d3a7eeb4f4462b329c1d0463cf324"
        configure_env(self.project_id)
        self.controller = Controller('projects')

    def test_index(self):
        result = self.controller.index()
        self.assertIsNotNone(result)

    # def test_show(self):
    #     result = self.controller.index()
    #     self.assertIsNotNone(result)

    def test_create_delete(self):
        list1 = self.controller.index()
        parameter = [{'name':'project_test4', 'description':' integration project test'}]
        result = self.controller.create(parameter)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(result.__len__(), parameter.__len__())
        list2 = self.controller.index()
        self.assertEqual(list1['projects'].__len__() + parameter.__len__(), list2['projects'].__len__())
        #delete
        self.controller.delete([{'id':result[0]['project']['id']}])
        list3 = self.controller.index()
        self.assertEqual(list1['projects'].__len__(), list3['projects'].__len__())

    def test_bunch_create_delete(self):
        list1 = self.controller.index()
        parameter = [{'name':'project_test111', 'description':' integration project test 1'},
                     {'name':'project_test222', 'description':' integration project test 2'}
                     ]
        result = self.controller.create(parameter)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(result.__len__(), parameter.__len__())
        list2 = self.controller.index()
        self.assertEqual(list1['projects'].__len__() + parameter.__len__(), list2['projects'].__len__())
        #delete
        param_delete = []
        for item in result:
            param_delete.append({'id':item['project']['id']})
        self.controller.delete(param_delete)
        list3 = self.controller.index()
        self.assertEqual(list1['projects'].__len__(), list3['projects'].__len__())

# class TestIntegrationNetwork(base.TestController):
#
#     def setUp(self):
#         super(TestIntegrationNetwork, self).setUp()
#         self.controller = network.Controller(None, "/v2.0", "127.0.0.1")
#         self.project_id = "86bf9730b23d4817b431f4c34cc9cc8e"
#         self.public_network = "cd58eade-79a1-4633-8fb7-c7d8a030c942"
#         self.new_network_name = "networkOCCINET"
#         self.req = KeySession().create_request_conection("admin", "stack1", self.project_id)
#
#     def test_list(self):
#         list = self.controller.index(self.req, None)
#         self.assertIsInstance(list.resources[0], network_extend.Network)
#         sortedList = sorted(list.resources, key=lambda Network: Network.title, reverse=True)
#         self.assertEqual("public", sortedList[0].title)
#
#     def test_list_by_tenant(self):
#         tenant_id = self.req.environ["HTTP_X_PROJECT_ID"]
#         list = self.controller.index(self.req, {"attributes": {"project": self.project_id}})
#         sortedList = sorted(list.resources, key=lambda Network: Network.title, reverse=True)
#         self.assertIsInstance(sortedList[0], network_extend.Network)
#         self.assertEqual("public", sortedList[0].title)
#
#     def test_list_by_tenant_error(self):
#         list = self.controller.index(self.req, {"attributes": {"project": "noexits"}})
#         self.assertIs(0, list.resources.__len__())
#
#     def test_show_network(self):
#         net = self.controller.show(self.req, self.public_network)
#         self.assertEqual("public", net.title)
#
#     def test_run_up_network(self):
#         body = None
#         out = None
#         try:
#             net = self.controller.run_action(self.req,self.public_network,body)
#         except Exception as e:
#             out = e
#         self.assertIsInstance(out, exception.NotFound)
#
#     def test_create_delete_network(self):
#         list1 = self.controller.index(self.req, None)
#         #Create
#         net = self.controller.create(self.req, {"attributes": {"occi.core.title": self.new_network_name,"project": self.project_id}})
#         self.assertEqual(self.new_network_name, net.title)
#         list2 = self.controller.index(self.req, None)
#         self.assertEqual(list1.resources.__len__() + 1, list2.resources.__len__())
#
#         # Delete
#         response = self.controller.delete(self.req, {"attributes":{"occi.core.id": net.id}})
#         self.assertIsInstance(response, list)
#         list3 = self.controller.index(self.req, None)
#         self.assertEqual(list1.resources.__len__(), list3.resources.__len__())
#
#     def test_create_delete_network_with_subnet(self):
#         list1 = self.controller.index(self.req, None)
#         ip_version = 4
#         cidr = "11.0.0.1/24"
#         gateway = "11.0.0.3"
#         #Create
#         param = {
#                 "attributes":
#                             {"occi.core.title": self.new_network_name,
#                              "occi.network.ip_version": ip_version,
#                              "occi.networkinterface.address": cidr,
#                              "occi.networkinterface.gateway": gateway,
#                              "project": self.project_id
#                              }
#                 }
#         net = self.controller.create(self.req, param)
#         self.assertEqual(self.new_network_name, net.title)
#         list2 = self.controller.index(self.req, None)
#         self.assertEqual(list1.resources.__len__() + 1, list2.resources.__len__())
#
#          # Delete
#         response = self.controller.delete(self.req, {"attributes":{"occi.core.id": net.id}})
#         self.assertIsInstance(response, list)
#         list3 = self.controller.index(self.req, None)
#         self.assertEqual(list1.resources.__len__(), list3.resources.__len__())
#
#
# """
#     def test_delete_network(self):
#         response = self.controller.delete(self.req, self.new_network_id)
#
#         self.assertEqual(204, response.status_code)
# """