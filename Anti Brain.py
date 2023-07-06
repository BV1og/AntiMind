import random
a = input("enter the script")
b = a.split()
c = ''
d = []
e = 0
f = 0
i = 0

for i in range(1, 200):
	d.append(0)
for c in b:
	if c == 'go':
		f +=1		
	if c == 'do':
		if d[f] == 1:
			d[f] = 0
		else:
			d[f] = 1
	if c == 'All':
		for e in d:
			print(e, end = ' ')
	if c == 'up':
		d[f] = 1
	if c == 'down':
		d[f] = 0
	if c == 'to':
		f -= 1
	if c == 'on':
		if d[f] + 1 == 1:
			d[f] = 0
		else:
			d[f] = 1
	if c == 'off':
		if d[f] + 1 == 1:
			d[f] = 1
		else:
			d[f] = 0
	if c == 'we':
		print(d[f])
	if c == 'an':
		d[f] = random.randint(0, 1)
				
