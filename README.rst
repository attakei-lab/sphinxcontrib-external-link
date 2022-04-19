===========================
sphinxcontrib-external-link
===========================

Override ref(link to docs) extension to open new tab(window)

Overview
========

If link has external link, set HTML attribute ``target`` and ``rel``.

- ``target`` : To open other window(tab)
- ``rel`` : For performance and vulnerability

Installation
============

Install package from GitHub Releases.

.. code-block:: console

   pip install --find-links=https://github.com/attakei-lab/sphinxcontrib-external-link/releases sphinxcontrib-external-link

Usage
=====

Add this extension into your ``conf.py`` of Sphinx.

.. code-block:: python

   extensions = [
       "sphinxcontrib.external_link",
   ]

License
=======

Apache-2.0
