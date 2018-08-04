"""
Combined Access Log Parser
http://httpd.apache.org/docs/current/logs.html#combined
"""

from parsers.log import LogParser

class Combined(LogParser):

  # 125.252.224.28 - - [17/Sep/2017:03:34:04 -0400] "GET /api/19302 HTTP/1.1" 200 1560 "https://www.jhu.edu/" "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0" "0" "120763" "www.jhu.edu" "219.143.147.4, 10.252.224.52" "219.143.147.4" "" "-" "-" "-" "_ceir=1; _ceg.s=ouwnv4; _ceg.u=ouwnv4; _ga=GA1.2.218068154.1454569410"

  pattern = ('^'
  '(\d+.\d+.\d+.\d+)\s'                                     # IP address
  '[^\s]+\s'                                                # identity of the user determined by identd (usually - on our server)
  '[^\s]+\s'                                                # user name determined by HTTP authentication
  '\[(\d{2}\/\w+\/\d{4}:\d{2}:\d{2}:\d{2}\s+-\d{4})\]\s'    # time the request was received
  '"(\w+)\s'                                                # HTTP method
  '([^\s]+)\s'                                              # Request URL
  'HTTP\/[0-9\.]+"\s'                                       # protocol
  '\d{3}\s'                                                 # status code
  '\d+\s'                                                   # size of the response
  '[^\s]+\s'                                                # referrer header (or "-" if no referrer header present)
  '"([^"]+)"'                                               # user agent string
  '.*$')                                                    # the rest

  matchmap = ['ip', 'datetime', 'method', 'url', 'useragent']
