#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import versioneer
import petal

versioneer.versionfile_source = 'src/_version.py'
versioneer.versionfile_build  = 'src/_version.py'
versioneer.tag_prefix = ''
versioneer.parentdir_prefix = 'petal-'

__author__ = "Isis Agora Lovecruft, 0xA3ADB67A2CDB8B35"
__contact__ = 'isis@patternsinthevoid.net'
__url__ = 'https://github.com/isislovecruft/petal'

setuptools.setup(
    zipsafe=False,
    ext_modules=[petal.ffi.verifier.get_extension()],

    name = "petal",
    description="A Python wrapper for GnuPG",
    long_description = """\
This module provides a Python API for working with Nettle_, a low-level C \
library of cryptographic primitives.\

.. _Nettle: http://www.lysator.liu.se/~nisse/nettle/
""",
    license="3-Clause BSD",

    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),

    author=__author__,
    author_email=__contact__,
    maintainer=__author__,
    maintainer_email=__contact__,
    url=__url__,

    package_dir={'src': 'petal'},
    packages=['petal'],
    package_data={'': ['README', 'LICENSE', 'TODO', 'requirements.txt']},
    scripts=['versioneer.py'],
    test_suite='py.test.XXX',

    install_requires=['cffi>=0.7.2'],
    extras_require={'docs': ["Sphinx>=1.1", "repoze.sphinx"]},

    platforms="Linux",
    download_url="https://github.com/isislovecruft/petal/archive/master.zip",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Security :: Cryptography",
        "Topic :: Utilities",]
)
