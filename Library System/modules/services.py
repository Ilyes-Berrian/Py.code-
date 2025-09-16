class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
         
        
class Library:
    def __init__(self):
        self.book_list=[]
        
    def add_books(self,books):
        if books:
            print()
            for bk in books:
                self.book_list.append(bk)
                print(f'Added book: {bk.title} by {bk.author} ({bk.year})')
        else:
            print('There are no new books.')
    def view_all(self):
        if not self.book_list:
            print('The library is empty!!')
        else:
            print('Books in the library:')
            for bk in self.book_list:
                print(f'- {bk.title} ({bk.year})')
        
    def remove_books(self): 
        if not self.book_list:
            print('The library is empty!!')
        else:
            rmv_book=input("Enter book's title you want to remove: ")
            rmvbook_author=input("Enter the book's author: ")
            for bk in self.book_list:  
                if bk.title == rmv_book and bk.author == rmvbook_author:
                    self.book_list.remove(bk)
                    print('\nRemoved book: ',bk.title)
                    break
            else:
                print('\nBook not found.')
            

class DigitalLibarary(Library):
    def __init__(self,website):
        super().__init__()
        self.website=website 
        
    def search(self):
        if not self.book_list:
            print('there are no uploaded books to the website.')
        else:  
            title=input('Search title: ')
            found=[bk for bk in self.book_list if title.lower() in bk.title.lower()]
            if found:
                print(f'Search results for {title} in {self.website}:')
                for bk in found:
                    print(f'\n- {bk.title} by {bk.author} ({bk.year})') 
            else:
                print(f'No results found for {title} in {self.website}')
                        