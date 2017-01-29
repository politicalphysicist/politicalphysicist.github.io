#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = u'C. MacMackin'
SITENAME = u'The Political Physicist'
SITESUBTITLE = u'&nbspThe ramblings of a left-wing grad student&hellip;'# in the city of dreaming spires&hellip;'
SITEURL = 'https://politicalphysicist.github.io'
PROFILE_IMAGE = '{filename}/images/subfusc.jpg'
FAVICON = '{filename}/images/favicon.png'
BACKDROP_IMAGE = '{filename}/images/oxford.jpg'
BLOGKEYWORDS = ('Socialism','Physics','Mathematics','Politics',
    'Environment','Computers','Linux','Open Source','Climate')
SITE_DESCRIPTION = "I am a DPhil student at Oxford studying Atmospheric, "\
                   "Oceanic and Planetary Physics. Outside of my studies, "\
                   "I am interested in computer programming and "\
                   "left-wing politics. "

TIMEZONE = 'Europe/London'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Linux Mint', 'http://linuxmint.com/'),
          ('New Scientist', 'http://newscientist.com'),
          ('Degenerate Conic','http://degenerateconic.com/'),
          ('Michael Laxer','http://rabble.ca/taxonomy/term/19493/0'),
          ('Socialist Project', 'http://www.socialistproject.ca'),
          ('SMBC', 'http://www.smbc-comics.com/'),
          ('XKCD', 'http://xkcd.com/'),
          ('AOPP Subdepartment','http://www2.physics.ox.ac.uk/research/atmospheric-oceanic-and-planetary-physics'),)

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search'))

DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 2
PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')

SOCIAL=[('Facebook','https://www.facebook.com/cmacmackin'),
        ('GitHub','https://github.com/cmacmackin')]
EMAIL='politicalphysicist@gmail.com'

THEME = "./backdrop"
STATIC_PATHS = ['images','attachments']

PLUGIN_PATHS = ['../../Code/pelican-plugins-local',]
PLUGINS = ['sitemap', 'render_math', 'representative_image', 'tipue_search', 'tag_cloud', 'figure-ref']#, 'github_activity']
#GITHUB_ACTIVITY_MAX_ENTRIES = 5
MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra','figureAltCaption']
TYPOGRIFY = True
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.7,
        'indexes': 0.5,
        'pages': 0.3
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'monthly',
        'pages': 'monthly'
    }
}

LICENSE = '<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/80x15.png" /></a>'

# Number of tags
TAG_CLOUD_MAX_ITEMS=15
YEAR = date.today().year

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
