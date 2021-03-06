# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
__author__="chianggq@163.com"
__mtime__ = '2017-02-07 10:42:51'
"""
from openerp import models, fields, api

class UfHandoverReport(models.AbstractModel):
    _name="report.ct_project_uf.uf_handover_report"

    @api.multi
    def get_name(self):
        return [self.env['uf.handover'].browse(self.ids)]

    @api.multi
    def get_alldata(self):
        orderby="id desc"
        return self.env['uf.handover'].search([],order=orderby)

    @api.multi
    def _formatDate(self,bdate,edate):
        if bdate and edate:
            return str(bdate)[11:16]+" - "+str(edate)[11:16]
        else:
            return ""

    @api.multi
    def render_html(self,data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('ct_project_uf.uf_handover_report')
        records = self.get_name()
        docargs={
            "doc_ids":self.ids,
            "doc_model":report.model,
            "docs":records,
            # "format_date": self._formatDate,
        }
        return report_obj.render('ct_project_uf.uf_handover_tpl',docargs)