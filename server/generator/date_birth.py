import logging
from jsonpath_ng import parse
import util

logger = logging.getLogger(__name__)


# generate a random name

def generate(ctx, params, doc, target):
    dob = ctx['fake'].date_of_birth(minimum_age=params['minimum_age'], maximum_age=params['maximum_age'])
    logger.info(f"generated dob '{dob}'")

    # put the name at the target
    jsonpath_expr = parse(target)
    doc = jsonpath_expr.update(doc, util.format_date(dob))

    return doc
