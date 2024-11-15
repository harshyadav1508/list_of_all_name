import requests
from bs4 import BeautifulSoup


def fetch_english_names(base_url, total_pages=91):
    names = []
    for page in range(2, total_pages + 1):
        url = f"{base_url}{page}"  # Construct the URL by appending the page number
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to retrieve data from {url}")
            continue  # Skip this page if there's an error loading it

        soup = BeautifulSoup(response.text, 'html.parser')
        name_elements = soup.find_all('span', class_='listname')

        for element in name_elements:
            name_link = element.find('a', class_='nll')
            if name_link and name_link.get_text().strip().isalpha():
                names.append(name_link.get_text().strip())
        print(f"Page {page} done")
    return names


def save_names_to_file(names, file_path):
    with open(file_path, 'w') as file:
        for name in names:
            file.write(name + '\n')

        # Base URL to a page with English names (replace this with the actual URL of the name list)


base_url = "https://www.behindthename.com/names/"  # Adjust the base URL as necessary
english_names = fetch_english_names(base_url)

# Save the names to a text file
file_path = 'english_names.txt'
save_names_to_file(english_names, file_path)

print(f"Names have been saved to {file_path}")