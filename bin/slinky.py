#!/usr/bin/env python

import argparse
import os
import shutil
import sys
import time

from pyrannosaurus.utils import binary_to_zip, zip

def cwd():
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

sys.path.append('/Users/kcshafer/workspace/slinky/')

from app import utils, deploy, generate, retrieve

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Develop with Salesforce')

    ## verbs ##
    parser.add_argument('--auth', '-A', action='store_true', help='Store login information')
    parser.add_argument('--retrieve', '-R', action='store_true', help='Retrieve components')
    parser.add_argument('--deploy', '-D', action='store_true', help='Deploy components')
    parser.add_argument('--build', '-b', action='store_true', help='Build a single file')
    parser.add_argument('--generate', action='store_true', help='generate code templates')

    ## nouns ## 
    parser.add_argument('--username', '-u', action='store', type=str)
    parser.add_argument('--password', '-p', type=str, action='store')
    parser.add_argument('--production', '-P', action='store_true', help='Authenticate with production')
    parser.add_argument('--file', '-f', type=str, action='store', help='File to build')
    parser.add_argument('--name', '-n', type=str, default=None, action='store', help='Name of new file')
    parser.add_argument('--type', '-t', type=str, action='store', help='Type of template to generate')
    parser.add_argument('--sObject', type=str, action='store', help='Type of sobject for trigger or standard controller')


    args = parser.parse_args()

    if args.auth:
        if args.username and args.password:
            utils.build_credentials(args.username, args.password, production=args.production)
        else:
            parser.error("Must include username and password when building authentication file")
    elif args.generate:
        generate.generate(args.type, args.name, args.sObject)
    elif not os.path.isfile('auth.ini'):
        print os.getcwd()
        parser.error("Must run slinky --auth first to generate credentials file")
    elif args.retrieve:
        retrieve.retrieve(args.file)
    elif args.deploy:
        deploy.deploy()
    elif args.build:
        if args.file:
            deploy.build(args.file)
        else:
            parser.error('Must include a file to build with -f or --file')
