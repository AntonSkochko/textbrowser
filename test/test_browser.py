from textbrowser.browser import TextBrowser
from textbrowser.cache import BrowserCache
from textbrowser.argparser import BrowserArgParser
from textbrowser.utils import InvalidQueryException

import pytest

@pytest.fixture
def browser():
    args = BrowserArgParser.parse_args()
    return TextBrowser(BrowserCache(args))


@pytest.fixture
def cache():
    args = BrowserArgParser.parse_args('--foo 1'.split())
    return BrowserCache(args)


VALID_DOMAINS = [
    ('https://google.com', ('https://', 'google', 'com')),
    ('google.com', ('https://', 'google', 'com')),
    ('python.org', ('https://', 'python', 'org')),
]

INVALID_DOMAINS = [
    'https://google',
    'google'
    'https://+-=_.com'
]

def test_valid_domains(browser):
    for domain, expected in VALID_DOMAINS:
        assert expected == tuple(browser.parse_query(domain))

def test_invalid_domains(browser):
    for domain in INVALID_DOMAINS:
        with pytest.raises(InvalidQueryException):
            browser.parse_query(domain)

def test_requests(browser):
    pass
    # TODO
