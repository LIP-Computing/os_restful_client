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

import mock
import testtools

from os_restfulcli.client.controller import Controller
from os_restfulcli.driver.openstack import OpenStackDriver


class TestCaseAPIController(testtools.TestCase):

    def setUp(self):
        super(TestCaseAPIController, self).setUp()
        os.environ.data['OS_AUTH_URL'] = '127.0.0.23'
        os.environ.data['OS_PORT'] = '5000'
        os.environ.data['OS_VERSION'] = 'v3'
        os.environ.data['OS_TOKEN'] = 'token'
        self.controller = Controller(mock.MagicMock())

    @mock.patch.object(OpenStackDriver, "index")
    def test_index(self, m_index):
        result = self.controller.index(None)
        self.assertIsNotNone(result)

    @mock.patch.object(OpenStackDriver, "create")
    def test_create(self, m_create):
        result = self.controller.create(None)
        self.assertIsNotNone(result)

    @mock.patch.object(OpenStackDriver, "delete")
    def test_create(self, m_create):
        parameters =[{'id':'78934'}]
        result = self.controller.delete(parameters)
        self.assertIsNotNone(result)