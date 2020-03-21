from operator import pos

from sqlalchemy.sql.expression import true


class InstaJSONExtracor:

    def __init__(self, data_json):
        try:
            self.json_data = data_json
            self.hashtag_name=self.json_data["hashTagData"]["graphql"]["hashtag"]["name"]
            self.hashtag_id=self.json_data["hashTagData"]["graphql"]["hashtag"]["id"]
            self.top_count = len(self.json_data["hashTagData"]["graphql"]["hashtag"]["edge_hashtag_to_top_posts"]["edges"])
            self.post_count = len(self.json_data["hashTagData"]["graphql"]["hashtag"]["edge_hashtag_to_media"]["edges"])
        except Exception as exce:
            raise exce
    def get_all_posts_count(self):
        try:
            return self.json_data["hashTagData"]["graphql"]["hashtag"]["edge_hashtag_to_media"]["count"]
        except Exception as exce:
            raise exce
    def get_post_count(self):
        try:
            return int(self.post_count)
        except Exception as exce:
            raise exce
    def get_toppost_count(self):
        try:
            return int(self.top_count)
        except Exception as exce:
            raise exce
    def get_insta_related_tags(self):
        try:
            return self.json_data["relatedHashTags"]["hashtags"]
        except Exception as exce:
            raise exce
    def get_top_posts(self):
        try:
            return self.json_data["hashTagData"]["graphql"]["hashtag"]["edge_hashtag_to_top_posts"]["edges"]
        except Exception as exce:
            raise exce
    def get_posts(self):
        try:
            return self.json_data["hashTagData"]["graphql"]["hashtag"]["edge_hashtag_to_media"]["edges"]
        except Exception as exce:
            raise exce
    @staticmethod
    def get_post_id_node(node):
        try:
            return InstaJSONExtracor.get_post(node)["id"]
        except Exception as exce:
            raise exce
    @staticmethod
    def get_post(node):
        try:
            return node["node"]
        except Exception as exce:
            raise exce
    @staticmethod
    def get_post_id(post):
        try:
            return post["id"]
        except Exception as exce:
            raise exce
    @staticmethod
    def get_post_text(post):
        try:
            return post["edge_media_to_caption"]["edges"][0]["node"]["text"]
        except Exception as exce:
            raise exce
    @staticmethod
    def get_post_isvideo(post):
        try:
            return post["is_video"] 
        except Exception as exce:
            raise exce
    @staticmethod
    def get_post_acces_text(post):
        try:
            if InstaJSONExtracor.get_post_isvideo(post) is True:
                return "unknown"
            else :
                return post["accessibility_caption"]
        except Exception as exce:
            raise exce
    @staticmethod
    def get_post_time(post):
        try:
            return post["taken_at_timestamp"]
        except Exception as exce:
            raise exce
    @staticmethod
    def get_post_comment_count(post):
        try:
            return post["edge_media_to_comment"]["count"]
        except Exception as exce:
            raise exce
    @staticmethod
    def get_post_like_count(post):
        try:
            return post["edge_liked_by"]["count"]
        except Exception as exce:
            raise exce
    @staticmethod
    def get_post_owner(post):
        try:
            return post["owner"]["id"]
        except Exception as exce:
            raise exce
    @staticmethod
    def get_post_link(post):
        try:
            return post["display_url"]
        except Exception as exce:
            raise exce
    
