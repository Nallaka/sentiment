import json

with open('news_data/nashville_news_links.json', 'r') as file:
    data = json.load(file)

# Extract the "link" field from each entry
links = [entry['link'] for entry in data]

# Remove duplicates
unique_links = list(set(links))

for link in unique_links:
    print(link)
