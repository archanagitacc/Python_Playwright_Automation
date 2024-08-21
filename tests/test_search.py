from models.search import SearchPage
import sys
from playwright.sync_api import Page, expect

# adding Folder_2 to the system path
#sys.path.append( '../')

def test_has_title(page: Page):
# in the test
    search_page = SearchPage(page)
    search_page.navigate()
    search_page.search("search query")
    