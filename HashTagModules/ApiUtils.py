import json as json, requests as requests
class ApiUtils :
    def getJsonDataForHashTag(self,key=""):
        try :

            data ={}
            requestData = requests.get("https://www.instagram.com/explore/tags/"+key+"/?__a=1")
            data.update( {"hashTagData" : json.loads(requestData.text)} )
            requestData = requests.get("https://www.instagram.com/web/search/topsearch/?context=blended&query=%23"+key+"&include_reel=true")
            data.update( {"relatedHashTags" : json.loads(requestData.text)} )
            return data
        except Exception as exce :
            raise exce
        