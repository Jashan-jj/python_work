class member:
    def __init__(self, name, mem_id):
        self.name= name
        self.mem_id= mem_id

class studentmember(member):
    def __init__(self, name , mem_id):
        super().__init__(name, mem_id)
        self.borrowbook = []

    def add_book(self, book_title):
        self.borrowbook.append(book_title)
        print("Book added.")

    def return_book(self, book_title):
        if book_title in self.borrowbook:
            self.borrowbook.remove(book_title)
            print("book returned Siccesfully.")
        else:
            print("book not found in borrow list.")
    
    def display_book(self):
        if self.borrowbook:
            print("Borrowed Books: ")
            for book in self.borrowbook:
                print(book)

std1= studentmember("Jashan", "S123")
std1.add_book("book1")
std1.add_book("book2")
std1.display_book()
std1.return_book("book1")
std1.display_book()

