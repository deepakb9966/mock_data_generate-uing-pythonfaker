import logging
import numpy
from jsonpath_ng import parse
import util

logger = logging.getLogger(__name__)


# generate a random name

def generate(ctx, params, doc, target):
    # check if we already have a name generated for this discriminator
    discriminator = params['discriminator']
    print(discriminator)
    if discriminator not in ctx:
        ctx[discriminator] = {}

        # gender matters for the name, randomly pick one if not already given.
        gender = ['male','female','other'][numpy.random.randint(3)]
        ctx[discriminator]['gender'] = gender

        fake = ctx['fake']
        if gender == 'male':
            prefix = fake.prefix_male()
            first_name = fake.first_name_male()
            last_name = fake.last_name_male()
            suffix = fake.suffix_male()
        elif  gender == 'female':
            prefix = fake.prefix_female()
            first_name = fake.first_name_female()    
            last_name = fake.last_name_female()
            suffix = fake.suffix_female()
        else:
            prefix = fake.prefix_nonbinary()
            first_name = fake.first_name_nonbinary()
            last_name = fake.last_name_nonbinary()
            suffix = fake.suffix_nonbinary()

        ctx[discriminator]['text'] = f'{prefix} {first_name} {last_name} {suffix}'.strip()
        ctx[discriminator]['family'] = last_name
        ctx[discriminator]['given'] = first_name
        ctx[discriminator]['prefix'] = prefix
        ctx[discriminator]['suffix'] = suffix

    # determine the address part requested
    part = target.rsplit('.',1)[1]

    # blank out if weighted items fail
    if part == 'prefix' and not util.made_weight(params.get('weight')):
        ctx[discriminator]['prefix'] = ''
    if part == 'suffix' and not util.made_weight(params.get('weight')):
        ctx[discriminator]['suffix'] = ''

    logger.info(f"generated name '{ctx[discriminator][part]}' given gender '{ctx[discriminator]['gender']}'")

    # put the name at the target
    jsonpath_expr = parse(target)
    doc = jsonpath_expr.update(doc, ctx[discriminator][part])

    return doc
