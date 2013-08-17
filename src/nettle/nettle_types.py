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

"""petal/nettle/nettle_types.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Basic types for use with the Nettle cryptographic library.
"""

from __future__ import absolute_import

import cffi

ffi = cffi.FFI()
ffi.cdef("""
    #define NETTLE_TYPES_H ...

    /* Pretend these types always exists. Nettle doesn't use them. */
    static const int _STDINT_HAVE_INT_FAST32_T;

    /* Randomness. Used by key generation and dsa signature creation. */
    typedef void nettle_random_func(void *ctx, size_t length, uint8_t *dst);

    /* Progress report function, mainly for key generation. */
    typedef void nettle_progress_func(void *ctx, int c);

    /* Realloc function, used by struct nettle_buffer. */
    typedef void *nettle_realloc_func(void *ctx, void *p, size_t length);

    /* Ciphers */
    typedef void nettle_set_key_func(void *ctx, size_t length,
                                     const uint8_t *key);

    /* Uses a void * for cipher contexts.

       For block ciphers it would make sense with a const void * for the
       context, but we use the same typedef for stream ciphers where the
       internal state changes during the encryption. */
    typedef void nettle_crypt_func(void *ctx, size_t length, uint8_t *dst,
			           const uint8_t *src);

    /* Hash algorithms */
    typedef void nettle_hash_init_func(void *ctx);
    typedef void nettle_hash_update_func(void *ctx, size_t length,
				         const uint8_t *src);
    typedef void nettle_hash_digest_func(void *ctx, size_t length,
                                         uint8_t *dst);

    /* ASCII armor codecs. NOTE: Experimental and subject to change. */
    typedef size_t nettle_armor_length_func(size_t length);
    typedef void nettle_armor_init_func(void *ctx);

    typedef size_t nettle_armor_encode_update_func(void *ctx,
                                                   uint8_t *dst,
                                                   size_t src_length,
                                                   const uint8_t *src);
    typedef size_t nettle_armor_encode_final_func(void *ctx, uint8_t *dst);
    typedef int nettle_armor_decode_update_func(void *ctx,
                                                size_t *dst_length,
                                                uint8_t *dst,
                                                size_t src_length,
                                                const uint8_t *src);
    typedef int nettle_armor_decode_final_func(void *ctx);
    """)
ffi.include(nettle_stdint.ffi)

lib = ffi.verify(
    """
    /* For size_t */
    #include <stddef.h>

    typedef void nettle_crypt_func(void *ctx, size_t length, uint8_t *dst,
                                   const uint8_t *src);
    """)

# class NettleTypes(type)
#

def crypt(ctx, length, dst, src):
    return lib.nettle_crypt_func(ctx, length, dst, src)

