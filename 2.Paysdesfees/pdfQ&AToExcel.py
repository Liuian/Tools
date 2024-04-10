import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import pandas as pd
import re

# Define a list of URLs from which to extract Q&A text
urls = [
    'http://paysdesfees.com/pages/clarity',
    'http://paysdesfees.com/pages/picoplus',
    'http://paysdesfees.com/pages/fotona_4d',
    'http://paysdesfees.com/pages/genius',
    'http://paysdesfees.com/pages/oligio',
    'http://paysdesfees.com/pages/ultraformer',
    'http://paysdesfees.com/pages/emsculpt_neo',
    'http://paysdesfees.com/pages/embody',
    'http://paysdesfees.com/pages/belkyra',
    'http://paysdesfees.com/pages/botox_neuronox',
    'http://paysdesfees.com/pages/sculptra',
    'http://paysdesfees.com/pages/ellanse',
    'http://paysdesfees.com/pages/fotona_nightlaser',
    'http://paysdesfees.com/pages/fotona_g',
    'http://paysdesfees.com/pages/fotona',
    'http://paysdesfees.com/pages/blepharoplasty',
    'http://paysdesfees.com/pages/double_eyelid',
    'http://paysdesfees.com/pages/top_surgery',
    'http://paysdesfees.com/pages/gynecomastia',
    'http://paysdesfees.com/pages/fat_transfer',
    'http://paysdesfees.com/pages/private_care',
    'http://paysdesfees.com/pages/liposuction',
]

# Create an empty list to store the data
data = []

# Iterate over each URL
for url in urls:
    print("Extracting from URL:", url)

    # Extract the last segment of the URL
    url_last_segment = urlparse(url).path.split('/')[-1]

    # Send a GET request to fetch the webpage content
    response = requests.get(url)

    # Check if the response status code is 200, indicating success
    if response.status_code == 200:
        # Get the webpage HTML content
        html_content = response.text

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all the questions and answers
        qa_items = soup.find_all('div', class_='panel')

        # Iterate over each Q&A item and extract the question and answer
        for item in qa_items:
            question = item.find('button', class_='panel-button').text.strip()
            answer = item.find('div', class_='panel-body').text.strip()

            # Remove newline characters from the answer, keeping only the first one
            answer = re.sub(r'\s+', '', answer)

            # Append the data to the list
            data.append({'URL': url_last_segment, 'Question': question, 'Answer': answer})

    else:
        print('Request failed, status code:', response.status_code)

# Create a DataFrame from the list of data
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel('qa_results.xlsx', index=False)
print("The results have been saved to qa_results.xlsx")