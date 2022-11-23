# Author: Tim Fleming, Mar 2022

import json
import yaml

import logging
import logging.config

from argparse import ArgumentParser

# from .process_path import *
import process_path

from faker import Faker

# global variables
args = None
cfg = None

logger = logging.getLogger()


def main(args):
    # read configuration
    print('arguments', args)
    init(args)

    # setup logging
    setup_logger()

    logger.info("running data rules '{}'...".format(args.rules_fname))

    # read the rules file
    fin = open(args.rules_fname, 'r')
    rules_json = json.load(fin)

    # populate the context
    ctx = rules_json['context']
    ctx['input_dir'] = args.input_dir
    ctx['fake'] = Faker(ctx.get('locale'))
    ctx['persistent_keys'] = cfg['context']['persistent_keys']

    doc = None

    # process top level paths
    for path in rules_json['paths']:
        # print(path)
        doc = process_path.process(ctx, None, doc, path)
        # print('doc', doc)

    # write output
    with open(args.output_fname, "w") as fout:
        json.dump(doc, fout)

    msg = 'Done. Output written to {}\n'.format(args.output_fname)
    print(msg)
    logger.info(msg)


# initialization
def init(args):
    global cfg

    #  parse config file
    config_file = args.config
    logger.info('reading config file "{}"'.format(config_file))
    with open(config_file, 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.SafeLoader)


def setup_logger():
    global cfg

    logging.config.dictConfig(cfg['logging'])

    logger = logging.getLogger(__name__)
    logger.info("main is starting")

print("__main__: ",__name__)

if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("-c", "--config", dest="config",
                        help="location of configuration file", default="config.yml")
    parser.add_argument("-i", "--input", dest="input_dir",
                        help="Directory root for sample json files")
    parser.add_argument("-r", "--rules", dest="rules_fname",
                        help="JSON file that gives the data generation rules")
    parser.add_argument("-o", "--output", dest="output_fname",
                        help="Path and filename for the output JSON file")
    parser.add_argument("--log_level", dest="log_level",
                        help="set root logging level")

    args = parser.parse_args()

    # print(args)
    main(args)
