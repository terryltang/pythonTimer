# pythonTimer
Python Timer. Equivalent of JavaScript setInterval/setTimeout function.

- Require Python standard library: threading 

- Call a function after a specified number of seconds:

    e.g.:
    timer = pythonTimer.PyTimer(5.0, handler_func, args=[], kwargs={})
    timer.start()
    timer.stop()     # stop the timer's action if it's still waiting

- Timer handler take positional arguments and keyword arguments: 

    e.g.: 
    timer = pythonTimer.PyTimer(0.5, timer_handler, args=["Terry", "Tang"], kwargs={"city":"Houston", "state":"Texas"})

- Stop and Resume timer. 

- Add a customized logger function for timer handler.

- Test cases included. 
