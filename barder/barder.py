a = 2
b = 2

# rumus baris aritmatika atau Un = a+(n-1)*b
def baris(a, b, n):
    return a+(n-1)*b

#rumus jumlah deret aritmatika = (a+Un)*n/2
def deret(a, b, n):
    Un = a + (n-1)*b
    return (a+Un)*n/2

print(baris(a,b,50))

print(deret(8,4,5))

#rumus baris ke n dari baris geometri atau Un Geometri = a*r^n-1
def baris_geometri(awal,rasio, n):
    return awal*(rasio**(n-1))

print(baris_geometri(2,2,10))

#rumus jumlah n suku pertama atau Sn
def deret_geometri(a,r,n):
    if r < 1:
        return (a*(1-(r**n)))/(1-r)
    elif r > 1:
        return (a*((r**n)-1))/(r-1)

print(deret_geometri(2,2,10))