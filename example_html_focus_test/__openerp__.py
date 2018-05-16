# -*- coding: utf-8 -*-

##############################################################################
#
# HTML widget focus stealing test
# Copyright (C) 2018 Opus Vision Limited (<https://opusvl.com>)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'HTML widget focus stealing test',
    'version': '0.1',
    'author': 'Opus Vision Limited',
    'website': 'https://opusvl.com',
    'summary': 'HTML widget focus stealing test',
    
    'category': 'Examples',
    
    'description': """HTML widget focus stealing test

    This is to check behaviour of pop-up edit/creation dialogues with HTML widgets near the bottom.
""",
    'images': [
    ],
    'depends': [
        'base',
        'web',
    ],
    'data': [
        'views/focustest.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
