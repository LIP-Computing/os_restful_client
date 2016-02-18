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
import os

auth_variables = ['OS_AUTH_URL',
                  'OS_TOKEN',
                  'OS_PORT',
                  "OS_VERSION"
                 ]
messages = { "empty": "No data found",
            "error": "There was an error"
          }
elements_to_delete = ["links","parent_id"]
elements_width = {'projects':{'domain_id':35,'name':20, 'id':35,'description':35}}


def get_table_headers(resource, json_data):
    default_width = 10
    headers_out = {}
    headers = json_data[0].keys()
    for del_it in elements_to_delete:
        if del_it in headers:
            headers.remove(del_it)
    for h in headers:
        # f_with = str(json_data[0][h]).__len__()
        # if f_with < h.__len__():
        #     f_with = h.__len__()
        # headers_out[h] = f_with + min_width
        if h in elements_width['projects']:
            headers_out[h] = elements_width[resource][h]
        else:
            headers_out[h] = default_width
    return headers_out


# def get_table_rows(headers, json_data):
#     fields = []
#     for row in json_data:
#         fields_row = dict()
#         for key,value in headers.iteritems():
#             if key in row:
#                 fields_row.update({str(row[key]), value})
#         fields.append(fields_row)
#     return fields

def print_table(resource, json_data):
    try:
        headers_info = get_table_headers(resource, json_data)
        #rows = get_table_rows(headers_info, json_data)

        table_width = sum(headers_info.values())
        print '{:-^{width}}'.format(' Results ',width=table_width)
        for h,w in headers_info.iteritems():
            print '{:<{width}} |'.format(h, width=w),
        print
        print '{:-^{width}}'.format('',width=table_width)

        for row in json_data:
            for h,w in headers_info.iteritems():
                print '{:<{width}} |'.format(row[h], width=w),
            print
        # for row in rows:
        #     for field, width in row.iteritems():
        #         print '{0:{width}}'.format(field, width=width),
        #     print
        print '{:-^{width}}'.format('',width=table_width)
    except:
        print messages["empty"]


def check_identity_variables():
    for var in auth_variables:
        if not os.getenv(var, None):
            return False
    return True


def get_identity_variables():
    var_list = {}
    for var in auth_variables:
        val = os.getenv(var)
        var_list[var]= val
    return var_list


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
        raise click.BadParameter("Format specified is %s. Choices: -cf json|yaml" % ctx.params['content_format'])
