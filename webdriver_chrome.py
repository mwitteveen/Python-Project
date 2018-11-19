#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 18:34:17 2018

@author: martijnwitteveen
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time



class websession:
    
    def __init__(self,path):
        #options = webdriver.ChromeOptions()
        #options.add_argument('headless') , chrome_options=options
        self.driver =webdriver.Chrome(executable_path=path)

    def GotoURL(self,url,id_new):
        self.driver.get(url)
        status = False
        tries =1
        while not(status):
            if tries != 20:
                try:
                    element = self.driver.find_element_by_id(id_new)
                    self.driver.get(url)
                    status = True
                except:
                    time.sleep(0.5)
                    tries+=1
                    pass
            else:
                print("Error in driver class")
                break
            
           
    def input_text(self,xpath,text):
        status = False
        tries = 1
        while not(status):
            if tries != 20:
                try:
                    element = self.driver.find_element_by_xpath(xpath)
                    element.send_keys(text)
                    status = True
                except:
                    time.sleep(0.5)
                    tries+=1
                    pass
            else:
                print("Error in driver class")
                break
            
    def push_btn(self,xpath,id_new):
        status = False
        tries = 1
        while not(status):
            if tries != 20:
                try:
                    btn = self.driver.find_element_by_xpath(xpath)
                    btn.click()
                    status = True
                    element = self.driver.find_element_by_id(id_new)
                except:
                    time.sleep(0.5)
                    tries+=1
                    pass
            else:
                print("Error in driver class")
                break
    
    def close(self):
        while self.driver.page_source != "":
            try:
                self.driver.close()
            except:
                pass
                
    
start = time.time()
path="/Users/martijnwitteveen/Desktop/Automator/chromedriver"

web = websession(path)
web.GotoURL("https://google.com", "tophf")
web.input_text("//input[@name='q']","test")

web.push_btn("//input[@value='Google zoeken']","sbfbl")
#aaaa

web.driver.save_screenshot('screen.png') # save a screenshot to disk

web.close()

eind = time.time()

print (eind-start)