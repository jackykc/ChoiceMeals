
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class JWTMiddleware(object):

	def process_view(self, request, view_func, view_args, view_kwargs):
		token = request.META.get('HTTP_AUTHORIZATION', '')
		if not token.startswith('JWT'):
			return
		jwt_auth = JSONWebTokenAuthentication()
		auth = None
		try:
			auth = jwt_auth.authenticate(request)
		except Exception as e:
			print(e)
			return 
		request.user = auth[0]



# below is Django 1.10+
#class JWTMiddleware(object):
	# def __init__(self, response):
	# 	self.get_response = response


	# def __call__(self, request):
	# 	token = request.META.get('HTTP_AUTHORIZATION', '')
	# 	print("Token is", token)
	# 	if not token.startswith('JWT'):
	# 		print("Token does not start with JWT")
	# 		return self.get_response(request)

	# 	jwt_auth = JSONWebTokenAuthentication()
	# 	auth = None
	# 	try:
	# 		auth = jwt_auth.authenticate(request)
	# 	except Exception as e:
	# 		print(e)
	# 		return self.get_response(request)
	# 	request.user = auth[0]
	# 	print("===================================")
	# 	print(request.user)
	# 	response = self.get_response(request)
	# 	print(response.content)
	# 	print("===================================")
		
	# 	return response