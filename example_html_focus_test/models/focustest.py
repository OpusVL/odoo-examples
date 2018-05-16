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

from openerp import models, fields, api


class HTMLFocusExample(models.Model):
    _name = 'example.html.focus'
    name = fields.Char(required=True)

    html_field = fields.Html()


for i in range(1, 51):
    setattr(HTMLFocusExample, "field_{:0>2}".format(i), fields.Char())

