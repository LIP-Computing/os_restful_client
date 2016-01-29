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
import sys

from os_restfulcli.api.controller import Controller
from os_restfulcli.client import client_utils

sys.tracebacklimit=0

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
    project_controller = Controller('projects')
    result = project_controller.index() # todo(jorgesece): parse result to json
    click.echo(result)


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
    project_controller = Controller('projects')
    resulting_message = "CREATED PROJECTS:\n ["
    if file:
        parameters = file
    elif attributes:
        parameters = [attributes]
    else:
        # click.get_current_context.get_help()
        raise click.BadArgumentUsage('You need to specify either --attributes or --file')
    try:
        result = project_controller.create(parameters=parameters)
    except Exception as e:
        raise click.ClickException(e.message)
    for item in result:
        resulting_message = '%s%s\n' % (resulting_message, item)
    resulting_message = '%s]' % resulting_message
    click.echo(resulting_message)


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
    project_controller = Controller('projects')
    if file:
        parameters = file
    elif id:
        parameters = [{"id":id}]
    else:
        raise click.BadArgumentUsage('You need to specify either --id or --file')

    try:
        result = project_controller.delete(parameters=parameters)
    except Exception as e:
        raise click.ClickException(e.message)
    click.echo(result)


@openstackcli.group()
def user():
    """Manages users."""


@user.command('create')
@click.argument('name')
@click.option('--description', '-d', help='Description of the user.')
def user_create(name,description):
    """Creates a new ship."""
    click.echo('NOT IMPLEMENTED. Created user %s' % name)


@user.command('createBunch')
@click.argument('file')
def user_create(file):
    """Creates a new ship."""
    click.echo('NOT IMPLEMENTED. Created user from a JSON file %s' % file)

