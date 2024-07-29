from bs4 import BeautifulSoup
import requests

# Save the content of a webpage to a file
def save_webpage_content(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"Page content saved to file {filename}")
    else:
        print(f"Failed to load page. Status code: {response.status_code}")

# Save the content of the page to a .html-file in a folder
save_webpage_content('https://example.com', 'example.html')

# Function to parse the content of a webpage
def parse_webpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find and print the page title
        title = soup.title
        if title is not None:
            print(f"Page title: {title.string}")
        else:
            print("The <title> tag was not found on the page.")
        
        # Find and print all links of the page
        links = soup.find_all('a')
        if links:
            print("Links on the page:")
            for link in links:
                href = link.get('href')
                if href is not None:
                    print(f"Link: {href}")
                else:
                    print("Link without href attribute.")
        else:
            print("No <a> tags found on the page.")
        
        # Find and print all paragraphs
        paragraphs = soup.find_all('p')
        if paragraphs:
            print("Paragraphs on the page:")
            for p in paragraphs:
                text = p.get_text()
                if text:
                    print(text)
                else:
                    print("Paragraph is empty.")
        else:
            print("No <p> tags found on the page.")
    else:
        print(f"Failed to load page. Status code: {response.status_code}")

# Testing the parsing function
parse_webpage('https://example.com')

# To use this code I write "python BeautifulSoup.py" in debug console (Windows).
# Code activation in the console may be different on other operating systems.
# Console response with default code settings:

'''
Page content saved to file example.html
Page title: Example Domain
Links on the page:
Link: https://www.iana.org/domains/example
Paragraphs on the page:
This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.
More information...
'''