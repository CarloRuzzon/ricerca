eps = 0.00001
low = 0.3
high = 0.75
counter = 1
while low < high:
	x = (low + high) / 2
   	eq = x**3 + 4.5 * x ** 2 + 3.5 * x - 3
 	eq1 = low ** 3 + 4.5 * low ** 2 + 3.5 * low - 3
 	eq2 = high ** 3 + 4.5 * high ** 2 + 3.5 * high - 3


 	if abs(eq) < eps:
         	break

	elif eq * eq1 > 0:
 		low = x
	else:
		high = x
  	counter += 1
print("Soluzione: %.3f, in %d passaggi" % (x, counter,))
