
from requests import get
from pprint import pprint

endpoint = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=8a46d51ed4764a71bda82b9a11222ab2'
response = get(endpoint)
data = response.json()
# pprint(data)

def create(source_id, source_name, author, title, description, url, publishedAt, content):
    new_article = {
        "source": {"id": source_id, "name": source_name},
        "author": author,
        "title": title,
        "description": description,
        "url": url,
        "publishedAt": publishedAt,
        "content": content
    }
    print("New article created:", new_article)
    return new_article

def get_article_by_author(author):
    found = False
    for article in data["articles"]:
        if article.get("author") and article["author"] == author:
            pprint(article)
            found = True
    if not found:
        return "Article not found"

def update_article_by_author(data, article_author):
    for article in data["articles"]:
        if article.get("author") == article_author:
            new_url = input("Enter new URL: ")
            article["url"] = new_url
            print("Article updated:", article)
            return article
    print(f"No article found by author: {article_author}")
    return None

def delete_article_by_author(data, article_author):
    data["articles"] = [article for article in data["articles"] if article["author"] != article_author]
    pprint(data)
    return data

while True:
    question = input("Enter a process name (create, read, update, delete): ").strip().lower()

    match question:
        case "create":
            source_id = input("Enter source id: ")
            source_name = input("Enter source name: ")
            author = input("Enter author: ")
            title = input("Enter title: ")
            description = input("Enter description: ")
            url = input("Enter url: ")
            publishedAt = input("Enter publishedAt: ")
            content = input("Enter content: ")
            print(create(source_id, source_name, author, title, description, url, publishedAt, content))

        case "read":
            author_name = input("Enter author name: ")
            print(get_article_by_author(author_name))

        case "update":
            article_author=input("Enter author name: ")
            print(update_article_by_author(data, article_author))

        case "delete":
            article_author = input("Enter article author to delete: ")
            data = delete_article_by_author(data, article_author)

        case _:
            print("Invalid process name. Please enter 'create', 'read', 'update', or 'delete'.")