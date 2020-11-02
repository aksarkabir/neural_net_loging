import simplejson as sj

f = open('light_data.txt', 'w')

arr = {}

arr['light_1']=0
arr['light_2']=0
arr['light_3']=0

sj.dump(arr,f)

f.close()
