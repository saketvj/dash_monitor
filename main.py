# In this I need to create decorators.
import logging.config
import time
import logging
import os
import csv

logger = logging.getLogger(__name__)
logging.basicConfig(encoding='utf-8', level=logging.INFO)


def monitor(
        start_time = True,end_time = True,execution_time = False,retry = {"attempts" :3,"backoff" : 1,"delay" : 2,"callback_func" : None}):
    def wrapper_outer(func_to_be_decorated):
        state = {
            'start_time' : None,
            'end_time' : None,
            'execution_time' : None,
        }

        csv_file = "report.csv"
        columns = ["Start Time", "End Time", "Execution Time"]

        if not os.path.exists("report.csv"):
            print("Yes")
            with open(csv_file, mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=columns)
                writer.writeheader() 

        # logger function to log into csv file

        def log_to_csv( state):
            with open(csv_file, mode="a", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=columns)
                writer.writerow({
                    "Start Time" : state['start_time'],
                    "End Time" : state['end_time'],
                    "Execution Time" : state['execution_time'],
                })

        # 1
        def log_start_time():
            state['start_time']  =time.time()

        # 2    
        def log_end_time():
            state['end_time'] = time.time()

        # 3
        def log_execution_time():
            state['execution_time'] = state['end_time']-state['start_time']

        # 4
        # function to retry with bacoff.
        def retry_with_backoff_func(options = {"attempts" :3,"backoff" : 1,"delay" : 2,"callback_func" : None}):
            
            def wrapper1(func_to_be_decorated):
                def wrapper2(*args,**kwargs):
                
                    # inital waittime equals the delay provided by the user.
                    waittime = options["delay"]

                    for attempt in range(0, options["attempts"]):

                        try:
                            logger.info(f"attempt no. =  {attempt}" )
                            logger.info(f"wait time = {waittime}")
                            return func_to_be_decorated(*args, **kwargs)
                        
                        except Exception as e:
                            logger.error(e)
                            time.sleep(waittime)
                            waittime = options["backoff"]*waittime
                            if attempt < options["attempts"]-1:
                                continue
                            logger.critical(f"Final error is:{e}")

                            #if callback func present then call it!!! 
                            if options["callback_func"]:
                                return options["callback_func"](*args,**kwargs)
                            
                            raise e
                return wrapper2
            return wrapper1



        # innermost wrapper
        def wrapper_inner(*args,**kwargs):

            if(start_time ):
                log_start_time()

            # the main function is executed here.
            if not retry:
                main_ans = func_to_be_decorated(*args,**kwargs)
            else:
                new_func=retry_with_backoff_func(retry)(func_to_be_decorated)
                main_ans = new_func(*args,**kwargs)

        
            if(end_time):
                log_end_time()

        
            if(execution_time):
                log_execution_time()

            # logging the details

            log_to_csv(state)

            # logger.info(f"start time and end time is {state['start_time']},{state['end_time']}, and execution_time is {state['execution_time']}")

            return main_ans
        return wrapper_inner
    return wrapper_outer


def add(a,b):
    return "Callback function has been called.."

options = {"attempts" :5,"backoff" : 1.2,"delay" : 2,"callback_func" : add}

@monitor(start_time=True,retry = options)
def foo(a,b):
    return a/b

print(foo(3,0))