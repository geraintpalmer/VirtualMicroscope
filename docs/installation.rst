============
Installation
============

VirtualMicroscope is `hosted on GitHub <https://github.com/evildmp/VirtualMicroscope>`_.

To install::

    git clone git@github.com:evildmp/VirtualMicroscope.git
    cd VirtualMicroscope
    git checkout hackday  # for now, until our work goes into the master branch
    virtualenv env  # create a virtual environment
    source env/bin/activate  # activate it
    pip install -r requirements.txt  # install required components

This repository includes a demo project, so we'll use that to get started.

Create your local database - you will need superuser access, so create a superuser when asked,
and start up the Python runserver::

    python manage.py syncdb
    python manage.py runserver

Assuming you're running on localhost on port 8000, visit ``http://localhost:8000/admin/`` and login.

Just to prove this works, we'll use the included image in the demo project. That image has been
tiled for you already, and is to be found in ``nyuvm/static/tiles``.

In the Django admin, create a new Slide:

* ``URL to slide directory:``: *http://localhost:8000/static/tiles*
* ``Label``: whatever you like
* ``Maximum Google Zoom Level``: ``4``

**Save** the Slide.

Add a new *Collection*, and make sure you are in the ``Authors``.

Add a *Collection Slide*, that refers to your news Slide and your new Collection; fill in the
other fields as you like.

Visit ``http://localhost:8000/virtualmicroscope``.

Choose your Collection from the *Collections* menu, and choose your slide below.

And that's it - now you can zoom in and out on Auraya the dog; you have a working implementation.