from ..Entities.Currencies import Currencies as cr
from .Commons import Commons as c
import datetime
from django.core.exceptions import ObjectDoesNotExist

class CurrenciesDAL:
	def allCurrencies(icv):
		return cr.objects.filter(user_id=icv).all()
	def addCurrency(ico):
		return cr.objects.create(name=ico.name, user_id=ico.user_id, shortname=ico.shortname, is_active=ico.is_active, created_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
	def selectSingleCurrency(ico):
		co = None
		try:
			co = cr.objects.get(id=ico.id, user_id=ico.user_id)
		except ObjectDoesNotExist:
		 	co = None
		return co
	def selectSingleCurrencyById(icv):
		co = None
		try:
			co = cr.objects.get(id=icv)
		except ObjectDoesNotExist:
		 	co = None
		return co
	def selectSingleCurrencyBySS(ico):
		co = None
		try:
			co = cr.objects.get(user_id=ico.user_id, shortname=ico.shortname)
		except ObjectDoesNotExist:
		 	co = None
		return co
	def updateCurrency(ico):
		qrr = cr.objects.filter(id=ico.id, user_id=ico.user_id).update(name=ico.name, shortname=ico.shortname, is_active=ico.is_active, updated_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
		return (None, cr.objects.get(id=ico.id)) [qrr != 0]
	def deleteCurrency(ico):
		qrr = cr.objects.filter(id=ico.id, user_id=ico.user_id).delete()
		return (False, True) [qrr[0] != 0]