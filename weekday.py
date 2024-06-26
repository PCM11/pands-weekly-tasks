# weekday.py
# this program prints out whether or not today is a weekday.

# ref: docs.python.org, stackoverflow.com
#ref: Phumi

import datetime

# Days of the week: (0 = Mon, 1 = Tue, 2 = Wed...)
weekdaynumber = datetime.datetime.today().weekday()

if weekdaynumber < 5:
    print("Yes, unfortunately today is a weekday")
else:
    print ("It is the weekend, yay!")

