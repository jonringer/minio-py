# MinIO Python Library for Amazon S3 Compatible Cloud Storage, (C) 2015 MinIO, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import re
import sys

from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

version = ''
with open('minio/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

packages = [
    'minio',
    'minio.select',
]

requires = [
    'future',
    'urllib3',
    'pytz',
    'certifi',
    'python-dateutil',
]

tests_requires = [
    'nose',
    'mock',
    'Faker',
]

setup(
    name='minio',
    description='MinIO Python Library for Amazon S3 Compatible Cloud Storage for Python',
    author='MinIO, Inc.',
    url='https://github.com/minio/minio-py',
    download_url='https://github.com/minio/minio-py',
    author_email='dev@min.io',
    version=version,
    long_description_content_type='text/markdown',
    package_dir={'minio': 'minio'},
    packages=packages,
    install_requires=requires,
    tests_require=tests_requires,
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    long_description=readme,
    package_data={'': ['LICENSE', 'README.md']},
    include_package_data=True,
)
