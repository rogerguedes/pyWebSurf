#!/usr/bin/python
import urllib2, urllib
#>>building the request object

myRequest = urllib2.Request('http://127.0.0.1/sandbox/pytest.php')


#>>building the opener

myOpener = urllib2.build_opener()
myReqHeaders = [\
('User-Agent', 'Mozilla/5.0 (X11; Linux i686; rv:37.0) Gecko/20100101 Firefox/37.0'),\
('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),\
('Accept-Language', 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3'),\
('Accept-Encoding', 'gzip, deflate'),\
('Connection', 'keep-alive')
]
myOpener.addheaders = myReqHeaders

#>>Running the request

response = myOpener.open(myRequest)

#>>dealing with response

print response.read()

#now with POST
data = {'name': "doidao", 'password': 'senhaDoida'}
encodedData = urllib.urlencode(data)
response = myOpener.open(myRequest, encodedData)
#>>dealing with response

print response.read()

