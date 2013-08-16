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

"""sha1.py
~~~~~~~~~~
SHA-1 hash digest functions.
"""

from __future__ import absolute_import

import cffi

from . import nettle_types

ffi = cffi.FFI()
ffi.cdef("""
    #define NETTLE_SHA1_H_INCLUDED ...

    /* Name mangling */
    #define sha1_init nettle_sha1_init
    #define sha1_update nettle_sha1_update
    #define sha1_digest nettle_sha1_digest
    """
    ## XXX #define SHA1_DIGEST_SIZE 20
    ## XXX #define SHA1_DATA_SIZE 64
    ## XXX #define _SHA1_DIGEST_LENGTH 5
    """
    /* SHA1 */
    static const int SHA1_DIGEST_SIZE;
    static const int SHA1_DATA_SIZE;

    /* Digest is kept internally as 5 32-bit words. */
    static const int _SHA1_DIGEST_LENGTH;

    struct sha1_ctx {
      uint32_t state[_SHA1_DIGEST_LENGTH];    /* State variables */
      uint32_t count_low, count_high;         /* 64-bit block count */
      uint8_t block[SHA1_DATA_SIZE];          /* SHA1 data buffer */
      unsigned int index;                     /* index into buffer */
    };

    void sha1_init(struct sha1_ctx *ctx);
    void sha1_update(struct sha1_ctx *ctx, size_t length, const uint8_t *data);
    void sha1_digest(struct sha1_ctx *ctx, size_t length, uint8_t *digest);

    /* Internal compression function. STATE points to 5 uint32_t words,
       and DATA points to 64 bytes of input data, possibly unaligned. */
    void _nettle_sha1_compress(uint32_t *state, const uint8_t *data);
    """)
ffi.include(nettle_types.ffi)

lib = ffi.verify(

)
