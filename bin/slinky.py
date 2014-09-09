#!/usr/bin/env bash

import argparse
import os
import shutil
import sys

from pyrannosaurus.clients.metadata import MetadataClient
from pyrannosaurus.utils import binary_to_zip

def cwd():
    return os.path.dirname(os.path.dirname(__file__))

sys.path.append(cwd())

from app import utils

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Develop with Salesforce')

    ## login arguments ##
    parser.add_argument('--auth', '-A', action='store_true', help='Store login information')
    parser.add_argument('--username', '-u', action='store', type=str)
    parser.add_argument('--password', '-p', type=str, action='store')
    parser.add_argument('--production', '-P', action='store_true', help='Authenticate with production')

    parser.add_argument('--retrieve', "-R", action='store_true', help='Retrieve components')

    args = parser.parse_args()

    if args.auth:
        if args.username and args.password:
            utils.build_credentials(args.username, args.password, production=args.production)
        else:
            parser.error("Must include username and password when building authentication file")
    elif args.retrieve:
        if(os.path.isfile('auth.ini')):
            client = MetadataClient()
            u, p, ip = utils.retrieve_credentials()
            client.login(u, p, is_production=p)
            retrieve_request = client.retrieve('src/package.xml')
            while client.check_status(retrieve_request.id)[0].done == False:
                pass
            retrieve_response = client.check_retrieve_status(retrieve_request.id)
            binary_to_zip(retrieve_response.zipFile)
            shutil.move('retrieve.zip', 'src/retrieve.zip')
            os.system('unzip -uo src/retrieve.zip -d src/ ')
        else:
            parser.error("Must run slinky --auth first to generate credentials file")
