from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--usename", "-u", help="学号")
parser.add_argument("--password", '-p', help="密码")
parser.add_argument("--liyou", '-l', help="出校理由", default='吃饭')
parser.add_argument("--xingcheng", '-x', help="出校行程", default='北大东门-五道口-北大东门')
arge = parser.parse_args()
user_name = arge.usename
password = arge.password
liyou = arge.liyou
xingcheng = arge.xingcheng
print(user_name)
print(liyou)
print(xingcheng)
n = 1
#user_name = '1801111502'
#password = 'chen677296'
#liyou = '吃饭'
#xingcheng = '北大东门-五道口-北大东门'
while (n > 0):
    url = 'https://iaaa.pku.edu.cn/iaaa/oauth.jsp?appID=portal2017&appName=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6%E6%A0%A1%E5%86%85%E4%BF%A1%E6%81%AF%E9%97%A8%E6%88%B7%E6%96%B0%E7%89%88&redirectUrl=https://portal.pku.edu.cn/portal2017/ssoLogin.do'
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    driver = webdriver.Chrome(chrome_options=option)
    #driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="user_name"]').send_keys(user_name)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(Keys.ENTER)
    time.sleep(1)
    #driver.find_element_by_class_name('a-btn').click()
    time.sleep(30)
    #driver.find_element_by_xpath(
    #    '//*[@id="ng-app"]/div[1]/header/section/section[1]/section[2]/ul[1]/li/a').click()
    #time.sleep(1)
    #driver.find_element_by_xpath('//*[@id="user_name"]').send_keys(user_name)
    #time.sleep(1)
    #driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    #time.sleep(1)
    #driver.find_element_by_xpath('//*[@id="password"]').send_keys(Keys.ENTER)
    #time.sleep(5)
    ActionChains(driver).move_by_offset(200, 100).click().perform()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="stuCampusExEnReq"]').click()
    windows = driver.current_window_handle
    all_handles = driver.window_handles
    for handle in all_handles:
        if handle != windows:
            driver.switch_to.window(handle)
    time.sleep(10)
    driver.find_elements_by_class_name(
        'el-card.box-card.card_marge.is-always-shadow')[0].click()
    time.sleep(1)
    #driver.find_elements_by_class_name('router-mg')[0].click() 
    #time.sleep(1)
    driver.find_elements_by_class_name(
        'el-input__suffix-inner')[0].click() 
    time.sleep(1)
    driver.find_elements_by_class_name(
        'el-select-dropdown__item')[5].click()  
    time.sleep(1)
    driver.find_elements_by_class_name(
        'el-textarea__inner')[0].send_keys(liyou)
    time.sleep(1)
    driver.find_elements_by_class_name(
        'el-textarea__inner')[1].send_keys(xingcheng)
    time.sleep(1)
    driver.find_element_by_class_name('el-checkbox').click()
    time.sleep(1)
    driver.find_element_by_class_name('el-icon-check').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '/html/body/div[4]/div/div[3]/button[2]').click()
    time.sleep(1)
    driver.find_element_by_class_name('el-page-header__title').click()
    time.sleep(1)
    driver.find_elements_by_class_name('router-mg')[0].click()  # 进入备案界面
    time.sleep(1)
    driver.find_elements_by_class_name(
        'el-input__suffix-inner')[0].click()  # 出入校菜单
    time.sleep(1)
    driver.find_elements_by_class_name(
        'el-select-dropdown__item')[6].click()  # 出校
    time.sleep(1)
    driver.find_elements_by_class_name(
        'el-textarea__inner')[0].send_keys(liyou)
    time.sleep(1)
    driver.find_elements_by_class_name(
        'el-input__suffix-inner')[3].click()  # 出入校菜单
    time.sleep(1)
    driver.find_elements_by_class_name('el-select-dropdown__item')[15].click()
    time.sleep(1)
    driver.find_elements_by_class_name(
        'el-textarea__inner')[1].send_keys('燕园街道')
    time.sleep(1)
    driver.find_elements_by_class_name('el-radio__input')[0].click()
    time.sleep(1)
    driver.find_element_by_class_name('el-checkbox').click()
    time.sleep(1)
    driver.find_element_by_class_name('el-icon-check').click()
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/button[2]').click()
    time.sleep(1)
    driver.quit()
    print(user_name)
    print(liyou)
    print(xingcheng)
    print('已备案: '+str(n)+' 天')
    n = n+1
    time.sleep(86400)