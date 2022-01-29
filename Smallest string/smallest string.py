alphs = [chr(ord('a')+i) for i in range(26)]
alt = []
alt.extend(alphs)
alt[0] = 'b'
alt[1] = 'a'
t = int(input())
for i in range(t):
	n, k = [int(i) for i in input().split()]
	if n<k or (n!=1 and k==1):
		print('-1')
		continue
	
	if n==k:
		print(*alphs[:k], end='', sep='')
		print()
		continue
	
	st = n - k
	for j in range(0,st,2):
		# temp = min(k, n-j)
		temp = min(2, st-j)
		print(*alphs[:temp], end='', sep='')
	if st%2 == 0:
		print(*alphs[:k], end='', sep='')
	else:
		print(*alt[:k], end='', sep='')
	print()