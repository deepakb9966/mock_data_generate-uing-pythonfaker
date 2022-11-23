import logging
from jsonpath_ng import parse
import util

logger = logging.getLogger(__name__)


# generate a random name

def generate(ctx, params, doc, target):
    start_date = None
    end_date = None
    rand_date = None
    # print(params)
    if 'from_date' in params and 'to_date' in params:
        start_date = params['from_date']
        end_date = params['to_date']
        rand_date = ctx['fake'].date_time_between(
            start_date=start_date, end_date=end_date)
    elif 'from_date' in params:
        start_date = params['from_date']
        end_date = 'now'
        rand_date = ctx['fake'].date_time_between(
            start_date=start_date, end_date=end_date)
    else:
        rand_date = ctx['fake'].date_time()

    logger.info(f"generated date '{rand_date}'")

    # put the name at the target
    jsonpath_expr = parse(target)
    doc = jsonpath_expr.update(doc, util.to_iso(rand_date))

    return doc
