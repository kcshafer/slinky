import os

from app import templates

CLASSES = [
	'class',
	'batchClass'
]

PAGES = [
	'standardPage',
	'customPage',
	'hybridPage'
]

def generate(t, n, o):
	if t in CLASSES:
		cls(t, n)
	if t in PAGES:
		page(t, n, o)
	if t == 'trigger':
		trigger(n)

def cls(t, n, o=None): 
	contents = 'NO CONTENT WAS GENERATED'
	if t == 'class':
		f = open('src/classes/' + n + '.cls', 'w+')
		contents = templates.cls.format(name=n)
	elif t == 'batchClass':
		f = open('src/classes/' + n + '.cls', 'w+')
		contents = templates.batch_class.format(name=n)
	elif t == 'controller':
		n = n + 'Controller'
		f = open('src/classes/' + n + '.cls', 'w+')
		contents = templates.controller.format(name=n)
	elif t == 'controller_extension':
		n = n + 'ControllerExtension'
		f = open('src/classes/' + n + '.cls', 'w+')
		contents = templates.controller_extension.format(name=n, object=o)

	f.write(contents.lstrip())
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

def trigger(n):
	if not os.path.exists('src/triggers'):
		os.mkdir('src/triggers')
	f = open('src/triggers/' + n + '.trigger', 'w+')
	f.write(templates.trigger.format(name=n))
	f.close()
	f = open('src/triggers/' + n + '.trigger-meta.xml', 'w+')
	f.write(templates.trigger_metadata.lstrip())
	f.close()
