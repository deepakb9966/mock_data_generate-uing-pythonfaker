import logging
from jsonpath_ng import parse

logger = logging.getLogger(__name__)


# generate a random address

def generate(ctx, params, doc, target):
    # generate an address if we don't have one in the context
    if 'address' not in ctx:
        address = ctx['fake'].address() # [street, landmark, area, city, state, pincode]
        street = address.split('\n')[0]
        csz = address.split('\n')[1]

        ctx['address'] = {}
        ctx['address']['text'] = address
        ctx['address']['line'] = street
        ctx['address']['city'] = csz.split(',')[0]
        ctx['address']['district'] = ''
        ctx['address']['state'] = csz.rsplit(' ',2)[1]
        ctx['address']['postalCode'] = csz.rsplit(' ',1)[1]
        ctx['address']['country'] = ctx['fake'].current_country_code()

    # determine the address part requested
    part = target.rsplit('.',1)[1]
    logger.debug(f"getting '{part}' of address '{ctx['address']}")

    # put the name at the target
    jsonpath_expr = parse(target)
    doc = jsonpath_expr.update(doc, ctx['address'][part])

    return doc
