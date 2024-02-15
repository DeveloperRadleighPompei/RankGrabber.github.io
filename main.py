import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()
chrome_options.add_argument("--headless")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

url = 'https://fortnitetracker.com/profile/all/2024%20rxlin'
while True:
    time.sleep(60)
    # Start the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)

    # Load the page in the Chrome driver
    driver.get(url)

    # Wait for the page to load
    driver.implicitly_wait(10)

    # Get the page source
    response = driver.page_source

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(response, 'html.parser')
    rank_element = soup.select_one("#overview > div.trn-grid.trn-grid__sidebar-right > aside > div.trn-grid.trn-grid--vertical > div.profile-current-ranks.trn-card.trn-card--no-overflow > div > div:nth-child(1) > div.profile-rank__container > div > div.profile-rank__value")
    rank = rank_element.text.strip() if rank_element else "N/A"
    rank_progress_element = soup.select_one("#overview > div.trn-grid.trn-grid__sidebar-right > aside > div.trn-grid.trn-grid--vertical > div.profile-current-ranks.trn-card.trn-card--no-overflow > div > div:nth-child(1) > div.profile-rank__container > div > div.profile-rank-progress")
    rank_progress = rank_progress_element.text.strip() if rank_element else "N/A"
    # Extract the data you want here, for example:
    rank_data_full = f"{rank} {rank_progress}"
    # Save the output to a file called output.txt
    if rank == "Bronze 1":
        rank_image_number = "1"
    elif rank == "Bronze 2":
        rank_image_number = "2"
    elif rank == "Bronze 3":
        rank_image_number = "3"
    elif rank == "Silver 1":
        rank_image_number = "4"
    elif rank == "Silver 2":
        rank_image_number = "5"
    elif rank == "Silver 3":
        rank_image_number = "6"
    elif rank == "Gold 1":
        rank_image_number = "7"
    elif rank == "Gold 2":
        rank_image_number = "8"
    elif rank == "Gold 3":
        rank_image_number = "9"
    elif rank == "Platnium 1":
        rank_image_number = "10"
    elif rank == "Platnium 2":
        rank_image_number = "11"
    elif rank == "Platnium 3":
        rank_image_number = "12"
    elif rank == "Diamond 1":
        rank_image_number = "13"
    elif rank == "Diamond 2":
        rank_image_number = "14"
    elif rank == "Diamond 3":
        rank_image_number = "15"
    elif rank == "Elite":
        rank_image_number = "16"
    elif rank == "Champion":
        rank_image_number = "17"
    elif rank == "Unreal":
        rank_image_number = "18"

    rank_image_link=f"https://trackercdn.com/cdn/fortnitetracker.com/icons/ranks/{rank_image_number}.png"   
    with open('output.txt', 'w') as f:
        f.write(soup.prettify())
    with open("rank.txt", "w") as f:
        f.write(rank)
        f.write("\n")
        f.write(rank_progress)
        f.write("\n")
        f.write(rank_image_number)
        f.write("\n")
        f.write(rank_image_link)

    # Close the Chrome driver
    driver.quit()
