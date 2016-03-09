import newspaper



def download(url, language='en'):
    a = newspaper.Article(url=url, language=language, keep_article_html=True)
    a.download()
    a.parse()
    return a
