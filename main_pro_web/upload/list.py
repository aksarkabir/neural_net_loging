import simplejson as js

f = open('data.txt','w')

a = {}
a["active"]=0
a['name']=''
a['number'] = 0

js.dump(a,f)
f.close()
