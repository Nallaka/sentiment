import newspaper
from newspaper import Article

cnn_paper = newspaper.build('http://cnn.com')

for article in cnn_paper.articles:
    print(article.url)

print(cnn_paper.size())

first_article = cnn_paper.articles[0]

first_article.download()

first_article.parse()

print(first_article.title)

print(first_article.text)

print(first_article.authors)

url = "https://www.tennessean.com/story/news/crime/2023/12/20/two-charged-year-long-probe-nashville-toddler-ariel-rose-death/71991923007/"

article = Article(url)

article.download()

article.parse()

print(article.title)

print(article.text)

print(article.authors)

print(article.publish_date)
