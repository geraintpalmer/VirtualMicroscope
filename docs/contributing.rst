#################################
Contributing to VirtualMicroscope
#################################

Like every open-source project, VirtualMicroscope is always looking for motivated
individuals to contribute to its source code.

************
Contributing
************

People interested in contributing to VirtualMicroscope can visit #virtualmicroscope
on the `freenode`_ IRC network for help and to discuss the development.

VirtualMicroscope is `hosted on GitHub <https://github.com/evildmp/VirtualMicroscope>`_.

The best method to contribute back is to create an account there, then fork the project. You can
use this fork as if it was your own project, and should push your changes to it.

When you feel your code is good enough for inclusion, "send us a `pull request`_", by using the
nice GitHub web interface.

**************************
Contributing Documentation
**************************

Documentation should be:

- written using valid `Sphinx`_/`restructuredText`_ syntax (see below for
  specifics) and the file extension should be ``.rst``
- written in English (we have standardised on British spellings)
- accessible - you should assume the reader to be moderately familiar with
  Python and Django, but not anything else. Link to documentation of libraries
  you use, for example, even if they are "obvious" to you
- wrapped at 100 characters per line


Documentation markup
====================

Sections
--------

We use Python documentation conventions for section marking:

* ``#`` with overline, for parts
* ``*`` with overline, for chapters
* ``=``, for sections
* ``-``, for subsections
* ``^``, for subsubsections
* ``"``, for paragraphs

Inline markup
-------------

* use backticks - ````settings.py```` - for:
    * literals
    * filenames
    * names of fields and other items in the Admin interface:
* use emphasis - ``*Home*`` around:
    * the names of available options in the Admin
    * values in or of fields
* use strong emphasis - ``**Add page**`` around:
    * buttons that perform an action

References
----------

Use absolute links to other documentation pages - ``:doc:`/installation``` -
rather than relative links - ``:doc:`../isntallation```. This makes it easier to
run search-and-replaces when items are moved in the structure.


.. _freenode : http://freenode.net/
.. _Sphinx: http://sphinx.pocoo.org/
.. _restructuredText: http://docutils.sourceforge.net/docs/ref/rst/introduction.html
.. _pull request : http://help.github.com/send-pull-requests/
