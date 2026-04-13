# 📰 News Headlines Scraper (Python Project)

## 📌 Project Description
This project is a Python-based News Headlines Scraper that fetches the latest news headlines from Times of India RSS feeds based on user-selected topics such as Sports, Business, Technology, AI, Bollywood, Politics, and Cricket.

The scraper extracts headlines and saves them into both TXT and CSV files automatically.

This project demonstrates practical usage of:
- Python
- Web scraping
- RSS feed parsing
- File handling
- CSV handling
- Error handling
- User input processing

---

## 🚀 Features

✅ Fetch latest news headlines  
✅ Topic-based headline filtering  
✅ Supports multiple categories  
✅ Saves headlines into TXT file  
✅ Saves headlines into CSV file  
✅ Avoids duplicate headlines  
✅ Automatically creates output folder  
✅ Timestamp-based file naming  

---

## 🛠 Technologies Used

- Python
- Requests Library
- BeautifulSoup Library
- CSV Module
- OS Module
- Datetime Module

---

## 📂 Project Structure
news_scraper.py
README.md
output/
sports_news_YYYY-MM-DD.txt
sports_news_YYYY-MM-DD.csv

---

## ▶️ How To Run The Project

Step 1:

Install required libraries
pip install requests beautifulsoup4

Step 2:

Run the script
python news_scraper.py

Step 3:

Enter topic example:
sports
business
technology
ai
cricket
bollywood
politics

Step 4:

Enter number of headlines

Example:
3

Output files will be saved inside the **output folder**

---

## 📊 Example Output

Example headlines:
1.IPL 2026 match updates
2.India squad announcement
3.Rohit Sharma interview

Saved as:
output/sports_news_YYYY-MM-DD.txt
output/sports_news_YYYY-MM-DD.csv

---

## 🎯 Learning Outcome

This project helped in understanding:

- Web scraping using Python
- Working with RSS feeds
- Handling structured data
- File handling automation
- CSV file creation
- Real-world data extraction workflow

---

## 👩‍💻 Author

Akanksha Jadhav  
MCA Student