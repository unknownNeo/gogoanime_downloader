import requests
import json

def default(url):
    file = 'tmp.txt'
    r = requests.get(url)
    #print(r)
    w = open(file,'w',encoding = 'utf-8')
    w.write(r.text)
    w.close()
    f = open(file,'r',encoding = 'utf-8').readlines()
    search = 'class="dowloads"'
    for line in f:
       if search in line:
           tmp = line
           break
           
    tmp = tmp.split('"')
    search = 'https://gogo-play.net'
    for i in tmp:
        if search in i:
            link = i
    
    #print(link)
    data = link.split('?')[1].split('&')
    data = data[0::2]
    second(data,url)
    
    
def second(data,r_url):
     file = 'tmp.txt'
     #print('second function')
     ref = data[0] + '&' + data[-1]
     #print(ref)
     url = 'https://gogo-play.net:443/ajax.php?' + ref + '' + r_url.split('/')[-1]
     #print(url)
     headers = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
     "Accept": "application/json, text/javascript, */*; q=0.01",
     "Accept-Language": "en-US,en;q=0.5",
     "Accept-Encoding": "gzip, deflate",
     "Prefer": "safe",
     "Referer": "https://gogo-play.net/streaming.php?" + ref,
     "X-Requested-With": "XMLHttpRequest",
     "Connection": "close"
     }
     r = requests.get(url,headers=headers)
     #print(r)
     w = open(file,'w',encoding = 'utf-8')
     w.write(r.text)
     w.close()
     f = open(file,'r',encoding = 'utf-8')
     data = json.load(f)
     print(data['source_bk'][0]['file'])
     print('done')

def streamsb(url):
     r = requests.get(url)
     w = open('tmp.txt','w',encoding = 'utf-8')
     w.write(r.text)
     w.close()
     f = open('tmp.txt','r',encoding = 'utf-8')
     search = 'streamsb.net'
     for line in f:
         if search in line:
             data = line
             break
     link = data.split(' ')[-1].split('=')[-1].replace('"','').replace('>','').replace('\n','')
     #print(link)
     ref = url
     url = link
     r = requests.get(url, headers = {'Referer' : ref})
     w = open('tmp.txt','w',encoding = 'utf-8')
     w.write(r.text)
     w.close()
     f = open('tmp.txt','r',encoding = 'utf-8')
     search = "setup'.split("
     for line in f:
         if search in line:
             data = line
     data = data.split('|||||')[-1]
     data = data.split('|')
     data = data[-14:][:11]
     url = 'https://' + data[-1] + '.' + data[-2] + '.com:443/' + data[-3] + '/' + data[-4] + ',' + data[-5] + ',' + data[-6] + ',.urlset/master.m3u8?xxx=123'
     #print(url)
     #url = 'https://www7.sbvideocdn.com:443/hls/tysxfsji4s66j6cdabnbxs2wf445becr2pteqyayt,6h4oppmgm7kop37lijq,em4mppmgm7ja2cdi5ra,.urlset/master.m3u8?xxx=123'
     headers = {'Referer' : link}
     r = requests.get(url, headers = headers)
     print(r)
     w = open('tmp.txt','w',encoding = 'utf-8')
     w.write(r.text)
     w.close()
     f = open('tmp.txt','r',encoding = 'utf-8').readlines()
     for line in f:
         if "#EXT-X-I-" in line:
             if 'http' in line:
              data = line.split(',')[1::2]
             print(data[0].replace('=',' : '))
             print('Video Link : ' + data[1].split('=')[-1])
     

def cloud9(url):
    #extracting link for cloud9
    ref = url
    r = requests.get(url)
    w = open('tmp.txt','w',encoding = 'utf-8')
    w.write(r.text)
    w.close()
    f = open('tmp.txt','r',encoding = 'utf-8')
    search = 'https://cloud9'
    for line in f:
        if search in line:
            data = line
            break        
    
    data = data.split(' ')
    for i in data:
        if 'https' in i:
            link = i
            break
        
    link = link.split('=')[-1].replace('"','').replace('\n','').replace('>','')
    url = link
    # sending requset for the link
    file = 'tmp.txt'
    url = "https://api.cloud9.to:443/stream/" + url.split('/')[-1]
    print(url)
    headers = {
    "Origin": "https://cloud9.to", 
    "Cookie": "_ga=GA1.2.206068324.1608459476; _gid=GA1.2.1383895840.1608459476; _gat=1", 
    "Accept": "application/json", 
    "User-Agent": "Mozilla/5.0 (X11; Linux aarch64; rv:78.0) Gecko/20100101 Firefox/78.0", 
    "Connection": "close", 
    "Host": "api.cloud9.to", 
    "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "en-US,en;q=0.5", 
    "Content-Type": "application/json"
    }
    r = requests.get(url,headers = headers)
    print(r)
    w = open(file,'w',encoding = 'utf-8')
    w.write(r.text)
    w.close()
    f = open(file,'r',encoding = 'utf-8')   
    data = json.load(f)
    try:
        for i in range(0,len(data['data']['sources'])):
            print('Resolution : ' + data['data']['sources'][i]['resolution'])
            print("Video Link : " + data['data']['sources'][i]['file'])
    except:
        print('link Not Found... try Another Server')
        
def gogo(url):
    r = requests.get(url)
    w = open('tmp.txt','w',encoding = 'utf-8')
    w.write(r.text)
    w.close()
    f = open('tmp.txt','r',encoding = 'utf-8')
    req = 'https://'
    search = '</i>Gogo server<span>'
    for line in f:
        if search in line:
            data = line
            break
    data = data.split(' ')
    for i in data:
        if 'gogo-play' in i:
            link = i
            break
    link = link.replace('data-video=','https:').replace('"','')
    url = link
    search = 'sources:[{file: '
    r = requests.get(url)
    file = 'tmp.txt'
    w = open('tmp.txt','w',encoding = 'utf-8')
    w.write(r.text)
    w.close()
    f = open('tmp.txt','r',encoding = 'utf-8').readlines()
    for line in f:
        if search in line:
           if 'https://www' in line:
               data = line
               break
               
    data = data.split(' ')
    for i in data:
        if 'https://' in i:
            print('Video Link : ' + i.split(',')[0].replace("'",''))
            break


