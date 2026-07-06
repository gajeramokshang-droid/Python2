# Implement the following hierarchy . The Book function has, name, n (number of authors), authors (list of authors),
# publisher, ISBN, and year as its data members and the derived class has course as its data member. The derived class
# method overrides (extends) the methods of the base
# class.

class book:     #Encapulastion
    def __init__(self,name,n,authors,publishers,isbn,year):
        self.name=name
        self.n=n
        self.authors=authors
        self.publishers=publishers
        self.isbn=isbn
        self.year=year


    def display(self):
        print("Name",self.name)
        print("N",self.n)
        print("Author",self.authors)
        print("Publisher",self.publishers)
        print("ISBN",self.isbn)
        print("Year",self.year)


class Teaching(book):    #Inheritense
    def __init__(self, name, n, authors, publishers, isbn, year,course):
        super().__init__(name, n, authors, publishers, isbn, year)
        self.course=course
    
    def display(self):     #Polymorphism
        super().display()
        print("Course:",self.course)


p1=Teaching("Mokshang",12,["Jesus","God"],"Holy",12,2025,"Bible")
p1.display()

