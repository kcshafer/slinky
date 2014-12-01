cls = '''
public class {name} {{

	public {name}() {{

	}}
}}
'''

batch_class = '''
global class {name} implements Database.Batchable<SObject> {{
	
	global Database.QueryLocator start(Database.BatchableContext bc){{

	}}

	global void execute(Database.BatchableContext bc, List<SObject> scope){{

	}}

	global void finish(Database.BatchableContext bc){{

	}}
}}	
'''

controller = '''
public class {name} {{
	
	public {name}(){{
	
	}}
}}
'''

controller_extension = '''
public class {name} {{

    private final {object} sobj;
    
    public {name}(ApexPages.StandardController stdController) {{
        this.sobj = (obj)stdController.getRecord(){{
    }}
}}
'''

standard_page = '''
<apex:page standardController="{object}">
</apex:page>
'''

custom_page = '''
<apex:page controller="{name}Controller">
</apex:page>
'''

hybrid_page = '''
<apex:page standardController="{object}" extensions="{name}">
<apex:page>
'''

trigger = '''
trigger {name} on sObject () {{

}}
'''

cls_metadata = '''
<?xml version="1.0" encoding="UTF-8"?>
	<ApexClass xmlns="http://soap.sforce.com/2006/04/metadata">
	<apiVersion>30.0</apiVersion>
	<status>Active</status>
</ApexClass>
'''

page_metadata = ''' 
<?xml version="1.0" encoding="UTF-8"?>
<ApexPage xmlns="http://soap.sforce.com/2006/04/metadata">
    <apiVersion>26.0</apiVersion>
    <label>{name}</label>
</ApexPage>
'''

trigger_metadata = '''
<?xml version="1.0" encoding="UTF-8"?>
<ApexTrigger xmlns="http://soap.sforce.com/2006/04/metadata">
    <apiVersion>31.0</apiVersion>
    <status>Active</status>
</ApexTrigger>
'''



