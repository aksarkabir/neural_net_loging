import simplejson as sj
hi = {}
hi["active"] = 1
hi["num"]="012"
hi["pass"]="qwerty"
hi["name"]="shihab"

fo = open('/var/www/html/main_pro/data.txt', 'w')
sj.dump(hi,fo)
fo.close()
