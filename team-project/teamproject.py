import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://coronaboard.kr/'

driver = webdriver.Chrome('C:/Users/82102/Desktop/first_git_project/team-project/chromedriver.exe')
driver.get(url) # url 불러오기
driver.implicitly_wait(3) # 3초 기다리기

data = driver.page_source # 페이지 소스 가져오기

soup = BeautifulSoup(data, 'html.parser')


print(soup.select('#country-table > div > div > table'))
df = pd.read_html(soup.prettify())[0]

print(type(df))

print(df)

driver.quit()




a=input()
for i in range(75):
    if a in df.iloc[i,1]:
        nation=i
        break
list=[]
c=''
for i in range(2,5):
    b=df.iloc[nation,i].split()[0]
    c+=' '+b
c=c.replace(',','').split()
c = [int(i) for i in c]

print(c)


font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)
x = np.arange(3)
d=['확진자','사망자','완치']
plt.bar(x, c)
plt.xticks(x, d)
plt.show()

