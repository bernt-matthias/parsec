import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('toolShed_get_repositories')
@pass_context
@bioblend_exception
@dict_output
def cli(ctx):
    """Get a list of all repositories in the Tool Shed
    """
    return ctx.gi.toolShed.get_repositories()
