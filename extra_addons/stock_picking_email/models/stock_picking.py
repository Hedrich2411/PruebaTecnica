# -*- coding: utf-8 -*-
from odoo import models,api

class Picking(models.Model):
    _inherit = 'stock.picking'

    def open_wizard_email_note(self):
        """
        Open the wizard for sending a note.

        :return: Dictionary representing the action to open the wizard.
        :rtype: dict
        """
        return {
            'name': 'Send Note',
            'type': 'ir.actions.act_window',
            'res_model': 'stock_picking_email.note_wizard',
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'new',
            'context': {'picking_id': self.id} 
        }
    
    