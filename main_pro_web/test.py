import simplejson as js

f = open('pass.txt','w')

nm = ['shihab','lima']
pas = {}

pas['shihab'] = 'qwerty'
pas['lima']='asdfgh'
ls = {}
ls['name'] = nm
ls['login'] = pas

js.dump(ls,f)

f.close()
