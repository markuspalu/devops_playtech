from re import L
import sys
import psutil

if sys.argv[1] == "cpu":

    print("CPU")
    print("---")
    print("cores")
    print("------")
    print(psutil.cpu_count())
    print("-\n")
    print("load average")
    print("------------")
    print("1\t 5\t 15\t")
    print("\n----\t----\t----\n")

    getloadavglist = psutil.getloadavg()

    print('\t'.join(str(x) for x in getloadavglist)) # remove commas and parenthesis
    print("\ntimes")
    print("\n-----")
    print("    user     nice     system   idle   iowait   irq   softirq   steal   guest   guest_nice")
    print("-- -------- -------- -------- ------ -------- ----- --------- ------- ------- ------------")

    for i in range(4):
        print(i, end=" ")
        for v in psutil.cpu_times(): # command is supposed to print 10 values as said in the documentation but this prints 5 values for me for some reason
            print(round(v, 2), end=" ")
        print('\n')

    print("utilization\n----------")
    print(" 0    1    2    3")
    print("---- ---- ---- ----")

    for i in range(4):
        print(psutil.cpu_percent(interval=1), end=" ")


if sys.argv[1] == "mem": 

    print("MEMORY\n")
    print("------\n\n")
    print("virtual memory\n")
    print("---------------\n")
    print("-------- -------\n")

    vmemory = psutil.virtual_memory() # command is supposed to print 11 values as said in the documentation but this prints 5 values for me for some reason

    print("available",vmemory[0])
    print("percent\t",vmemory[1])
    print("used\t",vmemory[2])
    print("active\t",vmemory[3])
    print("inactive",vmemory[4])
    # would add lines below if psutil.virtual_memory() displayed all values for me
    # print("buffers\t",vmemory[5])
    # print("cached\t",vmemory[6])
    # print("shared\t",vmemory[7])
    # print("slab\t",vmemory[8])
    print("-------- -------\n\n")
    print("swap\n")
    print("------- ------------")

    swapmemory = psutil.swap_memory()
    
    print("total\t",swapmemory[0])
    print("used\t",swapmemory[1])
    print("free\t",swapmemory[2])
    print("percent\t",swapmemory[3])
    print("sin\t",swapmemory[4])
    print("sout\t", swapmemory[5])
    print("------- ------------")



