# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core.utils import ChromeType
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service

# chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

# chrome_options = Options()
# options = [
#     "--headless",
#     "--disable-gpu",
#     "--window-size=1920,1200",
#     "--ignore-certificate-errors",
#     "--disable-extensions",
#     "--no-sandbox",
#     "--disable-dev-shm-usage"
# ]
# for option in options:
#     chrome_options.add_argument(option)

# driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# driver.get('http://nytimes.com')
# print(driver.title)

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from firebase_admin import db
import datetime
import pyperclip

# Selenium 설정
options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
# options.headless = False  # 브라우저 숨김 여부
driver = webdriver.Chrome(options=options)

def band_scrapping():
    try:
        # 로그인 정보
        ID = 'kinhyeonjin@naver.com'
        PW = 'vmfkdlajfl4!'

        # 로그인 페이지로 이동
        login_page = 'https://auth.band.us/email_login?keep_login=false'
        login_page = 'https://nid.naver.com/oauth2.0/authorize?svctype=0&response_type=code&client_id=C9hwybENgOtF&state=W37LXQI34N2UV3SA27GOOCNGDBCILHLC3ECDKSI7N2FDHBUVMJOHS4YYFLGRTDYA7JENYLO7PAQLQ===&redirect_url=https%3A%2F%2Fauth.band.us%2Fexternal_account_login%3Ftype%3Dnaver'
        driver.get(login_page)
        print('Navigated to login page.')

        # 이메일 입력
        # email_selector = '#input_email'
        email_selector = '#id'
        pyperclip.copy(ID)
        email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, email_selector)))
        email_input.send_keys(Keys.CONTROL, 'v')
        # email_input.send_keys(ID)

        # Enter 키를 눌러 다음 필드로 진행
        # email_input.send_keys(Keys.RETURN)

        # 패스워드 입력
        pass_selector = '#pw'
        pyperclip.copy(PW)
        password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, pass_selector)))
        password_input.send_keys(Keys.CONTROL, 'v')
        # password_input.send_keys(PW)

        # Enter 키를 눌러 로그인 시도
        password_input.send_keys(Keys.RETURN)

        # 로그인 성공 확인을 위한 요소 대기
        login_success_selector = '#content > section > div.homeMyBandList.gMat20.gPab35._myBandListWrap > div > ul > li:nth-child(2)'
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, login_success_selector)))

        print('로그인 성공')

        # 캘린더 페이지로 이동
        driver.get('https://band.us/band/77309128/calendar')
        print('Navigated to calendar page.')

    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        driver.quit()

if __name__ == "__main__":
    band_scrapping()
