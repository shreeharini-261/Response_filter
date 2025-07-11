from flask import Blueprint, jsonify, request
from models.db import db, Product
from models.schemas import ProductSchema, PublicProductSchema, PrivateProductSchema

main_bp = Blueprint('main', __name__)

product_schema = ProductSchema()
public_schema = PublicProductSchema(many=True)
private_schema = PrivateProductSchema(many=True)

@main_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify(public_schema.dump(products))

@main_bp.route('/admin/products', methods=['GET'])
def get_products_admin():
    products = Product.query.all()
    return jsonify(private_schema.dump(products))

@main_bp.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(public_schema.dump(product))

@main_bp.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    errors = product_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    
    product = Product(**product_schema.load(data))
    db.session.add(product)
    db.session.commit()
    
    return jsonify(public_schema.dump(product)), 201