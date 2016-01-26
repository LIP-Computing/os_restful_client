import click



@click.group()
@click.version_option()
def openstack():
    """Openstack restful client which directly uses the REST ful api of OS.
    """

@openstack.group()
def project():
    """Manages users."""


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


@openstack.group()
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