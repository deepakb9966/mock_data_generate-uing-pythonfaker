import json
import logging
import process_path
from jsonpath_ng import parse

# from openapi_server.controllers import run

# from openapi_server.controllers.mockdata_controller import return_c


# from mock_data.ru import get_count

# from mock_data.ru import get_count

logger = logging.getLogger(__name__)




def generate(ctx, params, doc, target):
    sample_fname = '{}/{}'.format(ctx['input_dir'], params['sample_file'])
    # count = params['count']
    count = 1
    print("collection", count)
    patient_id = params['patientId'] if ('patientId' in params) else ''
    logger.debug("params: " + str(params))
    result = []

    for idx in range(count):
        logger.info("loading sample json '{}' pass '{}'".format(
            sample_fname, str(idx + 1)))

        # clean up context each iteration
        new_ctx = {}
        for key in ctx['persistent_keys']:
            new_ctx[key] = ctx[key]
        ctx = new_ctx

        # load the sample json
        with open(sample_fname, 'r') as fin:
            doc = json.load(fin)

        # invoke each generator
        for path in params['paths']:
            doc = process_path.process(ctx, params, doc, path)

        result.append(doc)

    # replace target array
    logger.debug("updated doc at target '{}'".format(target))
    if target == '$':
        if patient_id:
            doc = {patient_id: result}
        else:
            doc = result
    else:
        jsonpath_expr = parse(target)
        jsonpath_expr.update(doc, result)

    return doc
