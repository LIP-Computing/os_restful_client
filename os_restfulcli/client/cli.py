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
    """Manages users."""
    resource = 'projects'
    ctx.obj = ControllerClient(resource)


@projects.command('list')
@list_common_options
@click.pass_context
def projects_list(ctx, out):
    ctx.obj.index(out)


@projects.command('show',help="Select project identification (ID)")
@out_format_option
@name_argument
@click.pass_context
def projects_show(ctx, project_name, out):
    """Show."""
    ctx.obj.show(project_name, out)


@projects.command('create', help="Select either --attributes or --file input")
@create_common_options
@click.pass_context
def projects_create(ctx, attributes, file, content_format, out):
    """Creates a new project."""
    ctx.obj.create(attributes, file, out)


@projects.command('delete',help="Select either --id or --file input")
@delete_common_options
@click.pass_context
def projects_delete(ctx, id, file, content_format, out):
    """Delete."""
    ctx.obj.delete(id, file, out)

#####################################
############ USERS ##################
#####################################


@openstackcli.group()
@click.pass_context
def users(ctx):
    """Manages users."""
    resource = 'users'
    ctx.obj = ControllerClient(resource)


@users.command('list')
@list_common_options
@click.pass_context
def users_list(ctx, out):
    ctx.obj.index(out)


@users.command('show',help="Select user identification (ID)")
@out_format_option
@name_argument
@click.pass_context
def users_show(ctx, user_name, out):
    """Show."""
    ctx.obj.show(user_name, out)


@users.command('create', help="Select either --attributes or --file input")
@create_common_options
@click.pass_context
def users_create(ctx, attributes, file, content_format, out):
    """Creates a new project."""
    ctx.obj.create(attributes, file, out)


@users.command('delete',help="Select either --id or --file input")
@delete_common_options
@click.pass_context
def users_delete(ctx, id, file, content_format, out):
    """Delete."""
    ctx.obj.delete(id, file, out)


#####################################
############ ROLES ##################
#####################################


@openstackcli.group()
@click.pass_context
def roles(ctx):
    """Manages users."""
    resource = 'roles'
    ctx.obj = ControllerClient(resource)


@roles.command('list')
@list_common_options
@click.pass_context
def roles_list(ctx, out):
    ctx.obj.index(out)


@roles.command('show',help="Select user identification (ID)")
@out_format_option
@name_argument
@click.pass_context
def roles_show(ctx, role_name, out):
    """Show."""
    ctx.obj.show(role_name, out)


@roles.command('create', help="Select either --attributes or --file input")
@create_common_options
@click.pass_context
def roles_create(ctx, attributes, file, content_format, out):
    """Creates a new project."""
    ctx.obj.create(attributes, file, out)


@roles.command('delete',help="Select either --id or --file input")
@delete_common_options
@click.pass_context
def roles_delete(ctx, id, file, content_format, out):
    """Delete."""
    ctx.obj.delete(id, file, out)

#####################################
######### GRANT_ROLES ##################
#####################################


@roles.command('list_grants')
@grant_arguments
@list_common_options
@click.pass_context
def roles_grant_list(ctx, out, project_name, user_name):
    path = "/projects/%s/users/%s" % (project_name, user_name)
    ctx.obj.update_path(path)
    ctx.obj.index(out)


@roles.command('create_grant', help="Select project_id, user_id and role_id")
@grant_arguments
@name_argument
@out_format_option
@click.pass_context
def roles_grant_create(ctx, role_name, project_name, user_name, out):
    """Creates a new project."""
    path = "/projects/%s/users/%s" % (project_name, user_name)
    ctx.obj.update_path(path)
    ctx.obj.link(role_name, out)


@roles.command('delete_grant',help="Select either --id or --file input")
@grant_arguments
@name_argument
@out_format_option
@click.pass_context
def roles_grant_delete(ctx, role_name, out, project_name, user_name):
    """Delete."""
    path = "/projects/%s/users/%s" % (project_name, user_name)
    ctx.obj.update_path(path)
    ctx.obj.delete(role_name, None, out)

@roles.command('grants_by_project',help="Select project id")
@name_list_argument
@out_format_option
@click.pass_context
def roles_grant_list_by_project(ctx, project_name, out):
    """Delete."""
    parameters = {}
    parameters["scope.project.id"] = project_name
    ctx.obj.update_path(None,'role_assignments')
    ctx.obj.list_roles_by_query(out_format=out, parameters=parameters)

@roles.command('grants_by_user',help="Select project id")
@name_list_argument
@out_format_option
@click.pass_context
def roles_grant_list_by_user(ctx, user_name, out):
    """Delete."""
    parameters = {}
    parameters["user.id"] = user_name
    ctx.obj.update_path(None,'role_assignments')
    ctx.obj.list_roles_by_query(out_format=out, parameters=parameters)


