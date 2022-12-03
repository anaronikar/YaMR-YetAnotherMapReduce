# YaMR-YetAnotherMapReduce
Implementation of the core components of Hadoop's Map Reduce Framework.

## OBJECTIVES
- MapReduce jobs are made to execute parallely across multiple nodes.
- Setting up a multi-node configuration that can store input data across multiple nodes and run Map and Reduce jobs.

## FRAMEWORK USED
This project mainly runs on the 'Flask' framework. It could however be built using socket programming or threading, as well.

## IMPLEMENTATION
The project consists of 3 code files, namely:
1. master.py
2. client.py
3. worker.py

### MASTER NODE
This project utilizes port number 8000 to run the master node file. The port number can be changed, as per the user's preference.
<br>
The master node is said to contain the number of worker nodes as specified by the user. It also maintains the metadata containing the worker nodes, including the port numbers in which they are being run.

### CLIENT NODE
This is said to perform Read, Write and MapReduce operations.
<br>
The input file data will be partitioned and thereby scheduled to different worker nodes. This partitioning is done by making use of <i>numpy.array.split()</i>, and the joining of outputs from all nodes is done by using the join function.

### WORKER NODE
Each worker node is said to start at port number 8001(this is hard-coded), and every consecutive worker node's(as many required by the user) port number is said to increment by 1. For example, worker node-1 works on port-8001, worker node-2 works on port-8002, worker node-3 works on port-8003 and so on.
<br>
This file is said to run all the functions that are specified in <i>client.py</i>. The mapper function takes input from the mapper file, of the file inputted and then writes the output to a file called <i>mapout</i>. The reducer function takes input from the reducer file and thus returns the output to a file called <i>redout</i>.

## RUNNING THE CODE
```pip install Flask``` <br>
```Input file name is assigned to input variable in the client file.``` <br>
```Mapper file name is assigned to the mapper variable in the client file.``` <br>
```Reducer file name is assigned to the reducer variable in the client file.``` <br>
```Run the Client file, Master file and then the Worker file respectively, on 3 different terminals, to obtain the outputs.```

---

### CONTRIBUTORS (Team Members)
1. Apoorva Naronikar
2. Amisha Mathew
3. Ananya Adiga
