

from bs4 import BeautifulSoup

soup = BeautifulSoup("<b></b>")
tag = soup.b
tag.append("Hello")
new_string = soup.new_string(" there")
tag.append(new_string)

new_comment = soup.new_string("Nice to see you.")
tag.append(new_comment)
print tag 

