from odoo import models, fields

class PurchaseRequest(models.Model):
    _name = 'purchase.request' #unique name for the model
    _description = 'Purchase Request'

    name = fields.Char(string='Request Name', required=True)#will show a label
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)#link to hr.employee model*
    product_id = fields.Many2one('product.product', string='Product', required=True)
    quantity = fields.Float(string='Quantity', required=True)
    reason = fields.Text(string='Reason for Purchase')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')

    #def confirm_request(self):
     #   self.write({'state': 'confirmed'})

    # def cancel_request(self):
    #     self.write({'state': 'cancelled'})
    #
    # def create_rfq(self):
    #     purchase_order_vals = {
    #         'partner_ids': [(6, 0, self.env['res.partner'].search([('supplier_rank', '>', 0)]).ids)],
    #         'order_line': [(0, 0, {
    #             'product_id': self.product_id.id,
    #             'product_qty': self.quantity,
    #             'price_unit': self.product_id.standard_price,
    #         })],
    #     }
    #     purchase_order = self.env['purchase.order'].create(purchase_order_vals)
    #     return purchase_order
