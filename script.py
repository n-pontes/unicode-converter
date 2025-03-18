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
