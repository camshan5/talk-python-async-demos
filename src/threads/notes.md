##  Notes: Hello Threads

[Talk Python Async Course- Chapter 5](https://training.talkpython.fm/player/course/async-in-python-with-threading-and-multiprocessing/lecture/180504)


#### Misc. Notes: 

* By default Threads in Python are 'Foreground Threads', 
  If any of those are running, even if your main thread 
  that started your program stops or exits, it's going to 
  keep on running.
  
* Good technique, you want to spin up a bunch of threads.
  You want to start them, do the work potentially and wait on them.
  You can use a list and list comprehensions to make this a 
  lot cleaner in Python.
