# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
__author__="chianggq@163.com"
__mtime__ = '2017-02-07 10:42:51'
"""
from odoo import models, fields,api
import time


# class ct_project_uf(models.Model):
#     _name = 'ct_project_uf.ct_project_uf'

#     name = fields.Char()

class UfLog(models.Model):

    _name = 'uf.log'

    name = fields.Char('Description', required=True)
    #seq = fields.Char('Sequence', required=True, default=lambda self:
    #self.env['ir.sequence'].get('uf.log') or '1000')
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)
    user_id = fields.Many2one('res.users', 'User',required=True, default=lambda self: self.env.user)
    last_use = fields.Datetime('LastUse',default=time.strftime('%Y-%m-%d %H:%M:%S'))
    #line_ids = fields.One2many('uf.log.line', 'tpl_id', 'Lines')
    state=fields.Selection([('draft', 'New'),
                                   ('open', 'In Progress'),
                                   ('close', 'Closed')],
                                  'Status', required=True, copy=False)
    name = fields.Char('name', required=True)
  


    # @api.model
    # def create(self, vals):
    #     print "uflogvals:", vals
    #     uflog_id = super(UfLog, self).create(vals)
    #     return uflog_id

    @api.one
    def do_toggle_done(self):
        #self.is_done = not self.is_done
        return True

    @api.multi
    def do_clear_done(self):
        #done_recs = self.search([('is_done', '=', True)])
        #done_recs.write({'active': False})
        return True

    def call_js(self, cr, uid, ids,context=None):
        context={}
        #context["key"]="value"
        print "call--js..."
        ret = {
            'type': 'ir.actions.client',
            'tag': 'mytest',
            #'context': context,
        }
        return ret

    @api.multi
    def do_action(self):
        ifdo=True
        res_id=0
        if True:
            return {
                'view_type': 'form',
                'view_mode': 'form,tree',
                'res_model': 'uf.handover',
                'res_id': res_id,
                'views': [(False, 'form'), (False, 'tree')],
                'type': 'ir.actions.act_window',
            }

        return True

    @api.multi
    def do_print(self, cr, uid, ids, context=None):
        assert len(ids) == 1, 'This option should only be used for a single id at a time'
        return self.pool['report'].get_action(cr, uid, ids, 'ct_project_uf.uf_log_report', context=context)

    @api.multi
    def do_preview(self, context=None):
        # assert len(self.ids) == 1, 'This option should only be used for a single id at a time'
        return {
            'name': 'action_uf_log_report',
            'type': 'ir.actions.act_url',
            'url': '/report/html/ct_project_uf.uf_log_report/'+str(self.ids[0]),
            'target': 'new',
        }


if __name__ == "__main__":
    pass