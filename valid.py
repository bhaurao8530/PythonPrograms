import re
import requests

def extract_emails(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            emails = re.findall(email_pattern, content)
            return emails
        else:
            print(f"Error: Unable to fetch the webpage. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    webpage_url = input("Enter the URL of the webpage: ")
    extracted_emails = extract_emails(webpage_url)
    if extracted_emails:
        print("Extracted emails:")
        for email in extracted_emails:
            print(email)
    else:
        print("No emails found on the webpage.")