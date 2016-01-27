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
from client import cli
from api import projects
from credentials.session import KeySession

import tests


class TestCommandProject(tests.TestCaseCommandLine):# todo(jorgesece): create as mock

    def setUp(self):
        super(TestCommandProject, self).setUp()
        # project_id = "484d3a7eeb4f4462b329c1d0463cf324"
        # app = KeySession().create_keystone("admin", "stack1", project_id)
        # token = app.auth_token # fixme(jorgesece): check what to do with auth ¿password or token?

    def test_no_exist(self):
        result = self.runner.invoke(cli.project, ['Noexist'])
        self.assertEqual(result.exit_code,2)
        self.assertIsNotNone(result.exception)

    #@mock.patch.object(api.projects,"create") todo(jorgesece): follow this way to make mock
    def test_project(self):
        result = self.runner.invoke(cli.project)
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    @mock.patch.object(projects.Controller, "index")
    def test_project_list(self, m_index):
        result = self.runner.invoke(cli.project, ['list'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    @mock.patch.object(projects.Controller, "create")
    def test_project_create(self, m_create):
        result = self.runner.invoke(cli.project, ['create','name1'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    def test_project_create_error_arg(self):
        result = self.runner.invoke(cli.project, ['create','name1','erroArg'])
        self.assertEqual(result.exit_code,2)
        self.assertIsNotNone(result.exception)

    def test_project_create_optional_arg(self):
        result = self.runner.invoke(cli.project, ['create','name','--description=description'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    def test_project_create_bunch(self):
        result = self.runner.invoke(cli.project, ['createBunch','file'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)


class TestCommandUser(tests.TestCaseCommandLine):# todo(create as mock)

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
        result = self.runner.invoke(cli.user, ['create','name1'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    def test_user_create_error_arg(self):
        result = self.runner.invoke(cli.user, ['create','name1','erroArg'])
        self.assertEqual(result.exit_code,2)
        self.assertIsNotNone(result.exception)

    def test_user_create_optional_arg(self):
        result = self.runner.invoke(cli.user, ['create','name','--description=description'])
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)

    def test_user_create_bunch(self):
        result = self.runner.invoke(cli.user, ['createBunch','file'])
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
