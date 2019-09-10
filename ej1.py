import re
from collections import Counter
from newspaper import Article

'''
Función que obtiene el contenido de un articulo y lo procesa para
obtener un historograma de las apariciones de cada palabra.
'''
def body(url, ordered = True, expr = r'[\W\d]+'):
    article = Article(url)
    article.download()
    article.parse()
    text = article.text.lower()
    words = filter(None, re.split(expr, text))
    count = Counter(words)
    return dict(sorted(count.items(), key=lambda kv: kv[1], reverse=True)) 