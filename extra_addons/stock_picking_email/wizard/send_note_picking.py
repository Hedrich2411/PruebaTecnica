# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import mimetypes
import re

class NotePickingWizard(models.TransientModel):
    """
    A class used to send an email with an informative note and an optional file attachment related to a stock picking record.

    Example Usage:
    ```python
    # Create an instance of the NotePickingWizard class
    note_wizard = NotePickingWizard()

    # Set the note and file fields
    note_wizard.note = "This is an informative note"
    note_wizard.file = b"file_data"
    note_wizard.filename = "example.pdf"

    # Call the send_email method to send the email
    note_wizard.send_email()
    ```

    Methods:
    - send_email: Sends an email with the note and file attachment to the partner associated with a stock picking record.
    - _check_file: Checks if the file attachment is a valid image or PDF file.
    - _validate_email: Validates the format of an email address.

    Fields:
    - note: A text field for the informative note.
    - file: A binary field for the file attachment.
    - filename: A char field for the name of the file.
    """

    _name = "stock_picking_email.note_wizard"

    note = fields.Text(string="Informative note", required=True)
    file = fields.Binary(string="File", help="The file must be an image or pdf")
    filename = fields.Char(string="File name")

    def send_email(self):
        """
        Sends an email with the note and file attachment to the partner associated with a stock picking record.
        """
        picking_obj = self.env["stock.picking"]
        picking_id = self.env.context.get("picking_id")
        if picking_id:
            picking = picking_obj.browse([picking_id])
            partner = picking.partner_id
            if partner:
                if partner.email and self.env.user.email:
                    if not self._validate_email(partner.email) or not self._validate_email(self.env.user.email):
                        raise ValidationError("Incorrectly formatted emails, check.")

                    message = '<p>Hello {},</p><p>{}.</p>'.format(partner.name, self.note)

                    mail_values = {
                        'subject': "Informative note -> {}".format(picking.name),
                        'email_from': self.env.user.email,
                        'email_to': partner.email,
                        'body_html': message
                    }
                    mail = self.env['mail.mail'].create(mail_values)
                    attachment_data = {
                        'name': self.filename,
                        'datas': self.file,
                        'res_model': 'mail.mail',
                        'res_id': mail.id,
                        'type': 'binary',
                    }
                    attachment = self.env['ir.attachment'].create(attachment_data)
                    mail.attachment_ids = [(4, attachment.id)]
                    mail.send()
                else:
                    raise ValidationError("Mail not defined in the sender or receiver.")

    @api.constrains("filename")
    def _check_file(self):
        """
        Checks if the file attachment is a valid image or PDF file.
        """
        for record in self:
            if record.filename:
                type_mime, _ = mimetypes.guess_type(record.filename)
                if type_mime not in ['application/pdf', 'image/png', 'image/jpeg', 'image/gif']:
                    raise ValidationError("The file must be an image or pdf")

    def _validate_email(self, email):
        """
        Validates the format of an email address.

        Args:
        - email: The email address to validate.

        Returns:
        - bool: True if the email address is valid, False otherwise.
        """
        patron = r'^\w+[\._]?\w+@\w+\.\w+$'
        return re.match(patron, email)