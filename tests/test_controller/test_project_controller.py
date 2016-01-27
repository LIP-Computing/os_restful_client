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
import mock # todo(jorgesece): add to de testing requirements.

from driver.openstack import OpenStackDriver
from api.projects import Controller


class TestCaseAPIController(testtools.TestCase):

    def setUp(self):
        super(TestCaseAPIController, self).setUp()
        self.controller = Controller(mock.MagicMock())

    @mock.patch.object(OpenStackDriver, "index")
    def test_index(self, m_index):
        result = self.controller.index(None)
        self.assertIsNotNone(result)

    @mock.patch.object(OpenStackDriver, "create")
    def test_create(self, m_create):
        result = self.controller.create(None)
        self.assertIsNotNone(result)