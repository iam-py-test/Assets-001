from random import choice
existingIDs = []
def mkID():
  id = ""
  for r in range(0,32):
    id += choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","-"])
  if id in existingIDs:
    id = mkID()
  return id
