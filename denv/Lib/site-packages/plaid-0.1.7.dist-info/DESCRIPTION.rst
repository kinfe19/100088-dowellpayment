===============================
Plaid
===============================


.. image:: https://img.shields.io/pypi/v/plaid.svg
        :target: https://pypi.python.org/pypi/plaid

.. image:: https://img.shields.io/pypi/l/plaid.svg
    :target: https://pypi.python.org/pypi/plaid

.. image:: https://img.shields.io/pypi/wheel/plaid.svg
    :target: https://pypi.python.org/pypi/plaid

.. image:: https://img.shields.io/pypi/pyversions/plaid.svg
    :target: https://pypi.python.org/pypi/plaid

.. image:: https://img.shields.io/travis/sqrvrtx/plaid.svg
        :target: https://travis-ci.org/sqrvrtx/plaid

.. image:: https://readthedocs.org/projects/plaid/badge/?version=latest
        :target: https://plaid.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


Python Ansible role checker


* Free software: MIT license
* Documentation: https://plaid.readthedocs.io.


Features
--------

Generic ansible role checker. Parses yaml, jinja2 templates and checks for
pep8/flake 8 python errors. Also check for files we expect and those we don't.
This is configured in the .plaidrc file::

    ---

    include_files:
      - README.md
      - molecule.yml

    exclude_files:
      - .travis.yml


Also in the case a user creates a base role using ansible-galaxy, the tool
checks for 'empty' main.yml files in 'tasks', 'defaults', 'handlers' and 'vars',
and checks for empty 'files' and 'templates' directories. In the future there
are plans to check the default information in the 'README.md', 'meta' and
'tests'.


=======
History
=======

0.1.0 (2017-02-09)
------------------

* First release on PyPI.


