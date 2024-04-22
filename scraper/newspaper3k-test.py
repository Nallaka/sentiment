import newspaper
from newspaper import Article

url = "https://www.tennessean.com/story/news/crime/2023/12/20/two-charged-year-long-probe-nashville-toddler-ariel-rose-death/71991923007/"

article = Article(url)

article.download()

article.parse()

print(article.title)

print(article.text)

print(article.authors)

print(article.publish_date)


# List of article links
article_links = [
    "https://www.tennessean.com/story/news/crime/2023/12/20/two-charged-year-long-probe-nashville-toddler-ariel-rose-death/71991923007",
    "https://www.newschannel5.com/news/researchers-define-4th-wave-of-the-overdose-crisis-due-to-fentanyl-increase",
    "https://www.axios.com/local/nashville/2022/08/01/opioid-fight-new-laws-tennessee"
]

def fetch_article_content(link):
    article = Article(link)
    article.download()
    article.parse()
    return article

def generate_newspaper(article_links):
    newspaper_content = ""
    for link in article_links:
        article = fetch_article_content(link)
        newspaper_content += f"Title: {article.title}\n"
        newspaper_content += f"Authors: {', '.join(article.authors)}\n" if article.authors else ""
        newspaper_content += f"Publication Date: {article.publish_date}\n" if article.publish_date else ""
        newspaper_content += f"Text: {article.text}\n\n"
    return newspaper_content


# Generate and print the newspaper
newspaper_content = generate_newspaper(article_links)
print(newspaper_content)