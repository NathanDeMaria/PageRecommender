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
    # TODO: actually get the text
    return raw_html