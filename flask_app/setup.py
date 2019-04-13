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
    'squid-py==0.5.14',
    'absl-py == 0.7.1',
    'astor == 0.7.1',
    'cachetools == 3.1.0',
    'chardet == 3.0.4',
    'gast == 0.2.2',
    'google-api-core == 1.9.0',
    'google-api-python-client == 1.7.8',
    'google-auth== 1.6.3',
    'google-auth-httplib2 == 0.0.3',
    'google-cloud-core == 0.29.1',
    'google-cloud-storage == 1.14.0',
    'google-cloud-vision == 0.36.0',
    'google-resumable-media == 0.3.2',
    'googleapis-common-protos == 1.5.9',
    'grpcio == 1.19.0',
    'h5py == 2.9.0',
    'httplib2 == 0.12.1',
    'idna == 2.8',
    'keras-applications == 1.0.7',
    'keras-preprocessing == 1.0.9',
    'markdown == 3.1',
    'mock == 2.0.0',
    'pbr == 5.1.3',
    'protobuf == 3.7.1',
    'pyasn1 == 0.4.5',
    'pyasn1-modules == 0.2.4',
    'requests == 2.21.0',
    'rsa == 4.0',
    'tensorboard == 1.13.1',
    'tensorflow == 1.13.1',
    'tensorflow-estimator == 1.13.0',
    'termcolor == 1.1.0',
    'uritemplate == 3.0.0',
    'urllib3 == 1.24.1',
    'werkzeug == 0.15.2',
    'smbus-cffi == 0.5.1'
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
