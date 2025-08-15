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
        from .author import Author
        if not isinstance(value, Author):
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
        from .magazine import Magazine
        if not isinstance(value, Magazine):
            return 
        if self._magazine and self in self._magazine.articles():
            self._magazine.articles().remove(self)
        self._magazine = value
        if self not in value.articles():
            value.articles().append(self)