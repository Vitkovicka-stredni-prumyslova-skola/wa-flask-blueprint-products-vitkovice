from flask import Blueprint, render_template
from API.api import ReadAllProducts
products_bp = Blueprint('products_bp', __name__,
    template_folder='templates',
    static_folder='static')

@products_bp.route('/products')
def index():
<<<<<<< HEAD
    data = GetAllProducts().json()
    #l = len(data)
    return render_template('products/products.html', products = data)
=======
    response = ReadAllProducts().json()
    
    return render_template('products/products.html', response=response)
>>>>>>> parent of c2a9854 (create get all products)
