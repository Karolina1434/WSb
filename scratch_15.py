print('KArolina')
a = 14
b = 16
x = int(input("podaj liczbe godzin"))
y = int(input("podaj liczbe zajzdów"))
def liczenie(a,b):
    wynik = a + b
    print (wynik)
print (liczenie(a,b))

def zajęcia(x,y):
    ilgodz= x*y
    śr = ilgodz/y
    print(ilgodz,śr)
print(zajęcia(x,y))