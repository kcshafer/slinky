import ConfigParser
from lxml import etree

METADATA_TYPES = {
    'object'   : 'CustomObject',
    'cls'      : 'ApexClass', 
    'page'     : 'ApexPage',
    'resource' : 'StaticResource',
    'trigger'  : 'ApexTrigger',
}

METADATA_DIRS = {
    'object'   : 'objects',
    'cls'      : 'classes',
    'resource' : 'staticresources',
    'trigger'  : 'triggers',
    'page'     : 'pages'
 }

CODE_FILES = [
    'cls',
    'page',
    'trigger',
    'resource',
]

NS = "http://soap.sforce.com/2006/04/metadata"
NAMESPACES = {"sf": NS}

def build_credentials(username, password, production):
    cp = ConfigParser.ConfigParser()
    f = open('auth.ini', 'w')
    
    cp.add_section('credentials')
    cp.set('credentials', 'username', username)
    cp.set('credentials', 'password', password)
    cp.set('credentials', 'production', production)

    cp.write(f)
    f.close()

def retrieve_credentials():
    cp = ConfigParser.ConfigParser()
    cp.read('auth.ini')
    c = 'credentials'
    u = 'username'
    p = 'password'
    r = 'production'
    return cp.get(c, u), cp.get(c, p), cp.get(c, r)

def build_package(member, type, dir, v='29.0'):
    new_pkg = etree.Element("Package")
    new_pkg.attrib['xmlns'] = "http://soap.sforce.com/2006/04/metadata"
    apiLevel = etree.SubElement(new_pkg,'apiAccessLevel')
    apiLevel.text = 'Unrestricted'
    types = etree.SubElement(new_pkg, "types")
    members = etree.SubElement(types,'members')
    members.text = member
    name = etree.SubElement(types,'name')
    name.text = METADATA_TYPES.get(type)
    version = etree.SubElement(new_pkg, 'version')
    version.text = v
    with open(dir + "package.xml", "w+") as f:
        #the doc type header needs to be appended on in front 
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + etree.tostring(new_pkg, pretty_print=True))