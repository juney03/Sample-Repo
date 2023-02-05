

import requests


r = requests.get("https://jueunyim.wixsite.com/greendreamchemistry")
print(r.status_code)
print(r.ok)
