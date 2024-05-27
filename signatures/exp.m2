R = QQ[x,y, MonomialOrder=>GRevLex]
f = x^2 + 1
g = x*y

I = ideal(f,g)
G = groebnerBasis(I)
