# Main settings
AUTHOR = 'sm4x'
SITENAME = 'B-Min'
SITEURL = "https://mysite.com" # See RELATIVE_URLS below for Development
PATH = "content"
TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = "%d %b %Y"
SUMMARY_MAX_LENGTH = 40
DELETE_OUTPUT_DIRECTORY = True

# Theme specific
THEME = "themes/bootstrap-minimal/"
THEME_STATIC_DIR = 'theme' # Default
THEME_STATIC_PATHS = ['static'] # Default
CSS_FILE = 'main.css' # Default

# Static pages
TEMPLATE_PAGES = {
    "pages/index.html": "index.html",
    "pages/404.html": "404.html",
    "pages/contact.html": "contact.php",
}
 

DIRECT_TEMPLATES = [] 
# DIRECT_TEMPLATES = ['index', 'authors', 'categories', 'tags', 'archives']
# List of templates that are used directly to render content. Typically direct templates are used to generate 
# index pages for collections of content (e.g., category and tag index pages). If the author, category and tag 
# collections are not needed, set DIRECT_TEMPLATES = ['index', 'archives']

# Static paths of the website
# The _redirects file is used by Netlify to create redirect rules
STATIC_PATHS = ["images"]
PAGE_PATHS = ['pages']
# Settings for the URLs of the blog and the articles
ARTICLE_PATHS = ["blog"]
ARTICLE_URL = "blog/{slug}/"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"
INDEX_SAVE_AS = "blog.html"

# Enable document-relative URLs when developing
RELATIVE_URLS = True

# Disable unneeded blog features
ARCHIVES_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAGS_SAVE_AS = ""

# Feed generation off while developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False




