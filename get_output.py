from subprocess import Popen, PIPE
import csv
import time
#p = Popen('bash ./launch_nbody.sh -r 10 -n 10000', shell=True, stdout=PIPE)

file = open('exec_time.csv', 'w')
writer = csv.writer(file)
writer.writerow(['N','Avg Exec Time'])

print ( 'N ; Avg Exec Time')
for n in range(10000, 10000000, 10000) :

    p = Popen('bash ./launch_nbody.sh -r 10 -n '+str(n), shell=True, stdout=PIPE, text=True)

    exec_time_sum = 0
    for line in iter(p.stdout.readline,'') :

        print(line)
        if line != '' :
            arg = line.split()
            print(arg)
            if len(arg) > 0 :
                exec_time = arg[1]
                exec_time_sum += int(exec_time)
            #print(exec_time)
        #time.sleep(2)
    exec_time_avg = exec_time_sum / 10 #10 is r ( number of repetitions )
    
    writer.writerow([n,exec_time_avg])
    #print( str(n)+'\t'+str(exec_time_avg))

