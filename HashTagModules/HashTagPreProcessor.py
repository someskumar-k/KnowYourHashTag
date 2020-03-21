from flask import json
from HashTagModules.utils.InstaJSONExtract import InstaJSONExtracor
from flask import jsonify

from HashTagModules.PreProcess.PreDataProcessor import PreDataProcessor
class HashTagPreProcessor :

    def __init__(self,json_data=None,hash_tag=None):
        try:
            self.return_dta = {}
            self.hash_tag = hash_tag
            self.json_data = {}
            if(json_data is None):
                self.json_data = None
            else :
                self.json_data = json_data
            self.extractor = InstaJSONExtracor(self.json_data)
            self.processor = PreDataProcessor(self.extractor,hash_tag)
            self.tp_dta=self.get_top_post_data()
            self.p_dta=self.get_post_data()
            self.constructJSONData()
        except Exception as exce:
            raise exce

    def constructJSONData(self):
        try:    
            self.return_dta.update({
                'total_post_count':self.extractor.get_post_count(),
                'all_post_count':self.extractor.get_all_posts_count(),
                'insta_rel_tags':self.extractor.get_insta_related_tags(),
                'top_post_id':self.tp_dta,
                'post_data':self.p_dta,
                'post_poplarity':self.processor.get_top_recent_percent(),
                'post_avg_likes':self.processor.get_avg_likes(),
                'post_avg_likes_persec':self.processor.get_avg_likes_persec(),
                'user_hashtags':self.processor.get_user_hashtags(),
                'access_captions':self.processor.get_access_keys(),
                'contributer_count':self.processor.get_contributers_count()

            })
        except Exception as exce:
            raise exce
        
    def getProcessedHashTagData(self):
        try:
            return {'processed_dta': self.return_dta}
        except Exception as exce:
            raise exce
    def get_post_data(self):
        data={}
        try:
            for node in self.extractor.get_posts() :
                data.update(self.processor.construct_post_data(node))
            return data
        except Exception as exce:
            raise exce
    def get_top_post_data(self):
        id=[]
        try:
            for node in self.extractor.get_top_posts() :
                id.append(self.extractor.get_post_id_node(node))
            return self.processor.add_top_post_id(id)
        except Exception as exce:
            raise exce
    