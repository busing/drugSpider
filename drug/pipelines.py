# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DrugPipeline(object):
    def process_item(self, item, spider):
        for field in item:
            print field + ': ' + item[field][0]
        return item


import json
import codecs
class jsonWithEncodingPipeline(object):
  def __init__(self):
    print('init jsonWithEncodingPipeline')
    self.file = codecs.open('F:\\git\\drug\\data\\data_utf8.json','w',encoding='utf-8')

  def process_item(self,item,splider):
    line = json.dumps(dict(item),ensure_ascii=False)+'\n'
    self.file.write(line)
    return item

  def close_spider(self,splider):
    print('close jsonWithEncodingPipeline')
    self.file.close()



import json
import codecs
import scrapy
from scrapy import FormRequest,Request
class sqlPipeline(object):
  def __init__(self):
    print('init sqlPipeline')
    self.file = open('F:\\git\\drug\\data\\data.sql','a')

  def process_item(self,item,splider):
    sql ='insert into t_drug_splider values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'\
         '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'\
         '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'\
         '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'\
         '%s,%s,%s,%s,%s,%s,%s,%s);\n' % (\
          ('\''+('' if item['code'] == None else item['code'])+'\''),\
          ('\''+('' if item['codename'] == None else item['codename'])+'\''),\
          ('\''+('' if item['namecn'] == None else item['namecn'])+'\''),\
          ('\''+('' if item['nameen'] == None else item['nameen'])+'\''),\
          ('\''+('' if item['aliascn'] == None else item['aliascn'])+'\''),\
          ('\''+('' if item['dosage'] == None else item['dosage'])+'\''),\
          ('\''+('' if item['categoryChild'] == None else item['categoryChild'])+'\''),\
          ('\''+('' if item['dosageUnit'] == None else item['dosageUnit'])+'\''),\
          ('\''+('' if item['packingNum'] == None else item['packingNum'])+'\''),\
          ('\''+('' if item['leastUnit'] == None else item['leastUnit'])+'\''),\
          ('\''+('' if item['buyUnit'] == None else item['buyUnit'])+'\''),\
          ('\''+('' if item['specification'] == None else item['specification'])+'\''),\
          ('\''+('' if item['newotc'] == None else item['newotc'])+'\''),\
          ('\''+('' if item['formula'] == None else item['formula'])+'\''),\
          ('\''+('' if item['composition'] == None else item['composition'])+'\''),\
          ('\''+('' if item['drugattribute'] == None else item['drugattribute'])+'\''),\
          ('\''+('' if item['gongneng'] == None else item['gongneng'])+'\''),\
          ('\''+('' if item['yongfa'] == None else item['yongfa'])+'\''),\
          ('\''+('' if item['adr'] == None else item['adr'])+'\''),\
          ('\''+('' if item['contraindication'] == None else item['contraindication'])+'\''),\
          ('\''+('' if item['note'] == None else item['note'])+'\''),\
          ('\''+('' if item['pregnantwomentaboo'] == None else item['pregnantwomentaboo'])+'\''),\
          ('\''+('' if item['childrentaboo'] == None else item['childrentaboo'])+'\''),\
          ('\''+('' if item['elderlytaboo'] == None else item['elderlytaboo'])+'\''),\
          ('\''+('' if item['interaction'] == None else item['interaction'])+'\''),\
          ('\''+('' if item['pharmacology'] == None else item['pharmacology'])+'\''),\
          ('\''+('' if item['storage'] == None else item['storage'])+'\''),\
          ('\''+('' if item['shelflife'] == None else item['shelflife'])+'\''),\
          ('\''+('' if item['refdrugcompanyname'] == None else item['refdrugcompanyname'])+'\''),\
          ('\''+('' if item['refcorpaddress'] == None else item['refcorpaddress'])+'\''),\
          ('\''+('' if item['titleimgURL'] == None else item['titleimgURL'])+'\''),\
          ('\''+('' if item['commonUse'] == None else item['commonUse'])+'\''),\
          ('\''+('' if item['is_chronic'] == None else item['is_chronic'])+'\''),\
          ('\''+('' if item['is_support'] == None else item['is_support'])+'\''),\
          ('\''+('' if item['simple_support'] == None else item['simple_support'])+'\''),\
          ('\''+('' if item['pinyin'] == None else item['pinyin'])+'\''),\
          ('\''+('' if item['standbyDosage'] == None else item['standbyDosage'])+'\''),\
          ('\''+('' if item['dosage_limit1'] == None else item['dosage_limit1'])+'\''),\
          ('\''+('' if item['dosage_limit2'] == None else item['dosage_limit2'])+'\''),\
          ('\''+('' if item['dosage_limit3'] == None else item['dosage_limit3'])+'\''),\
          ('\''+('' if item['frequency_limit'] == None else item['frequency_limit'])+'\''),\
          ('\''+('' if item['isReport'] == None else item['isReport'])+'\''),\
          ('\''+('' if item['salesFlag'] == None else item['salesFlag'])+'\''),\
          ('\''+('' if item['common_dosage'] == None else item['common_dosage'])+'\''),\
          ('\''+('' if item['common_dosage_unit'] == None else item['common_dosage_unit'])+'\''),\
          ('\''+('' if item['common_frequency'] == None else item['common_frequency'])+'\''),\
          ('\''+('' if item['common_days'] == None else item['common_days'])+'\''),\
          ('\''+('' if item['filePath'] == None else item['filePath'])+'\'')\
          )
    self.file.write(sql)
    return item

  def close_spider(self,splider):
    print('close sqlPipeline')
    self.file.close()



# import json
# import codecs
# import hashlib
# import scrapy
# from scrapy import FormRequest,Request
# class imagePipeline(object):
#   def __init__(self):
#     print('init imagePipeline')
#     self.title_image_path = 'F:\\git\\drug\\data\\image\\'

#   def process_item(self,item,splider):
#     print 'aaaaaaaaaa*****************************************aaaaaaaaa'
#     if item['filePath'] != None:
#         imageRequest = Request(
#             url=item['titleimgURL'],
#             callback=self.save_title_image
#         )
#         imageRequest.meta['filename'] = item['filePath']
#         yield imageRequest


#   def save_title_image(self,response):
#     print 'save_title_image'
#     filename = response.meta['filename']
#     print 'save title image as ',filename
#     with open(self.title_image_path+filename, 'wb') as f:
#       f.write(response.body)
#     pass
#     yield

#   def close_spider(self,splider):
#     print('close imagePipeline')
