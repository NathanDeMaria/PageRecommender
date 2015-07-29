import os
import pickle
from urllib2 import Request, urlopen


PICKLE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pickles')


def smart_wget(url):
    """
    Gets the contents of a URL. Firsts, checks a
    local pickle "cache", otherwise goes and
    gets the page, caching it for later
    :param url: URL of article to get text for
    :return: page data for the given URL
    """
    safe_filename = '{0}.pickle'.format(filter(str.isalnum, str(url)))
    safe_file = os.path.join(PICKLE_DIR, safe_filename)

    page_data = _read_pickle(safe_file)
    if page_data is not None:
        return page_data

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) '
                                              'AppleWebKit/537.36 (KHTML, like Gecko) '
                                              'Chrome/44.0.2403.107 Safari/537.36'})
    response = urlopen(req)
    page_data = response.read()

    _save_pickle(safe_file, page_data)

    return page_data


def _read_pickle(safe_file):
    """
    Read the pickle file
    :param safe_file: path to pickle file
    :return: contents of the pickle-cache, None if it doesn't exist
    """
    if os.path.isfile(safe_file):
        with open(safe_file, 'rb+') as f:
            return pickle.load(f)

    return None


def _save_pickle(safe_file, page_data):
    """
    Saves the page in a "pickle-cache"
    :param safe_file: path to pickle file
    :param page_data: text for the URL request
    """
    with open(safe_file, 'wb+') as f:
        pickle.dump(page_data, f)
