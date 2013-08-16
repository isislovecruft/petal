#!/bin/bash
#-----------------------------------------------------------------------------
# make-venv.sh
# ------------
# Create a Python virtualenv with virtualenvwrapper for petal.
# 
# :authors: Isis Agora Lovecruft, 0xa3adb67a2cdb8b35
# :license: Three-Clause BSD
# :version: 0.0.1
#-----------------------------------------------------------------------------

source `which virutualenvwrapper.sh`
mkvirtualenv -a "$PWD" --unzip-setuptools --setuptools petal
