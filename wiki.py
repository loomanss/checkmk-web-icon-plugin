#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File location : "/local/share/check_mk/web/plugins/icons/wiki.py"
# Tested with checkmk v2.0


#############################################$
#        REQUIREMENTS
#############################################$
#It's important that
#  -  add_custom_macro is set to True
#  -  show_in_table is set to True
#  - remove the # from the line starting with 'if'
#  - add following lines to  File location : /check_mk/multisite.d/wato/custom_attrs.mk
#############################################################
## Created by WATO
## encoding: utf-8

#if type(wato_host_attrs) != list:
#        wato_host_attrs = []
#    wato_host_attrs += [{'add_custom_macro': True,
#      'help': u'',
#      'name': 'WIKIID',
#      'show_in_table': True,
#      'title': u'WIKIID',
#      'topic': 'custom_attributes',
#      'type': 'TextAscii'}]
#############################################################
    

    # examples : https://github.com/tribe29/checkmk/tree/master/cmk/gui/plugins/views/icons
    
    @icon_and_action_registry.register
    class WIKIIcon(Icon):
        @classmethod
        def ident(cls):
            return "wiki"
    
        @classmethod
        def title(cls) :
            return _("Wiki")
    
        # if false it will go in dropdown menu otherwise it will be shown on the main-view of hosts
        def default_toplevel(self):
            return True
    
        def host_columns(self):
            return ['check_command', 'name', 'address']
    
        def render(self, what, row, tags, custom_vars):
            if (what == "service" and row.get("service_state") !=0)  or ( what == 'host'):
               url = 'http://www.wiki.local/search/?Id=' + str(custom_vars.get("WIKIID"))
            return 'wiki', _('Wiki'),(url, "_blank")
