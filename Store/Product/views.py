from flask import Blueprint, jsonify,  render_template, redirect, url_for, request
from Store import db
from Store.models import ProductCatalog
from Store.Product.forms import UploadRecord, SearchForm, UpdateRecord
from werkzeug.utils import secure_filename
import os
import pandas as pd
from datetime import datetime


product=Blueprint('Product',__name__,template_folder='templates')

@product.route('/catalog',methods=['GET','POST'])
def catalog():
    stockdetails = UploadRecord()
    searchform = SearchForm()
    print(request.method)
    if request.method=='POST' and stockdetails.validate_on_submit():
        file = stockdetails.stock_file.data
        filename = secure_filename(file.filename)
        data_dir = os.path.join(os.path.curdir,'data',filename)
        file.save(data_dir)
        df = pd.read_csv(data_dir)
        df.to_sql(name="product_catalog",con=db.engine,index=False,if_exists='append')
        db.session.commit()
        row,column=df.shape
        return redirect(url_for('Product.catalog'))
    if request.method=='GET':
        #print('dd')
        print(request.args)
        operator = request.args.get('operator')
        kvalue = request.args.get('value')
        keyword = request.args.get('keyword')
        #print(operator,kvalue)
        if kvalue and operator == 'EQ':
            if keyword == 'sku':
                record = ProductCatalog.query.filter_by(sku=kvalue).all()
            else:
                record = ProductCatalog.query.filter_by(product_name=kvalue).all()
        elif kvalue and operator == 'LIKE':
            if keyword == 'sku':
                record = ProductCatalog.query.filter(ProductCatalog.sku.like(kvalue)).all()
            else:
                record = ProductCatalog.query.filter(ProductCatalog.product_name.like(kvalue)).all()
    #page=request.args.get('page',1,type=int)
        else:
            record = ProductCatalog.query.all()
    else:
            record = ProductCatalog.query.all()
    return render_template("records.html",form=stockdetails,records=record,searchform=searchform)

@product.route('/catalog/delete/<sku>',methods=['GET','DELETE'])
def delete_catalog(sku):
    ProductCatalog.query.filter_by(sku=sku).delete()
    db.session.commit()
    request.method = 'GET'
    return jsonify({"Msg":"Record Deleted Successfully"})

@product.route("/catalog/update/<sku>",methods=['GET','POST'])
def update_catalog(sku):
    updateform = UpdateRecord()
    if request.method=='POST' and updateform.validate_on_submit():
        print(sku)
        product = ProductCatalog.query.filter_by(sku=sku).first()
        product.store_id = updateform.store_id.data
        product.sku = updateform.sku.data
        product.product_name = updateform.product_name.data
        product.price = updateform.price.data
        product.date = datetime.strftime(updateform.date.data,'%m/%d/%Y')
        db.session.commit()
        return redirect(url_for('Product.catalog'))
    product = ProductCatalog.query.filter_by(sku=sku).first()
    updateform.store_id.data = product.store_id 
    updateform.sku.data = product.sku
    updateform.product_name.data = product.product_name 
    updateform.price.data = product.price
    updateform.date.data = datetime.strptime(product.date,'%m/%d/%Y')
    #db.session.commit()
    return render_template('update_record.html',form=updateform,sku=sku)
    

