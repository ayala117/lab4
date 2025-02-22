
from datetime import datetime, timedelta

date1= datetime(2025, 2 , 20, 12, 0, 0)
date2=datetime(2025, 2, 22, 14, 30, 0)

difference= (date2- date1).total_seconds()
print("difference in seconds: ", difference)

#difference in seconds:  181800.0