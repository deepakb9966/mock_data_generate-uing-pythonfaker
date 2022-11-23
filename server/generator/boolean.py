import logging
from jsonpath_ng import parse
import util

logger = logging.getLogger(__name__)


# set a target true or false based on a weight
def generate(ctx, params, doc, target):
    result = util.made_weight(params.get('weight'))

    jsonpath_expr = parse(target)
    doc = jsonpath_expr.update(doc, result)
    return doc
