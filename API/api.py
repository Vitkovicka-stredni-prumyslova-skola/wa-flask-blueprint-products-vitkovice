from flask import Blueprint, render_template
import requests
<<<<<<< HEAD
import json

=======
>>>>>>> parent of c2a9854 (create get all products)
api_bp = Blueprint('api_bp', __name__,
    template_folder='templates',
    static_folder='static')
URL_API = "https://fakestoreapi.com"

<<<<<<< HEAD
#Načte  seznam produktů z API v JSON formátu a vrátí jej jako pole.
def GetAllProducts():   
    
    request = requests.get(f"{URL_API}/products")
    
   # return json.loads(request.text)
    return request
 
    

=======
def ReadAllProducts():
    return requests.get(f"{URL_API}/products")
    
#@api_bp.route('/')
#def index():
#    return render_template('zatím nic')
>>>>>>> parent of c2a9854 (create get all products)
