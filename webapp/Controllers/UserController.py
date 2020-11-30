from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.template import loader
from rest_framework_jwt.settings import api_settings

from ..BL.UsersBL import UsersBL as ubl
from ..Models import *
import json
class UserController:
	def userSignup(self, request):
		formMsg = ""
		if request.method == 'POST':
			formMsg = self.checkMissingRegisterFormKey(request)
			if(len(formMsg) == 0):

				if(request.POST['password'] == request.POST['pswRepeat']):
					udo = User.User()
					udo.username = request.POST['username']
					if(ubl.selectUserbyUsername(udo) is None):
						udo.password = request.POST['password']
						udo = ubl.addUser(udo)
						return redirect('/login')
					else:
						formMsg = "User Already Exists with the same Username Or Email !"
				else:
					formMsg = "Password didn't match with Repeat Password !"

		return render(request, 'register.html', {'formMsg': formMsg})

	def userLoginRd(self, request):
		return redirect('/login')

	def userLogin(self, request):
		formMsg = ""
		if request.method == 'POST':
			formMsg = self.checkMissingLoginFormKey(request)
			if(len(formMsg) == 0):
				usernameOrEmail = request.POST['usernameOrEmail']
				userpassword = request.POST['password']
				user = authenticate(request, username=usernameOrEmail, password=userpassword)
				if user is not None:
					login(request, user)
					jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
					jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
					payload = jwt_payload_handler(user)
					request.session['token'] = jwt_encode_handler(payload)
					return redirect('/')
				else:
					formMsg = "Username / Email not found or Password is incorrect !"
		return render(request, 'login.html', {'formMsg': formMsg, 'request':request})

	@method_decorator(login_required)
	def userDashboard(self, request):
		return render(request, 'index.html', {'records': None, 'precords': None})

	@method_decorator(login_required)
	def userLogout(self, request):
		logout(request)
		return redirect('/')

	def checkMissingRegisterFormKey(self, formRequest):
		dataStr = ""
		dataDict = dict()
		dataDict['username'] = "Username"
		dataDict['password'] = "Password"
		dataDict['pswRepeat'] = "Repeat Password"
		for x in dataDict:
			try:
				if((len(formRequest.POST[x]) > 0) == False):
					dataStr = dataDict[x] + " is missing."
					break
			except MultiValueDictKeyError:
				dataStr = dataDict[x] + " is missing."
				break
		return dataStr

	def checkMissingLoginFormKey(self, formRequest):
		dataStr = ""
		dataDict = dict()
		dataDict['usernameOrEmail'] = "Username or Email "
		dataDict['password'] = "Password "
		for x in dataDict:
			try:
				if((len(formRequest.POST[x]) > 0) == False):
					dataStr = dataDict[x] + " is missing."
					break
			except MultiValueDictKeyError:
				dataStr = dataDict[x] + " is missing."
				break
		return dataStr