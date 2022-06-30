from Store import db



class ProductCatalog(db.Model):
    __tablename__ = "product_catalog"

    store_id = db.Column('Store ID',db.Integer,nullable=False)
    sku = db.Column('SKU',db.String(10),nullable=False,primary_key=True)
    product_name = db.Column('Product Name',db.String(20),nullable=False)
    price = db.Column('Price',db.Numeric(10,2),nullable=False)
    date=db.Column(' Date',db.String,nullable=False)


    
