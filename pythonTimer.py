from threading import Timer

class PyTimer():
    """Python equivalent of JavaScript setInterval function 
       Call a function after a specified number of seconds:

            timer = pythonTimer(5.0, handler_func, args=[], kwargs={})
            timer.start()
            timer.cancel()     # stop the timer's action if it's still waiting

        Ref: https://hg.python.org/cpython/file/2.7/Lib/threading.py
    """
    def __init__(self, interval, timer_handler, args=[], kwargs={}):
        # timer interval, set integer or decimal for seconds or milliseconds
        self.interval = interval
        # real timer handler function
        self.timer_handler = timer_handler
        # positional arguments 
        self.args = args
        # keyword arguments 
        self.kwargs = kwargs
        # create an internal timer object of threading.Timer
        self.timer = Timer(self.interval, self.wrapper_handler, args=self.args, kwargs=self.kwargs)

    def wrapper_handler(self, *args, **kwargs):
        # actually call the timer handler, the timer thread will be destroyed after handler function execution 
        self.timer_handler(*args, **kwargs)
        # create a new timer thread to continue calling wrapper_handler
        self.timer = Timer(self.interval, self.wrapper_handler, args=args, kwargs=kwargs)
        # start the new timer thread, wait 'interval' amount of time and execute timer_hander again 
        self.timer.start()

    def start(self):
        self.timer.start()

    def cancel(self):
        self.timer.cancel()





