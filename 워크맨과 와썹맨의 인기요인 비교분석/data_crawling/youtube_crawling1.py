##cmd창 열기
#Scripts 경로 아래에 설치
#python -m pip install --upgrade pip
#pip install requests
#pip install bs4
#urllib 이미 설치되어 있는 경우 대부분
#pip install selenium
## Anaconda를 사용하고 있으면 반드시 Anaconda Prompt에서 설치해야 한다

##python 열기
# 필요한 모듈 import
import requests
from bs4 import BeautifulSoup
import time
import urllib.request
from selenium.webdriver import Chrome
import re
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import datetime as dt

# url 불러오기 위한 사전작업 실행
delay = 3
##chromedriver다운로드 후 파일 경로 입력
browser = Chrome('C:\\Users\\Rstudio\\Anaconda3\\Scripts\\chromedriver.exe')
browser.implicitly_wait(delay)
# Youtube url 접속
start_url = 'https://www.youtube.com'
browser.get(start_url)
browser.maximize_window()
#Youtube 접속 후 개발자도구(F12)실행
#ctrl+shift+c / 좌측 상단 화살표 클릭
##검색창 영역 클릭
browser.find_elements_by_xpath('//*[@id="search-form"]/div/div/div/div[2]/input')[0].click()
##검색어 입력
browser.find_elements_by_xpath('//*[@id="search-form"]/div/div/div/div[2]/input')[0].send_keys('탈북민')
##Enter
browser.find_elements_by_xpath('//*[@id="search-form"]/div/div/div/div[2]/input')[0].send_keys(Keys.RETURN)
##selenium으로 source추출 (너무 오래 걸림)
## 스크롤하기 위해 소스 추출
#body = browser.find_element_by_tag_name('body')
num_of_pagedowns = 20
while num_of_pagedowns:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
    num_of_pagedowns -= 1
#BeautifulSoup으로 page source추출
htm10 = browser.page_source
html = BeautifulSoup(htm10,'html.parser')
video_list0 = html.find('div',{'id':'content'})
video_list = video_list0.find_all('ytd-video-renderer', {'class':'style-scope ytd-item-section-renderer'})
#url데이터 추출
base_url = 'https://www.youtube.com'
talbookmin_url = []
for i in range(len(video_list)):
    url = base_url+video_list[i].find('a',{'id':'video-title'})['href']
    talbookmin_url.append(url)
#댓글수집
start_url = talbookmin_url[0]
browser.get(start_url)
body = browser.find_element_by_tag_name('body')
##인기순/작성순 선택할 수 있는 영역 클릭
browser.find_element_by_xpath('//paper-button[@class="dropdown-trigger style-scope yt-dropdown-menu"]').click()
##인기순 카테고리 클릭
browser.find_element_by_xpath('//paper-listbox[@class="dropdown-content style-scope yt-dropdown-menu"]/a[1]').click()
#스크롤링
num_page_down = 20
while num_page_down:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1.5)
    num_page_down -= 1
comment_list0 = html.find('div',{'id':'content'})
comment_list = comment_list0.find_all('ytd-comment-thread-renderer',{'class':'style-scope ytd-item-section-renderer'})
for i in range(len(video_list)):
    url = base_url+video_list[i].find('yt-formatted-string',{'id':'content-text'})['text']
    talbookmin_url.append(url)