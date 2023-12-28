# -*- coding: utf-8 -*-
from odoo import models,fields

class AccountMoveReversal(models.TransientModel):
    """
    Model for reversing accounting moves and updating the user responsible field of the reversed moves.
    """

    _inherit = "account.move.reversal"

    user_responsible = fields.Many2one("res.users", string="Responsible")

    def reverse_moves(self):
        """
        Reverses accounting moves and updates the user responsible field of the reversed moves.

        Returns:
            :class:`~odoo.models.Model`: The result of the parent reverse_moves method.
        """
        reverse = super().reverse_moves()
        for record in self:
            for move in record.new_move_ids:
                move.write({'user_responsible': record.user_responsible.id})
        return reverse