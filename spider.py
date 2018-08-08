from urllib.request import urlopen
from link_find import link_finder
import basic_func

class Spider:
    #class variables available to all the objects of class (common to all spiders)
    project = ''
    base_url = ''
    domain_name = ''
    waiting_list_file = ''            #files where data is stored 
    crawled_file = ''
    waiting_list = set()              #data storage while crawling(temporary)
    crawled = set()

    def __init__(self, project, base_url, domain):
        #initialises value when the first spider is created
        Spider.project = project
        Spider.base_url = base_url
        Spider.domain_name = domain
        Spider.waiting_list_file = project + '/waiting_list.txt'
        Spider.crawled_file = project + '/crawled.txt'

        #called when each spider is created
        self.boot()
        self.crawl_page('\nFirst spider', Spider.base_url)

    @staticmethod
    def boot():
        basic_func.create_crawler_dir(Spider.project)
        basic_func.create_storage_file(Spider.project, Spider.base_url)
        Spider.waiting_list = basic_func.file_to_set(Spider.waiting_list_file)
        Spider.crawled = basic_func.file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread, page):
        if page not in Spider.crawled:
            print(thread + ' now crawling ' + page)
            Spider.print_status()
            Spider.append_links_to_waiting_list(Spider.get_links(page))
            Spider.waiting_list.remove(page)
            Spider.crawled.add(page)
            Spider.update_files_status()

    @staticmethod
    def print_status():
        print('Waiting list = ' + str(len(Spider.waiting_list))+ ' ', end = '|')
        print(' Crawled = ' + str(len(Spider.crawled)))

    @staticmethod
    def get_links(page_url):
        try:
            response = urlopen(page_url)
            #print(response.getheader('Content-Type'))
            if response.getheader('Content-Type') in ['text/html;charset=UTF-8','text/html; charset=utf-8','text/html']:
                html_in_bytes = response.read()
                html_as_string = html_in_bytes.decode('utf-8')
                linkfinder = link_finder(Spider.base_url, page_url)
                linkfinder.feed(html_as_string)
                return linkfinder.links_in_page()
            
            else:
                #if the url is not a link to another site, but some other file
                #print('error')
                return set()    

        except:
            #SSL Certificate verification failed for the page
            #print('Error: This page cannot be crawled! ')
            error_file = Spider.project + '/error_links'
            if not basic_func.os.path.isfile(error_file):
                basic_func.write_file(error_file,page_url)
            else:
                basic_func.append_file(error_file,page_url)    
            return set()    
            

    @staticmethod
    def append_links_to_waiting_list(links):
        if links != set():
            for link in links.copy():
                if link in Spider.waiting_list or link in Spider.crawled:
                    continue
                elif Spider.domain_name not in link:
                    #to stop crawling pages of a different(unwanted) site       
                    continue     
                else:
                    Spider.waiting_list.add(link)

    @staticmethod
    def update_files_status():
        basic_func.save_data(Spider.waiting_list, Spider.waiting_list_file)
        basic_func.save_data(Spider.crawled, Spider.crawled_file)


