from app import db
from datetime import datetime
class catinfo(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	catname = db.Column(db.String(100), index=True)
	birthday = db.Column(db.DATE, index=True)
	sex = db.Column(db.String(200))
	headimage = db.Column(db.String(100),index=True)
	status = db.Column(db.Integer,index=True)
	timeinfos = db.relationship("timeinfo",backref = 'cat',lazy = 'dynamic')

	def __repr__(self):
		return '<catinfo {}>'.format(self.catname)
class timeinfo(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	description = db.Column(db.String(100),index=True)#描述
	recordtime =db.Column(db.DATE)#记录时间
	type=db.Column(db.Integer)#1生日，2疫苗时间
	cat_id = db.Column(db.Integer,db.ForeignKey('catinfo.id'))
	def __repr__(self):
		return '<timeinfo {}>'.format(self.description)