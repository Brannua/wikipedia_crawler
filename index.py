"""
Pseudo code:

    current_link = random_link_of_a_wikipedia_page
    article_chain = []

    页面标题不是哲学，并且我们尚未发现循环：

        将页面添加到 article_chain

        下载页面内容 => 在内容中查找第一个连接

        current_link = 该链接

        暂停片刻
"""

# current_url = # random_url_of_a_wikipedia_page
target_url = "https://en.wikipedia.org/wiki/Philosophy"
article_chain = []

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

# def find_first_link():

def web_crawl():
    while continue_crawl(target_url, article_chain):

        # 将页面添加到 article_chain
        article_chain.append(current_url)

        # 下载页面内容 => 在内容中查找第一个连接
        first_link = find_first_link(article_chain[-1])

        # current_link = 该链接
        current_url = first_link

        # 暂停片刻

