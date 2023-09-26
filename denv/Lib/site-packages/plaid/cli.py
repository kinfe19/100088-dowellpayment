# -*- coding: utf-8 -*-

import click


@click.command()
def main(args=None):
    """Console script for plaid"""
    import plaid
    plaid.main()


if __name__ == "__main__":
    main()
