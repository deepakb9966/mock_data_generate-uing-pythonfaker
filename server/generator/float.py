import logging
from jsonpath_ng import parse

logger = logging.getLogger(__name__)


# generate a random decimal number

def generate(ctx, params, doc, target):

    rand_num = ctx['fake'].random.uniform(params["min"], params["max"])
    rand_num = round(rand_num, 2)
    logger.info(f"generated random number '{rand_num}'")

    # put the name at the target
    jsonpath_expr = parse(target)
    doc = jsonpath_expr.update(doc, rand_num)

    return doc
