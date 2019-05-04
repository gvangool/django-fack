"""
Test support harness to make setup.py test work.
"""

import sys

import django
from django.conf import settings

settings.configure(
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory;"}},
    INSTALLED_APPS=[
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.messages",
        "django.contrib.sessions",
        "fack",
    ],
    MIDDLEWARE_CLASSES=[
        "django.middleware.common.CommonMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
    ],
    ROOT_URLCONF="fack.urls",
)
if hasattr(django, "setup"):
    django.setup()


def runtests():
    import django.test.utils

    runner_class = django.test.utils.get_runner(settings)
    test_runner = runner_class(verbosity=1, interactive=True)
    failures = test_runner.run_tests(["fack"])
    sys.exit(failures)
