from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


options = Options()
path = 'E:\pyhon_demo\chromedriver_win32\chromedriver.exe'
options.add_argument('headless')
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# print(time_now)

def submit():
    browser = webdriver.Chrome(executable_path=path, options=options)
    browser.maximize_window()
    browser.get('http://xgbd.cqust.edu.cn:866/')
    browser.implicitly_wait(30)
    time.sleep(2)
    browser.find_element_by_id("username").send_keys('你的学号')
    browser.find_element_by_id("password").send_keys('你的密码')
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="casLoginForm"]/p[5]/button').click()
    time.sleep(2)
    browser.get('http://xgbd.cqust.edu.cn:866/txxm/rsbulid/r_3_3_st_jkdatb.aspx?xq=2019-2020-2&nd=2017&msie=1')
    browser.implicitly_wait(30)
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="div0"]/table/tbody/tr[2]/td/img').click()
    time.sleep(2)
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="xsqr"]').click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="databc"]').click()
    time.sleep(2)
    dig_alert = browser.switch_to.alert
    result =dig_alert.text
    dig_alert.accept()
    # print(browser.page_source)
    browser.quit()

    # print(result)
    with open('E:\pyhon_demo\chromedriver_win32\奥兰日志.txt', 'a+') as f:
        f.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '已执行'+result+'\n')
    return result

def run():
    try:
        r_result = submit()
        time.sleep(2)
        print(r_result)
        return r_result
    except:
        print("超时连接，重新启动")
        submit()


if __name__ == '__main__':
    while True:
        time_now = time.strftime("%H:%M:%S",time.localtime())
        if time_now > "12:00:00":
            # print("开始了......")
            r_result = run()
            if r_result is not '请核实填报内容无误后勾选学生确认保存失败!':
                # print("填写结束了")
                break
            else:
                run()
        else:
            print("还没到指定时间.....")

            # with open('E:\pyhon_demo\chromedriver_win32\还未执行.txt', 'w') as f:
            #     f.write("还没到指定时间.....")
            time.sleep(1800)
            continue




