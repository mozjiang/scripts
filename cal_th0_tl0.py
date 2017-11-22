osc = [float(n) for n in input("晶振频率(单位 Mhz):  ").split()]

time_range = []
for o in osc:
	time_range.append(pow(2,16)*(12/o)/1000)
print("注意，对应的定时上限为(单位：ms): {}".format(time_range))

time = [int(n) for n in input("定时时间(单位 ms):  ").split()] 
print("晶振频率列表为(单位：Mhz)：{}".format(osc))
print("定时时间列表为(单位：ms):{}".format(time))

set_number = []
for o,t in zip(osc,time):
	set_number.append(pow(2,16) - (o/12)*t*1000)

print("频率(Mhz) 定时时间(ms) 设定初值(十进制) 十六进制")
for o,t,n in zip(osc,time,set_number):
	print("{:<10} {:<13} {:<15} {:<10} ".format(o,t,round(n),hex(round(n))))
