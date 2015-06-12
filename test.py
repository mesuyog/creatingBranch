import requests
import re
import hashlib
from bs4 import BeautifulSoup
import webbrowser
    
def getFileNameHash(filename):
    """hash of the filename is used in the form field in the upload"""
    return hashlib.md5(filename).hexdigest()

username = 'mesuyog'
password = 'gentlepornxs123'
 
filename = 'bikram2.mp4'
files = {'files[]': (filename, open(filename, 'rb'))}

s = requests.session()
login_url = "http://pornxs.com/ajax.php?action=create_login_view"
front_page = s.get(login_url)

soup = BeautifulSoup(front_page.text)
token = soup.find("input",{'type': '\\"hidden\\"'}).attrs["value"].replace('\\"', '').replace('\\/', "")


login_payload = {"token":token,'username': username, "password":password } 

response = s.post("http://pornxs.com/ajax.php?action=check_login",data=login_payload)
 
login_payload = {"token":token, 'username':username, "password":password, "login12": "Login"} 
response = s.post("http://pornxs.com/",data=login_payload)
 
user_page = s.get("http://pornxs.com/homepage.php")


upload_url = "http://encoding.pornxs.com/uploader_test.php"

soup = BeautifulSoup(user_page.text)
select = soup.find_all('input')
upload_token = select[1]["value"]
uid = select[2]["value"]

upload_token = soup.find("input",{'name': "token"}).attrs["value"]
uid = soup.find("input",{'id': "uid"}).attrs["value"]'''

print uid