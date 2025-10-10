phrase = 'PythonProgramming'
list_p = []

for p in phrase:
	if  p not in list_p:
		list_p.append(p)
print(list_p)
print(len(phrase), len(list_p))
print(len(phrase) - len(list_p))
