from threading import Timer

class PyTimer():
    """Python equivalent of JavaScript setInterval function 
       Call a function after a specified number of seconds:

            timer = pythonTimer.PyTimer(5.0, handler_func, args=[], kwargs={})
            timer.start()
            timer.stop()     # stop the timer's action if it's still waiting

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
        self.timer = self.create_timer()
        # timer controls 
        self.has_call_limit = False
        self.logger = None 
        self.running = False

    def create_timer(self):
        return threadingTimer(self.interval, self.wrapper_handler, args=self.args, kwargs=self.kwargs)
    
    def set_logger(self, logger, args=[], kwargs={}):
        """ This function sets a logger function for the timer, which will be called everytime after
            timer handler is called.  
        """
        self.logger = logger
        self.logger_args = args
        self.logger_kwargs = kwargs

    def set_call_limits(self, num): 
        """ This function sets timer counter as well as its uplimit number """
        self.has_call_limit = True
        self.call_limits = num 
        self.count = 0 

    def wrapper_handler(self, *args, **kwargs):
        if self.has_call_limit and self.count >= self.call_limits: 
            return
        # actually call the timer handler, the timer thread will be destroyed after handler function execution 
        self.timer_handler(*args, **kwargs)
        if self.has_call_limit: self.count += 1
        # call logger function 
        if self.logger:
            self.logger(*self.logger_args, **self.logger_kwargs)
        # create a new timer thread to continue calling wrapper_handler
        self.timer = self.create_timer()
        # start the new timer thread, wait 'interval' amount of time and execute timer_hander again 
        self.timer.start()

    def start(self):
        self.running = True
        # create a new internal timer object of threading.Timer. 
        self.timer = self.create_timer()
        self.timer.start()

    def stop(self):
        self.running = False
        self.timer.cancel()
        # The cancel function only prevents timer being called but the thread might still be active, so make 
        # sure you call join() to end the thread
        self.timer.join() 
        # Reset logger and call limit 
        self.has_call_limit = False
        self.set_logger(None)

    def is_running(self):
        return self.running


