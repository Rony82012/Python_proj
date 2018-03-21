class employee:
  def __int__(self,first,last,pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + last +'@company.com'


varun = employee('varun','dnd','10')

print (varun.last)

