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
    #define NETTLE_INTERNAL_H_INCLUDED ...

    /* Temporary allocation, for systems that don't support alloca. Note
      * that the allocation requests should always be reasonably small, so
      * that they can fit on the stack. For non-alloca systems, we use a
      * fix maximum size, and abort if we ever need anything larger. */
    #if HAVE_ALLOCA
    # define TMP_DECL(name, type, max) type *name
    # define TMP_ALLOC(name, size) (name = alloca(sizeof (*name) * (size)))
    #else /* !HAVE_ALLOCA */
    # define TMP_DECL(name, type, max) type name[max]
    # define TMP_ALLOC(name, size) \
    do { if ((size) > (sizeof(name) / sizeof(name[0]))) abort(); } while (0)
    #endif 

    /* Arbitrary limits which apply to systems that don't have alloca */
    static const int NETTLE_MAX_BIGNUM_BITS;
    static const float NETTLE_MAX_BIGNUM_SIZE;
    static const int NETTLE_MAX_HASH_BLOCK_SIZE;
    static const int NETTLE_MAX_HASH_DIGEST_SIZE;
    static const int NETTLE_MAX_SEXP_ASSOC;
    static const int NETTLE_MAX_CIPHER_BLOCK_SIZE;

    /* Doesn't quite fit with the other algorithms, because of the weak
     * keys. Weak keys are not reported, the functions will simply crash
     * if you try to use a weak key. */
    extern const struct nettle_cipher nettle_des;
    extern const struct nettle_cipher nettle_des3;
    extern const struct nettle_cipher nettle_blowfish128;

    /* For benchmarking only, sets no iv and lies about the block size. */
    extern const struct nettle_cipher nettle_salsa20;
    extern const struct nettle_cipher nettle_salsa20r12;

    /* Glue to openssl, for comparative benchmarking. Code in
     * examples/nettle-openssl.c. */
    extern const struct nettle_cipher nettle_openssl_aes128;
    extern const struct nettle_cipher nettle_openssl_aes192;
    extern const struct nettle_cipher nettle_openssl_aes256;
    extern const struct nettle_cipher nettle_openssl_arcfour128;
    extern const struct nettle_cipher nettle_openssl_blowfish128;
    extern const struct nettle_cipher nettle_openssl_des;
    extern const struct nettle_cipher nettle_openssl_cast128;

    extern const struct nettle_hash nettle_openssl_md5;
    extern const struct nettle_hash nettle_openssl_sha1;

    /* Tentative interface for "authenticated encryption with associated
    data" algorithms. Should be moved to nettle-meta.h when stable. */
    struct nettle_aead{
      const char *name;
      size_t context_size;

      /* Block size of the input, and the size of the output digest */
      size_t block_size;

      /* Suggested key size; other sizes are sometimes possible. */
      size_t key_size;

      nettle_set_key_func *set_key;
      nettle_set_key_func *set_iv;
      nettle_hash_update_func *update;
      nettle_crypt_func *encrypt;
      nettle_crypt_func *decrypt;
      nettle_hash_digest_func *digest;
    };

    #define _NETTLE_AEAD(type, TYPE, name, key_size) {	  \
      #type "-" #name #key_size,                          \
      sizeof(struct type##_##name##_ctx),		  \
      TYPE##_BLOCK_SIZE,		                  \
      key_size / 8,                                       \
      (nettle_set_key_func *) type##_##name##_set_key,	  \
      (nettle_set_key_func *) type##_##name##_set_iv,	  \
      (nettle_hash_update_func *) type##_##name##_update, \
      (nettle_crypt_func *) type##_##name##_encrypt,	  \
      (nettle_crypt_func *) type##_##name##_decrypt,	  \
      (nettle_hash_digest_func *) type##_##name##_digest, \
    }

    extern const struct nettle_aead nettle_gcm_aes128;
    extern const struct nettle_aead nettle_gcm_aes192;
    extern const struct nettle_aead nettle_gcm_aes256;

    extern const struct nettle_aead nettle_gcm_camellia128;
    extern const struct nettle_aead nettle_gcm_camellia192;
    extern const struct nettle_aead nettle_gcm_camellia256;

    extern const struct nettle_aead nettle_gcm_serpent128;
    extern const struct nettle_aead nettle_gcm_serpent192;
    extern const struct nettle_aead nettle_gcm_serpent256;

    extern const struct nettle_aead nettle_gcm_twofish128;
    extern const struct nettle_aead nettle_gcm_twofish192;
    extern const struct nettle_aead nettle_gcm_twofish256;
""")

lib = ffi.verify("""
    #include "nettle-meta.h"
""")
