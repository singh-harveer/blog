import grpc
import time
import blog_pb2
import blog_pb2_grpc
from model import Blog
from concurrent import futures
from base import protobuf_to_json
from addict import Dict

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class BlogServicer(blog_pb2_grpc.BlogServicer):

	def getResponse(self):

		return Dict({
			"meta":
			{
			"success":False,
			"message":"Ok",
			"code":200
			},
			"data":None
			}

			)


	#add new blog 
	def CreateBlog(self,request,context):

		result=self.getResponse()

		try:
			newBlog=Blog(request.Title,request.Author,request.Content)
			result.data = Blog.createBlog(newBlog)
			result.meta.success=True
			result.data='blog has been created successfully!!'

		except Exception as e:
			result.meta.message=str(e)
			result.meta.code=400
			result.data = ''
			return blog_pb2.BlogCreationResponse(**result)

		return blog_pb2.BlogCreationResponse(**result)

		

	def BlogListing(self,request,context):
		result=self.getResponse()
		try:

			result.data=Blog.getAllBlog()
			# print('===from server=======')
			# print(result)
			result.meta.success=True

		except Exception as e:
			print(str(e))
			result.meta.message:str(e)
			result.meta.code=400

		return blog_pb2.BlogListingResponse(**result)




	@classmethod
	def serve(cls, port=50051):
		server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
		blog_pb2_grpc.add_BlogServicer_to_server(BlogServicer(), server)
		server.add_insecure_port(f'[::]:{port}')
		server.start()
		print(f'Blog GRPC Server running on port : {port} ')
		try:
			while True:
				time.sleep(_ONE_DAY_IN_SECONDS)
		except KeyboardInterrupt as e:
			server.stop(0)
		print('Blog GRPC Server stopped ...')

if __name__ == '__main__':
	BlogServicer.serve()

