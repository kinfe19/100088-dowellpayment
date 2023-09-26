#!/usr/bin/env python
"""
Generic yaml parser
"""


import sys
import yaml


def parse(file_contents, file_name):
    """
    This takes a list of filenames and their paths of expected yaml files and
    tried to parse them, erroring if there are any parsing issues.

    Args:
        file_contents (str): Contents of a yml file

    Raises:
        yaml.parser.ParserError: Raises an error if the file contents cannot be
                                 parsed and interpreted as yaml
    """

    try:
        yaml.load(file_contents)
    except Exception:

        _, exc_value, _ = sys.exc_info()
        return("Cannot Parse: {file_name}: \n {exc_value}"
               .format(file_name=file_name, exc_value=exc_value))
