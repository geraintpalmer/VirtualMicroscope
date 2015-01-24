##################
Future development
##################

A few ideas for future development are listed below.

*******************
System architecture
*******************

In order to cover the largest number of deployment scenarios, a
slightly refactored architecture for our system is proposed here.

Without loosing much generality, we should be able to assume that
image files are already stored on the local filesystem and available
via a local path. Potentially, they are very large images and
uploading them through a web-browser might not make much sense anyway.

With this assumption in mind, the following workflow is then possible.

Additional feature: Django will allow the admin user to browse the
local image folder and mark the ones that are meant to be served
throught the system.

Additional feature: once the selection is confirmed, Django will start
processing the images and creating the tiles as a background task
(`Celery`_ may come in help here). Once the processing is done for a
particular image, this is marked as ready on the Django admin and will
be available for viewing to the final user.

The other parts of the software - most notably the front-end part that
allows images to be displayed - would remain as currently implemented.

.. _Celery : http://www.celeryproject.org/

******
Docker
******

Given the above architecture, the `Docker Engine`_ could be used to
create a dedicated image and containerize our whole application.

The image folder could be made available to Docker as a volume via the
`-v` option.

.. _Docker Engine : https://www.docker.com/

*******************************************
Leaflet.js as an alternative to Google Maps
*******************************************

`Leaflet`_ is an open source JavaScript library to build web mapping
applications, akin to the Google Maps API currently in use in the
project.

Leaflet could be taken into account as a replacement to Google Maps
since the latter is a proprietary solution.

The integration of Leaflet in VirtualMicroscope should be feasible
without major issues. A few references are listed below.

* http://omarriott.com/aux/leaflet-js-non-geographical-imagery/
* http://kempe.net/blog/2014/06/14/leaflet-pan-zoom-image.html
* http://hugepic.io/

.. _Leaflet : http://leafletjs.com/
