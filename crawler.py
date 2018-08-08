import threading
import time
from queue import Queue
from spider import Spider
from domain_getter import get_domain_name
from web_scrapper import web_sc
import basic_func 

def main(BASE_URL, keyword):
    PROJECT_NAME = 'web_crawler'
    WAITING_LIST = PROJECT_NAME + '/waiting_list.txt'
    CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
    NO_OF_THREADS = 8

    def create_crawlers():
        for _ in range(NO_OF_THREADS):
            t = threading.Thread(target=work)    #creating a thread 
            t.daemon = True                 #to kill the thread when the program ends
            t.start()                       

    def work():    
        while True:
            url = thread_queue.get()              #getting a url from the queue
            Spider.crawl_page(threading.current_thread.__name__, url)
            thread_queue.task_done()            

    def creating_jobs():
        for link in basic_func.file_to_set(WAITING_LIST):
            thread_queue.put(link)
        #avoids bumping of links
        thread_queue.join()                 #to make the thead queue to wait for its next turn
        crawl()

    def crawl():
        waiting_list_links = basic_func.file_to_set(WAITING_LIST)
        if len(waiting_list_links) > 0:
            print(str(len(waiting_list_links)) + ' links in waiting list')
            creating_jobs()

    #BASE_URL = 'http://www.skillrack.com/'
    #BASE_URL = 'http://www.vit.ac.in/'

    #input
    #BASE_URL = input('Enter the url of the page to be crawled: \n')
    DOMAIN_NAME = get_domain_name(BASE_URL)

    start_time = time.time()

    if(basic_func.check_internet_connection()):
        #setting up thread queue
        thread_queue = Queue()

        #creating the first spider
        Spider(PROJECT_NAME, BASE_URL, DOMAIN_NAME)

        #initiating the work
        print('\nNow crawling..............\n')
        create_crawlers()
        crawl()

        #final status after crawling
        Spider.print_status()
        print('\nEnd of crawling!!\n' + '----------------------')

        time_taken = time.time() - start_time
        print('Time taken to crawl: ' + str(time_taken) + ' s' + '\n')

        #print('Enter keyword to be searched: ')
        #keyword = input()

        gathered_links = basic_func.file_to_set(CRAWLED_FILE)

        no_of_pages = 0

        print('\nThe pages in the which the given keyword is found: \n')
        for link in gathered_links:
            if web_sc(link,keyword):
                no_of_pages = no_of_pages + 1

        if no_of_pages:
            print('The given keyword is found in ' + str(no_of_pages) + ' pages')
        else:
            print('The keyword is not found in any page! ')

        print('\nEnd of program!\n' + '-----------------------')                  



