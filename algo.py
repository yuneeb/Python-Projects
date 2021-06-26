import csv
import numpy as np

# Reads a list of the leaf capacitancies from chip.csv
# C is an 8x8 array that stores the capacitance values in 
# each partition in C units.
# C[0][0] represents V1 cap.  C[0][1] represents V3 cap, 
# ..., C[7][7] represents v64 cap.  ]

with open('chip.csv', newline='') as csvfile:
    C = list(csv.reader(csvfile))

# Td is a 8x8 array that should be filled with the calculated
# delay values: Td[0][0] should get V1 delay, Td[0][1] should
# get V3 delay, ... Td[7][7] should get V64 delay

N= len(C)
Td = np.zeros((int(N),int(N)))

#print(C)

sz = int(N)

count = 0
hl = int(N)/2
pairs = np.zeros((int(hl),int(N)))
for k in range(0, int(N), 2):
	for l in range(int(N)):
		pairs[count][l] = int(C[k][l]) + int(C[k+1][l])

	count = count+1

#print(pairs)


quads = np.zeros((int(hl),int(hl)))
for k in range(int(hl)):
	count2 = 0
	for l in range(0, int(N), 2):
		
		quads[k][count2] = int(pairs[k][l]) + int(pairs[k][l+1])
		count2 = count2+1

#print(quads)

totalfull = 0
totallefthalf = 0
totalrightthalf = 0

tlqr = 0
blqr = 0
trqr = 0
brqr = 0


for c in range(int(N)):
	for d in range(int(N)):
		totalfull = totalfull + int(C[c][d])

		if(d < (int(N)/2)):
			totallefthalf = totallefthalf + int(C[c][d])

			if(c < (int(N)/2)): 
				tlqr = tlqr + int(C[c][d])
				#top left quarter


			if(c >= (int(N)/2)): 
				blqr = blqr + int(C[c][d])
				#bottom left quarter



		if(d >= (int(N)/2)):
			totalrightthalf = totalrightthalf + int(C[c][d])


			if(c < (int(N)/2)): 
				trqr = trqr + int(C[c][d])
				#top right qr

			if(c >= (int(N)/2)): 
				brqr = brqr + int(C[c][d])
				#bottom right qr


#print("tlqr:" + str(tlqr) + "  blqr:"+ str(blqr) + "  trqr:" + str(trqr) + "  brqr:" + str(brqr))

#print("TF:" + str(totalfull) + "  TLH:"+ str(totallefthalf) + "  TLR:" + str(totalrightthalf))

for a in range(int(N)):
	for b in range(int(N)):

		T1 = 0
		T2 = 0
		T3 = 0
		T4 = 0
		T5 = 0
		T6 = 0
		T7 = 0

		
		T1 = 1*(1 + int(C[a][b]))

		if((a%2) == 0):
			T2 = 1*(3 + int(C[a][b]) + int(C[a+1][b]))

		if((a%2) == 1):
			T2 = 1*(3 + int(C[a][b]) + int(C[a-1][b]))


		qa = int(a/2)
		qb = int(b/2)
		T3 = 2*(8 + quads[qa][qa])


		if((qa%2) == 0):
			T4 = 2*(18 + int(quads[qa][qb]) + int(quads[qa+1][qb]))


		if((qa%2) == 1):
			T4 = 2*(18 + int(quads[qa][qb]) + int(quads[qa-1][qb]))

		##
		if( (b < sz/2) and (a < sz/2) ):
			T5 = 4*(40 + tlqr)

		if( (b < sz/2) and (a >= sz/2) ):
			T5 = 4*(40 + blqr)
		
		if( (b >= sz/2) and (a < sz/2) ):
			T5 = 4*(40 + trqr)
		
		if( (b >= sz/2) and (a >= sz/2) ):
			T5 = 4*(40 + brqr)

		##

		
		##
		if(b < (sz/2)):
			T6 = 4*(84 + totallefthalf)

		if(b >= (sz/2)):
			T6 = 4*(84 + totalrightthalf)
		##

		T7 = 8*(176 + totalfull)
		
		TT = T1 + T2 + T3 + T4 + T5 + T6 + T7

		Td[a][b] = TT

#############################################################

# Writes the delays in Td to q1.csv
result = open("q1.csv", "w") 
for i in range(N):
	for j in range(N):
		if j== N-1 :
			result.write(str(int(Td[i][j])) + "\n")
		else :
			result.write(str(int(Td[i][j])) + ",")		
result.close()

