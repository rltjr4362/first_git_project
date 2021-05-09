import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://coronaboard.kr'

driver = webdriver.Chrome('C:/Users/82102/Desktop/first_git_project/team-project/chromedriver.exe')
driver.get(url) # url 불러오기
driver.implicitly_wait(3) # 3초 기다리기

data = driver.page_source # 페이지 소스 가져오기

soup = BeautifulSoup(data, 'html.parser')


driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button').click()
driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button').click()

print(soup.select('#country-table > div > div > table'))
df = pd.read_html(soup.prettify())[0]

print(type(df))

print(df)

driver.quit()



