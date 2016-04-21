# _*_ coding:utf-8 _*_
from urllib import urlopen
from HTMLParser import HTMLParser


class Scraper(HTMLParser):

    in_h3 = False
    in_link = False

    def handle_starttag(self, tag, attrs): # attrs参数是由（键，值）元素组成的列表
        attrs = dict(attrs)                # 使用dict函数将它们转化为字典
        if tag == 'h3':
            self.in_h3 = True

        if tag == 'a' and 'href' in attrs:
            self.in_link = True
            self.chunks = []
            self.url = attrs['href']

    def handle_data(self, data):
        if self.in_link:
            self.chunks.append(data)

    def handle_endtag(self, tag):
        if tag == 'h3':
            self.in_h3 = False
        if tag == 'a'
            if self.in_h3 an self.in_link:
                print '%s (%s)' % (''.join(self, chunks), self.url)
            self.in_link = False
# feed 方法会调用handle_starttag()、handle_data()、handle_endtag()方法
text = urlopen('http://python.org/community/jobs').read()
parser = Scraper()
parser.feed(text)
parser.close()
