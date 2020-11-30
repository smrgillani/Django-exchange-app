from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.template import loader

from ..BL.CurrenciesBL import CurrenciesBL as cbl
from ..Models import *
import json
class CurrencyController:

	@method_decorator(login_required)
	def addUpdateCurrency(self, request, c_id=None):
		formMsg = ""
		co = Currency.Currency();

		if request.method == 'POST':
			formMsg = self.checkMissingFormKey(request)
			if(len(formMsg) == 0):

				uco = Currency.Currency();
				uco.Id = request.POST.get('cId',0)
				uco.userId = request.user.id
				uco.fullName = request.POST['fullName']
				uco.shortName = request.POST['shortName']
				uco.isActive = request.POST.get('isActive',False)
				uco.isActive = True if uco.isActive != False else False

				if uco.Id != '0':
					uco = cbl.updateCurrency(uco)
				else:
					uco = cbl.addCurrency(uco)
				return redirect('/currencies')
		else:
			if c_id is not None:
				co.Id = c_id
				co.userId = request.user.id
				co = cbl.selectCurrency(co)

		return render(request, 'currency.html', {'formMsg': formMsg, 'cObj': co})

	@method_decorator(login_required)
	def allCurrencies(self, request):
		return render(request, 'currencies.html', {'records': cbl.allCurrencies(request.user.id)})

	@method_decorator(login_required)
	def removeCurrency(self, request, c_id=None):
		if c_id is not None:
			co = Currency.Currency();
			co.Id = c_id
			co.userId = request.user.id
			cbl.deleteCurrency(co)
		return redirect('/currencies')

	def checkMissingFormKey(self, formRequest):
		dataStr = ""
		dataDict = dict()
		dataDict['fullName'] = "Full Name "
		dataDict['shortName'] = "Short Name "
		for x in dataDict:
			try:
				if((len(formRequest.POST[x]) > 0) == False):
					dataStr = dataDict[x] + " is missing."
					break
			except MultiValueDictKeyError:
				dataStr = dataDict[x] + " is missing."
				break
		return dataStr