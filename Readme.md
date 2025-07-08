# 📊 AI Job Skills Dashboard

A dynamic Streamlit dashboard that visualizes the **most in-demand skills** extracted from Data Scientist job postings on [Naukri.com](https://www.naukri.com). Built using **Streamlit**, **Selenium**, **Pandas**, and **Altair**, this project includes both **web scraping** and **interactive data visualization**.

---

## 🚀 Features

- 🔍 **Scrapes real job postings** from Naukri using Selenium
- 📈 **Analyzes skills** mentioned across postings
- 🧠 Displays **top 20 in-demand skills**
- 📅 Date range filtering (if available in dataset)
- 📊 Interactive bar & line charts using Altair
- 📋 Full data table viewer
- 📁 Clean modular codebase

---

## 📂 Project Structure

AI-Job-Postings-Dashboard/
├── app.py # (Optional) Alternate entry point for Streamlit
├── requirements.txt
├── .gitignore
├── scraper/
│ ├── dashboard.py # Main Streamlit dashboard
│ ├── extract_skills.py # Extracts and analyzes skills from scraped jobs
│ ├── indeed_scraper.py # Naukri.com scraper using Selenium
│ ├── chrome.exe # Local Chrome driver binary (optional)
│ ├── data/
│ │ ├── jobs.csv # Raw scraped job data
│ │ └── skill_trends.csv # Aggregated skill counts
│ └── naukri_debug.html # Debug file with raw page HTML

yaml
Copy
Edit

---

## 🖥️ How to Run Locally

### 1. 🔧 Install dependencies

```bash
pip install -r requirements.txt
Make sure you have Chrome installed and chrome.exe path set correctly for Selenium.

2. 🧪 Run the scraper (optional)
bash
Copy
Edit
python scraper/indeed_scraper.py
python scraper/extract_skills.py
This will save the cleaned data into scraper/data/.

3. 📊 Launch the dashboard
bash
Copy
Edit
streamlit run scraper/dashboard.py
