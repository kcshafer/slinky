cls = '''
public class {name} {{

	public {name}() {{

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

cls_metadata = '''
<?xml version="1.0" encoding="UTF-8"?>
	<ApexClass xmlns="http://soap.sforce.com/2006/04/metadata">
	<apiVersion>30.0</apiVersion>
	<status>Active</status>
</ApexClass>'
'''

page_metadata = ''' 
<?xml version="1.0" encoding="UTF-8"?>
<ApexPage xmlns="http://soap.sforce.com/2006/04/metadata">
    <apiVersion>26.0</apiVersion>
    <label>{name}</label>
</ApexPage>
'''