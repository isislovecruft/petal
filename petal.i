%module petal

  %{
  #include <time.h>
  #include <stddef.h>
  #include "include/nettle/nettle-stdint.h"
  #include "include/nettle/nettle-internal.h"
  #include "include/nettle/nettle-meta.h"
  #include "include/nettle/nettle-types.h"
  #include "include/nettle/bignum.h"
  #include "include/nettle/pgp.h"
  %}

%include "include/nettle/pgp.h"
