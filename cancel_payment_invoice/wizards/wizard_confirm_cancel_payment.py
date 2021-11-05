# -*- coding: utf-8 -*-

import time
from odoo import _, api, fields, models


class WizardConfirmation(models.TransientModel):
    _name = 'wizard.confirm.cancel.payment'
    _description = 'Wizard confirm cancel payment'

    move = fields.Many2many("account.move")

    def cancel_payment(self):
        self.move.cancel_payment_move()