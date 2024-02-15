from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

app = Flask(__name__)

@app.route('/')
def index():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    url = 'https://fortnitetracker.com/profile/all/2024%20rxlin'

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

    # Close the Chrome driver
    driver.quit()

    return render_template('index.html', rank=rank, rank_progress=rank_progress)

if __name__ == '__main__':
    app.run(debug=True)
