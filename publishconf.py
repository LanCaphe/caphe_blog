# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://lancaphe.github.io/caphe_blog/"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = 'feeds/all.rss.xml'


DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
FEED_RSS = None
FEED_ATOM = None
FEED_ALL_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# DISQUS_SITENAME = ""
