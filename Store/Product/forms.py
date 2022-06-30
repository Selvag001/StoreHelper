from msilib.schema import RadioButton
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms.fields import SubmitField,FileField,SelectField,StringField,IntegerField,FloatField,DateField
from wtforms.validators import DataRequired, ValidationError


class UploadRecord(FlaskForm):
    stock_file = FileField("Please choose a valid stock details file..",validators=[FileRequired(),FileAllowed(['csv'],'File Type is not valid. Expected .csv!!')])
    upload = SubmitField()

class SearchForm(FlaskForm):
    keyword = SelectField("keyword",choices=[("sku","SKU"),("name","Name")])
    operator = SelectField("operator",choices=[("EQ","EQ"),("LIKE","LIKE")])
    value = StringField()
    search = SubmitField()

class UpdateRecord(FlaskForm):
    store_id = IntegerField('Store ID')
    sku = StringField('SKU')
    product_name = StringField('Product Name')
    price = FloatField('Price')
    date=DateField('Date')
    update = SubmitField()

