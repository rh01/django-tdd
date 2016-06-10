# -*- coding:utf8 -*-
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys



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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        # 应用邀请他输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        # 他在一个文本框中输入了"Buy fish"
        inputbox.send_keys(Keys.ENTER)



        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
                any(row.text == '1: By fish' for row in rows)
        )

        
        # 他按下Enter键之后，页面更新了
        # 待办事项表格中显示了"1: Buy fish"
        
        # 页面有显示了一个文本框，可以输入其他的待办事项
        # 他输入了"Use Peacock feather to make a fly"
        
        # 页面再次鞥新，他的清单中线是了这两个待办事项
        
        # 小明想知道这个网站是否会记得他的清单


        # 他看到网站为他生成了一个唯一的URL
        # 而且页面中有一些文字解说这个功能

        self.fail("Finish the test")


        # 他访问那个URL，发现他的待办事项列表还在

if __name__ == '__main__':
    unittest.main(warnings='ignore')
