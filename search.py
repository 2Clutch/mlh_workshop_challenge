import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
base_url = u'https://twitter.com/search?q='
query = u'pascivite&f=live'
url = base_url + query

browser.get(url)
time.sleep(1)

body = browser.find_element_by_tag_name('body')

for _ in range(10):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)

tweets = browser.find_elements_by_css_selector('[data-testid="tweet"]')

for tweet in tweets:
    print(tweet.text)
