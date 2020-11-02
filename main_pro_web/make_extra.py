import simplejson as sj

f = open('data_extra.txt','w')
arr = {}

arr['active']=0
arr['name']=""

sj.dump(arr,f)

f.close()
