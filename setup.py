#!/usr/bin/env python
# Copyright (c) 2013 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# THIS FILE IS MANAGED BY THE GLOBAL REQUIREMENTS REPO - DO NOT EDIT
import setuptools

setuptools.setup(
    setup_requires=['pbr'],
    pbr=True)


# """
# Python openstack client which interacts with the OS restful api directly
# """
# from setuptools import find_packages, setup
#
# dependencies = ['click','testtools', 'mock']
#
# setup(
#     name='os_restful_client',
#     version='0.0.1',
#     url='https://github.com/LIP-Computing/os_restful_client',
#     license='APACHE 2.0',
#     author='Jorge Sevilla',
#     author_email='jorgesece@lip.pt',
#     description='Python openstack client which interacts with the OS restful api directly',
#     long_description=__doc__,
#     packages=find_packages(exclude=['tests']),
#     include_package_data=True,
#     zip_safe=False,
#     platforms='any',
#     install_requires=dependencies,
#     entry_points={
#         'console_scripts': [
#             'os_restful = os_restfulcli.client.cli:openstack',
#         ],
#     },
#     classifiers=[
#         # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
#         # 'Development Status :: 1 - Planning',
#         # 'Development Status :: 2 - Pre-Alpha',
#         # 'Development Status :: 3 - Alpha',
#         'Development Status :: 4 - Beta',
#         # 'Development Status :: 5 - Production/Stable',
#         # 'Development Status :: 6 - Mature',
#         # 'Development Status :: 7 - Inactive',
#         'Environment :: Console',
#         'Intended Audience :: Developers',
#         'License :: OSI Approved :: Apache License',
#         'Operating System :: Unix',
#         'Programming Language :: Python',
#         'Programming Language :: Python :: 2',
#         'Programming Language :: Python :: 3',
#         'Topic :: Software Development :: Libraries :: Python Modules',
#     ]
# )
