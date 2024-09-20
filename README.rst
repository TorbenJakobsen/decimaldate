.. _readthedocs: https://readthedocs.org/
.. _Sphinx: https://www.sphinx-doc.org/ 
.. _PyPI: https://pypi.org/
.. _Alabaster: https://sphinx-themes.readthedocs.io/en/latest/sample-sites/default-alabaster/
.. _ruff: https://docs.astral.sh/ruff/
.. _Python: https://www.python.org/
.. _rstcheck: https://github.com/rstcheck/
.. _flake8: https://github.com/pycqa/flake8
.. _mypy: https://www.mypy-lang.org/
.. _pytest: https://pytest.org/
.. _pytest-cov: https://pypi.org/project/pytest-cov/
.. _coverage: https://coverage.readthedocs.io/
.. _readthedocs-community: https://about.readthedocs.com/pricing/#/community

###############
  decimaldate
###############

.. start-badges

.. list-table::
    :stub-columns: 1

    * - general
      - |license|
    * - docs
      - |docs|
    * - code
      - |code-style| |commits-since|
    * - package
      - |wheel| |supported-versions| |supported-implementations| 
    * - downloads
      - |downloads-total| |downloads-monthly| |downloads-weekly|

.. |docs| image:: https://readthedocs.org/projects/decimaldate/badge/?version=latest
    :alt: Documentation Status
    :target: https://decimaldate.readthedocs.io/en/latest/?badge=latest

.. |code-style| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :alt: Using black formatter
   :target: https://github.com/psf/black

.. |commits-since| image:: https://img.shields.io/github/commits-since/TorbenJakobsen/decimaldate/v0.1.9.svg
   :alt: Commits since latest release
   :target: https://github.com/TorbenJakobsen/decimaldate/compare/v0.1.9...main

.. |license| image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg
   :alt: BSD 3 Clause
   :target: https://opensource.org/licenses/BSD-3-Clause

.. |wheel| image:: https://img.shields.io/pypi/wheel/decimaldate.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/decimaldate

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/decimaldate.svg
    :alt: Supported versions
    :target: https://pypi.org/project/decimaldate

.. |downloads-total| image:: https://static.pepy.tech/badge/decimaldate
   :alt: Total downloads counter
   :target: https://pepy.tech/project/decimaldate

.. |downloads-monthly| image:: https://static.pepy.tech/badge/decimaldate/month
   :alt: Weekly downloads counter
   :target: https://pepy.tech/project/decimaldate

.. |downloads-weekly| image:: https://static.pepy.tech/badge/decimaldate/week
   :alt: Weekly downloads counter
   :target: https://pepy.tech/project/decimaldate

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/decimaldate.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/decimaldate

.. end-badges

================
  Introduction
================

The source for this ``decimaldate`` project is publicly available on `GitHub <https://github.com/TorbenJakobsen/decimaldate>`_.

.. note::

   This project and the development of the module ``datetime`` is documented here, in *this* ``README.rst`` file.

   The Python ``decimaldate`` package itself, and its use, is documented in 
   the project's ``docs/source`` as reStructuredText to be processed with Sphinx_
   and made available on readthedocs_ as `decimaldate <https://decimaldate.readthedocs.io/>`_.

=========================
  Setup for Development
=========================

Use a virtual environment
-------------------------

It is optional, but *highly* recommended to create and use a virtual environment.
This documentation will assume the use of a virtual environment and ``venv``.

.. code:: bash

   python3 -m venv venv

.. note::
   
   You can use other virtualization tools as you prefer.

Activate (source) the virtual environment (remember the ``.``).

.. code:: bash

   . venv/bin/activate

.. note::

   | This will activate for macOS and Linux.
   | For Windows CMD or PowerShell run the activation scripts instead.

Install requirements
--------------------

Install requirements and their dependencies for development (which are not deployment dependencies).

.. code:: bash

   python3 -m pip install --upgrade -r requirements/development.txt

Build and Test
--------------

Build
~~~~~

Build (where the ``pyproject.toml`` file is located):

.. code:: bash

   python3 -m build

Install updated project with editing (remember the :code:`.`):

.. code:: bash

   python3 -m pip install --upgrade -e .

Test
~~~~

Test:

.. code:: bash

   pytest

Coverage:

.. code:: bash

   coverage run -m pytest tests

Make run coverage into report:

.. code:: bash

   coverage report -m

Make run coverage into report as HTML:

.. code:: bash

   coverage html

To see the HTML report, open the default location: ``htmlcov\index.html`` in a browser and/or light-weight http server.

Upload to PyPI
~~~~~~~~~~~~~~

Make sure you have ``build`` so the latest (and only the latest) version is in the ``dist`` directory.

.. note:: 
   
   You will need ``twine`` installed; which is part of the development requirements file.

.. code:: bash

   python3 -m twine upload --verbose --repository pypi dist/*

You will be asked for your API token:

.. image:: docs/source/_static/twine_upload.png
   :width: 540

See `Packaging Python Projects <https://packaging.python.org/en/latest/tutorials/packaging-projects/>`_ for more information.

.. note::

   If you see:

      | 400 The description failed to render for 'text/x-rst'.
      | See https://pypi.org/help/#description-content-type for more information.
   
   You may have put Sphinx_ specifics into the plain reStructuredText that PyPI_ wants.

   See rstcheck_ for a linter to help you. 

Comments
--------

.. note::
   
   These commands are available as ``make`` targets in the included ``Makefile``.

=================
  Documentation
=================

To build the documentation go to 
the ``docs`` directory and work with 
the reStructuredText (``.rst``) files and Sphinx_.

Use the ``make`` command to see options for documentation build using Sphinx_.

.. image:: docs/source/_static/sphinx_make_default.png
   :width: 800

When ready update documentation on readthedocs_.

It is highly recommended to test the update by uploading to 
https://test.pypi.org/
before updating PyPI_. 

Locally you can run ``make html`` to see the generated output,
and ``rstcheck`` to validate and lint your markup.

=========
  Tools 
=========

.. note:: 
   
   At some later date I will replace some of the tooling with ruff_.

python3
   Of course...
   
   See Python_.

flake8
   A Python linting tool for style guide enforcement.

   See flake8_.

mypy
   A static type checker for Python (type hints are optional and not enforced). 

   See mypy_.

pytest
   From the documentation:

      The pytest framework makes it easy to write small, readable tests, 
      and can scale to support complex functional testing for applications and libraries.

   See pytest_.

coverage
   From the documentation:

      Coverage.py is a tool for measuring code coverage of Python programs. 
      It monitors your program, noting which parts of the code have been executed,
      then analyzes the source to identify code that could have been executed but was not.

   My personal preference is to use ``coverage`` as is,
   and not the extension for pytest ``pytest-cov`` (see pytest-cov_).

   See coverage_.

sphinx 
   To generate local copy of documentation meant for readthedocs_.

   The `theme <https://sphinx-themes.readthedocs.io/en/latest/>`_ chosen
   is `Read The Docs <https://sphinx-themes.readthedocs.io/en/latest/sample-sites/sphinx-rtd-theme/>`_ 
   (the default is Alabaster_).

   See Sphinx_.

readthedocs
   A site building and hosting documentation.

   Sign up for a free account if you qualify (FOSS).
   The free account has a limit on concurrent builds (think GitHub actions and CI/CD) and displays a tiny advertisement (see readthedocs-community_).

   See readthedocs_.

rstcheck
   Lints your reStructuredText markdown files.

   From the documentation:

      Checks syntax of reStructuredText and code blocks nested within it.
   
   .. image:: docs/source/_static/rstcheck_run.png
      :width: 620

   The shown warnings/errors are benign and are caused by the autogeneration of links for sections.
   As some sections have the same name, this is flagged. These particular warnings I will ignore.

   See rstcheck_.
