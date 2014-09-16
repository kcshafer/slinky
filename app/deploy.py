import glob
import os
import shutil
import time

from pyrannosaurus.clients.metadata import MetadataClient
from pyrannosaurus.utils import zip

from app import utils

def build(filename):
    client = MetadataClient()
    u, p, ip = utils.retrieve_credentials()
    client.login(u, p, is_production=p)
    if os.path.exists('.build'):
        shutil.rmtree('.build/')
    os.mkdir('.build/')
    print "kc"
    print filename
    name, type = (filename.split("."))
    utils.build_package(name, type, '.build/')
    metadata_dir = utils.METADATA_DIRS.get(type, None)
    os.mkdir('.build/' + metadata_dir)
    src_dir = 'src/' + metadata_dir + '/' + filename
    bld_dir = '.build/' + metadata_dir + '/'
    if type in utils.CODE_FILES:
        for file in glob.glob(src_dir + "*"):
            shutil.copy(file, bld_dir)
    else:
        shutil.copyfile(src_dir, bld_dir)
    zip('.build')
    deploy_request = client.deploy('deploy.zip')
    while True:
        deploy_status = client.check_deploy_status(deploy_request.id)
        if deploy_status.done:
            break
        else:
            print deploy_status.status
            time.sleep(3)
    deploy_response = client.check_deploy_status(deploy_request.id)
    print deploy_response
    print "Deployment %s %s" % (deploy_response.id, deploy_response.status)

def deploy():
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
