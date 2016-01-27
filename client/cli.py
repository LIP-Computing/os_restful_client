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

from api.projects import Controller as ProjectController


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
    project_controller = ProjectController()
    result = project_controller.index() # todo(jorgesece): parse result to json
    click.echo(result)
    click.echo('NOT IMPLEMENTED. Created list')


@project.command('create')
@click.argument('name')
@click.option('--description', '-d', help='Description of the project.')
def project_create(name, description):
    """Creates a new project."""
    project_controller = ProjectController()
    parameters = {'name': name}
    if description:
        parameters['description'] = description
    result = project_controller.create(parameters=[parameters])
    click.echo(result)


@project.command('createBunch')
@click.argument('file')
@click.option('--content_format', '-f',  default='json', help='Format file (json or yaml).')
def project_create(file, content_format):
    """Creates new projects from a file."""
    resulting_message = "CREATED PROJECTS:"
    project_controller = ProjectController()
    try:
        parameters = utils.parse_file(file, content_format)
    except Exception as e:
        raise exception.ClientException(400, e.message)
    try:
        result = project_controller.create(parameters=parameters)
    except Exception as e:
        raise exception.ClientException(400, e.message) #todo(jorgesece): check it

    for item in result:
        resulting_message = '%s \n %s' % (resulting_message, item)
    click.echo(resulting_message)


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