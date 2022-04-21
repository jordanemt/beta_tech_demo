from odoo import fields, models


class PartnerInherit(models.Model):
    _inherit = 'res.partner'

    last_name = fields.Char(string='Apellidos')
    identification = fields.Char(string='Cédula', size=9)
    