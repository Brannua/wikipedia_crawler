"""
Pseudo code:

    current_url = # random_url_of_a_wikipedia_page
    target_url = "https://en.wikipedia.org/wiki/Philosophy"
    article_chain = []

    页面标题不是哲学，并且我们尚未发现循环：

        下载页面内容 => 在内容中查找第一个连接

        将页面添加到 article_chain

        current_link = 该链接

        Slow things down so as to not hammer Wikipedia's servers
"""

import time

import bs4
import requests

import urllib

current_url = "https://en.wikipedia.org/wiki/Bird" # random_url_of_a_wikipedia_page
target_url = "https://en.wikipedia.org/wiki/Philosophy"
article_chain = [current_url]

def continue_crawl(target_url, search_history, max_steps=25):
    if len(search_history) > max_steps:
        print("Too much searching. Terminating...")
        return False
    elif search_history[-1] == target_url:
        print("Find the target URL. Terminating...")
        return False
    elif target_url in search_history[:-1]:
        print("Find a loop. Terminating...")
        return False
    else:
        return True

def find_first_link(url):
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, "html.parser")

    article_link = None
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")

    # Find all the direct children of content_div that are paragraphs
    for element in content_div.find_all("p", recursive=False):
        # Find the first anchor tag that's a direct child of a paragraph.
        # It's important to only look at direct children, because other types
        # of link, e.g. footnotes and pronunciation, could come before the
        # first link to an article. Those other link types aren't direct
        # children though, they're in divs of various classes.
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break

    if not article_link:
        return

    # Build a full url from the relative article_link url
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)
    return first_link

def web_crawl():
    while continue_crawl(target_url, article_chain):

        # 下载页面内容 => 在内容中查找第一个连接
        first_link = find_first_link(article_chain[-1])

        # 将页面添加到 article_chain
        article_chain.append(first_link)

        # current_link = 该链接
        current_url = first_link

        print(current_url)

        # Slow things down so as to not hammer Wikipedia's servers
        time.sleep(2)

web_crawl()

