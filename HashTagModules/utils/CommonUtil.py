import datetime


class CommonUtil:

    @staticmethod
    def removeSpaces(data):
        rda = set()
        if(len(data)>0):
            for da in data :
                rda.update({str(da.strip())})
            return rda
        else:
            return set()
    
    def removeHashSymbol(self,key):
        try :
            if key.startswith("#") :
                if(len(key)==1):
                    raise Exception("Value Error")
                return key[1:]
            else :
                return key
        except Exception as exce :
            raise exce

    def utctime(self,stamp=None):
        if(stamp is None):
            return datetime.datetime.utcnow().replace(microsecond=0)
        else :
            return datetime.datetime.utcfromtimestamp(stamp).replace(microsecond=0)