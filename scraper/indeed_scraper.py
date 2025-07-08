from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time
import os

options = Options()
# options.add_argument("--headless")  # Uncomment this if you want headless scraping
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

query = "data scientist"
location = "remote"
url = f"https://www.naukri.com/{query.replace(' ', '-')}-jobs-in-{location}"
driver.get(url)
time.sleep(5)

# ✅ Updated selector
job_cards = driver.find_elements(By.CSS_SELECTOR, "div.cust-job-tuple")

print(f"🔍 Found {len(job_cards)} job cards.")

jobs = []

for card in job_cards:
    try:
        title = card.find_element(By.CSS_SELECTOR, "a.title").text
    except:
        title = None

    try:
        company = card.find_element(By.CSS_SELECTOR, "a.comp-name").text
    except:
        company = None

    try:
        experience = card.find_element(By.CSS_SELECTOR, "span.expwdth").text
    except:
        experience = None

    try:
        location = card.find_element(By.CSS_SELECTOR, "span.locWdth").text
    except:
        location = None

    try:
        description = card.find_element(By.CSS_SELECTOR, "span.job-desc").text
    except:
        description = None

    try:
        skills = ", ".join([li.text for li in card.find_elements(By.CSS_SELECTOR, "ul.tags-gt li")])
    except:
        skills = None

    jobs.append({
        "Title": title,
        "Company": company,
        "Experience": experience,
        "Location": location,
        "Description": description,
        "Skills": skills
    })

# ✅ Save to CSV
os.makedirs("data", exist_ok=True)
df = pd.DataFrame(jobs)
df.to_csv("data/jobs.csv", index=False)

print("✅ Scraping done. Saved to data/jobs.csv")

driver.quit()
