# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DrugItem(scrapy.Item):
    # define the fields for your item here like:
    code = scrapy.Field()
    codename = scrapy.Field()
    namecn = scrapy.Field()
    nameen = scrapy.Field()
    aliascn = scrapy.Field()
    dosage = scrapy.Field()
    categoryChild = scrapy.Field()
    dosageUnit = scrapy.Field()
    packingNum = scrapy.Field()
    leastUnit = scrapy.Field()
    buyUnit = scrapy.Field()
    specification = scrapy.Field()
    newotc = scrapy.Field()
    formula = scrapy.Field()
    composition = scrapy.Field()
    drugattribute = scrapy.Field()
    gongneng = scrapy.Field()
    yongfa = scrapy.Field()
    adr = scrapy.Field()
    contraindication = scrapy.Field()
    note = scrapy.Field()
    pregnantwomentaboo = scrapy.Field()
    childrentaboo = scrapy.Field()
    elderlytaboo = scrapy.Field()
    interaction = scrapy.Field()
    pharmacology = scrapy.Field()
    storage = scrapy.Field()
    shelflife = scrapy.Field()
    refdrugcompanyname = scrapy.Field()
    refcorpaddress = scrapy.Field()
    titleimgURL = scrapy.Field()
    commonUse = scrapy.Field()
    is_chronic = scrapy.Field()
    is_support = scrapy.Field()
    simple_support = scrapy.Field()
    pinyin = scrapy.Field()
    standbyDosage = scrapy.Field()
    dosage_limit1 = scrapy.Field()
    dosage_limit2 = scrapy.Field()
    dosage_limit3 = scrapy.Field()
    frequency_limit = scrapy.Field()
    isReport = scrapy.Field()
    salesFlag = scrapy.Field()
    common_dosage = scrapy.Field()
    common_dosage_unit = scrapy.Field()
    common_frequency = scrapy.Field()
    common_days = scrapy.Field()
    filePath = scrapy.Field()
    pass
