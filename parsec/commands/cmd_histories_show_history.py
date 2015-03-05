import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('histories_show_history')
@click.argument("history_id", type=str)
@click.option(
    "--contents",
    help="When true, the complete list of datasets in the given history.",
    type=str
)
@click.option(
    "--deleted",
    help="Used when contents=True, includes deleted datasets is history dataset list",
    type=str
)
@click.option(
    "--visible",
    help="Used when contents=True, includes only visible datasets is history dataset list",
    type=str
)
@click.option(
    "--details",
    help="Used when contents=True, includes dataset details. Set to 'all' for the most information",
    type=str
)
@click.option(
    "--types",
    help="???",
    type=str
)
@pass_context
@bioblend_exception
@dict_output
def cli(
        ctx,
        history_id,
        contents=False,
        deleted="",
        visible="",
        details="",
        types=""):
    """Get details of a given history. By default, just get the history meta information.
    """
    return ctx.gi.histories.show_history(
        history_id,
        contents=contents,
        deleted=deleted,
        visible=visible,
        details=details,
        types=types)
