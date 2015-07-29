import marshal
import types
from learning.model.save import DEFAULT_FILE

# NOTE: this is kinda dumb...have to import all dependencies of 'evaluate' here to get it to work
from learning.features.create import add_features, add_text


def load_model(filename):
    with open(filename, 'rb+') as f:
        evaluate = marshal.load(f)
    return types.FunctionType(evaluate, globals(), 'x')


if __name__ == '__main__':
    m = load_model(DEFAULT_FILE)
    print m('http://amidumb.com')
