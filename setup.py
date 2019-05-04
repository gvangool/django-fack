import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'django-fack',
    version = '1.1',
    description = 'A simple FAQ application for Django sites.',
    long_description = read('README.rst'),
    license = "BSD",

    author  ='Kevin Fricovsky',
    author_email = 'kfricovsky@gmail.com',
    url = 'http://django-fack.rtfd.org/',

    packages = find_packages(exclude=['example']),
    include_package_data=True,
    zip_safe = False,

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],

    install_requires = ['Django >= 1.3'],
    test_suite = "fack._testrunner.runtests",
    tests_require = ["mock"],
)
