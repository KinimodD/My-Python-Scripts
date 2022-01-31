# Import required modules
from lxml import html
import requests
  
# Request the page
page = requests.get('https://tryhardguides.com/wordle-answers/')
  
# Parsing the page
# (We need to use page.content rather than 
# page.text because html.fromstring implicitly
# expects bytes as input.)
tree = html.fromstring(page.content)  
  
# Get element using XPath
answer = tree.xpath('//*[@id="post-51348"]/div[2]/ul/li[1]/strong/text()')
print("Todays wordle answer is",answer[0])
