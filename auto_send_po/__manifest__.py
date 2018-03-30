{
    'name' : 'Auto Confirm & Send Purchase Order',
    'version' : '1.0',
    'category' : 'Purchase Management',
    'depends' : ['base', 'purchase'],
    'data':[
                'views/company_views.xml',
                'views/ir_cron.xml'
    		],
    'price': 49.99
    'currency': 'USD'
    'license': 'AGPL-3'
    'installable': True
    'images': ['static/description/Vendors_screenshot.png', 'static/description/Scheduler.png']
    'summary': """
        Automatically confirm & send purchase orders""",
    'description': """
        This module automatically confirms and sends purchase orders to specified vendors via email, using the purchase order template.    
    """,
    'author': "Samplize",
    'website': "http://www.samplize.com"
}
