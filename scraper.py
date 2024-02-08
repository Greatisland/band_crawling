import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from firebase_admin import db
import datetime
import pyperclip

# Selenium 설정
chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]

for option in options:
    chrome_options.add_argument(option)

chrome_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

def band_scrapping():
    try:
        # 로그인 정보
        ID = 'kinhyeonjin@naver.com'
        PW = 'vmfkdlajfl4!'

        # 로그인 페이지로 이동
        login_page = 'https://nid.naver.com/oauth2.0/authorize?svctype=0&response_type=code&client_id=C9hwybENgOtF&state=W37LXQI34N2UV3SA27GOOCNGDBCILHLC3ECDKSI7N2FDHBUVMJOHS4YYFLGRTDYA7JENYLO7PAQLQ===&redirect_url=https%3A%2F%2Fauth.band.us%2Fexternal_account_login%3Ftype%3Dnaver'
        driver.get(login_page)
        print('Navigated to login page.')



        # 패스워드 입력
        pass_selector = '#pw'
        password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, pass_selector)))

        # ID 입력 필드에 값을 설정
        # driver.execute_script("document.getElementById('id').value = '{ID}';")
        driver.execute_script(f"document.getElementById('id').value = '{ID}';")

        # 비밀번호 입력 필드에 값을 설정
        # driver.execute_script("document.getElementById('pw').value = '{PW}';")
        driver.execute_script(f"document.getElementById('pw').value = '{PW}';")

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
