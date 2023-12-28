# -*- coding: utf-8 -*-
from odoo import models,fields

class AccountMove(models.Model):
    """
    Model representing an account move in the Odoo framework.
    
    Inherits from the account.move model and adds a new field called 'user_responsible' to link the move with a responsible user.
    """
    _inherit = "account.move"

    user_responsible = fields.Many2one("res.users",string="Responsible")