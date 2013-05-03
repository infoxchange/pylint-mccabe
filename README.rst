McCabe complexity checker as a PyLint plugin
============================================

This module provides a PyLint plugin to check McCabe code complexity.


Usage
-----

In pylint.conf::

    [MASTER]
    load-plugins=pylint_mccabe

    [DESIGN]
    max-complexity=10

Dependencies
------------

* mccabe and pylint, obviously
* pep8: Not required for functionality but is used to check the code style
