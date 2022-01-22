from subprocess import Popen, PIPE
import csv
#p = Popen('bash ./launch_nbody.sh -r 10 -n 10000', shell=True, stdout=PIPE)

file = open('exec_time.csv', 'w')
writer = csv.writer(file)
writer.writerow(['N','Avg Exec Time'])

print ( 'N ; Avg Exec Time')
for n in range(1, 1000) :

    p = Popen('bash ./launch_nbody.sh -r 10 -n '+str(n), shell=True, stdout=PIPE)

    exec_time_sum = 0
    for line in iter(p.stdout.readline,'') :

        if line != '' :
            arg = line.split(' ')
            exec_time = arg[1]
            exec_time_sum += int(exec_time)
            #print(exec_time)
    exec_time_avg = exec_time_sum / 10 #10 is r ( number of repetitions )
    
    writer.writerow([n,exec_time_avg])
    #print( str(n)+'\t'+str(exec_time_avg))

