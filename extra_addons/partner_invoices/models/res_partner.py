# -*- coding: utf-8 -*-
from odoo import models,fields,api

class ResPartner(models.Model):
    """
    ResPartner class is a part of the Odoo framework and is used for managing partners and their overdue invoices.
    """

    _inherit = "res.partner"

    invoices_due_ids = fields.Many2many('account.move', string="Overdue Invoices", compute="_compute_invoice_due_ids")
    qty_invoice_due = fields.Integer(compute="_compute_qty_invoice_due")

    @api.depends("invoice_ids")
    def _compute_invoice_due_ids(self):
        """
        Compute method for the invoices_due_ids field.
        It retrieves the current date and constructs a domain to search for overdue invoices.
        The domain filters invoices based on the partner, invoice type, amount residual, state, and due date.
        The method performs the search using the domain and assigns the resulting invoices to the invoices_due_ids field.
        """
        for record in self:
            today = fields.Date.today()
            domain = [
                ('partner_id', '=', record.id),
                ('move_type', 'in', ['out_invoice', 'out_refund']),
                ('amount_residual', '>', 0),
                ('state', '=', 'posted'),
                ('invoice_date_due', '<', today)
            ]
            due_invoices = self.env["account.move"].search(domain)
            record.invoices_due_ids = due_invoices

    @api.depends("invoices_due_ids")
    def _compute_qty_invoice_due(self):
        """
        Compute method for the qty_invoice_due field.
        It calculates the number of overdue invoices by counting the records in the invoices_due_ids field.
        """
        for record in self:
            record.qty_invoice_due = len(record.invoices_due_ids)

    def open_action_partner_invoice_due(self):
        """
        Method to open a window displaying the overdue invoices for the partner.
        It returns an action to open the window.
        """
        return {
            'name': 'Overdue Invoice',
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'domain': [('id', 'in', self.invoices_due_ids.ids)],
            'view_mode': 'tree,form',
        }