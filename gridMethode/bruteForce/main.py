from bruteForce import *

if __name__ == '__main__':

	# bepaal de begintijd van het programma
	startTime = time.clock()

	# print het eiwit in arrayvorm
	print (eiwitList())

	# voert het algoritme uit en bewaart de gevonden oplossingen
	grids = bruteForce()

	# berekent de score hoogste scores van de gevonden oplossingen
	result = calcEndScore(grids)

	# print de gevonden grids
	x = 0
	for i in result:
		x += 1
		print (x)
		print (i)
		print ("__________________________________________________________________")

	# print de totale runtijd van het programma
	print ("Runtime", time.clock() - startTime, "seconds")