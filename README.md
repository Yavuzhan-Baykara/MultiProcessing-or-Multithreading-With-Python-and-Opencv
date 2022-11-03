# MultiProcessing-or-Multithreading-With-Python-and-Opencv

## Contents

- [Threading] <img align="left" alt="Facebook" width="22px" src="https://cdn-icons-png.flaticon.com/512/222/222231.png" />
</a> 

- [Multiprocessing] <img align="left" alt="Facebook" width="22px" src="https://cdn-icons-png.flaticon.com/512/5197/5197000.png" />
</a> 

- [MultiThreading] <img align="left" alt="Facebook" width="22px" src="https://cdn-icons-png.flaticon.com/512/3005/3005805.png" />
</a> 

- [MultiProcessing vs MultiThreading](#multiprocessing-vs-multithreading) <img align="left" alt="Facebook" width="22px" src="https://cdn-icons-png.flaticon.com/512/6329/6329016.png" />
</a> 

- [When to](#when-to) <img align="left" width="22px" src="https://cdn-icons-png.flaticon.com/512/3106/3106703.png">

- [When not to](#when-not-to) <img align="left" width="22px" src= "https://cdn-icons-png.flaticon.com/512/2169/2169949.png">

- [Performance measurement using opencv](#performance-measurement-using-opencv) <img align="left" alt="Facebook" width="22px" src="https://cdn-icons-png.flaticon.com/512/711/711284.png" />
</a>


[Multiprocessing]: https://github.com/Yavuzhan-Baykara/MultiProcessing-or-Multithreading-With-Python-and-Opencv/tree/main/multiprocessing%20and%20worker

[Threading]: https://github.com/Yavuzhan-Baykara/MultiProcessing-or-Multithreading-With-Python-and-Opencv/tree/main/Thread

[MultiThreading]: https://github.com/Yavuzhan-Baykara/MultiProcessing-or-Multithreading-With-Python-and-Opencv/tree/main/multithreading

[Performance]: None

<br>



## MultiProcessing vs MultiThreading


It is explained in a simple way; a single process runs each thread. It refers to the ability to execute multiple threads simultaneously.


<br/>

<img align="centreal" src="https://res.cloudinary.com/practicaldev/image/fetch/s--XmfUXLmh--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/b9a62hzkm6gjaxff5e9g.PNG">

<br/>

From the diagram above, we can see that in multithreading (right diagram) multiple threads share the same code, data and files, but work on a different register and stack.
However, as seen in the diagram on the left side, we can see that it runs data and files on a single stack.


<br/>


<img align="centreal" src="https://miro.medium.com/max/828/1*QiaqQ0HLT4Iy0N608A5mVA.png"> <br/>

Multiprocessing refers to the ability of a system to run multiple processors at the same time. Each processor can run one or more threads.


## When To

- Multithreading is useful when a thread is awaiting a response from another computer or piece of hardware. While one thread is blocked while performing the task, other threads can take advantage of the otherwise unburdened computer.
- By running time-consuming tasks on a parallel “worker” thread, the main UI thread is free to continue processing keyboard and mouse events.
- Code that performs intensive calculations can execute faster on multicore or multiprocessor computers if the workload is shared among multiple threads in a “divide-and-conquer” strategy
- Multithreading is useful for Io-dependent operations such as reading and writing files from a database. Because each thread can run the Io-bound process at the same time. For systems that will have more than one processor, multiprocessing will be of great benefit. It requires multi-core systems in CPU-dependent processes. At the same time, the importance of CPU speed will directly affect the processing size.
- Multiprocessing allows the same job to be done in a shorter time.
- Multiprocessing means more processing capacity because there are more processes.

## When not To

- Threading requires a resource and CPU cost in scheduling and swapping threads (when there are more active threads than CPU cores) and there is also a creation/tearing cost. Multithreading does not always speed up your application; it can even slow it down when used excessively or inappropriately. For example, when it comes to heavy disk I/O, having several worker threads running tasks sequentially can be faster than executing 10 threads at the same time. (In Wait and Pulse Signaling, we describe how to implement a producer/consumer queue that provides just this functionality.)

- When the process is executed, high data will transfer its operations to the next iteration in the event that it cannot complete its operations in each iteration. This situation is called a bottleneck.

## Performance Measurement Using Opencv
