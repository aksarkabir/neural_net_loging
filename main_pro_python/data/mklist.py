import simplejson as sj

arr = {}
arr['name'] = []
arr['count']=0

fo = open('data.txt', 'w')
sj.dump(arr,fo)
fo.close()
