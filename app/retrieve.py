import os
import shutil
import time

from pyrannosaurus.clients.metadata import MetadataClient
from pyrannosaurus.utils import binary_to_zip

from app import utils

def retrieve(filename, dir='src/'):
    client = MetadataClient()
    u, p, ip = utils.retrieve_credentials()
    ip = True if ip == 'True' else False
    client.login(u, p, is_production=ip)
    if not os.path.exists(dir):
        os.mkdir(dir)
    name, type = (filename.split("."))
    utils.build_package(name, type, dir)
    retrieve_request = client.retrieve(dir + 'package.xml')
    while client.check_status(retrieve_request.id)[0].done == False:
        pass
    retrieve_response = client.check_retrieve_status(retrieve_request.id)
    binary_to_zip(retrieve_response.zipFile)
    shutil.move('retrieve.zip', dir + 'retrieve.zip')
    os.system('unzip -uo ' + dir + '/retrieve.zip -d ' + dir)

def retrieve_package(dir='src/'):
    #################################################
    ##### Retrieve the contents specified of a ######
    ##### package.xml in the src directory ##########
    #################################################

    client = MetadataClient()
    u, p, ip = utils.retrieve_credentials()
    ip = True if ip == 'True' else False
    client.login(u, p, is_production=ip)
    if not os.path.exists(dir):
        os.mkdir(dir)
    retrieve_request = client.retrieve(dir + 'package.xml')
    while client.check_status(retrieve_request.id)[0].done == False:
        pass
    retrieve_response = client.check_retrieve_status(retrieve_request.id)
    binary_to_zip(retrieve_response.zipFile)
    shutil.move('retrieve.zip', dir + 'retrieve.zip')
    os.system('unzip -uo ' + dir + '/retrieve.zip -d ' + dir)

def retrieve_merge():
    ## Placeholder for a method that will retrieve a full package xml 
    ## and merge it into src
    pass

def retrieve_resource(name):
    retrieve(name + '.resource', dir='.rsrc/')
    f = open('.rsrc/staticresources/' + name + '.resource', 'r')
    tf = open('.rsrc/resource.zip', 'w+')
    tf.write(f.read())
    tf.close()
    os.system('unzip -uo .rsrc/resource.zip -d .rsrc/')