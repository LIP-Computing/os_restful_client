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
from tabulate import tabulate

auth_variables = ['OS_AUTH_URL',
                  'OS_TOKEN',
                  'OS_PORT',
                  "OS_VERSION"
                 ]
messages = { "empty": "No data found",
            "error": "There was an error"
          }
elements_to_delete = ["links","parent_id","id"]
elements_width = {'projects':{'domain_id':35,'name':20, 'id':35,'description':35}}

colors = { 'FAIL' : '\033[91m',
           'OK': '\033[92m',
           'WARNING': '\033[93m',
           'ENDC': '\033[0m'
         }



def get_table_headers(resource, json_data):
    default_width = 15
    headers_out = {}
    headers = json_data[0].keys()
    headers.sort(reverse=True)
    out_header = ["id"]
    for h in headers:
        if h not in elements_to_delete:
            out_header.append(h)
    # for del_it in elements_to_delete:
    #     if del_it not in headers:
    #         headers.remove(del_it)
    # for h in headers:
    #     # f_with = str(json_data[0][h]).__len__()
    #     # if f_with < h.__len__():
    #     #     f_with = h.__len__()
    #     # headers_out[h] = f_with + min_width
    #     if h in elements_width['projects']:
    #         headers_out[h] = elements_width[resource][h]
    #     else:
    #         headers_out[h] = default_width

    return out_header



def get_table_rows(headers, json_data):
    fields = []
    for row in json_data:
        fields_row = []
        for key in headers:
            if key in row:
                fields_row.append(str(row[key]))
        fields.append(fields_row)
    return fields




def print_table(resource, json_data, err=False):
    try:
        if err:
            message = colors['FAIL'] + ' ERROR ' + colors['ENDC']
        else:
            message = colors['OK'] + ' RESULTS ' + colors['ENDC']
        if json_data:
            print
            print '{:-^{width}}'.format(message,width=60)
            headers = get_table_headers(resource, json_data)
            rows = get_table_rows(headers,json_data)
            print tabulate(rows, headers=headers, tablefmt="orgtbl")
            print
    except:
        print messages["empty"]


def print_json(data, err =False):
    message = {}
    try:
        if data:
            print
            if err:
                print colors['FAIL']
                message['ERROR'] = data
            else:
                message['RESULTS'] = data
            print '{:<}'.format(json.dumps(message))
            print colors['ENDC']
    except:
        print "{EMPTY}"


def print_data(resource, data, format, type = False):
    if format == 'table':
        print_table(resource, data, type)
    else:
        print_json(data, type)


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
        raise click.BadParameter('\'{"name":"name_resource", "description":"description sentence",...}\' ')


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

###################################
######### UNUSED #################


def print_table1(resource, json_data, err=False):
    try:
        if err:
            message = colors['FAIL'] + ' ERROR ' + colors['ENDC']
        else:
            message = colors['OK'] + ' RESULTS ' + colors['ENDC']
        if json_data:
            headers_info = get_table_headers(resource, json_data)
            table_width = sum(headers_info.values())
            print
            print
            print '{:-^{width}}'.format(message,width=table_width + 10)
            for h,w in headers_info.iteritems():
                print '| {:<{width}}'.format(h, width=w),
            print '|'
            print '{:-^{width}}'.format('',width=table_width)

            for row in json_data:
                for h,w in headers_info.iteritems():
                    print '| {:<{width}}'.format(row[h], width=w),
                print'|'
            print '{:-^{width}}'.format('',width=table_width)

            # if json_errors:
            #     print '{:-^{width}}'.format(colors['FAIL'] + ' ERRORS ',width=80)
            #     for row in json_errors:
            #         for field in row.keys():
            #             print '{:<{width}} |'.format(row[field], width=40),
            #         print
            #     print '{:-^{width}}'.format('',width=table_width)
    except:
        print messages["empty"]


#
# def get_table_rows(headers, json_data):
#     fields = []
#     for row in json_data:
#         fields_row = dict()
#         for key,value in headers.iteritems():
#             if key in row:
#                 fields_row.update({str(row[key]), value})
#         fields.append(fields_row)
#     return fields