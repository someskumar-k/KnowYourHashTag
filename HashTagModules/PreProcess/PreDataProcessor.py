#LEVEL-2
#MODULE - DATA PREPROCESSOR
import re as re

from HashTagModules.utils.CommonUtil import CommonUtil

class PreDataProcessor :
    c_util = CommonUtil()
    # Define every variable as instance oriented unless its value remains constant for all hashtags
    def __init__(self,extractor,hashTag=None,withHash=False):
        self.extractor = extractor
        if(hashTag is None): 
            raise Exception('No HashTag Found')
        self.currentdate = self.c_util.utctime()
        self.withhash = withHash
        self.captions_dict = {}
        self.t_likes = 0
        self.t_likes_per_sec = 0.0
        self.t_comments = 0
        self.t_comments_per_sec=0.0
        self.accessibility_dict = {}
        self.contributers=set()
        self.top_post_id=set()
        self.top_recent_count=0
    #Total Data 
    def like_count(self,count):
        self.t_likes+=int(count)
        return count
    def comment_count(self,count):
        self.t_comments+=int(count)
        return count
    def like_per_second(self,count):
        self.t_likes_per_sec+=count
        return count
    def comment_per_second(self,count):
        self.t_comments_per_sec+=count
        return count
    def add_contributers(self,id):
        self.contributers.add(id)
        return id
    # DATE/TIME Related Processing
    def post_duration_utc(self, time):
        try: 
            return self.currentdate - time
        except Exception as exce:
            raise exce

    def post_datedetails(self,timeStamp):
        #des : Returns a dict has total hours,seconds,day for duration of the given time
        try:
            time=self.c_util.utctime(timeStamp)
            a = self.post_duration_utc(time)
            day,sec = a.days,a.total_seconds()
            rtd =  {'date':str(time),'t_days':day,'t_hrs':round(sec/3600),'t_sec':round(sec)}
            return rtd
        except Exception as exce:
            raise exce

    # end DATE/TIME
    #TEXT Processing
        ##Captions Maluplulating
    def add_caption(self,note):
        tags=[]
        try:
            if(len(note)>0):
                tags = self.extract_hashtags(str(note))
                self.count_hash_tag(tags)
            return tags
        except Exception as exc:
            raise exc

    def get_caption_ocurrence(self):
        return self.captions_dict

    def add_accessibility_caption(self,caption_text):
        captions=[]
        try:
            captions=self.extract_accessibility_caption(caption_text)
            self.count_accessibility_caption(caption_text)
            return captions
        except Exception as exc:
            raise exc

    def extract_accessibility_caption(self,caption_text):
        captions=[]
        try:
            caption_text = caption_text.split(':')
            if(len(caption_text)>1):
                caption_text=caption_text[1].split(',')
                temp=caption_text[len(caption_text)-1].split('and')
                captions = set(caption_text[:len(caption_text)-1])
                captions.update(set(temp))
                captions=self.c_util.removeSpaces(captions)
                return(captions)  
            else :
                return set({'novalue'})
        except Exception as exce:
            return set({'novalue'})

    def pre_add_owntags(self, data):
        if(('person' in data) or ('people' in data) or ('human' in data)):
            data = 'human'  
        return data
    def count_accessibility_caption(self,datas):
        try :
            if(len(datas)>0):
                for data in datas :
                    data = data.lower()
                    data = self.pre_add_owntags(data)
                    if data in self.accessibility_dict:
                        count = self.accessibility_dict.get(data) + 1
                        self.accessibility_dict.update({data:count})
                    else :
                        self.accessibility_dict.update({data:1})
        except Exception as exce:
            raise exce

    def extract_hashtags(self,data):
        try:
            if(self.withhash):
                return set(re.findall(r'#\w+', str(data)))
            else :
                return set(re.findall(r'#(\w+)', str(data)))
        except Exception as exce:
            raise exce
    
    def count_hash_tag(self,datas):
        # this method gets set of strings as keys and dict and build count the occurences
        try :
            if(len(datas)>0):
                for data in datas :
                    data = data.lower()
                    if data in self.captions_dict and data!=self.extractor.hashtag_name.lower():
                        count = self.captions_dict.get(data) + 1
                        self.captions_dict.update({data:count})
                    else :
                        self.captions_dict.update({data:1})
        except Exception as exce:
            raise exce
    
    # Post Data 
    
    def update_topinrecent_count(self,id):
        try:    
            if(self.top_post_id.__contains__(id)):
                self.top_recent_count+=1
        except Exception as exce:
            raise exce

    def add_top_post_id(self, id):
        try:
            self.top_post_id=set(id)
            return id
        except Exception as exce:
            raise exce
    def construct_post_data(self, node):
        try:
            post_data={}
            post=self.extractor.get_post(node)
            post_id=self.extractor.get_post_id(post)
            self.update_topinrecent_count(post_id)
            user_tags = self.add_caption(self.extractor.get_post_text(post))
            access_caption=self.add_accessibility_caption(self.extractor.get_post_acces_text(post))
            time=self.extractor.get_post_time(post)
            time=self.post_datedetails(time)
            comment=self.extractor.get_post_comment_count(post)
            like=self.extractor.get_post_like_count(post)
            self.like_count(like)
            self.comment_count(comment)
            like_persec=like/time.get('t_sec')
            comment_persec=comment/time.get('t_sec')
            self.like_per_second(like_persec)
            self.comment_per_second(comment_persec)
            post_data.update({
                'likes':like,
                'comments':comment,
                'like_per_sec':like_persec,
                'comment_per_sec':comment_persec,
                'time_data':time,
                'access_caption':access_caption,
                'user_tags':user_tags,
                'url':self.extractor.get_post_link(post),
                'owner': self.add_contributers(self.extractor.get_post_owner(post))
            })
            return {post_id:post_data}
        except Exception as exce:
            raise exce
    
    # get hash tag relate data
    def get_top_recent_percent(self):
        return (self.top_recent_count/self.extractor.get_toppost_count())*100
    def get_avg_likes(self):
        return self.t_likes/self.extractor.get_post_count()
    def get_avg_comment(self):
        return self.t_comments/self.extractor.get_post_count()
    def get_avg_likes_persec(self):
        return self.t_likes_per_sec/self.extractor.get_post_count()
    def get_avg_comment_persec(self):
        return self.t_comments_per_sec/self.extractor.get_post_count()
    def get_user_hashtags(self):
        return self.get_caption_ocurrence()
    def get_access_keys(self):
        return self.accessibility_dict
    def get_contributers_count(self):
        return self.contributers.__len__()
    
##TESTING-PART
# xy = DataUtils();
# print('',datetime.datetime.utcnow().replace(microsecond=0),'',datetime.datetime.utcfromtimestamp(1581559365).replace(microsecond=0))
# p = xy.post_duration_utc(1581559365)
# print(xy.post_datedetails(1581554365))