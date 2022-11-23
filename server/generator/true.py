import logging
from jsonpath_ng import parse

logger = logging.getLogger(__name__)


# set a target true
def generate(ctx, params, doc, target):
    jsonpath_expr = parse(target)
    doc = jsonpath_expr.update(doc, True)
    return doc
