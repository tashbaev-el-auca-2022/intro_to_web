#Exception Handling
try:
  print(x)
except:
  print("An exception occurred")

#Many Exceptions
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

#Else
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#Finally
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

#Raise an exception
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")