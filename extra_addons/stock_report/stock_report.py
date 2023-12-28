# -*- coding: utf-8 -*-
from odoo import models,fields,tools

class StockReport(models.Model):
    """
    Model representing a report on stock quantities.

    This model is used to create a view that aggregates stock quantities based on warehouse, location, product, product category, and unit of measure.
    """

    _name = 'stock_report.report'
    _auto = False

    warehouse_id = fields.Many2one('stock.warehouse', string='Warehouse')
    location_id = fields.Many2one('stock.location', string='Ubication')
    product_id = fields.Many2one('product.product', string='Product')
    product_categ_id = fields.Many2one('product.category', string='Product Category')
    uom_id = fields.Many2one('uom.uom', string='Unidad de Medida')
    quantity = fields.Float(string='Stock Físico')

    def init(self):
        """
        Initialize the StockReport view.

        This method creates a view in the database by executing a SQL query. The query joins the `stock_quant`, `product_product`, `product_template`, and `stock_location` tables to aggregate stock quantities based on various criteria. The resulting view is stored in the table specified by the `_table` attribute of the class.
        """
        sql = """CREATE OR REPLACE VIEW {} AS (
            SELECT
                min(q.id) as id,
                l.warehouse_id as warehouse_id,
                q.location_id as location_id,
                q.product_id as product_id,
                t.categ_id as product_categ_id,
                t.uom_id as uom_id,
                sum(q.quantity) as quantity
            FROM
                stock_quant q
            JOIN
                product_product p ON q.product_id = p.id
            JOIN
                product_template t ON p.product_tmpl_id = t.id
            JOIN
                stock_location l ON q.location_id = l.id
            GROUP BY
                l.warehouse_id,q.location_id, q.product_id, t.categ_id, t.uom_id
        )""".format(self._table)

        tools.drop_view_if_exists(self.env.cr,self._table)
        self.env.cr.execute(sql)