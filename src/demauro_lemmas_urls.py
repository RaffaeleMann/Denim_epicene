import requests
from bs4 import BeautifulSoup
import string

base_url = "https://dizionario.internazionale.it/lettera/"

# List to store the words
words = []

# List to store the URLs
urls = []

# Iterate over each letter of the alphabet
for letter in string.ascii_lowercase:
    page_number = 0
    
    while True:
        # URL for the current letter and page number
        url = base_url + letter + "-" + str(page_number)
        print(url)
        
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find all the word elements on the page
        word_elements = soup.find_all("li", class_="li_elements_result_lemma")
        
        # If no word elements are found, break the loop and move to the next letter
        if len(word_elements) == 0:
            break
        
        # Extract the text and URL of each word element and append them to the respective lists
        for element in word_elements:
            word_text = element.get_text().strip()
            print(word_text)
            word_url = element.find("a")["href"]
            print(word_url)
            words.append(word_text)
            urls.append(word_url)
        
        # Increment the page number for the next iteration
        page_number += 1
