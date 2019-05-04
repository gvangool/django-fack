===========
Django-Fack
===========

This is a simple FAQ application for a Django powered site, featuring:

* The basic Q&A model you'd expect.

* Question are grouped into topics.

* Topics can be ordered and arranged, as can questions within topics.

* Built-in views to drill down by topic and question, and individual
  question detail pages (for permalinks).

* A view for users to submit new questions (with or without answers). These
  go into moderation queue and need to be marked "active" before they'll
  show up on the site.

There's an example app (distributed with the source) to try out if you'd like
to get a taste of the app.

For more details, `see the documentation`__

__ http://django-fack.rtfd.org/

Requirements
============

Django 1.11+, Python 3.5+.

Installation
============

1. ``pip install django-fack``

2. Add ``"fack"`` to your ``INSTALLED_APPS`` setting.

3. Wire up the FAQ views by adding a line to your URLconf::

        url('^faq/', include('fack.urls'))


If you'd like to load some example data then run ``python manage.py loaddata
faq_test_data.json``

The app's written with quite a bit of customization in mind; `see the customization documentation`__ for details.

__ http://django-fack.rtfd.org/en/latest/customization.html

Example Site
============

There is a stand-alone example site distributed with the source in the
`example/` directory. To try it out:

1. Install django-fack (see above).

1. Run ``python manage.py migrate``

   This assumes that sqlite3 is available; if not you'll need to change the
   ``DATABASES`` setting first.

3. Load some example data by running
   ``python manage.py loaddata faq_test_data.json``

4. Run ``python manage.py runserver`` and you will have the example site up and
   running. The home page will have links to get to the available views as well
   as to the admin.

The capability to submit an FAQ is available and works whether or not you are a
logged in user. Note that a staff member will have to use the admin and review
any submitted FAQs and clean them up and set them to active before they are
viewable by the end user views.

Contributing
============

To run the tests, install tox__ (``pip install tox``) then run ``tox``.

__ https://tox.readthedocs.io/en/latest/

Development `takes place on GitHub`__. Bug reports, pataches, and pull requests
are always welcome!

__ https://github.com/revsys/django-fack
