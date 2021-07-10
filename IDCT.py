import math

N = input(number:)
N = int(N)

for y in range(N):
	for n in range(N):
		u = n
		v = y
		ans = 0
		rad = 0
		
		x = 2/N
		
		for i in range(N):
			for j in range(N):
				if i==0 and j==0:
					ans = 200
				elif i==2 and j==0:
					ans = 200
				else:
					ans=0
					
				if i != 0:
					cu = 1
				else:
					cu = 1/math.sqrt(2)
					
				if j != 0:
					cv = 1
				else:
					cv = 1/math.sqrt(2)
				
				m = math.cos(((2*u+1)*i)/(2*N)*math.pi)
				m *= math.cos(((2*v+1)*j)/(2*N)*math.pi)
				m *= ans * cu * cv
				rad += m
				
		x *= rad
		
		print(u,",",v,"=",x)