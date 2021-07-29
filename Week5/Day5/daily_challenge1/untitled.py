import time
import requests
import sys

now = time.time_ns()
requests.get(sys.argv[1])
print(sys.argv[1], 'took', (time.time_ns() - now) / 1000000000, 'seconds to fetch')
