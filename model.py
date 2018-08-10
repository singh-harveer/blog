import os
import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,DateTime,String,Integer
from base import Base, getSession
from sqlalchemy.exc import InternalError, IntegrityError


class Blog(Base):
	__tablename__='blog'

	id = Column( Integer, primary_key=True,autoincrement=True)
	title = Column( String(200), unique=True, nullable=False)
	author = Column(String(40), nullable=False)
	content=Column(String(2000),nullable=False)
	CreatedAt = Column(DateTime, default=datetime.datetime.utcnow,nullable=False)
	UpdatedAt = Column(DateTime, default=datetime.datetime.utcnow,onupdate=datetime.datetime.utcnow,nullable=False)

	#Base.metadata.create_all()

	def __repr__(self):

		return "Blog(id='%s',title='%s',author='%s',content='%s',)"%(self.id,self.title,self.author,self.content)

	def __init__(self,title,author,content):
		#self.id=id
		self.title=title
		self.author=author
		self.content=content

	#to add new blog into data base
	@classmethod
	def createBlog(cls, obj):

		try:
			session=getSession()
			print('1=======')
			session.add(obj)
			print('2======')
			session.commit()
			return obj
		except Exception as e:
			session.rollback()
			print(str(e))
			print("exception accured while trying to insert data in to blog DB")
		return obj

	#to return all blogs from
	@classmethod
	def getAllBlog(cls):

		
		result=[]

		try:
			session=getSession()
			#session.begin()
			for blog in session.query(Blog.title,Blog.author,Blog.content):
				data={}
			
				data['title']=blog[0]
				data['author']=blog[1]
				data['content']=blog[2]
				result.append(data)
				#print(blog)
		except Exception as e:
			session.rollback()
			print(str(e))
			return result

		#print('====from model/getAllBlog()=========')
		print(result)

		return result

		

		
#print(Blog.getAllBlog())


# blog1=Blog('my six blog','Harry','this is third blog content')
# print(blog1)
# blog1.addNewBlog()
# print(Blog.__table__)


