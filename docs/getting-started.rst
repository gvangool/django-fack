Getting starting with Django-Fack
=================================

Installation
------------

1. ``pip install django-fack``

2. Add ``"fack"`` to your ``INSTALLED_APPS`` setting.

3. Wire up the FAQ views by adding a line to your URLconf::

        url('^faq/', include('fack.urls'))

If you'd like to load some example data then run
``python manage.py loaddata faq_test_data.json``

FAQ entries can be edited in the admin, and also via the submit view (at
``<prefix>/submit``).

The app's written with quite a bit of customization in mind; see
:doc:`customization` for details. You'll almost certain want to :ref:`customize
the templates <custom-templates>` to make the app "fit in" to your site.

Example Site
------------

There is a stand-alone example site distributed with the source in the
``example/`` directory. To try it out:

1. Install Django-Fack (see above).

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
