import requests  
from bs4 import BeautifulSoup 

def convert_text_to_unicode(input_text):  
    url = "https://lsgkerala.gov.in/unicode/Default.aspx"  
    session = requests.Session()  
    response = session.get(url)  

if response.status_code == 200:  
    soup = BeautifulSoup(response.text, "html.parser")  
    viewstate = soup.find("input", {"name": "__VIEWSTATE"})["value"]  
    eventvalidation = soup.find("input", {"name": "__EVENTVALIDATION"})["value"]  

data = {  
    "__VIEWSTATE": viewstate,  
    "__EVENTVALIDATION": eventvalidation,  
    "txtMLTTRevathy": input_text,  
    "btnConvert": "-- Convert --"  
}  

post_response = session.post(url, data=data)  

if post_response.status_code == 200:  
    soup = BeautifulSoup(post_response.text, "html.parser")  
    unicode_text = soup.find("textarea", {"name": "txtUnicode"}).text  
    return unicode_text.strip()  
else:  
    return "Error: Could not submit the form successfully."  

input_text = input("Enter text to convert from FML Ravathi to Unicode Malayalam: ")  
converted_text = convert_text_to_unicode(input_text)  
print("Converted Unicode Malayalam Output:")  
print(converted_text)  



