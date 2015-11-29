zrodlo = open('nazwa_pliku').readlines()
cel = open('nazwa_pliku', 'w')
for s in zrodlo:
	cel.write(s.replace("co zamieniæ", "na co"))
cel.close()
