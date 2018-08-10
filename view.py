from flask import Flask, jsonify
from flask_restplus import Api,Resource
from pythonClient import blogClient
import json
from addict import Dict



app = Flask(__name__)
api = Api(app)

@api.route('/blogs')
class BlogListing(Resource):

	def get(self):

		dataList = []

		result = Dict(**{

		"meta":
		{
			"success":True,
			"message":'Ok',
			"code":400
		},
		"data":None
		})


		blogData = Dict({
			"title":'',
			"success":'',
			"code":''
			})


		try:


			blog = blogClient()
			blogList=blog.blogListing('this is title')

			result.meta.success = blogList.meta.success
			result.meta.message = blogList.meta.message
			result.meta.code = blogList.meta.code
			for data in blogList.data:
				print('title is: {}'.format(data.title))
				print('author is: {}'.format(data.author))
				blogData.title = data.title
				blogData.author = data.author
				blogData.content = data.content
				dataList.append(blogData)

			result.data = dataList
		except exception as ex:
			result.meta.code = 400
			result.meta.message = str(ex)

			return jsonify(result)

		return jsonify(result)


if __name__ == '__main__':
	app.run(debug=True)
