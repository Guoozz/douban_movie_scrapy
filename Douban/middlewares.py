# -*- coding:utf-8 -*-

from scrapy.http import FormRequest
from PIL import Image
from StringIO import StringIO
import httplib2

class DoubanCaptchaMiddleware(object):
    
    def process_response(self,request,response,spider):
        if response.status == 403:
            image_url = response.xpath('//img[@alt="captcha"]/@src').extract_first()
            captcha_value = response.xpath('//input[@name="captcha-id"]/@value').extract_first()
            original_url = response.xpath('//input[@name="original-url"]/@value').extract_first()
            
            h = httplib2.Http('.cache')
            response2,image = h.request(image_url,headers=spider.settings.getdict('DEFAULT_REQUEST_HEADERS'))
            assert image is not None,'can not download picture'
            
            im = Image.open(StringIO(image))
            im.show()
            
            captcha = raw_input(u'请输入验证码\n'.encode('utf-8'))

            return FormRequest('http://www.douban.com/misc/sorry',formdata={'captcha-solution':captcha,
                                                                            'captcha-id':captcha_value,
                                                                            'original-url':original_url,}
                               ,callback=None)
        return response

