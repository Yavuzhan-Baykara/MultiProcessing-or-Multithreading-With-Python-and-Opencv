# MultiProcessing-or-Multithreading-With-Python-and-Opencv

## Contents

- [Multiprocessing] <img align="left" alt="Facebook" width="22px" src="https://cdn-icons-png.flaticon.com/512/5197/5197000.png" />
</a> 

- [Threading] <img align="left" alt="Facebook" width="22px" src="https://cdn-icons-png.flaticon.com/512/222/222231.png" />
</a> 

- [MultiThreading] <img align="left" alt="Facebook" width="22px" src="https://cdn-icons-png.flaticon.com/512/3005/3005805.png" />
</a> 

- [MultiProcessing vs MultiThreading](#multiprocessing-vs-multithreading) <img align="left" alt="Facebook" width="22px" src="https://cdn-icons-png.flaticon.com/512/6329/6329016.png" />
</a> 

- Performance measurement using opencv. <img align="left" alt="Facebook" width="22px" src="https://cdn-icons-png.flaticon.com/512/711/711284.png" />
</a>


[Multiprocessing]: https://github.com/Yavuzhan-Baykara/MultiProcessing-or-Multithreading-With-Python-and-Opencv/tree/main/multiprocessing%20and%20worker

[Threading]: https://github.com/Yavuzhan-Baykara/MultiProcessing-or-Multithreading-With-Python-and-Opencv/tree/main/Thread

[MultiThreading]: https://github.com/Yavuzhan-Baykara/MultiProcessing-or-Multithreading-With-Python-and-Opencv/tree/main/multithreading

[Performance]: None

<br>



## MultiProcessing vs MultiThreading
It is explained in a simple way; a single process runs each thread. It refers to the ability to execute multiple threads simultaneously.
Multiprocessing refers to the ability of a system to run multiple processors at the same time. Each processor can run one or more threads.

<img align="centreal" src="https://res.cloudinary.com/practicaldev/image/fetch/s--XmfUXLmh--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/b9a62hzkm6gjaxff5e9g.PNG"> <br/>


From the diagram above, we can see that in multithreading (right diagram) multiple threads share the same code, data and files, but work on a different register and stack.
However, as seen in the diagram on the left side, we can see that it runs data and files on a single stack.

<img align="centreal" src="https://miro.medium.com/max/828/1*QiaqQ0HLT4Iy0N608A5mVA.png"> <br/>
