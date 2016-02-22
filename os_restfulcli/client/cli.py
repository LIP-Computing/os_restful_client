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

import sys

import click

from os_restfulcli.client import client_utils
from os_restfulcli.client.controller import ControllerResource
from os_restfulcli.client.controller import ControllerClient

#sys.tracebacklimit=0

@click.group()
@click.version_option()
def openstackcli():
    """Openstack restful client which directly uses the REST ful api of OS.
    """
    pass


@openstackcli.group()
def project():
    """Manages users."""



@project.command('list')
def project_list():
    resource = 'projects'
    project_controller = ControllerResource(resource)
    result = project_controller.index() # todo(jorgesece): parse result to json
    client_utils.print_table(resource, result)


@project.command('create', help="Select either --attributes or --file input")
@click.option('--attributes', '-a', default=None, type=click.STRING
              , callback=client_utils.validate_attributes
              , help='Project attributes: {"name":"name_project", "description":"description project",...}')
@click.option('--file', '-f', default=None, type=click.File('r')
              , help='File with list of projects attributes'
              , callback=client_utils.validate_file_attributes)
@click.option('--content_format', '-cf',  default='json'
              , help='Format file.' , is_eager =True
              , type=click.Choice(['json', 'yaml']))
def project_create(attributes, file, content_format):
    """Creates a new project."""
    try:
        resource = 'projects'
        client_controller = ControllerClient(resource)
        result, errors = client_controller.create(attributes, file, content_format)
    except TypeError as e:
        raise click.BadArgumentUsage(e.message)
    except Exception as e:
            raise click.ClickException(e.message)
    client_utils.print_table(resource, result)
    client_utils.print_table(resource, errors, 'FAIL')


@project.command('delete',help="Select either --id or --file input")
@click.option('--id', '-i', default=None
              , type = click.STRING
              , help='Identification of project')
@click.option('--file', '-f', default=None,
              help='File with list of projects ids. [{"id"="xx"},{"id"="xx2"}..]',
              type=click.File('r')
              , callback=client_utils.validate_file_attributes)
@click.option('--content_format', '-cf',  default='json'
              , help='Format file.', is_eager=True
              , type=click.Choice(['json', 'yaml']))
def project_delete(id, file, content_format):
    """Delelete."""
    try:
        resource = 'projects'
        client_controller = ControllerClient(resource)
        result,errors = client_controller.delete(id, file, content_format)
    except TypeError as e:
        raise click.BadArgumentUsage(e.message)
    except Exception as e:
        raise click.ClickException(e.message)
    client_utils.print_table(resource, result)
    client_utils.print_table(resource, errors, 'FAIL')


@openstackcli.group()
def users():
    """Manages users."""

@users.command('list')
def project_list():
    project_controller = ControllerResource('users')
    result = project_controller.index()
    click.echo(result)

@users.command('create', help="Select either --attributes or --file input")
@click.option('--attributes', '-a', default=None, type=click.STRING
              , callback=client_utils.validate_attributes
              , help='Project attributes: {"name":"name_project", "description":"description project",...}')
@click.option('--file', '-f', default=None, type=click.File('r')
              , help='File with list of projects attributes'
              , callback=client_utils.validate_file_attributes)
@click.option('--content_format', '-cf',  default='json'
              , help='Format file.' , is_eager =True
              , type=click.Choice(['json', 'yaml']))
def users_create(attributes, file, content_format):
    """Creates a new project."""
    try:
        client_controller = ControllerClient('users')
        result = client_controller.create(attributes, file, content_format)
    except TypeError as e:
        raise click.BadArgumentUsage(e.message)
    except Exception as e:
            raise click.ClickException(e.message)
    click.echo(result)


@users.command('delete',help="Select either --id or --file input")
@click.option('--id', '-i', default=None
              , type = click.STRING
              , help='Identification of project')
@click.option('--file', '-f', default=None,
              help='File with list of projects ids. [{"id"="xx"},{"id"="xx2"}..]',
              type=click.File('r')
              , callback=client_utils.validate_file_attributes)
@click.option('--content_format', '-cf',  default='json'
              , help='Format file.', is_eager=True
              , type=click.Choice(['json', 'yaml']))
def users_delete(id, file, content_format):
    """Delelete."""
    try:
        client_controller = ControllerClient('users')
        result = client_controller.delete(id, file, content_format)
    except TypeError as e:
        raise click.BadArgumentUsage(e.message)
    except Exception as e:
        raise click.ClickException(e.message)
    click.echo(result)

