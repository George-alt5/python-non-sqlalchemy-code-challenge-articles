class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        self._articles = []
        self._name = None
        self._category = None
        self.name = name
        self.category = category
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            if not hasattr(self, "_name") or self._name is None:
                pass

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            if not hasattr(self, "_category") or self._category is None:
                pass

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        if not self._articles:
            return None
        return [a.title for a in self._articles]

    def contributing_authors(self):
        if not self._articles:
            return None
        authors = [a.author for a in self._articles]
        uniq = set(authors)
        many = [au for au in uniq if authors.count(au) > 2]
        return many if many else None

    @classmethod
    def top_publisher(cls):
        if not cls.all_magazines:
            return None
        if sum(len(m.articles()) for m in cls.all_magazines) == 0:
            return None
        return max(cls.all_magazines, key=lambda m: len(m.articles()))