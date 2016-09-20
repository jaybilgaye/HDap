from os import system as cmd
from time import sleep as sleep

hostname=[]
file=open("/opt/bi/hadoop_hosts","r")
for line in file.readlines():
	if (len(line)<3):
        	continue
	hostname.append(line.strip())
        file.close()

length=len(hostname)
json_host=open("{{ tmp_bi_files }}host_service.json","a+")
json_host.write("\"fqdn\" : \"" + hostname[0] + "\"\n } ] }")

#for  node1
if(length>1):
	json_host.write(",\n{ \"name\":\"node1\",\n \"hosts\":[ { \n")
        json_host.write("\"fqdn\" : \"" + hostname[1] + "\"\n } ] }")

#for node2
if(length>2):
	json_host.write(",\n{ \"name\":\"node2\",\n \"hosts\":[ ")
       	json_host.write("{\n\"fqdn\" : \"" + hostname[2] + "\"\n } ] }")

#for node3
if(length>3):
        json_host.write(",\n{ \"name\":\"node3\",\n \"hosts\":[ ")
        json_host.write("{\n\"fqdn\" : \"" + hostname[3] + "\"\n } ] }")

#for rest of datanodes
if(length>4):
        json_host.write(",\n{ \"name\":\"data_nodes\",\n \"hosts\":[ ")
        i=4
        while(i<length):
                json_host.write("{\n\"fqdn\" : \"" + hostname[i] + "\"\n }")
                if (i < length-1):
                        json_host.write(",")
                i=i+1
        json_host.write(" ] }")

json_host.write("\n] }")
