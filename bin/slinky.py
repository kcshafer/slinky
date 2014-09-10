#!/usr/bin/env python

import argparse
import os
import shutil
import sys
import time

from pyrannosaurus.utils import binary_to_zip, zip

def cwd():
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

sys.path.append('/Users/kshafer/workspace/slinky/')

from app import utils, deploy

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Develop with Salesforce')

    ## verbs ##
    parser.add_argument('--auth', '-A', action='store_true', help='Store login information')
    parser.add_argument('--retrieve', '-R', action='store_true', help='Retrieve components')
    parser.add_argument('--deploy', '-D', action='store_true', help='Deploy components')
    parser.add_argument('--build', '-b', action='store_true', help='Build a single file')

    ## nouns ## 
    parser.add_argument('--username', '-u', action='store', type=str)
    parser.add_argument('--password', '-p', type=str, action='store')
    parser.add_argument('--production', '-P', action='store_true', help='Authenticate with production')
    parser.add_argument('--file', '-f', type=str, action='store', help='File to build')

    args = parser.parse_args()

    if args.auth:
        if args.username and args.password:
            utils.build_credentials(args.username, args.password, production=args.production)
        else:
            parser.error("Must include username and password when building authentication file")
    elif not os.path.isfile('auth.ini'):
        print os.getcwd()
        parser.error("Must run slinky --auth first to generate credentials file")
    elif args.retrieve:
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
    elif args.deploy:
        client = MetadataClient()
        u, p, ip = utils.retrieve_credentials()
        client.login(u, p, is_production=p)
        zip('src/')
        deploy_request = client.deploy('deploy.zip')
        while True:
            deploy_status = client.check_deploy_status(deploy_request.id)
            if deploy_status.done:
                break
            else:
                print deploy_status.status
                time.sleep(3)
        deploy_response = client.check_deploy_status(deploy_request.id)
        print "Deployment %s %s" % (deploy_response.id, deploy_response.status)
    elif args.build:
        if args.file:
            deploy.build(args.file)
        else:
            parser.error('Must include a file to build with -f or --file')