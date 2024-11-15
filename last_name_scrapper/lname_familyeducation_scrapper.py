import requests
from bs4 import BeautifulSoup


def fetch_last_names(url):
    response = requests.get(url)
    last_names = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        name_lists = soup.find_all('ul', class_='baby-names-list')
        for name_list in name_lists:
            last_names.extend([name.get_text().strip() for name in name_list.find_all('li')])
        if last_names[0] == 'No results found.':
            return []
    return last_names


def start():
    base_url = "https://www.familyeducation.com/baby-names/surname/"
    letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]

    with open('last_names.txt', 'w') as file:
        for letter in letters:
            page = 0
            while True:
                if page == 0:
                    url = f"{base_url}{letter}"
                else:
                    url = f"{base_url}{letter}?page={page}"

                names = fetch_last_names(url)
                if not names:  # If no names are found, break the loop and move to next letter
                    print(f"No names found on {url}. Moving to next letter.")
                    break

                for name in names:
                    file.write(f"{name}\n")  # Write each name in a new line

                print(f"Found {len(names)} names on {url}")
                page += 1


start()