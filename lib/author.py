class Author:
    def __init__(self, name):
        self._articles = []
        self.name = name 

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, "_name"):
            return
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            self._name = value  


    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        from .article import Article
        return Article(self, magazine, title)

    def topic_areas(self):
            if not self._articles:
            return None
        return list({m.category for m in self.magazines()})