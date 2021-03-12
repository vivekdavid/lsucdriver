import requests

from requests import Request, Session 

import bs4
from bs4 import BeautifulSoup 

import selenium
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import traceback 


s = requests.session()


driver_path = 'path to driver'
driver= webdriver.Firefox(executable_path=driver_path)
patience_time=60

driver.implicitly_wait(3) 

url_1 =("https://www2.lsuc.on.ca/LawyerParalegalDirectory/loadSearchPage.do")
driver.get(url_1)


crim =driver.find_element_by_xpath("//input[@name='pa[8].PA' and @value='on']").click()

city = driver.find_element_by_id("chooseCity")
city.send_keys("Toronto")

driver.find_element_by_xpath("//input[@value='Submit']").click()

# first page of results  

url_= driver.current_url
page=s.get(url_, timeout=None)

soup = BeautifulSoup(page.content, 'html.parser')

content_tag_1 = soup.select('a', class_='content') 

r_data_1 = [names.get_text() for names in content_tag_1] 
        
lis_1 = r_data_1

driver.find_element_by_link_text("Next Results").click()


# function to remove duplicate names and words  

def del_dupe(x,y):
    x2=x.copy()
    y2=y.copy()
    for v in x[:]:
        if v in y:
            x.remove(v)
            y.remove(v)

    return x, y

# for deleting duplicates after the first set of results  
    
url_n = driver.current_url
page_n = s.get(url_n,timeout=None)

soup_n = BeautifulSoup(page_n.content, 'html.parser')

content_tag = soup_n.select('a', class_='content')

r_data= [names_n.get_text() for names_n in content_tag]

lis = r_data
lis_2 = del_dupe(lis_1,lis)
        


                 

        
