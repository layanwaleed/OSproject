#OS Project Spring 2020/2021 
#by Rahaf Al Abed 20180254 & Layan Waleed 20180193

def PR(proc, n):
    queue = []
    start = [0] * n
    end = [0] * n
    wait = [0] * n
    response = [0] * n
    turn = [0] * n
    seq = []
    time = 0
    Finish = False
    p = proc.copy()

    while Finish == False:

        for i in range(n):
            if p[i][1] != -1:
                if p[i][0] <= time:
                    queue.append(p[i])

        while len(queue) == 0:
            time+=1
            for i in range(n):
                if p[i][1] != -1:
                    if p[i][0] <= time:
                        queue.append(p[i])

        queue = sorted(queue, key = lambda x:x[2])    

        while len(queue) != 0: 
            process = queue[0]

            start[process[3]] = time
            wait[process[3]] = start[process[3]] - process[0]
            time += process[1]
            end[process[3]] = time
            response[process[3]] = start[process[3]] - process[0]
            turn[process[3]] = end[process[3]] - process[0]

            seq.append("P" + str(process[3]))
            p[process[3]][1] = -1    
            queue.pop(0)

            for j in range(n):
                if (p[j][1] != -1) and (p[j] not in queue):
                    if p[j][0] <= time:
                        queue.append(p[j])
            queue = sorted(queue, key = lambda x:x[2]) 

        Finish = True
        for i in range(n):
            if p[i][1] != -1:
                Finish == False
    
    print("Safe State Sequence: " + str(seq))
    print("\n")
    print("Waiting times: " + str(wait))
    avgwait=sum(wait)/n
    print("Average Waiting time: " + str(avgwait))
    print("\n")
    print("Start times: " + str(start))
    print("End times: " + str(end))
    print("\n")
    print("Response times: " + str(response))
    avgresponse=sum(response)/n
    print("Average Response time: " + str(avgresponse))
    print("\n")
    print("Turnaround times: " + str(turn))
    avgturna=sum(turn)/n
    print("Average Turnaround time: " + str(avgturna))
    print("\n")
    print("Total time: " + str(time))
    print("\n")
    throughput = n/time
    print("Throughput: " + str(throughput) + " seconds")



def priority():
    n = int(input("Enter number of processes: "))

    arrival = [0] * n
    burst = [0] * n
    priority = [0] * n

    rows, cols = (n, 4)
    proc = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(n):
        arrival[i] = int(input("Enter arrival for P" + str(i) + ": "))
        burst[i] = int(input("Enter burst for P" + str(i) + ": "))
        priority[i] = int(input("Enter priority for P" + str(i) + ": "))
        print("\n")

        proc[i][0] = arrival[i]
        proc[i][1] = burst[i]
        proc[i][2] = priority[i]
        proc[i][3] = i

    print("Processes: " + str(proc))
    print("\n")

    PR(proc, n)
    
def roundrobin():
    print("")
    quantum=input("Please enter the quantum number : ")
    print("")
    num_of_proc=input("Please enter the number of processes : ")
    print("")
    arrival_list=[]
    burst_list=[]
    remaining_burst_time=[]
    waiting_list=[]
    turnaround_list=[]
    time=0


    for i in range(int(num_of_proc)):
        arrival=input("Please enter the arrival time of process "+ str(i+1)+' : ')
        arrival_list.insert(i,int(arrival))
        print("")

        burst=input("Please enter the burst time of process "+ str(i+1) + ' : ')
        burst_list.insert(i,int(burst))
        print("")

    for i in range(len(burst_list)):
        remaining_burst_time.append(burst_list[i])

    gantt_pro=[]
    gantt_time=[]

    ganttime=0
    while True:
        flag = '1'
        for i in range(int(num_of_proc)):
            if(remaining_burst_time[i]>0):
                flag = '0'
                if(int(arrival_list[i])<=time):
                    if(int(remaining_burst_time[i])>int(quantum)):
                        gantt_pro.append(i+1)
                        gantt_time.append(ganttime)
                        ganttime+=int(quantum)
                        time+=int(quantum)
                        remaining_burst_time[i]=int(remaining_burst_time[i])-int(quantum)
                    else:
                        gantt_pro.append(i+1)
                        gantt_time.append(ganttime)
                        ganttime+=int(remaining_burst_time[i])
                        time+=int(remaining_burst_time[i])
                        x=time-int(burst_list[i])
                        waiting_list.insert(i,x)
                        remaining_burst_time[i]=0
        if (flag == '1'):
            break

    gantt_time.append(ganttime)
    for i in range(int(num_of_proc)):
        turnaround_list.append(int(burst_list[i])+int(waiting_list[i]))
    print("")
    print("The order in which the processes are executed is : ")
    print(gantt_pro)
    print(gantt_time)
    avg_waiting=0
    for i in range(len(waiting_list)):
        avg_waiting+=int(waiting_list[i])

    print("")
    print("the waiting time of each process is : ")
    print(waiting_list)
    print("The average waiting time is : " )
    print(round(avg_waiting/int(num_of_proc),2))

    print("")
    response=0
    for i in range(int(num_of_proc)):
        response+=int(gantt_time[i]-int(arrival_list[i]))
    print("The average response time is : " )
    print(response/int(num_of_proc))

    print("")
    avg_turnaround=0
    for i in range(len(turnaround_list)):
        avg_turnaround+=int(turnaround_list[i])
    print("The average turnaround time is : " )
    print(round(avg_turnaround/int(num_of_proc),2))


    print("")
    tptime=gantt_time[int(len(gantt_time))-1]
    throughput=int(num_of_proc)/int(tptime)

    print("the throughput in seconds is : "+ str(round(throughput,3)) )
    print("")

 
if __name__ =="__main__":
    choice=input("Please choose one of the following scheduling algorithms : \n 1)Round Robin \n 2)Non-Preemtive priorty \n")

    if(choice == '1'):
        roundrobin()
    elif (choice=='2'):
        priority()
    else:
        print("please choose 1 or 2")
