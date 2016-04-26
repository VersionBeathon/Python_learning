# _*_ coding:utf-8 _*_
from urllib import urlopen
from bs4 import BeautifulSoup
import lxml

text = urlopen('http://python.org/community/jobs').read()

soup = BeautifulSoup(text, "lxml")

jobs = set()
for header in soup('h3'):
    links = header('a', 'reference')
    if not links: continue
    link = link[0]
    jobs.add('%s (%s)' % (link.string, link['href']))

print '\n'.join(sorted(jobs, key=lambda s: s.lower()))