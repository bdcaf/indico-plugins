# This file is part of the Indico plugins.
# Copyright (C) 2017 - 2021 Max Fischer, Martin Claus, CERN
#
# The Indico plugins are free software; you can redistribute
# them and/or modify them under the terms of the MIT License;
# see the LICENSE file for more details.
import os

from setuptools import find_packages, setup


repo_base_dir = os.path.abspath(os.path.dirname(__file__))
# pull in the packages metadata
package_about = {}
with open(os.path.join(repo_base_dir, 'indico_sixpay', '__about__.py')) as about_file:
    exec(about_file.read(), package_about)

setup(
    name=package_about['__title__'],
    version=package_about['__version__'],
    description=package_about['__summary__'],
    long_description=package_about['__doc__'].strip(),
    author=package_about['__author__'],
    author_email=package_about['__email__'],
    url=package_about['__url__'],
    entry_points={
        'indico.plugins': {
            'payment_sixpay = indico_sixpay.plugin:SixpayPaymentPlugin'
        }
    },
    packages=find_packages(),
    package_data={'indico_sixpay': ['templates/*.html']},
    install_requires=['requests', 'indico>=3.0', 'iso4217'],
    python_requires='~=3.9.0',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Communications :: Conferencing',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    zip_safe=False,
    keywords='indico epayment six sixpay plugin',
)
