from time import time
import datetime
begin = time()
start = datetime.datetime(1901, 1, 1).date()
end = datetime.datetime(2000, 12, 31).date()
a = [(start + datetime.timedelta(days=x)) for x in range(0, (end-start).days)]
print(sum([1 for j in a if j.weekday() == 6 and j.day == 1]))
print(time()-begin)
