#!venv/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/freq_api/")

from freq_api import app as application
