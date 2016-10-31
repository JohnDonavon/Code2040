import urllib
import urllib2

fetchUrl = "http://challenge.code2040.org/api/reverse"
validateUrl = "http://challenge.code2040.org/api/reverse/validate"

data = urllib.urlencode({'token':'76e4355f17281fc74fbda85754ed1e3e'})

response = urllib2.urlopen(fetchUrl,data)
string = response.read()
reverseString = string[::-1]

postData = urllib.urlencode({'token':'76e4355f17281fc74fbda85754ed1e3e','string':reverseString})
post = urllib2.urlopen(validateUrl, postData)