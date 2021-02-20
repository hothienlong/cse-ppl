class Rational:
  def __init__(self, n=0,  d=1):
    if(d == 0):
      raise SystemExit("d = 0")
    else:
      self.n = n #2
      self.d = d #4
      self.g = self.gcd(n,d) #4
      self.numer = self.n/self.g #2/4
      self.denom = self.d/self.g #4/4

  def gcd(self,a,b):
    if(b == 0):
      return a
    else: 
      return self.gcd(b, a%b)

  def __add__(self, that):
    if(isinstance(that, Rational)):
      return Rational(self.numer*that.denom + that.numer*self.denom,
                  self.denom*that.denom)
    elif(isinstance(that,int)):
      return self + Rational(that)
    else:
      return None

  def __str__(self):
    return str(self.numer) + "/" + str(self.denom)
