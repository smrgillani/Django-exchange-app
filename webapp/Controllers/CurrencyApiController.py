from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from ..BL.CurrenciesBL import CurrenciesBL as cbl
from ..Models import *
import json
class CurrencyApiController(APIView):
	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)
	@api_view(['GET'])
	def allCurrency(request, format=None):
		data = cbl.allCurrencies(request.user.id)
		return HttpResponse(Common.Common().ConverttoJson(data), content_type="application/json")

	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)
	@api_view(['POST'])
	def addCurrency(request, format=None):
		ud = json.loads(request.body)
		crncy = Currency.Currency()
		crncy.userId = request.user.id
		crncy.fullName = ud['fullname']
		crncy.shortName = ud['shortname']
		crncy.isActive = ud['isactive']
		data = cbl.addCurrency(crncy)
		return HttpResponse(Common.Common().ConverttoJson(data), content_type="application/json")

	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)
	@api_view(['GET'])
	def getCurrency(request, format=None):
		ud = json.loads(request.body)
		crncy = Currency.Currency()
		crncy.userId = request.user.id
		crncy.Id= ud['id']
		data = cbl.selectCurrency(crncy)
		return HttpResponse(Common.Common().ConverttoJson(data), content_type="application/json")

	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)
	@api_view(['POST'])
	def updateCurrency(request, format=None):
		ud = json.loads(request.body)
		crncy = Currency.Currency()
		crncy.userId = request.user.id
		crncy.Id= ud['id']
		crncy.fullName = ud['fullname']
		crncy.shortName = ud['shortname']
		crncy.isActive = ud['isactive']
		data = cbl.updateCurrency(crncy)
		return HttpResponse(Common.Common().ConverttoJson(data), content_type="application/json")
	
	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)
	@api_view(['GET'])
	def removeCurrency(request, format=None):
		ud = json.loads(request.body)
		crncy = Currency.Currency()
		crncy.userId = request.user.id
		crncy.Id= ud['id']
		data = cbl.deleteCurrency(crncy)
		return HttpResponse(Common.Common().ConverttoJson(data), content_type="application/json")