from itertools import chain
from bs4 import BeautifulSoup, NavigableString, Comment
from wget import smart_wget


def add_text(article):
    """
    Adds a 'text' item to the article dict
    containing the get from the page for the article
    :param article: article dict
    :return: article dict with 'text' item
    """
    raw_html = smart_wget(article['url'])
    article['text'] = _get_text(raw_html)
    return article


def _get_text(raw_html):
    """
    Takes all the HTML for a page and parses
    out just the text contents
    :param raw_html: all the raw HTML for a page
    :return: just the text
    """
    bs = BeautifulSoup(raw_html)
    text_nodes = bs.find_all(_is_text_tag)
    text_elements = [_get_child_text(node) for node in text_nodes]
    return ' '.join(chain(*chain(*text_elements)))


def _get_child_text(node):
    """
    Get generator of all text children
    :param node: text-ish node
    :return: yields all text children
    """
    for child in node.children:
        if isinstance(child, NavigableString) and not isinstance(child, Comment):
            yield child.split()


def _is_text_tag(tag):
    """
    Function for filtering BeautifulSoup nodes down to
    nodes that have "interesting" text
    :param tag: soup tag
    :return: True if I care about the text inside this tag
    """
    return tag.name not in ['script', 'style']
