import sys
import time
import signal
import datetime
import threading
from pythonTimer import PyTimer


def test_handler_0():
  """ no argument """
  print "\ntest_handler_0 :", "there is no argument"

def test_handler_1(firstname): 
  """ take only one positional argument """
  print "\ntest_handler_1 :", "hello", firstname

def test_handler_2(firstname, lastname):
  """ take two positional arguments """
  print "\ntest_handler_2 :", "hello", firstname, lastname

def test_handler_3(firstname="foo"):
  """ take only one keyword argument """
  print "\ntest_handler_3 :", "hello", firstname

def test_handler_4(firstname="foo", lastname="bar"):
  """ take two keyword arguments """
  print "\ntest_handler_4 :", "hello", firstname, lastname

def test_handler_5(firstname, lastname="bar"):
  """ take one positional argument and one keyword argument """
  print "\ntest_handler_5 :", "hello", firstname, lastname

def test_handler_6(firstname, lastname, city="foo", state="bar"):
  """ take two positional arguments and two keyword arguments """
  print "\ntest_handler_6 :", "hello", firstname, lastname, "from", city, state


def timer_factory(): 
  """ This is a generator to generate timers """
  for ind in range(7): 
    if ind == 0: 
      timer = PyTimer(0.5, test_handler_0)
    elif ind == 1: 
      timer = PyTimer(0.5, test_handler_1, args=["Terry"])
    elif ind == 2: 
      timer = PyTimer(0.5, test_handler_2, args=["Terry", "Tang"])
    elif ind == 3: 
      timer = PyTimer(0.5, test_handler_3, kwargs={"firstname":"Terry"})
    elif ind == 4: 
      timer = PyTimer(0.5, test_handler_4, kwargs={"firstname":"Terry", "lastname":"Tang"})
    elif ind == 5: 
      timer = PyTimer(0.5, test_handler_5, args=["Terry"], kwargs={"lastname":"Tang"})
    elif ind == 6: 
      timer = PyTimer(0.5, test_handler_6, args=["Terry", "Tang"], kwargs={"city":"Houston", "state":"Texas"})
    timer.start()
    yield(timer)

def test_pass_arguments(): 
  """ This test function test different methods to pass arguments into PyTimer handler """

  print ">>>>>>>>>>>>>>>>>>> test passing arguments to timer handler <<<<<<<<<<<<<<<<<<<<"
  for temp_timer in timer_factory(): 
    def timer_killer(signum, frame):
      # Refer to: https://docs.python.org/2/library/signal.html
      # can only pass variables to signal.signal as globals?! nasty! Here we use closure to change timer obj 
      # http://stackoverflow.com/questions/12371361/using-variables-in-signal-handler-require-global
      temp_timer.cancel()
      print " \n ------------------ timer terminated -------------------- \n"

    signal.signal(signal.SIGALRM, timer_killer)
    signal.setitimer(signal.ITIMER_REAL, 3)

    time.sleep(4)

def verify_timer_interval(): 
  """ This test function verifies the interval between two consecutive invocations """
  global last_stamp
  last_stamp = datetime.datetime.now()
  
  print ">>>>>>>>>>>>>>>>>>> verifies timer interval <<<<<<<<<<<<<<<<<<<<"
  def check_interval():
      global last_stamp
      delta = (datetime.datetime.now() - last_stamp)
      print "Delay since last call: ", delta.total_seconds() * 1000  # milliseconds
      last_stamp = datetime.datetime.now()

  timer = PyTimer(1, check_interval)
  timer.start()


if __name__ == '__main__':
  # Global timestamp for testing
  global last_stamp
  test_pass_arguments()
  verify_timer_interval()


