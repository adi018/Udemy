import time
from workers.WikiWorker import WikiWorker
from workers.YahooFinanceWorkers import YahooFinancepriceScheduler

from multiprocessing import Queue

def main():
    scraper_start_time = time.time()
    symbol_queue = Queue()

    wikiWorker = WikiWorker()

    yahoo_finance_price_scheduler_threads = []

    # Number of workers that consumes from the Queue i.e. symbol_queue whenever we put something in the queue
    num_yahoo_finance_price_scheduler_workers = 4
    for i in range(num_yahoo_finance_price_scheduler_workers):
        # Although we initialise our threading worker here, but it would wait in class YahooFinancepriceScheduler()
        # at line "val = self._input_queue.get()" to get a value which happens in "symbol_queue.put(symbol)"
        yahooFinancepriceScheduler = YahooFinancepriceScheduler(input_queue=symbol_queue)
        yahoo_finance_price_scheduler_threads.append(yahooFinancepriceScheduler)
    # end

    for symbol in wikiWorker.get_sp_500_companies():
        symbol_queue.put(symbol)
    # end

    # For every instance of queued threads, we put one "DONE" as we want
    # every instance of the queued thread to break
    for i in range(len(yahoo_finance_price_scheduler_threads)):
        symbol_queue.put("DONE")
    # end

    for i in range(len(yahoo_finance_price_scheduler_threads)):
        yahoo_finance_price_scheduler_threads[i].join()
    # end


    print("Extracting time took: ", round(time.time() - scraper_start_time, 1))



if __name__=="__main__":
    main()
