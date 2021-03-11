import os
import re
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#for windows file .exe
# CHROME_EXECUTABLE_PATH = os.getenv('CHROM_DRIVER_FILE', "./chromedriver.exe")
# print(CHROME_EXECUTABLE_PATH)
WEB_BASE_HREF = 'https://citybus.taichung.gov.tw'

HOME_PAGE_URI = 'https://citybus.taichung.gov.tw/ebus'


SELENIUM_REMOTE = os.getenv('SELENIUM_REMOTE', "http://localhost:4444/wd/hub")
uriNotHttpRegEx = '^(?!http(s)?).*'

web_is_not_found_regex = '404'
# URI = 'https://www.cwb.gov.tw/V8/C/'

def get_page_source_by_chrome(uri):
  chrome_options = Options()
  # chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-gpu')
  chrome_options.add_argument('--disable-dev-shm-usage')

  driver = webdriver.Remote(
    command_executor=SELENIUM_REMOTE,
    desired_capabilities=DesiredCapabilities.CHROME
  )
  driver.get(uri)
  # wait for quering datas
  # time.sleep(2)
  page_res = driver.page_source
  return page_res

def getHrefFromLink(link):
  href = link.get('href')
  return href

def getLinksAllHrefs(links):
  linkHrefs = map(getHrefFromLink, links)
  linkHrefsList = list(linkHrefs)
  return linkHrefsList

def checkHrefIsShortLink(link):
  matchedRes = re.search(uriNotHttpRegEx, link)
  if(matchedRes is None):
    return False
  else:
    return True

def crawlWeb(uri):
  page_res = get_page_source_by_chrome(uri)
  quriedHTML = BeautifulSoup(page_res, 'html.parser')
  return quriedHTML

def getAllHrefShortLinks(uri): 
    quriedHTML = crawlWeb(uri)
    links = quriedHTML.find_all('a')

    linkHrefsList = getLinksAllHrefs(links)
    filteredHrefs = filter(checkHrefIsShortLink, linkHrefsList)
    filteredHrefsList = list(filteredHrefs)

    # print(linkHrefs)
    # print(linkHrefsList)
    # print(filteredHrefsList)
    return filteredHrefsList

    
    # print("quriedHTML: ", quriedHTML.prettify())
    # print("Queried links: ", links)

def checkPageIs404(uri):
  quried = crawlWeb(uri)
  quriedText = quried.getText()
  pageIsNot404 = re.search(web_is_not_found_regex, quriedText)
  # print(quriedText)
  # print(pageIsNot404)
  return pageIsNot404
  # page_content = quried.

def findAllHrefPagesInHomePageWhichIs404():
  links = getAllHrefShortLinks(HOME_PAGE_URI)
  page404Links = []

  for link in links:
    uri = WEB_BASE_HREF + link
    is404 = checkPageIs404(uri)
    print('Checking: ', uri)
    if(is404):
      page404Links.append(link)

  if(len(page404Links) > 0):
    print('404 Page links: ', page404Links)
  else:
    print('All links are fine!')
  return page404Links

# getAllHrefShortLinks(HOME_PAGE_URI)
# checkPageIs404(HOME_PAGE_URI)
def main():
  findAllHrefPagesInHomePageWhichIs404()

if __name__ == "__main__":
    main()