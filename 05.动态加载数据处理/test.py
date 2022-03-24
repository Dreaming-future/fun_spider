import requests
from selenium import webdriver
from lxml import etree
import time
from selenium.webdriver.chrome.options import Options
 
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')
chrome_options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
# driver = webdriver.Chrome(executable_path='./chromedriver')
path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'

driver = webdriver.Chrome(options = chrome_options)

driver.get('https://passport.csdn.net/login?code=mobile')

time.sleep(2)

#在web 应用中经常会遇到frame 嵌套页面的应用，使用WebDriver 每次只能在一个页面上识别元素，对于frame 嵌套内的页面上的元素，直接定位是定位是定位不到的。这个时候就需要通过switch_to_frame()方法将当前定位的主体切换了frame 里。

driver.find_element_by_id('tabOne').click()
# driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('all').clear()
driver.find_element_by_id('all').send_keys('13790699906')  #这里填写你的QQ号
driver.find_element_by_id('password-number').clear()
driver.find_element_by_id('password-number').send_keys('a13790699906')  #这里填写你的QQ密码
driver.find_element_by_css_selector("[class='btn btn-primary']").click()


# driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# time.sleep(2)
# page_text = driver.page_source
# tree = etree.HTML(page_text)
# #执行解析操作
# li_list = tree.xpath('//ul[@id="feed_friend_list"]/li')
# for li in li_list:
#     text_list = li.xpath('.//div[@class="f-info"]//text()|.//div[@class="f-info qz_info_cut"]//text()')
#     text = ''.join(text_list)
#     print(text+'\n\n\n')
# driver.close()
