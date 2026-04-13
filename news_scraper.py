import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

topic = input("Enter news topic (example: AI, Cricket, Bollywood, Politics): ")

print()

topic = topic.lower()

url = f"https://news.google.com/rss/search?q={topic}&hl=en-IN&gl=IN&ceid=IN:en"

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

soup = BeautifulSoup(response.text, "xml")
print("Source: Google News RSS Feed")
print()

items = soup.find_all("item")

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
    writer.writerow(["No", "Headline", "Link", "Fetched Time"])

unique_headlines = set()
count = 1

try:
    limit = int(input("How many headlines to fetch? "))
except ValueError:
    print("Please enter a valid number.")
    exit()
print()

existing_headlines = set()

if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as read_file:
        for line in read_file:
            existing_headlines.add(line.strip().split(". ", 1)[-1])

for item in items[:limit]:
    text = item.title.text.strip()
    link = item.link.text.strip()
    fetched_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    if text != "" and text not in unique_headlines:
        print(f"{count}. {text}")
        print("   Link:", link)

        if text not in existing_headlines:
            formatted_headline = f"{count}. {text}"
            file.write(formatted_headline + "\n")
            writer.writerow([count, text, link, fetched_time])
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