import blog_pb2 as blog_message
import blog_pb2_grpc as blog_services
import grpc
import sys
from base import protobuf_to_json

class blogClient(object):

	def __init__(self):
		self.host='localhost'
		self.port=50051
		self.channel=grpc.insecure_channel('{}:{}'.format(self.host,self.port))
		self.stub=blog_services.BlogStub(self.channel)
		self.blog_message=blog_message



	def blogListing(self,title):

		request=self.blog_message.BlogListingRequest(Title=title)
		response=self.stub.BlogListing(request)
		
		return response

	#create a new blog

	def createBlog(self,title,author,content):

		createBlogRequest = self.blog_message.BlogCreationObject(Title=title,Author=author,Content=content)
		response = self.stub.CreateBlog(createBlogRequest)
		if response:
			print(response)
		return response



if __name__ == '__main__':

	blog=blogClient()
	blog.blogListing('testName')
	#blog.createBlog('python tutorials-1','paython star','welcome to python!!!')







