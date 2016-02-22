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
from os_restfulcli.client.controller import ControllerClient

sys.tracebacklimit=0


@click.group()
@click.version_option()
def openstackcli():
    """Openstack restful client which directly uses the REST ful api of OS.
    """
    pass


@openstackcli.group()
@click.pass_context
def projects(ctx):
    """Manages users."""
    resource = 'projects'
    ctx.obj = ControllerClient(resource)


@projects.command('list')
@click.pass_context
def projects_list(ctx):
    ctx.obj.index()


@projects.command('show',help="Select either --id")
@click.option('--id', '-i', default=None
              , type = click.STRING
              , help='Identification of project')
@click.pass_context
def projects_show(ctx, id):
    """Show."""
    ctx.obj.show(id)


@projects.command('create', help="Select either --attributes or --file input")
@click.option('--attributes', '-a', default=None, type=click.STRING
              , callback=client_utils.validate_attributes
              , help='Project attributes: {"name":"name_project", "description":"description project",...}')
@click.option('--file', '-f', default=None, type=click.File('r')
              , help='File with list of projects attributes'
              , callback=client_utils.validate_file_attributes)
@click.option('--content_format', '-cf',  default='json'
              , help='Format file.' , is_eager =True
              , type=click.Choice(['json', 'yaml']))
@click.pass_context
def projects_create(ctx, attributes, file, content_format):
    """Creates a new project."""
    ctx.obj.create(attributes, file, content_format)


@projects.command('delete',help="Select either --id or --file input")
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
@click.pass_context
def projects_delete(ctx, id, file, content_format):
    """Delete."""
    ctx.obj.delete(id, file, content_format)



@openstackcli.group()
@click.pass_context
def users(ctx):
    """Manages users."""
    resource = 'users'
    ctx.obj = ControllerClient(resource)


@users.command('list')
@click.pass_context
def users_list(ctx):
    ctx.obj.index()


@users.command('show',help="Select either --id")
@click.option('--id', '-i', default=None
              , type = click.STRING
              , help='Identification of project')
@click.pass_context
def users_show(ctx, id):
    """Show."""
    ctx.obj.show(id)


@users.command('create', help="Select either --attributes or --file input")
@click.option('--attributes', '-a', default=None, type=click.STRING
              , callback=client_utils.validate_attributes
              , help='Project attributes: {"name":"name_user", "description":"user description ",...}')
@click.option('--file', '-f', default=None, type=click.File('r')
              , help='File with list of projects attributes'
              , callback=client_utils.validate_file_attributes)
@click.option('--content_format', '-cf',  default='json'
              , help='Format file.' , is_eager =True
              , type=click.Choice(['json', 'yaml']))
@click.pass_context
def users_create(ctx, attributes, file, content_format):
    """Creates a new project."""
    ctx.obj.create(attributes, file, content_format)


@users.command('delete',help="Select either --id or --file input")
@click.option('--id', '-i', default=None
              , type = click.STRING
              , help='Identification of project')
@click.option('--file', '-f', default=None,
              help='File with list of useres ids. [{"id"="xx"},{"id"="xx2"}..]',
              type=click.File('r')
              , callback=client_utils.validate_file_attributes)
@click.option('--content_format', '-cf',  default='json'
              , help='Format file.', is_eager=True
              , type=click.Choice(['json', 'yaml']))
@click.pass_context
def users_delete(ctx, id, file, content_format):
    """Delelete."""
    ctx.obj.delete(id, file, content_format)


