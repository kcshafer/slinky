import os

from app import templates

DIRS = {
	'class' : 'classes',
	'standardPage' : 'pages',
}

EXTENSIONS = {
	'class' : 'cls',
	'standardPage' : 'page',
}


def generate(t, n, o):
	if t == 'class':
		cls(n)
	if t in ['customPage', 'standardPage', 'hybridPage']:
		page(t, n, o)

def cls(t, n, o=None): 
	if t == 'class':
		f = open('src/classes/' + n + '.cls', 'w+')
		f.write(templates.cls.format(name=n).lstrip())
		f.close()
	elif t == 'controller':
		n = n + 'Controller'
		f = open('src/classes/' + n + '.cls', 'w+')
		f.write(templates.controller.format(name=n).lstrip())
		f.close()
	elif t == 'controller_extension':
		n = n + 'ControllerExtension'
		f = open('src/classes/' + n + '.cls', 'w+')
		f.write(templates.controller_extension.format(name=n, object=o).lstrip())
		f.close()
	f = open('src/classes/' + n + '.cls-meta.xml', 'w+')
	f.write(templates.cls_metadata.lstrip())
	f.close()

def page(t, n, o):
	if t == 'standardPage':
		f = open('src/pages/' + n + '.page', 'w+')
		f.write(templates.standard_page.format(object=o))
		f.close()
	elif t == 'customPage':
		f = open('src/pages/' + n + '.page', 'w+')
		f.write(templates.custom_page.format(name=n))
		f.close()
		cls('controller', n)
	elif t == 'hybridPage':
		f = open('src/pages/' + n + '.page', 'w+')
		f.write(templates.hybrid_page.format(name=n, object=o).lstrip())
		f.close()
		cls('controller_extension', n, o=o)
	f = open('src/pages/' + n + '.page-meta.xml', 'w+')
	f.write(templates.page_metadata.format(name=n).lstrip())
