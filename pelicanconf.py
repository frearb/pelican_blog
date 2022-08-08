AUTHOR = 'frearb'
SITENAME = '不系之舟'
SITEURL = ''
THEME = '../pelican-themes/pelican-hss'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'Chinese (Simplified)'

SUMMARY_MAX_LENGTH = 27

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('github', 'http://github.com/ametaireau'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARCHIVES_URL = 'archives.html'

STATIC_PATHS = [
    'images',
    'static',
    ]

TAGLINE = '信息浪潮中的一座孤岛'

# theme setting
USER_LOGO_URL = '/images/logo96.png'

CUSTOM_CSS_URL = '/static/custom.css'