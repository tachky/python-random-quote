import random
def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes)
  rnd = random.randint(0,last)
  rnd_m = random.randint(0,last)

  print(quotes[rnd] + quotes[rnd_m])

if __name__== "__main__":
  primary()
