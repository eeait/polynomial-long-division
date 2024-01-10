# POLYNOMIAL LONG DIVISION ALGORITHM WITH INTEGER COEFFICIENTS

# This code is quite old and ugly, also it's in Finnish.
# It does the algorithm recursively just like you would do it with pen and paper.

from fractions import Fraction
import time

def aste(pituus, indeksi):
    return(pituus-indeksi-1)
def indeksi(pituus, aste):
    return(pituus-aste-1)

def polynominAste(polynomi):
    aste = len(polynomi)-1
    for t in polynomi:
        if t == 0:
            aste -= 1
        else:
            break
    return aste

def esitys(polynomi):
    string = ""
    for i in range(len(polynomi)):
        if polynomi[i] != 0:
            if polynomi[i] < 0:
                string += "   -("
            else:
                string += "   +("
            string += str(abs(polynomi[i])) \
                      + ")x^" + str(aste(len(polynomi), i))
    if string == "":
        string = "0"
    return string

print("\n\n\nPOLYNOMIAL LONG DIVISION (INTEGER COEFFICIENTS)\n")
print("\nCalculate the division P(x)/B(x).\n")

time.sleep(1)

a1 = int(input("Enter the degree of the dividend polynomial P: "))
print("Enter the coefficients of the terms:")

p = [0]*(a1+1)
for i in range(a1+1):
    p[i] = int(input("x^"+str(a1-i)+"\t"))

print("P(x) =", esitys(p))
print("\n")

time.sleep(1)

a2 = int(input("Enter the degree of the divisor polynomial B: "))
print("Enter the coefficients of the terms:")

b = [0]*(a2+1)
for i in range(a2+1):
    b[i] = int(input("x^"+str(a2-i)+"\t"))

print("B(x) =", esitys(b))

jakajanKorkein = b[0]
osamaara = [0]*len(p)

rivit = []

def jaaKerroVahenna(jaettava):
    rivit.append(jaettava)
    if polynominAste(jaettava) >= polynominAste(b):

        for t in range(len(p)):
            if jaettava[t] != 0:
                osamaaranAste = aste(len(p), t)-aste(len(b), 0)
                osamaaranIndeksi = indeksi(len(p), osamaaranAste)
                jako = Fraction(jaettava[t], jakajanKorkein)
                osamaara[osamaaranIndeksi] = jako
                break

        vahentaja = [0]*len(p)
        for t in range(len(b)):
            terminAste = aste(len(b), t)
            tulonAste = osamaaranAste+terminAste
            tulonIndeksi = indeksi(len(p), tulonAste)
            vahentaja[tulonIndeksi] = jako * b[t]

        erotus = [0]*len(p)
        for i in range(len(p)):
            erotus[i] = jaettava[i]-vahentaja[i]
        return jaaKerroVahenna(erotus)
        
    else:
        return [osamaara, jaettava]

tulos = jaaKerroVahenna(p)[0]
jaannos = jaaKerroVahenna(p)[1]

def jjNolla(jakojaannos):
    for t in jakojaannos:
        if int(t) != 0:
            return False
    return True

time.sleep(1)

print("\n")
print("The result of the division P(x)/B(x) is")
if jjNolla(jaannos):
    print(str(esitys(tulos)) + ".")
    print("The division is exact!")
else:
    print(str(esitys(tulos)) + ",")
    print("the remainder is")
    print(str(esitys(jaannos))+ ".")

print("\n")