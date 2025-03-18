import requests  
from bs4 import BeautifulSoup 

def convert_text_to_unicode(input_text):  
    url = "https://lsgkerala.gov.in/unicode/Default.aspx"  
    session = requests.Session()  
    response = session.get(url)  
