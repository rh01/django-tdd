# -*- coding:utf8 -*-
from selenium import webdriver
import unittest


class NewVisionTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()


    def test_can_start_a_list_and_retrieve_it_later(self):
        # 小明听说有一个很酷的在线待办事件应用
        # 他去看了一下这个网站的首页
        self.browser.get('http://localhost:8000')
        
        # 他注意到网页的标题和头部都包含"TO-DO"这个词
        self.assertIn("To-Do" ,self.browser.title)
        self.fail("Finish the test")

        
        # 他在一个文本框中输入了"Buy fish"
        
        # 他按下Enter键之后，页面更新了
        # 待办事项表格中显示了"1: Buy fish"
        
        # 页面有显示了一个文本框，可以输入其他的待办事项
        # 他输入了"Use Peacock feather to make a fly"
        
        # 页面再次鞥新，他的清单中线是了这两个待办事项
        
        # 小明想知道这个网站是否会记得他的清单


        # 他看到网站为他生成了一个唯一的URL
        # 而且页面中有一些文字解说这个功能



        # 他访问那个URL，发现他的待办事项列表还在

if __name__ == '__main__':
    unittest.main(warnings='ignore')
