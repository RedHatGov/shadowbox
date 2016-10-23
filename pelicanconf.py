#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jamie Duncan'
SITENAME = u'Shadowbox'
#SITEURL = 'jduncan-rva.github.io'
SITEURL = 'https://www.rhshadowbox.com'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_DOMAIN = 'https://www.rhshadowbox.com'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_RSS = 'feeds/rss.xml'

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
        ('twitter', 'http://www.twitter.com/rh_shadowbox'),
        ('code', 'http://www.github.com/RedHatGov'),
    )

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['asciidoc_reader', 'sitemap', 'gravatar', 'filetime_from_git', 'gallery', 'thumbnailer', 'disqus_static']

THEME = "pelican-theme"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

STATIC_PATHS = [
    'ansible',
    'pictures',
    'extra/robots.txt',
    'extra/favicon.ico',
    'extra/CNAME'
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'}
}

# blueidea settings
DISPLAY_CATEGORIES_ON_SUBMENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_SEARCH_FORM = True

# thumbnailer settings
THUMBNAIL_DIR = 'pictures'
THUMBNAIL_KEEP_NAME = True
THUMBNAIL_KEEP_TREE = True

# disqus_static settings
DISQUS_SITENAME = 'shadowbox-1'
DISQUS_PUBLIC_KEY = 'Zuy9Hu0Lj35N0FNLnke5ye9No0cJhsBvZKNGJ701eIJQf4adgeKYnGeROOHm1OgG'
DISQUS_SECRET_KEY = 's8BQwXKdKek2WAAHeIGAo9yzQrAMFDGjmBr3OmYq5IewowmeASmPllkUlkYRipVs'

# Gallery settings

GALLERY_PATH = 'pictures/gallery'
RESIZE = [
        ('gallery', False, 200,200),
      ]
