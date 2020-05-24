import urllib
import requests

urlApi = 'https://unsplash.com/napi/search/photos\?query\=desktop%20background\&xp\=\&per_page\=20\&page\=1'


import pycurl
from io import BytesIO 

b_obj = BytesIO() 
crl = pycurl.Curl() 

# Set URL value
crl.setopt(crl.URL, urlApi)

# Write bytes that are utf-8 encoded
crl.setopt(crl.WRITEDATA, b_obj)

# Perform a file transfer 
crl.perform() 

# End curl session
crl.close()

# Get the content stored in the BytesIO object (in byte characters) 
get_body = b_obj.getvalue()

# Decode the bytes stored in get_body to HTML and print the result 
print('Output of GET request:\n%s' % get_body.decode('utf8')) 
print(get_body)