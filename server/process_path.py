import logging
import importlib

# import export as export

# export PYTHONPATH=/home/deep/Desktop/mock_data_generator-main
logger = logging.getLogger(__name__)
def process(ctx, params, doc, path):
    logger.debug("processing path: "+str(path))
    target = path['path']

    generator = 'generator.{}'.format(path['generator'])

    params = path.get('params')
    if params is None:
        params = {}

    logger.debug("using params: "+str(params))
    logger.info("calling generator '{}'".format(generator))

    gen_function = 'generator.{}.generate'.format(path['generator'])
    mod_name, func_name = gen_function.rsplit('.',1)
    # print('y8why8thhibw',type(mod_name))
    # print(importlib.import_module(mod_name))
    mod = importlib.import_module(mod_name)

    func = getattr(mod, func_name)

    # call generator
    doc = func(ctx, params, doc, target)

    return doc