import os
import marshal
from learning.features.create import create_data, to_dict, add_features
from learning.features.text import add_text


DEFAULT_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'model.pickle')


def save_model(filename):
    """
    Saves a model to a file to use later
    :param filename: marshal filename
    """
    model = create_model()
    with open(filename, 'wb+') as f:
        marshal.dump(model.func_code, f)


def create_model():
    """
    Use the data to create a model
    :return: model function
    """
    feature_generators = [to_dict, add_text]
    data = list(create_data(feature_generators))

    # TODO: actually create model based on the data.
    # Wrap the model in a function that returns a probability
    # given a url of a new site. For now, I'm doing this model
    def evaluate(url):
        featured = list(add_features([add_text], [dict(url=url)]))[0]
        if 'Taylor Swift' in featured['text']:
            return 1.0
        return 0.0

    return evaluate


if __name__ == '__main__':
    save_model(DEFAULT_FILE)
