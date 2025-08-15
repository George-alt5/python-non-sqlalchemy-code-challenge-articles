from lib.author import Author
from lib.magazine import Magazine

a1 = Author("Alice")
m1 = Magazine("TechDaily", "Tech")

art1 = a1.add_article(m1, "How to Code Well")
print("Author articles:", [a.title for a in a1.articles()])          
print("Magazine titles:", m1.article_titles())                       
print("Topic areas:", a1.topic_areas())                              