import random

def primerito():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  last = 13
  rnd = random.randint(0, last)
  rmd = random.randint(-1, last)


  print(quotes[rnd]) 
  print(quotes[rmd])

if __name__== "__main__":
  primerito()
