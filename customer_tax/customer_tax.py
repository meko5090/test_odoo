from openerp import models, fields
#from odoo import models, fields, api


import itertools
import psycopg2

import odoo.addons.decimal_precision as dp

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm

class customer_tax(models.Model):
    _name="res.partner"
    _inherit= "res.partner"
    tax=fields.Integer("tax number",required=True)
    com=fields.Integer("Commercial Register",required=True)
    _sql_constraints = [
        ('phone_unique', 'unique(phone)', 'phone already exists!')
        ('mobile_unique', 'unique(mobile)', 'mobile already exists!')
        ('email_unique', 'unique(email)', 'email already exists!')
        ('com_unique', 'unique(com)', 'Commercial Register already exists!')
        ('tax_unique', 'unique(tax)', 'tax number already exists!')
        ('fax_unique', 'unique(fax)', 'fax number already exists!')
        ('website_unique', 'unique(website)', 'website already exists!')
    ]