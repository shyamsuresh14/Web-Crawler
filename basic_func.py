import os
import shutil
import urllib
import spider

def create_crawler_dir(directory):
    if not os.path.exists(directory):
        print('\nCreating directory ' + directory + '..........')
        os.makedirs(directory)
    else:
        with open(spider.Spider.waiting_list_file,'r') as f:
            base_url = f.readline().split()[1]
        if base_url != spider.Spider.base_url:
            shutil.rmtree(directory)
            create_crawler_dir(directory)
    '''else:
        crawlers = file_to_set('crawlers.txt')
        flag = 0
        for crawler in crawlers.copy():
            if crawler == spider.Spider.base_url:
                flag = 1
                break
        if flag == 0:
            create_crawler_dir(directory + '-2') #+ str(NO_OF_CRAWLING_PROJECTS))  
            spider.Spider.project = directory + '-2' #+ str(NO_OF_CRAWLING_PROJECTS)    
            spider.Spider.waiting_list_file = directory + '/waiting_list.txt'
            spider.Spider.crawled_file = directory + '/crawled.txt'
    '''

#create_crawler_dir('thisisus')
def write_file(file,data):
    f = open(file,'w')
    f.write(data + '\n')
    f.close()

def create_storage_file(project, base_url):
    waiting_list = project + '/waiting_list.txt'               #queue file
    crawled = project + '/crawled.txt'                         #crawled file
    if not os.path.isfile(waiting_list):
        write_file(waiting_list, 'Base_url: ' + base_url + '\n' + base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')    

#create_storage_file('test','www.google.com')    
def append_file(file,data):
    with open(file,'a') as f:
        f.write(data +'\n')

def clear_file(file):
    with open(file,'w'):
        pass

def file_to_set(file):
    links = set()
    with open(file,'r') as f:
        f.readline()
        for line in f:
            url = (line.replace('\n',''))
            #links.add(line[:len(line)-1])           #removing the newline character
            if url != '':
                links.add(url)              
    return links

def save_data(links,file):                        #set_to_file function
    with open(file,'w') as f:
        f.write('Base_url: ' + spider.Spider.base_url + '\n')
        for line in links.copy():
            f.write(line+'\n')

def check_internet_connection():
    try:
        urllib.request.urlopen('http://www.vit.ac.in/')
        return True
    except:
        print('\nPlease check your internet connection!!!')
        return False    
                

#create_storage_file('test','www.google.com')
#print(file_to_set('testqueue.txt'))
#save_data(file_to_set('testqueue.txt'),'testcrawled.txt')


