P = [.999,0,0;0,.95,.06;.001,.05,.94]
n = [375;375;0]
for k = 0:48
	r = P^k * n
	q = r'
	save -ascii -append markovRes.dat q
endfor
