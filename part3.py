import urllib
import urllib2
import ast

fetchUrl = "http://challenge.code2040.org/api/haystack"
validateUrl = "http://challenge.code2040.org/api/haystack/validate"

token = urllib.urlencode({'token':'76e4355f17281fc74fbda85754ed1e3e'})
response = urllib2.urlopen(fetchUrl, token)
collection = ast.literal_eval(response.read())
check = collection["needle"]
index = collection["haystack"].index(check)

postData = urllib.urlencode({'token':'76e4355f17281fc74fbda85754ed1e3e','needle':index})
post = urllib2.urlopen(validateUrl,postData)