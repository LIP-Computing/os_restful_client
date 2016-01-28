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

import json

import six
import six.moves.urllib.parse as urlparse
import yaml

from os_restfulcli.driver.exception import ParseException


def utf8(value):
    """Try to turn a string into utf-8 if possible.

    Code is modified from the utf8 function in
    http://github.com/facebook/tornado/blob/master/tornado/escape.py

    """
    if isinstance(value, six.text_type):
        return value.encode('utf-8')
    assert isinstance(value, str)
    return value


def join_url(base, parts):
    """Join several parts into a url.

    :param base: the base url
    :parts: parts to join into the url
    """
    url = base
    if not isinstance(parts, (list, tuple)):
        parts = [parts]

    for p in parts:
        if p.startswith("/"):
            # We won't get an absolute url
            p = p[1:]
        url = urlparse.urljoin(url, p)
    return url


def get_resource_from_path(str, delete_last):
    out = str.rsplit('/', 1)[-1]
    if delete_last:
        return out[:-1]
    return out


def parse_file(fp, content_format):
    # try:
    #     fp = open(file, 'r')
    # except:
    #     raise Exception("File not found or corrupt")
    try:
        if content_format == 'json':
            str = json.load(fp)
        elif content_format == 'yaml':
            str = yaml.load(fp)
        else:
    #        fp.close()
            raise Exception("Invalid format")
    except Exception as e:
        raise ParseException(400, "Invalid format")
    return str

#'--attributes={name=name1,definition="una definition"'
def parse_attributes(str):
    try:
        out = json.loads(str.replace("{", "{\"").replace("}", "}").replace(":", "\":").replace(",", ",\""))
    except Exception as e:
        raise ParseException(code=400,message="Invalid format")
    return [out]

