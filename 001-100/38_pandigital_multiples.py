from itertools import count
def ispandigital(initial):
   digits = str(initial)
   for i in count(2):
      ndig = len(digits)
      if ndig < 9: digits += str(initial * i)
      elif ndig == 9 and set(digits) == set('123456789'):
         return int(digits)
      else: return False

print(max(map(ispandigital, range(1, 10000))))
