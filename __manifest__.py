{
    'name': 'Multi Vendor RFQ',
    'version': '1.0',
    'depends': ['purchase', 'hr'],
    'author': 'Mitchell Wanjiru',
    'category': 'Purchases',
    'description': 'Allows assigning multiple vendors to one RFQ',
    'data': [
        #'views/bid_views.xml',
        'security/ir.model.access.csv',
        'views/views.xml'
        #'views/purchase_request_menu',
        #'views/purchase_request_views.xml'
    ],
    'installable': True,
    'application': False,
}
