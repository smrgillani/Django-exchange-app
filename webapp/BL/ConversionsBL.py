from ..DAL.ConversionsDAL import ConversionsDAL as cv
from ..DAL.CurrenciesDAL import CurrenciesDAL as cc
from ..Models.Conversion import Conversion
from ..Entities.Conversions import Conversions

class ConversionsBL():

	def allConversions(icv):
		act = cv.allConversions(icv)
		Conversions = list()
		for i in act:
			cvrn = Conversion()
			cvrn.Id = i.id
			cvrn.currencyFromShortName = cc.selectSingleCurrencyById(i.from_id).shortname
			cvrn.currencyToShortName = cc.selectSingleCurrencyById(i.to_id).shortname
			cvrn.rate = i.rate
			Conversions.append(cvrn)
		return Conversions

	def addConversion(ico):
		cvrn = Conversions();
		cvrn.user_id = ico.userId
		cvrn.from_id = ico.fromId
		cvrn.to_id = ico.toId
		cvrn.rate = ico.rate
		rcto = cv.addConversion(cvrn)
		if rcto is None:
			return None
		cvrn = Conversion()
		cvrn.Id = rcto.id
		cvrn.currencyFromShortName = cc.selectSingleCurrencyById(rcto.from_id).shortname
		cvrn.currencyToShortName = cc.selectSingleCurrencyById(rcto.to_id).shortname
		cvrn.rate = rcto.rate
		return cvrn

	def selectConversion(ico):
		cvrn = Conversions();
		cvrn.id = ico.Id
		cvrn.user_id = ico.userId
		rcto = cv.selectSingleConversion(cvrn)
		if rcto is None:
			return None
		cvrn = Conversion()
		cvrn.Id = rcto.id
		cvrn.currencyFromShortName = cc.selectSingleCurrencyById(rcto.from_id).shortname
		cvrn.currencyToShortName = cc.selectSingleCurrencyById(rcto.to_id).shortname
		cvrn.rate = rcto.rate
		return cvrn

	def selectConversionByTAFId(ico):
		cvrn = Conversions();
		cvrn.id = ico.Id
		cvrn.user_id = ico.userId
		cvrn.from_id = ico.fromId
		cvrn.to_id = ico.toId
		rcto = cv.selectSingleConversionByToAndFromId(cvrn)
		if rcto is None:
			return None
		cvrn = Conversion()
		cvrn.rate = rcto.rate
		return cvrn

	def updateConversion(ico):
		cvrn = Conversions();
		cvrn.id = ico.Id
		cvrn.user_id = ico.userId
		cvrn.from_id = ico.fromId
		cvrn.to_id = ico.toId
		cvrn.rate = ico.rate
		rcto = cv.updateConversion(cvrn)
		if rcto is None:
			return None
		cvrn = Conversion()
		cvrn.Id = rcto.id
		cvrn.currencyFromShortName = cc.selectSingleCurrencyById(rcto.from_id).shortname
		cvrn.currencyToShortName = cc.selectSingleCurrencyById(rcto.to_id).shortname
		cvrn.rate = rcto.rate
		return cvrn

	def deleteConversion(ico):
		cvrn = Conversions();
		cvrn.id = ico.Id
		cvrn.user_id = ico.userId
		rcto = cv.deleteConversion(cvrn)
		if rcto is None:
			return False
		else:
			return True