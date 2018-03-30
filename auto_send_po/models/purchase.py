
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    
    @api.multi
    def auto_confirm_order(self):
        vendors = self.env.user.company_id.notify_vendor_ids
        if not vendors:
            raise UserError(
                _('There is no vendors configured in purchase settings.Please configure and try.'))
        rfqs = []
        for vendor in vendors:
            order = self.search([('partner_id', '=', vendor.id),('state', 'in', ['draft'])])
            rfqs.append(order)
        if rfqs:
            for rfq in rfqs:
                rfq.button_confirm()
                rfq.action_sendmail()
        return True
    
    @api.multi
    def action_sendmail(self):
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = self.env.ref('purchase.email_template_edi_purchase', False)
        except ValueError:
            template_id = False
        local_context = self.env.context.copy()
        template_id.with_context(local_context).send_mail(self.id, force_send=True)
    
