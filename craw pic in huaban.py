
import urllib2,re

#source url
add = 'http://huaban.com/boards/38075012/'

#open the url and put all codes into buf
req = urllib2.urlopen(add)
buf = req.read()

#to see what we have crawed
print buf

#use re to filter the img tag,result is a list
listurl = re.findall(r'<img src="//.+?>',buf)
print '111111111111'

#each of listurl is a string
#and go on filter the url,cut"<img src="
#we just want the pure url
strlist=[]
for e in listurl:
    strlist+= re.findall(r'"//.+?"',e)
    print strlist

#keep filter,cut",use sub func to replace
#the first " is replaced with http:
#the final " is replaced with null
#we must use the list's func:append
imglist = []
for e in strlist:
    tmp = re.sub(r'"','http:', e,1)
    tmp2 = re.sub(r'"','',tmp)
    imglist.append(tmp2)
print imglist

#finally we just output the img we've crawed
i = 0
for url in imglist:
    f = open(str(i)+'.jpg','w')
    req = urllib2.urlopen(url)
    buf = req.read()
    f.write(buf)
    i+=1
#and just go to the project's root dir to see