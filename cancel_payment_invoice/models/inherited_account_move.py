# -*- coding: utf-8 -*-
import time
from odoo import api, fields, models, _

class AccountMove(models.Model):
    _inherit = "account.move"

    def cancel_payment_move(self):
        payments = self.env['account.payment'].search([])
        payment_to_cancel = payments.filtered(lambda x: x.reconciled_invoice_ids.id == self.id)
        payment_to_cancel.action_draft()
        time.sleep(1)
        payment_to_cancel.action_cancel()
        self.button_draft()


    def cancel_payment(self):
        return {
            'name': 'Cancel payment',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'wizard.confirm.cancel.payment',
            'target': 'new',
            'context': {'default_move': self.ids}
        }
