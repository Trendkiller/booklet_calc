# wzór:
# zawnętrzne (vertical reverse): 
#           n, n+3, n+1, n+3...
# przykład: 1, 4, 5, 8...
# wewnętrzne (vertical):
#           n+1,n+1,

strona_startowa = input("Strona startowa: ")
liczba_stron = input("Ilosc stron: ")

def outer(x, y):
    print("Vertical reverse range:")
    while x <= y:
        print(x, end=",") # 1
        x += 3
        print(x, end=",") # 1 + 3 = 4
        x += 1  
    print("\n")

def inner(x,y):
    print("Vertical range:")
    while x <= y:
        x +=1
        print(x, end=",") # 2
        x +=1
        print(x, end=",") # 2 + 1 = 3
        x +=2
    print("\n")

def a3_umber_of_pages(x):
    print("Number of A4 pages: ")
    print(int(x) / 4)

outer(int(strona_startowa), int(liczba_stron))
inner(int(strona_startowa), int(liczba_stron))
a3_umber_of_pages(liczba_stron)
