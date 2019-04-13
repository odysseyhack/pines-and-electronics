#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open('README.md') as readme_file:
    readme = readme_file.read()

install_requirements = [
    'coloredlogs==10.0',
    'Flask==1.0.2',
    'Flask-Cors==3.0.6',
    'flask-swagger==0.2.14',
    'flask-swagger-ui==3.20.9',
    'gunicorn==19.9.0',
    'PyYAML==5.1',
    'pytz==2018.5',
    'squid-py==0.5.14'
]

setup_requirements = ['pytest-runner==2.11.1', ]

dev_requirements = [
    'bumpversion==0.5.3',
    'pkginfo==1.4.2',
    'twine==1.11.0',
    # not virtualenv: devs should already have it before pip-installing
    'watchdog==0.8.3',
]

test_requirements = [
    'codacy-coverage==1.3.11',
    'coverage==4.5.1',
    'mccabe==0.6.1',
    'pylint==2.2.2',
    'pytest==3.4.2',
    'tox==3.2.1',
]

setup(
    author="leucothia",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="🚗 Car backend.",
    extras_require={
        'test': test_requirements,
        'dev': dev_requirements + test_requirements,
    },
    include_package_data=True,
    install_requires=install_requirements,
    keywords='pines backend',
    license="Apache Software License 2.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    name='car-backend',
    packages=find_packages(include=['car']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/odysseyhack/pines-and-electronics',
    version='0.1.0',
    zip_safe=False,
)
