a = 2
b = 2

# rumus baris aritmatika = a+(n-1)*b
def baris(a, b, n):
    return a+(n-1)*b

#rumus jumlah deret aritmatika = (a+Un)*n/2
def deret(a, b, n):
    Un = a + (n-1)*b
    return (a+Un)*n/2

print(baris(a,b,50))

print(deret(8,4,5))

def baris_geometri(awal,rasio, n):
    return awal*(rasio**(n-1))

print(baris_geometri(2,2,10))

