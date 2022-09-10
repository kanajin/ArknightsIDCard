import os
from Draw import draw

os.makedirs('./OutPut', exist_ok=True)
try:
    draw()
except Exception as error:
    print(error)

