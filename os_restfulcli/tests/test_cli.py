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
        result = self.runner.invoke(cli.project, ['Noexist'])
        self.assertEqual(result.exit_code,2)
        self.assertIsNotNone(result.exception)

    def test_project(self):
        result = self.runner.invoke(cli.project)
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "index")
    def test_project_list(self, m_new, m_index):
        result = self.runner.invoke(cli.project, ['list'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "create")
    def test_project_create_no_param(self, m_new, m_create):
        result = self.runner.invoke(cli.project, ['create'])
        self.assertEqual(result.exit_code, 2)
        self.assertIsNotNone(result.exception)

    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "create")
    def test_project_create(self, m_new, m_create):
        result = self.runner.invoke(cli.project, ['create', '--attributes={"name":"name1","definition":"una definition"}'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "create")
    def test_project_create_error_arg(self, m_new, m_create):
        result = self.runner.invoke(cli.project, ['create', '--attributes={"name":"name1"}', 'erroArg'])
        self.assertEqual(result.exit_code,2)
        self.assertIsNotNone(result.exception)

    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "create")
    def test_project_create_bunch_error_file(self, m_new, m_create):
        result = self.runner.invoke(cli.project, ['create', '--file=file_does_not_exist'])
        self.assertEqual(result.exit_code, 2)
        self.assertIsNotNone(result.exception)
        self.assertEqual(result.exception.code, 2)
    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "create")
    def test_project_create_bunch_wrong_format(self, m_new, m_create):
        result = self.runner.invoke(cli.project, ['create', '--file=yaml_file_example.yml', '--content_format=format_err'])
        self.assertEqual(result.exit_code, 2)
        self.assertIsNotNone(result.exception)

    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "create")
    def test_project_create_bunch_default_format(self, m_new, m_create):
        result = self.runner.invoke(cli.project, ['create', '--file=json_file_example.json'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "create")
    def test_project_create_bunch_truncate_format(self, m_new, m_create):
        result = self.runner.invoke(cli.project, ['create', '--file=yaml_file_example.yml', '--content_format=json'])
        self.assertEqual(result.exit_code, 2)
        self.assertIsNotNone(result.exception)


    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "create")
    def test_project_create_bunch_yaml_ok(self, m_new, m_create):
        result = self.runner.invoke(cli.project, ['create', '--file=yaml_file_example.yml', '--content_format=yaml'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "create")
    def test_project_create_bunch_json_ok(self, m_new, m_create):
        result = self.runner.invoke(cli.project, ['create', '--file=json_file_example.json', '--content_format=json'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "delete")
    def test_project_delete(self, m_new, m_delete):
        result = self.runner.invoke(cli.project, ['delete', '--id=89434'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)
    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "delete")
    def test_project_delete_bunch(self, m_new, m_delete):
        result = self.runner.invoke(cli.project, ['delete', '--file=json_file_example.json', '--content_format=json'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    @mock.patch.object(controller.ControllerResource, "__new__")
    @mock.patch.object(controller.ControllerResource, "delete")
    def test_project_delete_bunch(self, m_new, m_delete):
        result = self.runner.invoke(cli.project, ['delete'])
        self.assertEqual(result.exit_code,2)
        self.assertIsNotNone(result.exception)



class TestCommandUser(os_restfulcli.tests.TestCaseCommandLine):# todo(create as mock)

    def setUp(self):
        super(TestCommandUser, self).setUp()

    def test_no_exist(self):
        result = self.runner.invoke(cli.user, ['Noexist'])
        self.assertEqual(result.exit_code,2)
        self.assertIsNotNone(result.exception)

    def test_user(self):
        result = self.runner.invoke(cli.user)
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    def test_user_create(self):
        result = self.runner.invoke(cli.user, ['create', 'name1'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    def test_user_create_error_arg(self):
        result = self.runner.invoke(cli.user, ['create', 'name1', 'erroArg'])
        self.assertEqual(result.exit_code,2)
        self.assertIsNotNone(result.exception)

    def test_user_create_optional_arg(self):
        result = self.runner.invoke(cli.user, ['create', 'name', '--description=description'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    def test_user_create_bunch(self):
        result = self.runner.invoke(cli.user, ['createBunch', 'file'])
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
