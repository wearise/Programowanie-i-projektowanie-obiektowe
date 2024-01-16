class Polynomial:
  def __init__(self,*args):

    if(type(args[0]) is list):
      self._coefficients = args[0].copy()
      self._coefficients.reverse()

    if(type(args[0]) is int):
      self._coefficients = []
      i = len(args)-1
      while(i>=0):
        self._coefficients.append(args[i])
        i-=1

    if(type(args[0]) is Polynomial):
      self._coefficients = args[0]._coefficients

  @property
  def coefficients(self):
    return self._coefficients.copy()

  def __str__(self) -> str:

    if not (self._coefficients[0]==0):
      wiel_napis = str(self._coefficients[0])

    if(len(self._coefficients)>1):
      if(self._coefficients[1]==0):
        pass
      elif (wiel_napis[0] == '-'):
        wiel_napis = str(self._coefficients[1]) + "*x - " + wiel_napis[1::]
      else:
        wiel_napis = str(self._coefficients[1]) + "*x + " + wiel_napis

    for i in range(2,len(self._coefficients)):
      if(self._coefficients[i]==0):
        pass
      elif (wiel_napis[0] == '-'):
        wiel_napis = str(self._coefficients[i]) + "*x^" + str(i) + " - " + wiel_napis[1::]
      else:
        wiel_napis = str(self._coefficients[i]) + "*x^" + str(i) + " + " + wiel_napis

    return wiel_napis

  def __add__(self,wiel : "Polynomial") -> "Polynomial":
    if (len(self._coefficients)<len(wiel._coefficients)):
      new_params = wiel._coefficients.copy()
      for i in range(len(self._coefficients)):
          new_params[i] += self._coefficients[i]
    else:
      new_params = self._coefficients.copy()
      for i in range(len(wiel._coefficients)):
          new_params[i] += wiel._coefficients[i]
    new_params.reverse()
    return Polynomial(new_params)

  def __sub__(self, wiel : "Polynomial") -> "Polynomial":
    new_params = self._coefficients.copy()

    if (len(self._coefficients) < len(wiel._coefficients)):

      i=0
      while(i<len(self._coefficients)):
        new_params[i] -= wiel._coefficients[i]
        i+=1
      while(i<len(wiel._coefficients)):
        new_params.append(-wiel._coefficients[i])
        i+=1

    else:
      for i in range(len(wiel._coefficients)):
        new_params[i] -= wiel._coefficients[i]

    new_params.reverse()
    return Polynomial(new_params)

  def __mul__(self,wiel : "Polynomial") -> "Polynomial": #tutaj w sumie wiel może być typu "Polynomial" albo typu int
    new_params = []
    if (type(wiel) is Polynomial):
      for i in range(len(self._coefficients)):
        for j in range(len(wiel._coefficients)):
          if(len(new_params)<=i+j):
            new_params.append(self._coefficients[i]*wiel._coefficients[j])
          else:
            new_params[i+j] += self._coefficients[i]*wiel._coefficients[j]

    elif(type(wiel) is int):
      new_params = [wiel*x for x in self._coefficients]

    new_params.reverse()
    return Polynomial(new_params)

if __name__ == '__main__':
        ww = Polynomial(1,0,-5,2)
        print(ww)