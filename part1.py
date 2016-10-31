import urllib
import urllib2

url = "http://challenge.code2040.org/api/register"
data = urllib.urlencode({'token':'76e4355f17281fc74fbda85754ed1e3e', 'github':'https://github.com/JohnDonavon/Code2040'})

response = urllib2.urlopen(url,data)

print(response)