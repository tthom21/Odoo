# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class Company(models.Model):
    _inherit = 'res.company'
    
    notify_vendor_ids = fields.Many2many('res.partner', 'purchase_vendor_rel', 'purchase_config_id', 'vendor_id', string="Auto Notify Vendors", copy=False)
