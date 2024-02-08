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
        # ID = 'kinhyeonjin@naver.com'
        ID = 'destroyer_4@naver.com'
        PW = 'vmfkdlajfl4!'

        # 로그인 페이지로 이동
        # login_page = 'https://nid.naver.com/oauth2.0/authorize?svctype=0&response_type=code&client_id=C9hwybENgOtF&state=W37LXQI34N2UV3SA27GOOCNGDBCILHLC3ECDKSI7N2FDHBUVMJOHS4YYFLGRTDYA7JENYLO7PAQLQ===&redirect_url=https%3A%2F%2Fauth.band.us%2Fexternal_account_login%3Ftype%3Dnaver'
        login_page = 'https://band.us/home'
        driver.get(login_page)
        print('Navigated to login page.')
        driver.save_screenshot('process_screenshot.png')

        login_selector = '#container > div > div.sloganArea > div > div._signupRegion > div > div > div.buttonBox > a.button._loginBtn'

        login_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, login_selector)))

        login_btn.click()
        print('process 0')
        driver.save_screenshot('process_screenshot.png')

        time.sleep(1)

        naver_login_selector = '#login_list > li:nth-child(3) > a > span'

        naver_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, naver_login_selector)))

        naver_btn.click()
        print('process 1')
        driver.save_screenshot('process_screenshot.png')

        time.sleep(1)

        # # 패스워드 입력
        pass_selector = '#pw'
        password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, pass_selector)))

        # # ID 입력 필드에 값을 설정
        driver.execute_script(f"document.getElementById('id').value = '{ID}';")

        # # 비밀번호 입력 필드에 값을 설정
        driver.execute_script(f"document.getElementById('pw').value = '{PW}';")

        # # Enter 키를 눌러 로그인 시도
        password_input.send_keys(Keys.RETURN)
        print('process 2')
        driver.save_screenshot('process_screenshot.png')

        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.btn_cancel")))
            element.click()
        except:
            print("기기등록 '등록안함' 버튼이 없노!")
        
        time.sleep(10)

        # 로그인 성공 확인을 위한 요소 대기
        # login_success_selector = '#content > section > div.homeMyBandList.gMat20.gPab35._myBandListWrap > div > ul > li:nth-child(2)'
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, login_success_selector)))

        print('로그인 성공')
        driver.save_screenshot('success_screenshot.png')

        # 캘린더 페이지로 이동
        # driver.get('https://band.us/band/77309128/calendar')
        # print('Navigated to calendar page.')

    except Exception as e:
        print(f'An error occurred: {e}')
        print(repr(e))
        driver.save_screenshot('error_screenshot.png')
    finally:
        # Include screenshots in the GitHub Actions workflow logs
        with open('process_screenshot.png', 'rb') as file:
            print('##[group]Process Screenshot')
            print('![Process Screenshot](data:image/png;base64,' + base64.b64encode(file.read()).decode('utf-8') + ')')
            print('##[endgroup]')

        with open('success_screenshot.png', 'rb') as file:
            print('##[group]Success Screenshot')
            print('![Success Screenshot](data:image/png;base64,' + base64.b64encode(file.read()).decode('utf-8') + ')')
            print('##[endgroup]')

        with open('error_screenshot.png', 'rb') as file:
            print('##[group]Error Screenshot')
            print('![Error Screenshot](data:image/png;base64,' + base64.b64encode(file.read()).decode('utf-8') + ')')
            print('##[endgroup]')
        driver.quit()

if __name__ == "__main__":
    band_scrapping()
