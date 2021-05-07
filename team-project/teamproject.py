from urllib.request import urlopen
from bs4 import BeautifulSoup


html=urlopen("https://kosis.kr/statHtml/statHtml.do?orgId=127&tblId=DT_120019N_2016_001&vw_cd=&list_id=&scrId=&seqNo=&lang_mode=ko&obj_var_id=&itm_id=&conn_path=E1&docId=0313756944&markType=S&itmNm=%EC%A0%84%EA%B5%AD")
soup=BeautifulSoup(html, "lxml")

statistics_table = soup.find_all('table', {"id":"maintable"})


