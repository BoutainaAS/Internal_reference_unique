from openerp.osv import osv
from openerp.tools.translate import _ 
from openerp import api


class product_product(osv.osv):
    _inherit = "product.product"
    _name = "product.product"
	
    _sql_constraints = [
        ('defaut_code', 'unique(default_code)', "A external reference already exists with this name . External reference must be unique!"),	
		]

product_product()


# class product_product(osv.osv):
    # _inherit = "product.product"
    
    # def copy(self, cr, uid, id, default=None, context=None):
        # if not default:
            # default = {}
            
        # product_default_code = self.browse(cr, uid, id, context=context)
        
        # default['default_code'] = product_default_code.default_code and product_default_code.default_code + ' (copy)' or False
            
        # return super(product_product, self).copy(cr, uid, id, default=default, context=context)
    
    # _sql_constraints = [('default_code_unique', 'unique (default_code)','Le code du produit doit etre unique !')]


# from openerp.osv import osv 
# from openerp.tools.translate import _ 
# from openerp import api

# class product_product(osv.osv):
    # _name = 'product.product'
    # _inherit = 'product.product'
   
    # @api.one
    # @api.constrains('company_id','default_code', 'active')
    # def check_unique_company_and_default_code(self):
        # if self.active and self.default_code and self.company_id:
            # filters = [('company_id', '=', self.company_id.id),('default_code', '=', self.default_code),('active', '=', True)]
            # prod_ids = self.search(filters)
            # if len(prod_ids) >= 1:
                # raise Warning (("REFERENCE EXISTE DEJA : Impossible d'entrer deux articles actives de même sociéte avec même référnce interne"))
            # return True        