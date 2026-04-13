import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

topic = input("Enter news topic (example: AI, Cricket, Bollywood, Politics): ")

print()

topic = topic.lower()

category_urls = {
    "sports": "https://timesofindia.indiatimes.com/rssfeeds/4719148.cms",
    "cricket": "https://timesofindia.indiatimes.com/rssfeeds/54829575.cms",
    "business": "https://timesofindia.indiatimes.com/rssfeeds/1898055.cms",
    "technology": "https://timesofindia.indiatimes.com/rssfeeds/66949542.cms",
    "ai": "https://timesofindia.indiatimes.com/rssfeeds/66949542.cms",
    "bollywood": "https://timesofindia.indiatimes.com/rssfeeds/1081479906.cms",
    "politics": "https://timesofindia.indiatimes.com/rssfeeds/296589292.cms"
}

url = category_urls.get(topic)

if url is None:
    print("Topic not available. Showing general headlines instead.\n")
    url = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"

print(f"Fetching latest '{topic}' news headlines...\n")
folder_name = "output"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)
try:
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    print("Website accessed successfully!\n")

except requests.exceptions.RequestException as error:
    print("Error accessing website:", error)
    exit()

soup = BeautifulSoup(response.text, "html.parser")
print("Website Title:", soup.title.text)
print()

headlines = soup.find_all("title")

safe_topic = topic.replace(" ", "_")

filename = folder_name + "/" + safe_topic + "_news_" + str(datetime.now().date()) + ".txt"
file = open(filename, "a", encoding="utf-8")

csv_filename = folder_name + "/" + safe_topic + "_news_" + str(datetime.now().date()) + ".csv"
csv_file = open(csv_filename, "a", newline="", encoding="utf-8")
writer = csv.writer(csv_file)

if os.stat(filename).st_size ==0:
    file.write("Top News Headlines\n")
    file.write("Fetched on: " + str(datetime.now()) + "\n\n")

if os.stat(csv_filename).st_size ==0:
    writer.writerow(["Top News Headlines"])
    writer.writerow(["Fetched on: ", str(datetime.now())])
    writer.writerow([])

unique_headlines = set()
count = 1

limit = int(input("How many headlines to fetch? "))
print()

existing_headlines = set()

if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as read_file:
        for line in read_file:
            existing_headlines.add(line.strip().split(". ", 1)[-1])

for headline in headlines[1:limit+1]:
    text = headline.text.strip()

    if topic not in category_urls:
        if topic not in text.lower():
            continue

    if text != "" and text not in unique_headlines:
        print(f"{count}. {text}")

        if text not in existing_headlines:
            formatted_headline = f"{count}. {text}"
            file.write(formatted_headline + "\n")
            writer.writerow([count, text])
            existing_headlines.add(text)

        unique_headlines.add(text)
        count +=1
        
print("\nTotal headlines saved:", count - 1)
file.close()

csv_file.close()
def main():
    pass

print("\nHeadlines saved successfully.")
print("Files saved inside 'output' folder.")
print("TXT file:", filename)
print("CSV file:", csv_filename)

if __name__ == "__main__":
    main()