from ..Entities.Conversions import Conversions as cv
from .Commons import Commons as c
import datetime
from django.core.exceptions import ObjectDoesNotExist

class ConversionsDAL:
	def allConversions(icv):
		return cv.objects.filter(user_id=icv).all()
	def addConversion(ico):
		return cv.objects.create(user_id=ico.user_id, from_id=ico.from_id, to_id=ico.to_id, rate=ico.rate)
	def selectSingleConversionByToAndFromId(ico):
		co = None
		try:
			co = cv.objects.get(user_id=ico.user_id, from_id=ico.from_id, to_id=ico.to_id)
		except ObjectDoesNotExist:
		 	co = None
		return co
	def selectSingleConversion(ico):
		co = None
		try:
			co = cv.objects.get(id=ico.id, user_id=ico.user_id)
		except ObjectDoesNotExist:
		 	co = None
		return co
	def updateConversion(ico):
		qrr = cv.objects.get(id=ico.id, user_id=ico.user_id)
		qrr.from_id=ico.from_id
		qrr.to_id=ico.to_id
		qrr.rate=ico.rate
		qrr.save()
		return (None, cv.objects.get(id=ico.id)) [qrr != 0]
	def deleteConversion(ico):
		qrr = cv.objects.filter(id=ico.id, user_id=ico.user_id).delete()
		return (False, True) [qrr[0] != 0]