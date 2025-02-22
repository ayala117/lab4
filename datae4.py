from datetime import datetime

current_datetime = datetime.now().replace(microsecond=0)
print("Datetime without microseconds:", current_datetime)
# Datetime without microseconds: 2025-02-22 22:44:28