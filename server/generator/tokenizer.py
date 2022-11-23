import logging
from jsonpath_ng import parse

logger = logging.getLogger(__name__)


# given a jsonpath to a string value, split the string into tokens and insert one of
# tokens into the target jsonpath.
def generate(ctx, params, doc, target):
    input_path = params['input']
    token = params['token']
    print(input_path)
    print(token)
    logger.debug("getting token '{}' from '{}'".format(token, input_path))

    # put the name at the target

    jsonpath_expr = parse(input_path)
    # doc = jsonpath_expr.update(doc, str.split()[token])
    # print(jsonpath_expr.find())
    str = jsonpath_expr.find(doc)[0].value
    logger.debug("got '{}' to tokenize".format(str))
    # put the name at the target
    jsonpath_expr = parse(target)
    doc = jsonpath_expr.update(doc, str.split()[token])

    return doc
