import sys
import requests

print(requests.get(sys.argv[1]).json())
