# -*- coding: utf-8 -*-

# Copyright 2015 LIP - Lisbon
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

from os_restfulcli.client.controller import ControllerClient
from os_restfulcli.client.decorators import *

#sys.tracebacklimit=0


@click.group()
@click.version_option()
def openstackcli():
    """Openstack restful client which directly uses the REST ful api of OS.
    """
    pass

def test_decorator():
    return  openstackcli();
#####################################
########## PROJECTS ################
#####################################

@openstackcli.group()
@click.pass_context
def projects(ctx):
    """Manages projects."""
    resource = 'projects'
    ctx.obj = ControllerClient(resource)


@projects.command('list', help="List projects.")
@list_common_options
@click.pass_context
def projects_list(ctx, out):
    ctx.obj.index(out)


@projects.command('show',help="Show a project details.")
@out_format_option
@name_argument
@click.pass_context
def projects_show(ctx, project_name, out):
    """Show."""
    ctx.obj.show(project_name, out)


@projects.command('create', help="Create  a a single or group of project. Select either --attributes or --file input.")
@create_common_options
@click.pass_context
def projects_create(ctx, attributes, file, content_format, out):
    """Creates a new project."""
    ctx.obj.create(attributes, file, out)


@projects.command('delete',help="Delete a single or group of projects. Select either --project_name or --file input.")
@delete_common_options
@click.pass_context
def projects_delete(ctx, project_name, file, content_format, out):
    """Delete."""
    ctx.obj.delete(project_name, file, out)

#####################################
############ USERS ##################
#####################################


@openstackcli.group()
@click.pass_context
def users(ctx):
    """Manages users."""
    resource = 'users'
    ctx.obj = ControllerClient(resource)


@users.command('list',help="List users.")
@list_common_options
@click.pass_context
def users_list(ctx, out):
    ctx.obj.index(out)


@users.command('show',help="Show user details.")
@out_format_option
@name_argument
@click.pass_context
def users_show(ctx, user_name, out):
    """Show."""
    ctx.obj.show(user_name, out)


@users.command('create', help="Create a a single or group of users. Select either --attributes or --file input.")
@create_common_options
@click.pass_context
def users_create(ctx, attributes, file, content_format, out):
    """Creates a new project."""
    ctx.obj.create(attributes, file, out)


@users.command('delete',help="Delete a a single or group of users. Select either --user_name or --file input.")
@delete_common_options
@click.pass_context
def users_delete(ctx, user_name, file, content_format, out):
    """Delete."""
    ctx.obj.delete(user_name, file, out)


#####################################
############ ROLES ##################
#####################################


@openstackcli.group()
@click.pass_context
def roles(ctx):
    """Manages roles and grant users in projects."""
    resource = 'roles'
    ctx.obj = ControllerClient(resource)


@roles.command('list', help="List roles.")
@list_common_options
@click.pass_context
def roles_list(ctx, out):
    ctx.obj.index(out)


@roles.command('show',help="Show role details.")
@out_format_option
@name_argument
@click.pass_context
def roles_show(ctx, role_name, out):
    """Show."""
    ctx.obj.show(role_name, out)


@roles.command('create', help="Create a single or group of roles. Select either --attributes or --file input.")
@create_common_options
@click.pass_context
def roles_create(ctx, attributes, file, content_format, out):
    """Creates a new project."""
    ctx.obj.create(attributes, file, out)


@roles.command('delete',help="Delete a single or group of roles. Select either --role_name or --file input.")
@delete_common_options
@click.pass_context
def roles_delete(ctx, id, file, content_format, out):
    """Delete."""
    ctx.obj.delete(id, file, out)

#####################################
######### GRANT_ROLES ##################
#####################################


@roles.command('list_grants', help="List every grant of an user in a project.")
@grant_arguments
@list_common_options
@click.pass_context
def roles_grant_list(ctx, out, project_name, user_name):
    path = "/projects/%s/users/%s" % (project_name, user_name)
    ctx.obj.update_path(path)
    ctx.obj.index(out)


@roles.command('create_grant', help="Grant an user in a project with a role.")
@grant_arguments
@name_argument
@out_format_option
@click.pass_context
def roles_grant_create(ctx, role_name, project_name, user_name, out):
    """Creates a new project."""
    path = "/projects/%s/users/%s" % (project_name, user_name)
    ctx.obj.update_path(path)
    ctx.obj.link(role_name, out)


@roles.command('delete_grant',help="Delete grant of an user in a project with a role.")
@grant_arguments
@name_argument
@out_format_option
@click.pass_context
def roles_grant_delete(ctx, role_name, out, project_name, user_name):
    """Delete."""
    path = "/projects/%s/users/%s" % (project_name, user_name)
    ctx.obj.update_path(path)
    ctx.obj.delete(role_name, None, out)

@roles.command('grants_by_project',help="List users with grants in a project.")
@name_list_argument
@out_format_option
@click.pass_context
def roles_grant_list_by_project(ctx, project_name, out):
    """Delete."""
    parameters = {}
    parameters["scope.project.id"] = project_name
    ctx.obj.update_path(None,'role_assignments')
    ctx.obj.list_roles_by_query(out_format=out, parameters=parameters)

@roles.command('grants_by_user',help="List projects in which an user has grants.")
@name_list_argument
@out_format_option
@click.pass_context
def roles_grant_list_by_user(ctx, user_name, out):
    """Delete."""
    parameters = {}
    parameters["user.id"] = user_name
    ctx.obj.update_path(None,'role_assignments')
    ctx.obj.list_roles_by_query(out_format=out, parameters=parameters)


