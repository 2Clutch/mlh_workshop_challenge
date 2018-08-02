import time
from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

app = Flask(__name__)

browser = webdriver.Chrome()
base_url = u'https://twitter.com/search?f='
query = u'tweets&vertical=default&q=mlh%20hackathon'
url = base_url + query

browser.get(url)
time.sleep(1)

body = browser.find_element_by_tag_name('body')

for _ in range(10):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)

tweets = browser.find_elements_by_class_name('tweet-text')


@app.route("/")
def index():
    for tweet in tweets:
        print(tweet.text)


if __name__ == "__main__":
    app.run()

