from brutePruning import *

if __name__ == '__main__':

	# bepaal de begintijd van het programma
	startTime = time.clock()

	# print het eiwit in arrayvorm
	print (eiwitList())

	# voert het algoritme uit en bewaart de gevonden oplossingen
	result = bruteForce()

	# print het aantal oplossingen en de grid-vouwing en score per oplossing
	print (len(result))
	for i in result:
	    print (i.score)
	    print (i.grid)

	# print de totale runtijd van het programma
	print (time.clock() - startTime, "seconds")
