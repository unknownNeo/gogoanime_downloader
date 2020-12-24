import gogoanime
import requests
from html2text import html2text
from glob import glob

def episode():
    url = str(input('Enter the url : '))
    
    if '-episode' in url:
        anime = url.split('/')[-1].split('-episode')[0]
    else:
        anime = url.split('/')[-1]
    print(anime)
    url = 'https://gogoanime.so/category/' + anime 
    r = requests.get(url)
    file = 'tmp.txt'
    w = open(file,'w',encoding = 'utf-8')
    w.write(r.text)
    w.close()
    f = open(file,'r').readlines()
    for line in f:
        if 'ep_end =' in line:
            data = line
            break
    data = html2text(data).replace('\n','')
    print('Total Episode : ' + data.split('-')[-1])
    w = open(anime + '.txt','w',encoding = 'utf-8')
    for i in range(1,int(data.split('-')[-1]) + 1):
        w.write('https://gogoanime.so/' + anime + '-episode-' + str(i))
        w.write('\n')
    w.close()    
    return select(anime)
    

def select(anime):
    f = open(anime + '.txt', 'r', encoding = 'utf-8').readlines()
    for i in range(0,len(f)):
        print('Ep. No. : ' + str(i + 1) + ' || ' + f[i])
    print('Total episodes are : ' + str(len(f)))
    num = int(input('Select Episode number : '))
    if num > len(f) + 1 or num < 1:
        print("[!] Enter From above list....")
        return 0
    
    ep = f[num - 1]
    return ep

def priv():
    lists = glob('*.txt')
    lists.remove('tmp.txt')
    if len(lists) == 0:
        print('No anime List found')
        return 0    
        
    for i in range(0,len(lists)):
        print(str(i + 1) + ' || ' + lists[i].replace('.txt',''))
    while True:
        num = int(input('Select the anime : '))
        if num > len(lists) + 1 or num < 0:
            print("[!] Enter Only Number Avilable in List...")
        else:
            file = lists[num - 1]
            break
    f = open(file,'r', encoding = 'utf-8').readlines()
    total = len(f)
    for i in range(0,len(f)):
        print("Ep no. " + str(total - (1 + i) + 1) + " : " + f[i])
    print('Total Episodes are : ' + str(total))
    num = input('Enter the episode number : ')
    ep = f[int(num) - 1]
    return ep

'''
try:
    num = input(' 1 || Check Priv. Anime Lists\n 2 || Enter Url\n : ')
    int(num)
    if int(num) > 2 or int(num) < 1:
        print('[!]Enter From The above options...')
    elif int(num) == 1:
        url = priv()
        if url != 0:
            servers(url)
    elif int(num) == 2:
        url = episode()
        if url != 0:
            servers(url)

except:
    print('Enter only Number.... ')        
'''

def menu():
    num = input(' 1 || Check Priv. Anime Lists\n 2 || Enter Url\n : ')
    int(num)
    if int(num) > 2 or int(num) < 1:
        print('[!]Enter From The above options...')
    elif int(num) == 1:
        url = priv()
        if url != 0:
            servers(url)
    elif int(num) == 2:
        url = episode()
        if url != 0:
            servers(url)
            
def servers(url):
    print(' 1 || Default-server\n 2 || gogo-server\n 3 || cloud9\n 4 || streamsb')
    while True:
        server = str(input('Enter the server number : '))
        if server == '1':
            gogoanime.default(url)
            break
        if server == '2':
            gogoanime.gogo(url)
            break
        if server == '3':
            gogoanime.cloud9(url)
            break
        if server == '4':
            gogoanime.streamsb(url)
            break
        else:
            print('Enter only From options')
            
menu()