# -*- coding:utf-8 -*-
from flask import render_template,flash,redirect,url_for,request,g,jsonify,current_app
from  app import db,photos,create_app
from app.main import bp
from app.models import catinfo,timeinfo
from app.main.forms import addCatForm,addtimeForm
from config import config
import os
import requests
from flask_uploads import UploadSet,IMAGES,configure_uploads


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
	cat = catinfo.query.all()
	return render_template('index.html',cats=cat)

@bp.route('/addCat',methods = ['GET', 'POST'])
def addCat():
	'''添加一只猫'''
	form = addCatForm()
	if form.validate_on_submit():#验证表单数据
		headimage = form.headimage.data
		a = photos.save(headimage)
		cat = catinfo(catname=form.catname.data,birthday=form.birthday.data
					  ,sex = form.sex.data,headimage = photos.url(a),status=1)
		db.session.add(cat)
		db.session.commit()
		flash('保存成功')
		return  redirect(url_for('main.index'))
	return  render_template('addcat.html',form=form)

@bp.route('/alterCat/<id>',methods = ['GET', 'POST'])
def alterCat(id):
	cat = catinfo.query.filter_by(id=id).first()
	form = addCatForm()
	print(form.catname.data)
	print(form.birthday.data)
	print(form.sex.data)
	print(form.headimage.data)
	print(form.validate_on_submit())
	if form.validate_on_submit():#验证表单数据
		headimage = form.headimage.data
		a = photos.save(headimage,headimage.filename)
		cat.catname = form.catname.data
		cat.birthday = form.birthday.data
		cat.sex = form.sex.data
		cat.headimage=photos.url(a)

		db.session.commit()
		flash('修改成功')
		return  redirect(url_for('main.index'))
	return render_template("alterCat.html",cat=cat,form=form)
basedir = os.path.abspath(os.path.dirname(__file__))
def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1].lower() in config.ALLOWED_EXTENSIONS

@bp.route('/deleteCat/<id>',methods = ['GET'])
def deleteCat(id):
	cat = catinfo.query.filter_by(id=id).first()
	if cat :
		cat.status=0
		db.session.commit()
		flash("删除成功")
		return jsonify({'code':0,"message":'删除成功'})
	return jsonify({'code':-1,"message":'删除失败'})
@bp.route('/addtime/<id>',methods = ['GET', 'POST'])
def addtime(id):
	cat = catinfo.query.filter_by(id=id).first()

	form = addtimeForm()
	if form.validate_on_submit():
		time_info = timeinfo(description=form.description.data, recordtime=form.time.data, type=form.type.data, cat_id=id)
		db.session.add(time_info)
		db.session.commit()
		return redirect(url_for("main.index"))
	# print(cat.timeinfos.all())
	return render_template("abouttime.html",form=form,times = cat.timeinfos)


