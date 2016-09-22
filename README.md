# pythonTimer
Python Timer. Equivalent of JavaScript setInterval/setTimeout function.

- Call a function after a specified number of seconds:

    e.g.:
    timer = pythonTimer.PyTimer(5.0, handler_func, args=[], kwargs={})
    timer.start()
    timer.cancel()     # stop the timer's action if it's still waiting

- Timer handler take positional arguments and keyword arguments: 

    e.g.: 
    timer = pythonTimer.PyTimer(0.5, timer_handler, args=["Terry", "Tang"], kwargs={"city":"Houston", "state":"Texas"})

- Test cases included. 
