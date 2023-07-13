class Url_Manager():
    """
    URL管理器的实现
    """

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None or len(url) == 0:
            return
        if url in self.new_urls or url in self.old_urls:
            return
        self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def get_url(self):
        if self.has_new_url():
            new_url = self.new_urls.pop()
            self.old_urls.add(new_url)
            return new_url
        else:
            return None

    def has_new_url(self):
        return len(self.new_urls) > 0


if __name__ == "__main__":
    url_manager = Url_Manager()
    url_manager.add_new_url("http://www.baidu.com")
    url_manager.add_new_url("http://www.sina.com")
    print(url_manager.new_urls, url_manager.old_urls)

    print("#"*30)
    print(url_manager.has_new_url())

    print("#" * 30)
    print(url_manager.get_url())

    print("#" * 30)
    print(url_manager.get_url())

    print("#" * 30)
    print(url_manager.get_url())

    print("#" * 30)
    print(url_manager.has_new_url())

    print("#" * 30)
    print(url_manager.new_urls, url_manager.old_urls)
