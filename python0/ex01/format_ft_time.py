import time
import datetime
from datetime import date

# second since epoch
second = time.time()
scientific_not = "{:.2e}".format(second)

# today date
today = date.today()
x = datetime.datetime(today.year, today.month, today.day)

print("Seconds since January 1, 1970:", end=' ')
print("{:,}".format(second) + " or ", end='')
print(scientific_not + " in scientific notation")
print(today.strftime("%b %d %Y"))
