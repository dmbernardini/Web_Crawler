import threading
from queue import Queue
from spider import spider
from domain import *
from general import *

#Constant, if running command line you can enter the txt
project_name = 'thenewboston'
homepage = 'https://thenewboston.com/'
domain_name = get_domain_name(homepage)
queue_file = project_name + '/queue.txt'
crawled_file = project_name + '/crawled.txt'
number_of_threads = 8
queue queue()
spider(project_name, homepage, domain_name)

#Create worker threads (die when main exits)
def create_workers():
    for _ in range(number_of_threads)
        t = threading.thread(target=work)
        t.daemon = True
        t.start()

#Do the next job in the queue
def work():
    while True:
        url = queue.get()
        spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

#Each queued link is a new job
def create_jobs():
    for link in file_to_set(queue_file):
        queue.put(link)
    queue.join()
    crawl()

#Check items in queue, if so crawl them
def crawl():
    queued_links = file_to_set(queue_file)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + 'links in the queue')
        create_jobs()

create_workers()
crawl()

# Code @ https://github.com/buckyroberts/Spider