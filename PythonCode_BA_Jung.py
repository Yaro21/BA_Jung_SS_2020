#!/usr/bin/env python
# coding: utf-8

# In[4]:


from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

userdata = {
  "username": "USERNAME",
  "password": "PASSWORD",
}

queries = {
    'query1': "Klimaschutz",
    'query2': "Klimaerwärmung",
    'query3': "Klimawandel",
    'query4': "Klimaschutzpolitik",
    'query5': "CO2",
    'query6': "Klimaveränderung",
    'query7': "Treibhauseffekt",
    'query8': "Erderwärmung",
    'query9': "Klimakonferenz",
}


options = Options()
ua = UserAgent()
userAgent = ua.Chrome
options.add_argument(f'user-agent={userAgent}')
driver = webdriver.Chrome(options=options, executable_path=r'C:\Program Files\Webdriver\chromedriver.exe')

#in Google Account einloggen
driver.get("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(userdata["username"])
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
sleep(10)
driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(userdata["password"])
driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
sleep(60)

#Auf Google Search wechseln, Suche nach Query1
driver.get('https://google.com')
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(queries["query1"])
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]').submit()
#Suchvorschläge abspeichern, Sprache Deutsch
driver.get('https://clients1.google.com/complete/search?client=firefox&q=Klimaschutz&hl=de')

sleep(3)

#Suche nach Query2
driver.get('https://google.com')
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(queries["query2"])
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]').submit()
#Suchvorschläge abspeichern
driver.get('https://clients1.google.com/complete/search?client=firefox&q=Klimaerwärmung&hl=de')

#Suche nach Query3
driver.get('https://google.com')
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(queries["query3"])
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]').submit()
#Suchvorschläge abspeichern
driver.get('https://clients1.google.com/complete/search?client=firefox&q=Klimawandel&hl=de')

sleep(3)

#Suche nach Query4
driver.get('https://google.com')
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(queries["query4"])
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]').submit()
#Suchvorschläge abspeichern
driver.get('https://clients1.google.com/complete/search?client=firefox&q=Klimaschutzpolitik&hl=de')

#Suche nach Query5
driver.get('https://google.com')
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(queries["query5"])
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]').submit()
#Suchvorschläge abspeichern
driver.get('https://clients1.google.com/complete/search?client=firefox&q=CO2l&hl=de')

sleep(3)

#Suche nach Query6
driver.get('https://google.com')
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(queries["query6"])
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]').submit()
#Suchvorschläge abspeichern
driver.get('https://clients1.google.com/complete/search?client=firefox&q=Klimaveränderung&hl=de')

#Suche nach Query7
driver.get('https://google.com')
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(queries["query7"])
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]').submit()
#Suchvorschläge abspeichern
driver.get('https://clients1.google.com/complete/search?client=firefox&q=Treibhauseffekt&hl=de')

sleep(3)

#Suche nach Query8
driver.get('https://google.com')
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(queries["query8"])
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]').submit()
#Suchvorschläge abspeichern
driver.get('https://clients1.google.com/complete/search?client=firefox&q=Erderwärmung&hl=de')


#Suche nach Query9
driver.get('https://google.com')
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(queries["query9"])
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]').submit()
#Suchvorschläge abspeichern
driver.get('https://clients1.google.com/complete/search?client=firefox&q=Klimakonferenz&hl=de')

sleep(3)

driver.quit()


# In[ ]:





# In[ ]:




