from ..DAL.CurrenciesDAL import CurrenciesDAL as cc
from ..Models.Currency import Currency
from ..Entities.Currencies import Currencies

class CurrenciesBL():

	def allCurrencies(icv):
		act = cc.allCurrencies(icv)
		Currencies = list()
		for i in act:
			crncy = Currency()
			crncy.Id = i.id
			crncy.fullName = i.name
			crncy.shortName = i.shortname
			crncy.isActive = i.is_active
			Currencies.append(crncy)
		return Currencies

	def addCurrency(ico):
		crncy = Currencies();
		crncy.name = ico.fullName
		crncy.user_id = ico.userId
		crncy.shortname = ico.shortName
		crncy.is_active = ico.isActive
		rcto = cc.addCurrency(crncy)
		if rcto is None:
			return None
		crncy = Currency()
		crncy.Id = rcto.id
		crncy.fullName = rcto.name
		crncy.shortName = rcto.shortname
		crncy.isActive = rcto.is_active
		return crncy

	def selectCurrency(ico):
		crncy = Currencies();
		crncy.id = ico.Id
		crncy.user_id = ico.userId
		rcto = cc.selectSingleCurrency(crncy)
		if rcto is None:
			return None
		crncy = Currency()
		crncy.Id = rcto.id
		crncy.fullName = rcto.name
		crncy.shortName = rcto.shortname
		crncy.isActive = rcto.is_active
		return crncy

	def selectCurrencyBySS(ico):
		crncy = Currencies();
		crncy.id = ico.Id
		crncy.user_id = ico.userId
		crncy.shortname = ico.shortName
		rcto = cc.selectSingleCurrencyBySS(crncy)
		if rcto is None:
			return None
		crncy = Currency()
		crncy.Id = rcto.id
		crncy.fullName = rcto.name
		crncy.shortName = rcto.shortname
		crncy.isActive = rcto.is_active
		return crncy

	def updateCurrency(ico):
		crncy = Currencies();
		crncy.id = ico.Id
		crncy.name = ico.fullName
		crncy.user_id = ico.userId
		crncy.shortname = ico.shortName
		crncy.is_active = ico.isActive
		rcto = cc.updateCurrency(crncy)
		if rcto is None:
			return None
		crncy = Currency()
		crncy.Id = rcto.id
		crncy.fullName = rcto.name
		crncy.shortName = rcto.shortname
		crncy.isActive = rcto.is_active
		return crncy

	def deleteCurrency(ico):
		crncy = Currencies();
		crncy.id = ico.Id
		crncy.user_id = ico.userId
		rcto = cc.deleteCurrency(crncy)
		if rcto is None:
			return False
		else:
			return True