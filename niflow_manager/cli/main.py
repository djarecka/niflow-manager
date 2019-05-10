import click
import subprocess as sp
from .. import __version__
from .init import init


@click.group()
@click.version_option(__version__)
def main():
    pass


main.command()(init)


@main.command()
def install():
    print("install command not yet implemented")


@main.command() 
@click.argument('workflow_dir', type=click.Path(), default='.')
def test(workflow_dir):
    #path, full_name, organization, workflow = normalize_path(name)
    print(f'testing {workflow_dir}') 
    #path.mkdir(parents=True, exist_ok=True)
    sp.run(['testkraken', str(workflow_dir)], check=True)
