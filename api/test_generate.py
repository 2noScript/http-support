import json

from browser_headers import getBrowserHeaders









data=getBrowserHeaders(10)


pretty_json_string = json.dumps(data, indent=4)
print(pretty_json_string)
# print(browserHeaders)
