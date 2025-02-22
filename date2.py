
from datetime import datetime, timedelta

today =datetime.now()
yesterday= today - timedelta(days=1)
tommorow= today + timedelta(days=1)
print("yesterday:", yesterday.strftime("%Y-%m-%d"))
print("today:", today.strftime("%Y-%m-%d"))
print("tommorow:", tommorow.strftime("%Y-%m-%d"))

# yesterday: 2025-02-21
# today: 2025-02-22
# tommorow: 2025-02-23