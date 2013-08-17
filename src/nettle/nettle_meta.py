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

"""petal/nettle/nettle_meta.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
I'm So Meta Even This Acronym
"""

from __future__ import absolute_import

import cffi

ffi = cffi.FFI()
ffi.cdef("""
    #define NETTLE_META_H_INCLUDED ...

    struct nettle_cipher{
      const char *name;
      unsigned context_size;

      /* Zero for stream ciphers */
      unsigned block_size;

      /* Suggested key size; other sizes are sometimes possible. */
      unsigned key_size;

      nettle_set_key_func *set_encrypt_key;
      nettle_set_key_func *set_decrypt_key;

      nettle_crypt_func *encrypt;
      nettle_crypt_func *decrypt;
    };

    #define _NETTLE_CIPHER(name, NAME, key_size) {	\
    #name #key_size,				\
    sizeof(struct name##_ctx),			\
    NAME##_BLOCK_SIZE,				\
    key_size / 8,					\
    (nettle_set_key_func *) name##_set_key,	\
    (nettle_set_key_func *) name##_set_key,	\
    (nettle_crypt_func *) name##_encrypt,		\
    (nettle_crypt_func *) name##_decrypt,		\
    }

    #define _NETTLE_CIPHER_SEP(name, NAME, key_size) {	\
    #name #key_size,					\
    sizeof(struct name##_ctx),				\
    NAME##_BLOCK_SIZE,					\
    key_size / 8,						\
    (nettle_set_key_func *) name##_set_encrypt_key,	\
    (nettle_set_key_func *) name##_set_decrypt_key,	\
    (nettle_crypt_func *) name##_encrypt,			\
    (nettle_crypt_func *) name##_decrypt,			\
    }

    #define _NETTLE_CIPHER_SEP_SET_KEY(name, NAME, key_size) {\
    #name #key_size,					\
    sizeof(struct name##_ctx),				\
    NAME##_BLOCK_SIZE,					\
    key_size / 8,						\
    (nettle_set_key_func *) name##_set_encrypt_key,	\
    (nettle_set_key_func *) name##_set_decrypt_key,	\
    (nettle_crypt_func *) name##_crypt,			\
    (nettle_crypt_func *) name##_crypt,			\
    }

    #define _NETTLE_CIPHER_FIX(name, NAME) {	\
    #name,						\
    sizeof(struct name##_ctx),				\
    NAME##_BLOCK_SIZE,					\
    NAME##_KEY_SIZE,					\
    (nettle_set_key_func *) name##_set_key,		\
    (nettle_set_key_func *) name##_set_key,		\
    (nettle_crypt_func *) name##_encrypt,			\
    (nettle_crypt_func *) name##_decrypt,			\
    }

    /* null-terminated list of ciphers implemented by this version of nettle */
    extern const struct nettle_cipher * const nettle_ciphers[];

    extern const struct nettle_cipher nettle_aes128;
    extern const struct nettle_cipher nettle_aes192;
    extern const struct nettle_cipher nettle_aes256;

    extern const struct nettle_cipher nettle_arcfour128;

    extern const struct nettle_cipher nettle_camellia128;
    extern const struct nettle_cipher nettle_camellia192;
    extern const struct nettle_cipher nettle_camellia256;

    extern const struct nettle_cipher nettle_cast128;

    extern const struct nettle_cipher nettle_serpent128;
    extern const struct nettle_cipher nettle_serpent192;
    extern const struct nettle_cipher nettle_serpent256;

    extern const struct nettle_cipher nettle_twofish128;
    extern const struct nettle_cipher nettle_twofish192;
    extern const struct nettle_cipher nettle_twofish256;

    extern const struct nettle_cipher nettle_arctwo40;
    extern const struct nettle_cipher nettle_arctwo64;
    extern const struct nettle_cipher nettle_arctwo128;
    extern const struct nettle_cipher nettle_arctwo_gutmann128;

    struct nettle_hash {
      const char *name;

      /* Size of the context struct */
      unsigned context_size;

      /* Size of digests */
      unsigned digest_size;
  
      /* Internal block size */
      unsigned block_size;

      nettle_hash_init_func *init;
      nettle_hash_update_func *update;
      nettle_hash_digest_func *digest;
    };

    #define _NETTLE_HASH(name, NAME) {            \
      #name,                                      \
      sizeof(struct name##_ctx),                  \
      NAME##_DIGEST_SIZE,                         \
      NAME##_DATA_SIZE,                           \
      (nettle_hash_init_func *) name##_init,      \
      (nettle_hash_update_func *) name##_update,  \
      (nettle_hash_digest_func *) name##_digest   \
    } 

    /* null-terminated list of digests implemented by this version of nettle */
    extern const struct nettle_hash * const nettle_hashes[];

    extern const struct nettle_hash nettle_md2;
    extern const struct nettle_hash nettle_md4;
    extern const struct nettle_hash nettle_md5;
    extern const struct nettle_hash nettle_gosthash94;
    extern const struct nettle_hash nettle_ripemd160;
    extern const struct nettle_hash nettle_sha1;
    extern const struct nettle_hash nettle_sha224;
    extern const struct nettle_hash nettle_sha256;
    extern const struct nettle_hash nettle_sha384;
    extern const struct nettle_hash nettle_sha512;
    extern const struct nettle_hash nettle_sha3_224;
    extern const struct nettle_hash nettle_sha3_256;
    extern const struct nettle_hash nettle_sha3_384;
    extern const struct nettle_hash nettle_sha3_512;

    struct nettle_armor {
      const char *name;
      unsigned encode_context_size;
      unsigned decode_context_size;
      unsigned encode_final_length;

      nettle_armor_init_func *encode_init;
      nettle_armor_length_func *encode_length;
      nettle_armor_encode_update_func *encode_update;
      nettle_armor_encode_final_func *encode_final;
  
      nettle_armor_init_func *decode_init;
      nettle_armor_length_func *decode_length;
      nettle_armor_decode_update_func *decode_update;
      nettle_armor_decode_final_func *decode_final;
    };

    #define _NETTLE_ARMOR(name, NAME) {				\
    #name,							\
    sizeof(struct name##_encode_ctx),				\
    sizeof(struct name##_decode_ctx),				\
    NAME##_ENCODE_FINAL_LENGTH,					\
    (nettle_armor_init_func *) name##_encode_init,		\
    (nettle_armor_length_func *) name##_encode_length,		\
    (nettle_armor_encode_update_func *) name##_encode_update,	\
    (nettle_armor_encode_final_func *) name##_encode_final,	\
    (nettle_armor_init_func *) name##_decode_init,		\
    (nettle_armor_length_func *) name##_decode_length,		\
    (nettle_armor_decode_update_func *) name##_decode_update,	\
    (nettle_armor_decode_final_func *) name##_decode_final,	\
    }

    #define _NETTLE_ARMOR_0(name, NAME) {			\
    #name,							\
    0,								\
    sizeof(struct name##_decode_ctx),				\
    NAME##_ENCODE_FINAL_LENGTH,					\
    (nettle_armor_init_func *) name##_encode_init,		\
    (nettle_armor_length_func *) name##_encode_length,		\
    (nettle_armor_encode_update_func *) name##_encode_update,	\
    (nettle_armor_encode_final_func *) name##_encode_final,	\
    (nettle_armor_init_func *) name##_decode_init,		\
    (nettle_armor_length_func *) name##_decode_length,		\
    (nettle_armor_decode_update_func *) name##_decode_update,	\
    (nettle_armor_decode_final_func *) name##_decode_final,	\
    }

    /* null-terminated list of armor schemes implemented by this
     * version of nettle */
    extern const struct nettle_armor * const nettle_armors[];
    extern const struct nettle_armor nettle_base64;
    extern const struct nettle_armor nettle_base16;
""")

lib = ffi.verify("""
    #include "nettle-types.h"
""")
