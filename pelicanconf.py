from datetime import datetime

AUTHOR = 'Lan Cà phê'
SITENAME = 'Sudio Cà phê'
SITEURL = "https://lancaphe.github.io/caphe_blog/"
SITETITLE = 'Studio Cà phê'
SITESUBTITLE = 'Développeuse à roulettes doptée au café'
SITELOGO = "/images/avatar.jpg"
SITEDESCRIPTION = "Les aventures d'une dêveloppeuse en fauteuil"

PATH = "content"

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Desactive some options
FEED_ALL_ATOM = None

CATEGORY_FEED_ATOM = None
CATEGORY_URL = False
CATEGORY_SAVE_AS = False
CATEGORIES_SAVE_AS = False
CATEGORY_FEED_RSS = None

TRANSLATION_FEED_ATOM = None

AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
AUTHOR_URL = False
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False

# Social widget
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/thanhlandoublier/"),
    # ("Github", "https://github.com/LanCaphe"),
    ("Blusky", "https://bsky.app/profile/lancaphe.bsky.social")
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
STATIC_PATHS = ['images']
ROBOTS = 'index, follow'
OUTPUT_PATH = 'output/'

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

ARCHIVES_SAVE_AS = 'blog/index.html'
YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

THEME = "Flex"

MAIN_MENU = True
MENUITEMS = (
    ('Archives', '/archives'),
    ('Categories', '/categories'),
    ('Tags', '/tags')
)

DISABLE_URL_HASH = True

COPYRIGHT_YEAR = datetime.now().year
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True
