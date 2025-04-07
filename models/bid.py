from odoo import models, fields, api

class PurchaseBid(models.Model):
    _name = 'purchase.bid'
    _description = 'Vendor Bid'

    purchase_id = fields.Many2one('purchase.order', string='RFQ', required=True, ondelete='cascade')
    partner_id = fields.Many2one('res.partner', string='Vendor', required=True, domain="[('supplier_rank', '>', 0)]")
    price = fields.Float(string='Bid Price', required=True)
    delivery_time = fields.Integer(string='Delivery Time (days)', required=True)
    notes = fields.Text(string='Additional Notes')
    is_winner = fields.Boolean(string='Winning Bid')

    _sql_constraints = [
        ('unique_bid', 'unique(purchase_id, partner_id)', 'Each vendor can only submit one bid per RFQ.')
    ]

    @api.model
    def create(self, vals):
        if vals.get('is_winner'):
            self.search([
                ('purchase_id', '=', vals['purchase_id']),
                ('is_winner', '=', True)
            ]).write({'is_winner': False})
        return super(PurchaseBid, self).create(vals)

    def write(self, vals):
        if vals.get('is_winner'):
            self.search([
                ('purchase_id', '=', self.purchase_id.id),
                ('is_winner', '=', True)
            ]).write({'is_winner': False})
        return super(PurchaseBid, self).write(vals)
