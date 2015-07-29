from itertools import imap
from text import add_text


def create_data(feature_functions):
    """
    Creates the data in the form of a list of dicts,
    where each dict represents an Article and its features
    :param feature_functions: list of functions to apply to rows of the data
    :return: list of article dicts, with features included
    """
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_app.settings")
    from extension.models import Article

    articles = Article.objects.all()
    return add_features(feature_functions, articles)


def add_features(feature_functions, articles):
    """
    Adds features to each article based on feature functions
    :param feature_functions: list of functions to apply to rows of the data
    :param articles: list of articles to add features to
    :return: articles with added features
    """
    for feature in feature_functions:
        articles = imap(feature, articles)
    return articles


def to_dict(article):
    """
    Turns an Article into a dict representing its base info
    :param article: Article model
    :return: dict representing the Article model
    """
    return dict(
        time=article.access_time,
        response=article.response,
        url=article.url
    )


if __name__ == '__main__':
    feature_generators = [to_dict, add_text]
    print list(create_data(feature_generators))
