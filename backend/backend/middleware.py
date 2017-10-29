
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class JWTMiddleware(object):

	def __init__(self, response):
		self.get_response = response


	def __call__(self, request):
		token = request.META.get('HTTP_AUTHORIZATION', '')
		print(request.META)
		print("Token is", token)
		if not token.startswith('JWT'):
			print("Token does not start with JWT")
			return self.get_response(request)

		jwt_auth = JSONWebTokenAuthentication()
		auth = None
		try:
			auth = jwt_auth.authentication(request)
		except Exception:
			return self.get_response(request)
		request.user = auth[0]
		response = self.get_response(request)
		return response