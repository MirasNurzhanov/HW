import requests
from bs4 import BeautifulSoup

url = "https://www.olx.kz/list/q-елки"

for page_num in range(1, 4):
    page_url = f"{url}/?page={page_num}"
    response = requests.get(page_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')  
        all_trees = soup.find_all("h6", class_="css-16v5mdi er34gjf0")

        for tree in all_trees:
            description = tree.find("div", class_="css-1t507yq er34gjf0") 

            if description:
                description_text = description.get_text(strip=True)
                print(description_text)
            else:
                print(f"Ошибка при получении страницы {page_url}: {response.status_code}")
    else:
        print(f"Ошибка при получении страницы {page_url}: {response.status_code}")
