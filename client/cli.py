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
    """Creates a new ship."""
    click.echo('NOT IMPLEMENTED. Created project %s' % name)


@project.command('createBunch')
@click.argument('file')
def project_create(file):
    """Creates a new ship."""
    click.echo('NOT IMPLEMENTED. Created project from a JSON file %s' % file)


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