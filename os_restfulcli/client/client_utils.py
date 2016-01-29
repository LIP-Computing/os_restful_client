# -*- coding: utf-8 -*-

# Copyright 2015 Spanish National Research Council
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

import click
import json
import yaml

def validate_attributes(ctx, param, value):
    if not value:
        return value
    try:
        dic_value = json.loads(value)
        return dic_value
    except ValueError:
        raise click.BadParameter('{"name":"name_project", "description":"description project",...}')

def validate_file_attributes(ctx, param, value):
    if not value:
        return value
    try:
        if ctx.params['content_format'] == 'json':
            return json.load(value)
        else:
            return yaml.load(value)

    except ValueError:
        raise click.BadParameter("Innvalid file format")