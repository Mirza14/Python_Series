import re
text = '10.20.100.24 - - [11/Jul/2024:16:01:33 -0700] "GET http://proxy1:3128/squid-internal-static/icons/SN.png HTTP/1.1" 200 13051 "http://192.168.56.30:3128/" "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0" TCP_HIT:HIER_NONE'
pattern = r'"(Mozilla\/5\.0 \(X11; Linux x86_64; rv:109\.0\) Gecko\/20100101 Firefox\/115\.0)"'
match = re.search(pattern, text)
if match:
    print(match.group(1))
else:
    print("Sorry, you get better at RegEx Kiddo!")