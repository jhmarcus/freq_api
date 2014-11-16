#!/usr/bin/python
import os
import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/freq_api/")

BASE_DIR = os.path.join(os.path.dirname(__file__))
activate_this = os.path.join(BASE_DIR, "venv/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

from freq_api import app as application
