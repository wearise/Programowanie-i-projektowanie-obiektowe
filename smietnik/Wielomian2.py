from typing import Self
class Polynomial:
  def __init__(self,*args):

    if(type(args[0]) is list):
      self.coefficients = args[0].copy()
      self.coefficients.reverse()

    if(type(args[0]) is int):
      self.coefficients = []
      i = len(args)-1
      while(i>=0):
        self.coefficients.append(args[i])
        i-=1

    if(type(args[0]) is Polynomial):
      self.coefficients = args[0].coefficients

  # @property
  # def coefficients(self):
  #   return self.coefficients.copy()

  def __str__(self):

    if not (self.coefficients[0]==0):
      wiel_napis = str(self.coefficients[0])

    if(len(self.coefficients)>1):
      if(self.coefficients[1]==0):
        pass
      elif (wiel_napis[0] == '-'):
        wiel_napis = str(self.coefficients[1]) + "*x - " + wiel_napis[1::]
      else:
        wiel_napis = str(self.coefficients[1]) + "*x + " + wiel_napis

    for i in range(2,len(self.coefficients)):
      if(self.coefficients[i]==0):
        pass
      elif (wiel_napis[0] == '-'):
        wiel_napis = str(self.coefficients[i]) + "*x^" + str(i) + " - " + wiel_napis[1::]
      else:
        wiel_napis = str(self.coefficients[i]) + "*x^" + str(i) + " + " + wiel_napis

    return wiel_napis

  def __add__(self,wiel : Self):
    if (len(self.coefficients)<len(wiel.coefficients)):
      new_params = wiel.coefficients.copy()
      for i in range(len(self.coefficients)):
          new_params[i] += self.coefficients[i]
    else:
      new_params = self.coefficients.copy()
      for i in range(len(wiel.coefficients)):
          new_params[i] += wiel.coefficients[i]
    new_params.reverse()
    return Polynomial(new_params)

  def __sub__(self, wiel : Self):
    new_params = self.coefficients.copy()

    if (len(self.coefficients) < len(wiel.coefficients)):
      # new_params = wiel.coefficients.copy()
      i=0
      while(i<len(self.coefficients)):
        new_params[i] -= wiel.coefficients[i]
        i+=1
      while(i<len(wiel.coefficients)):
        new_params.append(-wiel.coefficients[i])
        i+=1

    else:
      for i in range(len(wiel.coefficients)):
        new_params[i] -= wiel.coefficients[i]

    new_params.reverse()
    return Polynomial(new_params)

  def __mul__(self,wiel : Self):
    new_params = []
    if (type(wiel) is Polynomial):
      for i in range(len(self.coefficients)):
        for j in range(len(wiel.coefficients)):
          if(len(new_params)<=i+j):
            new_params.append(self.coefficients[i]*wiel.coefficients[j])
          else:
            new_params[i+j] += self.coefficients[i]*wiel.coefficients[j]

    elif(type(wiel) is int):
      for x in self.coefficients:
        new_params.append(wiel*x)

    new_params.reverse()
    return Polynomial(new_params)

if __name__ == '__main__':
        ww = Polynomial(1,5)
        print(ww)