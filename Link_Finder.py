from html.parser import HTMLParser
from urllib import parse


class linkfinder(HTMLParser):
    def __init__(self, base_url, page_url):
        super()._init_()
        self.base_url = base_url
        self.page_url = pague_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass


finder = LinkFinder()
finder.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')
