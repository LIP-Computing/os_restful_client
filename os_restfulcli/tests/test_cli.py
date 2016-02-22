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
import mock

import os_restfulcli.tests
from os_restfulcli.client import cli, controller


class TestCommandProject(os_restfulcli.tests.TestCaseCommandLine):

    def setUp(self):
        super(TestCommandProject, self).setUp()

    def test_no_exist(self):
        result = self.runner.invoke(cli.projects, ['Noexist'])
        self.assertEqual(result.exit_code,2)
        self.assertIsNotNone(result.exception)

    def test_project(self):
        result = self.runner.invoke(cli.projects)
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "index")
    def test_project_list(self, m_new, m_index):
        result = self.runner.invoke(cli.projects, ['list'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    @mock.patch.object(controller.ControllerClient, "__new__")
    @mock.patch.object(controller.ControllerClient, "show")
    def test_project_show(self, m_new, m_show):
        result = self.runner.invoke(cli.projects, ['show'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)


    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "create")
    def test_project_create_no_param(self, m_new, m_create):
        result = self.runner.invoke(cli.projects, ['create'])
        self.assertEqual(result.exit_code, 2)
        self.assertIsNotNone(result.exception)

    @mock.patch.object(controller.ControllerClient, "__new__")
    @mock.patch.object(controller.ControllerClient, "create")
    def test_project_create(self, m_create, m_new):
        m_new.return_value.create.return_value = (2,3)
        result = self.runner.invoke(cli.projects, ['create', '--attributes={"name":"name1","definition":"una definition"}'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "create")
    def test_project_create_error_arg(self, m_create, m_new):
        m_new.return_value.create.return_value = (2,3)
        result = self.runner.invoke(cli.projects, ['create', '--attributes={"name":"name1"}', 'erroArg'])
        self.assertEqual(result.exit_code,2)
        self.assertIsNotNone(result.exception)

    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "create")
    def test_project_create_bunch_error_file(self, m_new, m_create):
        result = self.runner.invoke(cli.projects, ['create', '--file=file_does_not_exist'])
        self.assertEqual(result.exit_code, 2)
        self.assertIsNotNone(result.exception)
        self.assertEqual(result.exception.code, 2)
    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "create")
    def test_project_create_bunch_wrong_format(self, m_new, m_create):
        result = self.runner.invoke(cli.projects, ['create', '--file=yaml_file_example.yml', '--content_format=format_err'])
        self.assertEqual(result.exit_code, 2)
        self.assertIsNotNone(result.exception)

    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "create")
    def test_project_create_bunch_default_format(self, m_create, m_new):
        m_new.return_value.create.return_value = (2,3)
        result = self.runner.invoke(cli.projects, ['create', '--file=json_file_example.json'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "create")
    def test_project_create_bunch_truncate_format(self, m_create, m_new):
        m_new.return_value.create.return_value = (2,3)
        result = self.runner.invoke(cli.projects, ['create', '--file=yaml_file_example.yml', '--content_format=json'])
        self.assertEqual(result.exit_code, 2)
        self.assertIsNotNone(result.exception)


    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "create")
    def test_project_create_bunch_yaml_ok(self, m_create, m_new):
        m_new.return_value.create.return_value = (2,3)
        result = self.runner.invoke(cli.projects, ['create', '--file=yaml_file_example.yml', '--content_format=yaml'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "create")
    def test_project_create_bunch_json_ok(self, m_create, m_new):
        m_new.return_value.create.return_value = (2,3)
        result = self.runner.invoke(cli.projects, ['create', '--file=json_file_example.json', '--content_format=json'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "delete")
    def test_project_delete(self, m_delete, m_new):
        m_new.return_value.delete.return_value = (2,3)
        result = self.runner.invoke(cli.projects, ['delete', '--id=89434'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)
    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "delete")
    def test_project_delete_bunch(self, m_delete, m_new):
        m_new.return_value.delete.return_value = (2,3)
        result = self.runner.invoke(cli.projects, ['delete', '--file=json_file_example.json', '--content_format=json'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "delete")
    def test_project_delete_bunch(self, m_delete, m_new):
        m_new.return_value.delete.return_value = (2,3)
        result = self.runner.invoke(cli.projects, ['delete'])
        self.assertEqual(result.exit_code,2)
        self.assertIsNotNone(result.exception)



class TestCommandUser(os_restfulcli.tests.TestCaseCommandLine):# todo(create as mock)

    def setUp(self):
        super(TestCommandProject, self).setUp()

    def test_no_exist(self):
        result = self.runner.invoke(cli.users, ['Noexist'])
        self.assertEqual(result.exit_code,2)
        self.assertIsNotNone(result.exception)

    def test_project(self):
        result = self.runner.invoke(cli.users)
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "index")
    def test_project_list(self, m_new, m_index):
        result = self.runner.invoke(cli.users, ['list'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    @mock.patch.object(controller.ControllerClient, "__new__")
    @mock.patch.object(controller.ControllerClient, "show")
    def test_project_show(self, m_new, m_show):
        result = self.runner.invoke(cli.users, ['show'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)


    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "create")
    def test_project_create_no_param(self, m_new, m_create):
        result = self.runner.invoke(cli.users, ['create'])
        self.assertEqual(result.exit_code, 2)
        self.assertIsNotNone(result.exception)

    @mock.patch.object(controller.ControllerClient, "__new__")
    @mock.patch.object(controller.ControllerClient, "create")
    def test_project_create(self, m_create, m_new):
        m_new.return_value.create.return_value = (2,3)
        result = self.runner.invoke(cli.users, ['create', '--attributes={"name":"name1","definition":"una definition"}'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)


    # def test_cli_with_option(self):
    #     result = runner.invoke(cli.main, ['--as-cowboy'])
    #     assert not result.exception
    #     assert result.exit_code == 0
    #     assert result.output.strip() == 'Howdy, world.'
    #
    #
    # def test_cli_with_arg(self):
    #     result = runner.invoke(cli.main, ['Jorge'])
    #     assert result.exit_code == 0
    #     assert not result.exception
    #     assert result.output.strip() == 'Hello, Jorge.'
