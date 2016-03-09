import re

import newspaper
import lxml.html
import lxml.html.clean

newline = re.compile(r'(?:[\r\n]\s*)+')

def clean_html(html: str) -> str:
    root = lxml.html.fromstring(lxml.html.clean.clean_html(html))
    for elem in root.iter('*'):
        if elem.text is not None:
            elem.text = newline.sub(' ', elem.text)
        if elem.tail is not None:
            elem.tail = newline.sub(' ', elem.tail)
    return lxml.html.tostring(root, encoding='unicode', method='html', pretty_print=True)

def download(url, language='en'):
    a = newspaper.Article(url=url, language=language, keep_article_html=True)
    a.download()
    a.parse()
    a.article_html = clean_html(a.article_html)
    return a
