import time

from serpapi import search
import json

nashvile_queries = ["nashville opioid abuse", "nashville opioid overdose", "nashville opiod deaths"]

places = [nashvile_queries]

for place in places:
    for query in place:
        params = {
            "engine": "google_news",
            "q": query,
            "api_key": "42b0d9e716ea8d286b73e1a0628e3bde3ef019f62296a5500da8544edf964c55"
        }

        searchresults = search(params)
        results_dict = searchresults.as_dict()
        news_results = results_dict["news_results"]

        print(news_results)
        print(len(news_results))

        with open('/content/news_data/nashville_news_links.json', 'a') as file:
            json_data = json.dumps(news_results)

            file.write(json_data + '\n')

        time.sleep(2)