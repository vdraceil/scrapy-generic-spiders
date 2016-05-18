import logging

from constants import Regex
from controller import SpiderController


logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# create an instance of the Controller
controller = SpiderController()

# define a scraping job (website_list)
website_list = [
    # (<site>, <max_depth>)
    ('http://www.uniquemetalworks.net', 2),
]

# define patterns
pattern_dict = {
    'email': Regex.PT_EMAIL
}

# define output file
out_file = './output0.txt'

# invoke the Crawl API
# it will block till it completes
controller.contact_info_crawl(website_list, pattern_dict, out_file)
print "CRAWL COMPLETE!!"