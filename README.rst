.. _readthedocs: https://readthedocs.org/
.. _Sphinx: https://www.sphinx-doc.org/ 
.. _PyPI: https://pypi.org/

###############
  decimaldate
###############

.. image:: https://readthedocs.org/projects/decimaldate/badge/?version=latest
    :target: https://decimaldate.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/pypi/pyversions/decimaldate
   :alt: PyPI - Python Version

.. image:: https://img.shields.io/pypi/v/decimaldate.svg
   :target: https://pypi.org/project/decimaldate/
   :alt: Package on PyPI

.. image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg
   :target: https://opensource.org/licenses/BSD-3-Clause
   :alt: BSD 3 Clause

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black


================
  Introduction
================

The source for this ``decimaldate`` project is available on `GitHub <https://github.com/TorbenJakobsen/decimaldate>`_.

.. note::

   This project and the development of the module ``datetime`` is documented here, in *this* ``README.rst`` file.

   The Python module itself, and its use, is documented in the ``docs/source`` as reStructuredText to be processed with Sphinx_
   and made available on `readthedocs <https://decimaldate.readthedocs.io/>`_.

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

Activate the virtual environment (remember the ``.``).

.. code:: bash

   . venv/bin/activate

.. note::

   This will activate for macOS and Linux.
   For Windows CMD or PowerShell run the activation scripts instead.

Install requirements
--------------------

Install requirements and their dependencies for development (which are not deployment dependencies).

.. code:: bash

   python3 -m pip install --upgrade -r requirements/development.txt

Build and Test
--------------

Build (where the ``pyproject.toml`` file is located):

.. code:: bash

   python3 -m build

Install updated project with editing (remember the :code:`.`):

.. code:: bash

   python3 -m pip install --upgrade -e .

Test:

.. code:: bash

   pytest

Coverage:

.. code:: bash

   coverage run -m pytest tests

Make coverage report:

.. code:: bash

   coverage report -m

Make coverage report as HTML:

.. code:: bash

   coverage html

To see the HTML report, open the default location: ``htmlcov\index.html`` in a browser and/or light-weight http server.


Upload to PyPI

Make sure you have ``build`` so the latest (and only the latest) version is in the ``dist`` directory.

.. code:: bash
   python3 -m twine upload --verbose --repository pypi dist/*

.. note:: 
   You will need ``twine`` installed; which is part of the reqirements file.

See `Packaging Python Projects <https://packaging.python.org/en/latest/tutorials/packaging-projects/>`_ for more information.

.. note::
   If you see:
      400 The description failed to render for 'text/x-rst'.
      See https://pypi.org/help/#description-content-type for more information.
   You most likely have put in Sphinx_ into the reStructuredText that PyPI_ likes.

Comments
--------

.. note::
   
   These commands are available as ``make`` targets in the included ``Makefile``

=================
  Documentation
=================

To build the documentation go to 
the ``docs`` directory and work with 
the reStructuredText (``.rst``) files and Sphinx_.

Use the ``make`` command to see options for documentation build using Sphinx_.

.. image:: docs/source/_static/sphinx_make_default.png
   :width: 800


readthedocs
-----------

See readthedocs_.
