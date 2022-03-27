This python program can be run by running:
python metrics.py cpu

python metrics.py mem

"python metrics.py cpu" creates a table and prints various CPU metrics.

The "psutil.cpu_times" command is supposed to print 10 values as said in the documentation but this prints 5 values for me which I don't know the reason of.

"python metrics.py mem" creates a table and prints various memory metrics. 

The "psutil.virtual_memory()" command is supposed to print 11 values as said in the documentation but this prints 5 values for me which again I don't know the reason of.

In line 55 if "psutil.virtual.memory()" worked as it is supposed to according to the documentation page, I would add the following lines. For people that get 5 values like me, these lines should be ommitted.

print("active\t",vmemory[5])

print("inactive\t",vmemory[6])

print("buffers\t",vmemory[7])

print("cached\t",vmemory[8])

print("shared\t",vmemory[9])

print("slab\t",vmemory[10])
