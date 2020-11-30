from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from ..BL.ConversionsBL import ConversionsBL as cnbl
from ..BL.CurrenciesBL import CurrenciesBL as cbl
from ..Models import *
import json
class ConversionApiController(APIView):
	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)
	@api_view(['GET'])
	def allConversions(request, format=None):
		data = cnbl.allConversions(request.user.id)
		return HttpResponse(Common.Common().ConverttoJson(data), content_type="application/json")

	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)
	@api_view(['POST'])
	def addConversion(request, format=None):
		ud = json.loads(request.body)
		cvrn = Conversion.Conversion()
		cvrn.userId = request.user.id

		crncy = Currency.Currency()
		crncy.userId = request.user.id
		crncy.shortName= ud['currency_from_short_name']
		cvrn.fromId = cbl.selectCurrencyBySS(crncy).Id

		crncy = Currency.Currency()
		crncy.userId = request.user.id
		crncy.shortName= ud['currency_from_short_to']
		cvrn.toId = cbl.selectCurrencyBySS(crncy).Id
		
		cvrn.rate = ud['rate']
		data = cnbl.addConversion(cvrn)
		
		return HttpResponse(Common.Common().ConverttoJson(data), content_type="application/json")

	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)
	@api_view(['POST'])
	def getConversion(request, format=None):
		ud = json.loads(request.body)
		cvrn = Conversion.Conversion()
		cvrn.userId = request.user.id
		cvrn.Id= ud['id']
		data = cnbl.selectConversion(cvrn)
		return HttpResponse(Common.Common().ConverttoJson(data), content_type="application/json")

	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)
	@api_view(['POST'])
	def getConversionRate(request, format=None):
		ud = json.loads(request.body)
		cvrn = Conversion.Conversion()
		cvrn.userId = request.user.id

		crncy = Currency.Currency()
		crncy.userId = request.user.id
		crncy.shortName= ud['currency_from_short_name']
		cvrn.fromId = cbl.selectCurrencyBySS(crncy).Id

		crncy = Currency.Currency()
		crncy.userId = request.user.id
		crncy.shortName= ud['currency_from_short_to']
		cvrn.toId = cbl.selectCurrencyBySS(crncy).Id
		
		data = cnbl.selectConversionByTAFId(cvrn)
		return HttpResponse(Common.Common().ConverttoJson(data), content_type="application/json")

	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)
	@api_view(['POST'])
	def updateConversion(request, format=None):
		ud = json.loads(request.body)
		cvrn = Conversion.Conversion()
		cvrn.Id = ud['Id']
		cvrn.userId = request.user.id

		crncy = Currency.Currency()
		crncy.userId = request.user.id
		crncy.shortName= ud['currency_from_short_name']
		cvrn.fromId = cbl.selectCurrencyBySS(crncy).Id

		crncy = Currency.Currency()
		crncy.userId = request.user.id
		crncy.shortName= ud['currency_from_short_to']
		cvrn.toId = cbl.selectCurrencyBySS(crncy).Id
		
		cvrn.rate = ud['rate']
		data = cnbl.updateConversion(cvrn)
		
		return HttpResponse(Common.Common().ConverttoJson(data), content_type="application/json")
	
	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)
	@api_view(['POST'])
	def removeConversion(request, format=None):
		ud = json.loads(request.body)
		cvrn = Conversion.Conversion()
		cvrn.userId = request.user.id
		cvrn.Id= ud['id']
		data = cnbl.deleteConversion(cvrn)
		return HttpResponse(Common.Common().ConverttoJson(data), content_type="application/json")