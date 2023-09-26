"""
Generic jinja2 parser
"""


import sys

from jinja2 import Environment


def parse(file_contents, file_name):
    '''
    Takes a list of files which are assumed to be jinja2 templates and tries to
    parse the contents of the files

    Args:
        file_contents (str): File contents of a jinja file

    Raises:
        Exception: An exception is raised if the contents of the file cannot be
                   parsed.
    '''

    env = Environment()
    result = ""
    try:
        env.parse(file_contents)
    except Exception:
        _, exc_value, _ = sys.exc_info()
        result += "ERROR: Jinja2 Template File: {0}".format(file_name)
        result += repr(exc_value) + '\n'

    return result
