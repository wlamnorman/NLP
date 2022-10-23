# calculates the Levenshtein distance from the two strings
# details of alg can be found here: https://en.wikipedia.org/wiki/Levenshtein_distance
# below there is a cost to substituting and there is a cost to adding/deleting, this can be changed

def lev_d(str_1,str_2,sub_cost,move_cost):
	# going with the matrix thing on wikipedia that uses memoization
	l_1 = len(str_1)
	l_2 = len(str_2)
	M = [[0 for col in range(0,l_1+1)] for row in range(0,l_2+1)]
	
	# filling in the first row and column:
	for i in range(0,l_1):
		M[0][i] = i

	for j in range(1,l_2):
		M[j][0] = j

	# going through the other rows and filling in with
	for i in range(1,l_1+1):
		for j in range(1,l_2+1):
			if(str_1[i-1] == str_2[j-1]):
				sub_mod = 0
			else:
				sub_mod = 1

			# the "memoization" part
			M[j][i] = min(M[j-1][i] + move_cost, M[j][i-1] + move_cost, M[j-1][i-1] + sub_mod*sub_cost)

	return (M[l_2 - 1][l_1 - 1])

# an example
print(lev_d("Jag heter Benjamin!", "Jag heter Benjamin!",2,1))





