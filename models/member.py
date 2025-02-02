from odoo import models, fields

class CommitteeMember(models.Model):
    _name = 'committee.member'
    _description = 'Committee Member'

    name = fields.Char(string='Name', required=True)
    profile_picture = fields.Binary(string='Profile Picture')
    bio = fields.Text(string='Bio')
    committee_id = fields.Many2one('committee.organizing', string='Organizing Committee')
    board_id = fields.Many2one('committee.advisory', string='Advisory Board')



class OrganizingCommittee(models.Model):
    _name = 'committee.organizing'
    _description = 'Organizing Committee'

    name = fields.Char(string='Committee Name', required=True)
    active = fields.Boolean(string='Active', default=True)
    member_ids = fields.One2many('committee.member', 'committee_id', string='Members')

    def toggle_active(self):
        self.active = not self.active



class AdvisoryBoard(models.Model):
    _name = 'committee.advisory'
    _description = 'Advisory Board'

    name = fields.Char(string='Board Name', required=True)
    active = fields.Boolean(string='Active', default=True)
    member_ids = fields.One2many('committee.member', 'board_id', string='Members')

    def toggle_active(self):
        self.active = not self.active