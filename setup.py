import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'django-fack',
    version = '1.2.0',
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
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
    ],

    install_requires = ['Django >= 1.11'],
    test_suite = "fack._testrunner.runtests",
    tests_require = ["mock"],
)
