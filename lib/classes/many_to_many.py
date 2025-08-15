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
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self._articles:
            return None
        return list({m.category for m in self.magazines()})


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
        authors = [art.author for art in self._articles]
        uniq = set(authors)
        result = [au for au in uniq if authors.count(au) > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not cls.all_magazines:
            return None
        if sum(len(m.articles()) for m in cls.all_magazines) == 0:
            return None
        return max(cls.all_magazines, key=lambda m: len(m.articles()))


class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._author = None
        self._magazine = None
        self._title = None

        self.author = author
        self.magazine = magazine
        self.title = title

        Article.all.append(self)

        if self not in author.articles():
            author.articles().append(self)
        if self not in magazine.articles():
            magazine.articles().append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(self, "_title") and self._title is not None:
            return
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value
        else:
            self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            return
        if self._author is value:
            return
        if self._author and self in self._author.articles():
            self._author.articles().remove(self)
        self._author = value
        if self not in value.articles():
            value.articles().append(self)

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            return
        if self._magazine is value:
            return
        if self._magazine and self in self._magazine.articles():
            self._magazine.articles().remove(self)
        self._magazine = value
        if self not in value.articles():
            value.articles().append(self)
