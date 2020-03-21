import PIL.Image
from PIL import ExifTags

class ExifData:
    def getExifData(self,path):
        img = PIL.Image.open(path)
        exifDataRaw = img._getexif()
        return self.assignTags(exifDataRaw)
        
    def assignTags(self,RawData):
        exifData = {}
        for tag, value in RawData.items():
            decodedTag = ExifTags.TAGS.get(tag, tag)
            exifData[decodedTag] = value
        return exifData
