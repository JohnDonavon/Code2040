import urllib
import urllib2
import ast

fetchUrl = "http://challenge.code2040.org/api/prefix"
validateUrl = "http://challenge.code2040.org/api/prefix/validate"

token = urllib.urlencode({'token':'76e4355f17281fc74fbda85754ed1e3e'})
response = urllib2.urlopen(fetchUrl, token)
collection = ast.literal_eval(response.read())

prefix = collection["prefix"]
array = collection["array"]
ansArray = []
for i in array:
	if not i.startswith(prefix):
		ansArray.append(i)

postData = urllib.urlencode({'token':'76e4355f17281fc74fbda85754ed1e3e','array[]':ansArray},True)
post = urllib2.urlopen(validateUrl,postData)