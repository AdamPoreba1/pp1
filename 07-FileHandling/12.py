name = "Adam Poreba"
university = "Krakow University of Economics"
field = "Applied Informatics"

file = open("student.txt", 'a')
file.write(name+"\n"+university+"\n"+field+"\n")
file.close()