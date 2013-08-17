# -*- coding: utf-8 -*-
#
# :authors: Isis Agora Lovecruft <isis@patternsinthevoid.net> 0xA3ADB67A2CDB8B35
# :license: LGPLv3+
# :copyright: (c) 2013 Isis Agora Lovecruft
#             Nettle is copyright (c) 2002-2013 Niels Möller and others.
#             See included LICENSE file for details.
#
# This file is part of PETAL, a Python module for working with Nettle, a
# low-level C library for cryptographic primitives.
# 
# PETAL is free software: you can redistribute it and/or modify it under the
# terms of the Lesser GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
# 
# PETAL is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the Lesser GNU General Public License for
# more details.
# 
# You should have received a copy of the GNU General Public License along with
# PETAL. If not, see <http://www.gnu.org/licenses/>.
#
# Details for <sha1.h> file from Nettle: 
# The C implementation of the SHA1 message digest is written by Peter Gutmann,
# and hacked some more by Andrew Kuchling and Niels Möller. Released into the
# public domain. Assembler for x86, x86_64 and ARM by Niels Möller, released
# under the LGPL.

"""__init__.py
~~~~~~~~~~~~~~
Python Foreign-Function Interface wrappers for Nettle.
"""

from __future__ import absolute_import

import cffi

__all__ = ['lib', 'ffi']
