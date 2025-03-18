# Malayalam to Unicode Converter

A Python script to convert Malayalam text from FML Revathi format to Unicode using the Kerala Government's Unicode Converter website.

## Features

- Fetches the Malayalam Unicode Converter webpage using HTTP GET request.
- Extracts hidden form data (__VIEWSTATE and __EVENTVALIDATION) for form submission.
- Submits the Malayalam text and retrieves the converted Unicode text using HTTP POST request.
- Outputs the converted Unicode text in the terminal.

## Setup

1. Clone the Repository

- Open terminal and run:

```bash
git clone https://github.com/your-username/toUnicodeConverter.git  
cd toUnicodeConverter  
```

2. Create and Activate Virtual Environment

- Create a virtual environment:
```bash
python3 -m venv venv  
```
3. Activate it:

- Linux/macOS:
```bash
source venv/bin/activate  
```
Windows:
```bash
.\venv\Scripts\activate  
```

4. Install Dependencies
- Use the requirements.txt file to install dependencies:
```bash
pip install -r requirements.txt  
```

### Usage

Run the script:
```bash
python converter.py  
```

Enter the text in FML Revathi format when prompted. The script will output the converted Unicode text in the terminal.

Enter text to convert from FML Ravathi to Unicode Malayalam: നമസ്കാരം  
Converted Unicode Malayalam Output: നമസ്കാരം  

Dependencies
requests – For handling HTTP GET and POST requests
beautifulsoup4 – For parsing and extracting data from HTML

🚨 Troubleshooting
If you get a ModuleNotFoundError, ensure the virtual environment is activated and dependencies are installed using pip install -r requirements.txt.
If the conversion fails, check your internet connection or try rerunning the script.

📄 License
This project is licensed under the MIT License.