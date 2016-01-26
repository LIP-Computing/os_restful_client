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
import mock

from click.testing import CliRunner
from client import cli


class TestCaseCommandLine(testtools.TestCase):# todo(create as mock)
    runner = None

    def setUp(self):
        super(TestCaseCommandLine, self).setUp()
        self.runner = CliRunner()

    def test_openstack(self):
        result = self.runner.invoke(cli.openstack)
        self.assertEqual(result.exit_code,0)
        self.assertIsNone(result.exception)