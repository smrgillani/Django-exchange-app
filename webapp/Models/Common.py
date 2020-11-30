import json
import datetime

class Common():
    def ConverttoJson(self,data):
        #return json.dumps(data, default=lambda o: o.__dict__, indent=4)
        return json.dumps(data, default=lambda o: o.__dict__, sort_keys=True, indent=4)
