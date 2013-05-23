#!/bin/bash
#-------------------------------------------------------------------------------
# make-venv.sh
# ------------
# Create a Python virtualenv with virtualenvwrapper for petal.
# 
# :authors: Isis Agora Lovecruft, 0xa3adb67a2cdb8b35
# :license: maybe AGPLv3, not sure yet
# :version: 0.0.1
#-------------------------------------------------------------------------------

source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv -a "$PWD" --no-site-packages --unzip-setuptools --distribute petal
