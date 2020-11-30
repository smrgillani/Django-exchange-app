import datetime
import hashlib
class Commons:
	def getUniqueId(ico):
		unq_id = ico
		if(unq_id != None):
			unq_id = unq_id.u_id
		else:
			unq_id = 0
		unq_id = datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f") + str(unq_id)
		unq_id = hashlib.md5(unq_id.encode())
		unq_id = unq_id.hexdigest()
		return unq_id