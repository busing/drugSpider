# coding: utf-8
import scrapy
from scrapy import FormRequest,Request
from scrapy.spidermiddlewares.httperror import HttpError
import sys
import os
import json
import codecs


class DrugImageSpider(scrapy.Spider):
  name = "drugImage"
  allowed_domains=["manager.youdeyi.com","image.youdeyi.com"]
  json_file = 'F:\\git\\drug\\data\\data_utf8.json'
  start_urls = []
  title_image_path = 'F:\\git\\drug\\data\\image\\'

  def start_requests(self):
    print 'start_requests '
    fo = codecs.open(self.json_file,'r','utf-8')
    for line in fo.readlines():
      try:
        json_data = json.loads(line)
        if json_data['titleimgURL'] == '':
          continue
        if os.path.exists(self.title_image_path+json_data['filePath']):
          continue
        imageRequest = Request(
            url=json_data['titleimgURL'],
            callback=self.save_title_image
        )
        imageRequest.meta['filename'] = json_data['filePath']
        yield imageRequest
      except BaseException as e:
        print 'exception'
        continue

  def save_title_image(self,response):
    print 'save_title_image'
    filename = response.meta['filename']
    print 'save title image as ',filename
    with open(self.title_image_path+filename, 'wb') as f:
      f.write(response.body)
    pass



