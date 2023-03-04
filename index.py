"""
Pseudo code:

    current_link = random_link_of_a_wikipedia_page
    article_chain = []

    页面标题不是哲学，并且我们尚未发现循环：

        将页面添加到 article_chain

        下载页面内容
        在内容中查找第一个连接
        页面=该连接

        暂停片刻
"""

def continue_crawl(target_url, search_history):
    if len(search_history) > 25:
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

# target_url = random_url_of_a_wikipedia_page
# article_chain = []

while continue_crawl(target_url, article_chain):
    # to be continue...

