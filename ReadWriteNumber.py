
file = open("A01.txt","r")

for line in file:
  #Let's split the line into an array called "fields" using the ";" as a separator:
  fields = line.split("|")
  

 # Varaible for multiplication
  a = 2
  Num1 = int (fields[0]) * a
  Num2 = int (fields[1]) * a
  Num3 = int (fields[2]) * a
  Num4 = int (fields[3]) * a






  
  #Print
  print (str (Num1) + " , " + str (Num2) + " , " + str(Num3) + " , " + str(Num4))
  file2 = open("A02.txt","w+")
  b = ("[" + str (Num1) + " , " + str (Num2) + " , " + str(Num3) + " , " + str(Num4) + "]")
  file2.write(b)
  file2.close()
  
file.close()



