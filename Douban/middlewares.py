# -*- coding:utf-8 -*-

from scrapy.http import FormRequest,Request
from PIL import Image
from StringIO import StringIO
import httplib2

class DoubanCaptchaMiddleware(object):
    '''
    由于请求是并发的，因此会导致返回多个验证码的问题。
    验证码的数量与并发数正相关
    '''
    error_403_count = 0
    
    def is_allow_post(self,spider):
        concurrent_requests = spider.settings.getint('CONCURRENT_REQUESTS')
        return self.error_403_count % concurrent_requests*2 == 0
    
    def process_response(self,request,response,spider):
        if response.status == 403:
            self.error_403_count += 1
            image_url = response.xpath('//img[@alt="captcha"]/@src').extract_first()
            captcha_value = response.xpath('//input[@name="captcha-id"]/@value').extract_first()
            original_url = response.xpath('//input[@name="original-url"]/@value').extract_first()

            if self.is_allow_post(spider):
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
            else:
                return Request(original_url)
            
        return response


