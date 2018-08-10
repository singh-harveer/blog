'''test'''
import json
from flask import Flask
from flask_restplus import Api, Resource
from utils import message_to_Json
from pythonClient import blogClient


app = Flask(__name__)
api = Api(app)


@api.route('/blogs')
class BlogListing(Resource):
    '''test'''

    def get(self):
        '''test'''

        try:
            blog = blogClient()
            blogList = blog.blogListing('this is title')
        except Exception as ex:
            return str(ex)
        return json.loads(message_to_Json(blogList))


if __name__ == '__main__':
    app.run(debug=True)
