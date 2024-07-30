import click
from calculadora.model import Calculator




@click.group()
@click.pass_context
def calc(ctx: click.context):
    """A simple calculator"""

    ctx.obj = {"calculator_object", Calculator()}