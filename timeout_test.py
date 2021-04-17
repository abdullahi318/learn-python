#!/usr/bin/env python3

from threading import Thread, Event
import time
 
 
# Event object used to send signals from one thread to another
stop_event = Event()


def get_user_details():

    name = input("Enter your name: ")
    age = int(input("How old are you? "))
    dept = input("Which department are you? ")

    if stop_event.is_set():
        stop_event.set()

 
 
def do_something():
    """
    Function that should timeout after 5 seconds. It simply prints a number and waits 1 second.
    :return:
    """
    i = 6
    while i > 0:
        i -= 1
        print(i)
        #get_user_details()
       

        time.sleep(1)
 
        # Here we make the check if the other thread sent a signal to stop execution.
        if stop_event.is_set():
            break
 
 
if __name__ == '__main__':
    # We create another Thread
    action_thread = Thread(target=do_something)
 
    # Here we start the thread and we wait 5 seconds before the code continues to execute.
    action_thread.start()
    action_thread.join(timeout=5)
 
    # We send a signal that the other thread should stop.
    stop_event.set()
 
    print("Timed out!, Please try again")