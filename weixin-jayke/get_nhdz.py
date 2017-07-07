import requests,random,json,time

# url='http://neihanshequ.com/'
# url='http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time=%s'% time.time()

def nhdz():
    url = 'http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time=%s' % time.time()
    r=requests.get(url).content
    res=json.loads(r)
    return random.sample(res['data']['data'],1)[0]['group']['text']
