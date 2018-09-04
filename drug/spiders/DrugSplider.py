# coding: utf-8
import scrapy
from scrapy import FormRequest,Request
from scrapy.spidermiddlewares.httperror import HttpError
import sys
sys.path.append("/spiders")
from drug.items import *
import os
import re
import sys  
reload(sys)  
import json
import hashlib
sys.setdefaultencoding('utf8')   


class DrugSpider(scrapy.Spider):
  name = "drug"
  allowed_domains=["manager.youdeyi.com","image.youdeyi.com"]
  start_urls="http://manager.youdeyi.com/index.php/Westerndrug/getDrugListByValue?hospitalCode=00001683&value=&pharmacyCode=&age=0&code="
  # drug_count = 3410
  drug_count = 3410
  prefix = '000000'

  def start_requests(self):
    self.md5 = hashlib.md5()
    for index in range(1,self.drug_count+1):
      drug_id = str(index)
      prefix_length = len(self.prefix)-len(drug_id)
      drug_id = self.prefix[0:prefix_length]+drug_id
      url = self.start_urls+drug_id
      print '======================request url============================='
      print url
      print '======================request url end============================='
      yield scrapy.Request(url=url,callback=self.parse)
 

  def errback(self,failure):
    print 'fuckerr back'
    print failure.value
    print 'err back'


  def parse(self,response):
    print 'success back'
    json_data = json.loads(response.text)
    json_drug = json_data['list'][0]
    if json_drug == None:
        return
    drug_item = DrugItem()
    drug_item['code'] = json_drug['code']
    drug_item['codename'] = json_drug['codename']
    drug_item['namecn'] = json_drug['namecn']
    drug_item['nameen'] = json_drug['nameen']
    drug_item['aliascn'] = json_drug['aliascn']
    drug_item['dosage'] = json_drug['dosage']
    drug_item['categoryChild'] = json_drug['categoryChild']
    drug_item['dosageUnit'] = json_drug['dosageUnit']
    drug_item['packingNum'] = json_drug['packingNum']
    drug_item['leastUnit'] = json_drug['leastUnit']
    drug_item['buyUnit'] = json_drug['buyUnit']
    drug_item['specification'] = json_drug['specification']
    drug_item['newotc'] = json_drug['newotc']
    drug_item['formula'] = json_drug['formula']
    drug_item['composition'] = json_drug['composition']
    drug_item['drugattribute'] = json_drug['drugattribute']
    drug_item['gongneng'] = json_drug['gongneng']
    drug_item['yongfa'] = json_drug['yongfa']
    drug_item['adr'] = json_drug['adr']
    drug_item['contraindication'] = json_drug['contraindication']
    drug_item['note'] = json_drug['note']
    drug_item['pregnantwomentaboo'] = json_drug['pregnantwomentaboo']
    drug_item['childrentaboo'] = json_drug['childrentaboo']
    drug_item['elderlytaboo'] = json_drug['elderlytaboo']
    drug_item['interaction'] = json_drug['interaction']
    drug_item['pharmacology'] = json_drug['pharmacology']
    drug_item['storage'] = json_drug['storage']
    drug_item['shelflife'] = json_drug['shelflife']
    drug_item['refdrugcompanyname'] = json_drug['refdrugcompanyname']
    drug_item['refcorpaddress'] = json_drug['refcorpaddress']
    drug_item['titleimgURL'] = json_drug['titleimgURL']
    drug_item['commonUse'] = json_drug['commonUse']
    drug_item['is_chronic'] = json_drug['is_chronic']
    drug_item['is_support'] = json_drug['is_support']
    drug_item['simple_support'] = json_drug['simple_support']
    drug_item['pinyin'] = json_drug['pinyin']
    drug_item['standbyDosage'] = json_drug['standbyDosage']
    drug_item['dosage_limit1'] = json_drug['dosage_limit1']
    drug_item['dosage_limit2'] = json_drug['dosage_limit2']
    drug_item['dosage_limit3'] = json_drug['dosage_limit3']
    drug_item['frequency_limit'] = json_drug['frequency_limit']
    drug_item['isReport'] = json_drug['isReport']
    drug_item['salesFlag'] = json_drug['salesFlag']
    drug_item['common_dosage'] = json_drug['common_dosage']
    drug_item['common_dosage_unit'] = json_drug['common_dosage_unit']
    drug_item['common_frequency'] = json_drug['common_frequency']
    drug_item['common_days'] = json_drug['common_days']
    if drug_item['titleimgURL'] != None:
        self.md5.update((drug_item['code']+'_'+drug_item['codename']).encode("utf-8"))
        filename = self.md5.hexdigest()
        pos = drug_item['titleimgURL'].rfind('.')
        suffix = drug_item['titleimgURL'][pos:]
        drug_item['filePath'] = filename+suffix
        pass
    return drug_item

