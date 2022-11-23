import logging
from jsonpath_ng import parse
import util

logger = logging.getLogger(__name__)


# set a target blank
def generate(ctx, params, doc, target):
    if util.made_weight(params.get('weight')):
        jsonpath_expr = parse(target)
        doc = jsonpath_expr.update(doc, '')
    return doc
