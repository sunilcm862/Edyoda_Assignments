class power_class():
     def pow_func(self, x, n):
          power = abs(n)
          #print(power)
          res = 1.0
          while power:
               #print(power)
               if power & 1:
                    res= res* x
               x*=x
               power>>=1
               if n<0:
                    return 1/res
          return res
ob1 = power_class()
print(int(ob1.pow_func(10, 2)))
print(ob1.pow_func(12, 4))
