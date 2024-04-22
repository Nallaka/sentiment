import time

from serpapi import search
import json

nashvile_queries = ["nashville opioid abuse", "nashville opioid overdose", "nashville opiod deaths"]

for query in nashvile_queries:
    params = {
        "engine": "google_news",
        "q": query,
        "api_key": "42b0d9e716ea8d286b73e1a0628e3bde3ef019f62296a5500da8544edf964c55"
    }

    searchresults = search(params)
    nashville_results = searchresults.as_dict()
    nashville_news_results = nashville_results["news_results"]

    print(nashville_news_results)
    print(len(nashville_news_results))

    with open('news_data/nashville_news_links.json', 'a') as file:
        json_data = json.dumps(nashville_news_results)

        file.write(json_data + '\n')

    time.sleep(5)