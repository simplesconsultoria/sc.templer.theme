# -*- coding:utf-8 -*-

import os
from setuptools import setup, find_packages

version = '20111209.01'

setup(
    name='sc.templer.theme',
    version=version,
    description="Base templer structures for Simples Consultoria.",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "INSTALL.txt")).read() + "\n" +
                       open(os.path.join("docs", "CREDITS.txt")).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone :: 4.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='simples_consultoria web command-line skeleton project',
    author='Simples Consultoria',
    author_email='products@simplesconsultoria.com.br',
    url='http://www.simplesconsultoria.com.br/',
    namespace_packages=['sc', 'sc.templer'],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        "sc.templer.core",
    ],
    entry_points="""
    [paste.paster_create_template]
    theme_diazo = sc.templer.theme.diazo:Diazo
    theme_plone = sc.templer.theme.plone:PloneTheme
    """,
    )
