'''test'''
import json
from flask import Flask
from flask_restplus import Api, Resource
from utils import message_to_Json
from pythonClient import blogClient


app = Flask(__name__)
api = Api(app)


@api.route('/blogs/')
class BlogListing(Resource):
    def get(self):
        try:
            blog = blogClient()
            blogList = blog.blogListing('this is title')
        except Exception as ex:
            return str(ex)
        return json.loads(message_to_Json(blogList))


@api.route('/create/')
class CreateBlog(Resource):
    '''to create a new blog'''
    def post(self):
        payload = self.api.payload
        title = payload.get('title')
        author = payload.get('author')
        content = payload.get('content')
        blog=blogClient()
        blogCreationResponse = blog.createBlog(title,author,content)
        return json.loads(message_to_Json(blogCreationResponse))


if __name__ == '__main__':
    app.run(debug=True)
