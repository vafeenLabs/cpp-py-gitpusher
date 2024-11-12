import os
from datetime import datetime

today = datetime.today()

month = ""
minute = ""
if(today.month<10):
    month = f"0{today.month}"
else:
    month = f"{today.month}"
if(today.minute<10):
    minute = f"0{today.minute}"
else:
    minute = f"{today.minute}"
string = "{}.{}.{} {}:{}".format(
    today.day, month, today.year, today.hour, minute
)

os.system("git add .")
os.system(f"git commit -m \"{string}\"")
os.system("git push")
