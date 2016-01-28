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

from driver import utils
from driver import exception

from api.controller import Controller


@click.group()
@click.version_option()
def openstackcli():
    """Openstack restful client which directly uses the REST ful api of OS.
    """


@openstackcli.group()
def project():
    """Manages users."""


@project.command('list')
def project_list():
    project_controller = Controller('projects')
    result = project_controller.index() # todo(jorgesece): parse result to json
    click.echo(result)
    click.echo('NOT IMPLEMENTED. Created list')


@project.command('create', help="Select either --attributes or --file input")
@click.option('--attributes', '-a', default=None#,callback=utils.validate_attributes)
              , help='Name project of the project: {name:"name_project", description:"description project",...}')#,callback=utils.validate_attributes)
@click.option('--file', '-f', default=None, help='File with list of projects attributes', type=click.File('r'))
@click.option('--content_format', '-cf',  default='json'
              , help='Format file.'
              , type=click.Choice(['json', 'yaml']))
def project_create(attributes, file, content_format):
    """Creates a new project."""
    project_controller = Controller('projects')
    resulting_message = "CREATED PROJECTS:\n ["
    try:
        if file:
            parameters = utils.parse_file(file, content_format)
        elif attributes:
            parameters = utils.parse_attributes(attributes)
        else:
            raise exception.ClientException(400, 'You need to specify either --attributes or --file')
        result = project_controller.create(parameters=parameters)
        for item in result:
            resulting_message = '%s%s\n' % (resulting_message, item)
        resulting_message = '%s]' % resulting_message
    except Exception as e:
        raise exception.ClientException(e.code, e.message) #todo(jorgesece): check it
    click.echo(resulting_message)


@project.command('delete',help="Select either --id or --file input")
@click.option('--id', '-i', default=None, help='Identification of project')
@click.option('--file', '-f', default=None,
              help='File with list of projects ids. [{"id"="xx"},{"id"="xx2"}..]',
              type=click.File('r'))
@click.option('--content_format', '-cf',  default='json'
              , help='Format file.'
              , type=click.Choice(['json', 'yaml']))
def project_delete(id, file, content_format):
    """Delelete."""
    project_controller = Controller('projects')
    if file:
        project_controller = Controller('projects')
        try:
            parameters = utils.parse_file(file, content_format) #fixme(jorgesece): check if file contains id
        except Exception as e:
            raise exception.ClientException(400, e.message)
    else:
        if id:
            parameters = [{'id': id}]
        else:
            raise exception.ClientException(404, "You should indicate an id or a list of them")
    result = project_controller.delete(parameters=parameters)
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