# -*- encoding: utf-8 -*-
{
  'name' : 'Website Header Modifier',
  'description' : 'the module will modify the website header to a custom hamburger menu',
  'category' : 'website/header',
  'version' : '17.0',
  'author' : 'Calvin Dube',
  'depends' : ['website'],
  'inherits' : ['website'],
  'application' : True,
  'installable' : True,
  'data': [
        'views/header_template.xml'
    ],
    'assets':{
        'header.assets':[
          'website_header_modifier/static/src/js/**/*',
          'website_header_modifier/static/src/scss/**/*',
          'website_header_modifier/static/src/css/**/*'
        ]
    }
}