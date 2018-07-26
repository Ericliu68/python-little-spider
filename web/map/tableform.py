#coding:utf-8
import re
import psycopg2
import json

def datatojson(sightlist):  #直接生成json数据
    json_geo = {}
    bjsonlist = []
    ejsonlist1 = []
    ejsonlist2 = []
    attr={}
    ejsonlist4=[]
    num = 1
    for l in sightlist:
        p = '(.*?),(.*?)$'
        geo = re.findall(p,l[7])[0]
        json_geo['lat'] = geo[1]
        json_geo['count'] = int(l[4])/100
        json_geo['lng'] = geo[0]
        bjsonlist.append(json_geo)
        print '正在生成第' + str(num) + '个景点的经纬度'
        ejson1 = {l[1] : [geo[0],geo[1]]}
        ejsonlist1 = dict(ejsonlist1,**ejson1)
        ejson2 = {'name' : l[1],'value' : int(l[4])/100}
        ejsonlist2.append(ejson2)
        num +=1
        # print l
        attr['name']=l[1]
        attr['level']=l[2]
        # attr['area']=l[3]
        attr['price']=l[3]
        attr['soldnum']=l[4]
        attr['hot']=l[5]
        attr['address']=l[6]
        attr['time']=l[8]
        print attr
        ejsonlist4.append(attr)
    bjsonlist =json.dumps(bjsonlist)
    
    ejsonlist3={'data':ejsonlist2,'geoCoordMap':ejsonlist1}
    ejsonlist5={'data':ejsonlist4}
    ejsonlist1 = json.dumps(ejsonlist1,ensure_ascii=False)
    ejsonlist2 = json.dumps(ejsonlist2,ensure_ascii=False)
    ejsonlist3 = json.dumps(ejsonlist3,ensure_ascii=False)
    ejsonlist5=json.dumps(ejsonlist5,ensure_ascii=False)
    with open('aaa.json','w') as f:
        f.write(ejsonlist3)
    with open('bbb.json','w') as f:
        f.write(ejsonlist5)
    
def main(plece):
    place='北京'
    try:
        conn=psycopg2.connect(database='postgres',user='postgres',password='9090',host='127.0.0.1',port='5432')
        # print '*'
        cur=conn.cursor()
        cur.execute("select id from city where city like '%"+ str(place) +"%';")
        city_id=list(cur.fetchall()[0])[0]
        # print city_id
        cur.execute("select id from area where city_foreign_id=%d;" % int(city_id))
        area_id=cur.fetchall()
        sightlist=[] 
        # cur.close()
        # conn.close()
        # print area_id
        # datatojson(area_id)
        for id1 in area_id:
            # print id1[0]
            cur.execute("select * from attractions where area_foreign_id=%d" % int(id1[0]))
            rows=cur.fetchall()
            for i in range(len(rows)):
                sightlist.append(rows[i])
        datatojson(sightlist) 
    except KeyError,e:
        # return e
        # traceback()
        print 'wrong'
main()