from services import Book ,DigitalLibarary


print(f'{'\nDigital Library System':=>45}')
print('='*22)  

library=DigitalLibarary('www.digbook.com')   

while True:  
    print('''\nSelect from Menu:
1- Add new book.
2- View all books.
3- Remove a book.
4- Search a book.
5- Exit\n''')
    num=input('\n> ')
    
    if num == '1':
        while True:
            try:
                N=int(input('How many books do you want to add: '))
                break
            except ValueError:
                print(f'\nthe "N" data type must be number!!')
                
        books=[]
        for count in range(N):
            print(f'\nBook{count+1}:')
            title=input('Enter the title: ')
            author=input('Enter the author: ')
            year=int(input('Enter the year: '))
            book=Book(title,author,year)
            books.append(book)
                
        library.add_books(books)
        
        

    elif num == '2':
        library.view_all()
        
    elif num == '3':
        library.remove_books()
            
    elif num == '4':
        library.search()
    elif num == '5':
        exit('Thanks for working with us')
