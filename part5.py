import urllib
import urllib2
import ast
import dateutil.parser
import datetime
from datetime import timedelta

fetchUrl = "http://challenge.code2040.org/api/dating"
validateUrl = "http://challenge.code2040.org/api/dating/validate"

token = urllib.urlencode({'token':'76e4355f17281fc74fbda85754ed1e3e'})
response = urllib2.urlopen(fetchUrl, token)
collection = ast.literal_eval(response.read())
convertedDate = dateutil.parser.parse(collection["datestamp"])
date = convertedDate + timedelta(seconds = collection["interval"])
date = date.isoformat()
date = date.split("+", 1)[0] + "Z"

postData = urllib.urlencode({'token':'76e4355f17281fc74fbda85754ed1e3e','datestamp':date})
post = urllib2.urlopen(validateUrl,postData)