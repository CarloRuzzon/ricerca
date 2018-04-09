x = 0.3 #valore iniziale
x_f = 0.75 #valore finale
passo = 0.001 #passo
counter = 0 #contatore
z = 0.00001 #valore per cui si annulla il primo membro
while x < x_f:
    counter += 1
    if abs(x*x*x+4.5*x*x+3.5*x-3) < z:
        break
    x += passo

print ("La risposta:  %.3f ci siamo arrivati con %d  passaggi." % (x, counter,)) 

