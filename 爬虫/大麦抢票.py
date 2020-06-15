from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

URL = "https://piao.damai.cn/146290.html?spm=a2o6e.search.0.0.7e2b4d157EDtjL"

HOUR = 19
MIN  = 0
USERNAME = "1730933627"

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)
driver.get(URL)


def choose(seletor):
    try:
        # 控件可点击时才选定
        choice = wait.until(EC.element_to_be_clickable((By.XPATH, seletor)))
        return choice
    except TimeoutException as e:
        print("Time out!")
        return None
    except Exception:
        print("Not found!")
        return None

def login():
    login = choose('//*[@id="userLoginInfo"]/span/a[1]')
    login.click()
    username = choose('//*[@id="login_email"]')
    username.send_keys(USERNAME)
    """
    由于密码框控件被设置为不可见
    先自行输入密码并记住密码
    方便刷新
    （也可用cookie实现）
    """
    password = choose('//*[@id="login_pwd_txt"]')
    try:
        password.click()
        password.send_keys("wh20010210")
    except Exception:
        print(password)
        print("密码不能click")

def buy():
    # 点击价格
    try:
        price = None
        plus = None
        buybtn = None
        submit = None
        booker = None
        select = None
        confirm = None
        driver.get(URL)
        # 选择价格
        while None == price:
            # 这里选的是580票面的，如果选其他票面，修改最后的li[*]即可
            price = choose('//*[@id="priceList"]/div/ul/li[3]')
        price.click()
        # 数量加1
        while None == plus:
            plus = choose('//*[@id="cartList"]/div[1]/ul/li/span[3]/a[2]')
        plus.click()
        # 立即抢购
        while None == buybtn:
            buybtn = choose('//*[@id="btnBuyNow"]')
        driver.execute_script("arguments[0].scrollIntoView();", buybtn) 
        buybtn.click()
        # 选择购票人
        while None == booker:
            booker = choose('/html/body/div[3]/div[3]/div[2]/div[2]/div/a')
        driver.execute_script("arguments[0].scrollIntoView();", booker) 
        booker.click()
        # 选择、确定
        while None == select:
            select = choose('/html/body/div[3]/div[3]/div[12]/div/div[2]/div/div[2]/div/table/tbody/tr/label/td[1]/input')
        driver.execute_script("arguments[0].scrollIntoView();", select) 
        select.click()
        while None == confirm:
            confirm = choose('/html/body/div[3]/div[3]/div[12]/div/div[2]/div/p/div/a')
        driver.execute_script("arguments[0].scrollIntoView();", confirm) 
        confirm.click()
        # 提交订单
        while None == submit:
            submit = choose('//*[@id="orderConfirmSubmit"]')
        driver.execute_script("arguments[0].scrollIntoView();", submit) 
        submit.click()
    except Exception:
        print("抢票失败，尝试重新抢票")
        buy()

def test():
    login()
    time.sleep(20)
    print("开始抢票")
    buy()
    print("抢票成功")

def main():
    login()
    time.sleep(20)
    while 1:
        if MIN == time.localtime().tm_min:
            print("开始抢票")
            buy()
            print("抢票成功")

if __name__ == '__main__':
    test()
    test_mobile()
    main()
