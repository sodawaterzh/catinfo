from flask_wtf import FlaskForm
from  wtforms import StringField,SubmitField,SelectField,DateField,FileField
from wtforms.validators import ValidationError,DataRequired
from flask_wtf.file import  FileAllowed, FileRequired,FileField
from app.models import catinfo

class addCatForm(FlaskForm):
	catname = StringField("名字",validators=[DataRequired()])
	birthday =DateField('生日',validators=[DataRequired()])
	sex = SelectField('性别',choices=[('公','公'), ('母', '母')])
	headimage =FileField('image',validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
	submit = SubmitField('保存')

class addtimeForm(FlaskForm):
	time = DateField("记录时间",validators=[DataRequired()])
	description = StringField("描述",validators=[DataRequired()])
	type = SelectField('记录类型',choices=[('0','三联疫苗注射'),("1","狂犬疫苗注射"),("2","体内驱虫"),
									   ("3","体外驱虫")])
	submit = SubmitField("保存")