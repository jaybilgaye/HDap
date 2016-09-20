#!/usr/bin/python
# -*- coding: utf-8 -*-
DOCUMENTATION = '''
---
module: security
author: Prakul Singhal (From Persistent System Limited)

This module add firewall rules in all machine irrespective of OS version(Redhat/Centos 6,7 or Ubuntu/Debian). For using that module we have to copy that file in library directory in the playbook

example:
 - variables:
	portlist= (required variable) list of port seperated by ',' need to be added in firewall rules.
	protocol= (Optional variable) type of protocol (tcp or udp). bny default set to tcp.
	policy= (Optional variable) Need to provide rules for input, output or both. by default all is set for both direction (input, output and all). But as in Centos 7 there is no such concept of policy in place of that it used zone. by default public zone is active in the OS, so this module define another variable as zone for centos 7 only.
	zone= (Optional variable)for defining zone in centos 7. by default public zone is taken, if you have some other zone as active than provide the name of that zone in this variable.
	destlist= (Optional variable) list of IP  or Hostname betwwen which firewall rule is needed. By default it is set none, so open the particular port for whole world.
	target= (Optional variable) By default ACCEPT target is taken. (ACCEPT, REJECT and DROP) This variable take the target decisoin for the rule, whether we want to accept,reject or drop that port.
	interface= (Optional variable) By default None interface is taken. This varaible take the interface for which we want to deploy the rule.

 - For single port 22 open for incoming and outgoing (both input and output)
	 security: portlist="22"
   The above call add 22 port for tcp protocol open for all in the firewall rules

 - For list of port 22,80,444 open incoming and outgoing for particular destination
  	security: portlist="22,80,444" destlist="192.168.1.10"

 - For list of port 22,80,444 open for particular destination in input direction(not for centos 7) only for udp protocol
	security: portlist="22,80,444" protocol="udp"  destlist="192.168.1.10" policy="input"

 - For single port 80 open for particular destinationis in output direction(not for centos 7)  only for udp protocol 
	security: portlist="80" protocol="udp" destlist="192.168.1.10,192.168.1.11,192.168.1.12" policy="output" 

 - For single port 80 closed for all destinationis only for tcp protocol
        security: portlist="80" protocol="tcp" target="DROP"

 - For single port 22 open for particular destinationis for home zone(in centos 7 only) 
        security: portlist="22" destlist="192.168.1.10,192.168.1.11,192.168.1.12" zone="home"

 - For all port open for particular interface
	security: portlist="all" policy="input" interface="lo" target="ACCEPT"	
'''

def preparerule(portlist,protocol,policy,target):
	newfilecontent=""	
	for port in portlist:
        	newinputrule='-A INPUT -p '+protocol+' --dport '+port+' -m state --state NEW,ESTABLISHED -j ' + target
                newoutputrule='-A OUTPUT -p '+protocol+' --dport '+port+' -m state --state NEW,ESTABLISHED -j ' + target
		newsrcinputrule='-A INPUT -p '+protocol+' --sport '+port+' -m state --state NEW,ESTABLISHED -j ' + target
		newfrwrule='-A FORWARD -p '+protocol+' --sport '+port+' -m state --state NEW,ESTABLISHED -j ' + target
                if policy == 'input' :
                        newfilecontent+=newinputrule+"\n"
			newfilecontent+=newsrcinputrule+"\n"
                elif policy == 'output':
                        newfilecontent+=newoutputrule+"\n"
		elif policy == 'forward':
                        newfilecontent+=newfrwrule+"\n"
                else:
                        newfilecontent+=newinputrule+"\n"
			newfilecontent+=newsrcinputrule+"\n"
			newfilecontent+=newoutputrule+"\n"

	return newfilecontent


def preparerulewithDestlist(destlist,portlist,protocol,policy,target):
	newfilecontent=""	
	for dest in destlist:
        	for port in portlist:
               		newinputrule='-A INPUT -p '+protocol+' --dport '+port+' -m state --state NEW,ESTABLISHED -s '+dest+' -j ' + target
                	newoutputrule='-A OUTPUT -p '+protocol+' --dport '+port+' -m state --state NEW,ESTABLISHED -d '+dest+' -j ' + target
                	newsrcinputrule='-A INPUT -p '+protocol+' --sport '+port+' -m state --state NEW,ESTABLISHED -s '+dest+' -j ' + target
			newfrwrule='-A FORWARD -p '+protocol+' --dport '+port+' -m state --state NEW,ESTABLISHED -d '+dest+' -j ' + target
               		if policy == 'input' :
                       		newfilecontent+=newinputrule+"\n"
				newfilecontent+=newsrcinputrule+"\n"
                	elif policy == 'output':
                        	newfilecontent+=newoutputrule+"\n"
                        elif policy == 'forward':
                                newfilecontent+=newfrwrule+"\n"
                	else:
                        	newfilecontent+=newinputrule+"\n"
				newfilecontent+=newsrcinputrule+"\n"
				newfilecontent+=newoutputrule+"\n"
        return newfilecontent

def prepareruleforall(policy,target,interface):
	newfilecontent=""
	if interface is None:
		newinputrule='-A INPUT -j ' + target
		newoutputrule='-A OUTPUT -j ' + target
	else:
		newinputrule='-A INPUT -i '+ interface +' -j ' + target
                newoutputrule='-A OUTPUT -o '+ interface +' -j ' + target
	if policy == 'input' :
		newfilecontent+=newinputrule+"\n"
	elif policy == 'output':
        	newfilecontent+=newoutputrule+"\n"
	else:
        	newfilecontent+=newinputrule+"\n"
                newfilecontent+=newoutputrule+"\n"
	return newfilecontent

def removeDuplicate(filepath):
	lines_seen = set() # holds lines already seen
	newcontent=''
	readfile=open(filepath, "r")
	for line in readfile:
    		if line not in lines_seen and not re.match(r'^\s*$', line) and '##### ' not in line: # not a duplicate
        		newcontent+=line
        		lines_seen.add(line)
	readfile.close()
	outfile = open(filepath, "w")
	outfile.write(newcontent)
	outfile.close()


def firewall():
        module = AnsibleModule(argument_spec = dict( portlist = dict(required=True, aliases=['portlist']),protocol = dict(required=False, aliases=['protocol']), policy=dict(required=False, aliases=['policy']), target=dict(required=False, aliases=['target']), zone=dict(required=False, aliases=['zone']),interface = dict(required=False, aliases=['destlist']), destlist = dict(required=False, aliases=['destlist'])))
        portlist = module.params.get('portlist').replace(' ','').split(",")
	if module.params.get('destlist') is not None:
		destlist =  module.params.get('destlist').replace(' ','').split(",")
		destlist = module.params.get('destlist').split(",")

        if module.params.get('protocol') is not None:
                protocol = module.params.get('protocol').lower()
        else:
                protocol = 'tcp'
	if module.params.get('target') is not None:
                target = module.params.get('target').upper()
        else:
                target = 'ACCEPT'
	if module.params.get('policy') is not None:
		policy = module.params.get('policy').lower()
	else:
		policy = 'all'
        if module.params.get('zone') is not None:
                zone = module.params.get('zone').lower()
        else:
                zone = 'public'
	if module.params.get('interface') is not None:
                interface = module.params.get('interface').lower()
        else:
                interface = None

	iptables_file_path='/etc/sysconfig/iptables'
	directory='/etc/iptables/'
	flavour=platform.platform()

	if 'Ubuntu' in flavour or 'debian' in flavour:
		if not os.path.exists(directory):
			os.makedirs(directory)
		iptables_file_path='/etc/iptables/rules.v4'
		if not os.path.exists(iptables_file_path):
                        os.system("sudo iptables -L > /dev/null")
			os.system("sudo iptables-save > " + iptables_file_path)

        if 'centos-6' in  flavour or 'Ubuntu' in flavour or 'redhat-6' in flavour or 'debian' in flavour:
                inputmarkup='-A INPUT -m state --state NEW -m tcp -p tcp --dport 22 -j ACCEPT\n-A OUTPUT -p tcp --sport 22 -j ACCEPT\n-A OUTPUT -p tcp --dport 22 -j ACCEPT\n-A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT\n-A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT\n-A OUTPUT -p tcp --dport 80 -j ACCEPT\n-A OUTPUT -p udp --dport 53 -j ACCEPT\n-A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT\n##### Acceptrules\n##### Forwardrules\n##### Rejectrules\n##### Droprules'
		searchmarkup=':OUTPUT ACCEPT'
		filecontent=''
		newrules=''
                newacceptrules=''
                newforwardrules=''
                newrejectrules=''
                newdroprules=''
                alldroprules='-A OUTPUT -j DROP\n-A INPUT -j DROP\nCOMMIT'

		initialfile = open(iptables_file_path)
		for line in initialfile :
                	filecontent+=line
			if searchmarkup in line:
				filecontent+=inputmarkup+'\n'
		initialfile.close()

		if module.params.get('destlist') is  None and 'all' not in portlist:
			newrules=preparerule(portlist,protocol,policy,target)			
		elif module.params.get('destlist') is  not None and 'all' not in portlist:
			newrules=preparerulewithDestlist(destlist,portlist,protocol,policy,target)
		else:
			newrules=prepareruleforall(policy,target,interface)

		filecontent=filecontent.replace('##### Acceptrules','##### Acceptrules\n'+newrules)
		for line in filecontent.splitlines():
			if  ' FORWARD' in line:
				newforwardrules+=line.strip()+'\n'
			elif 'ACCEPT' in line:
                                newacceptrules+=line.strip()+'\n'
                        elif 'REJECT' in line:
                                newrejectrules+=line.strip()+'\n'
                        else:
                                newdroprules+=line.strip()+'\n'

		filecontent='*filter\n'
		filecontent+=newacceptrules
		filecontent+=newforwardrules
		filecontent+=newrejectrules
		filecontent+=newdroprules
		filecontent=filecontent.replace('COMMIT',alldroprules)
		cfgfile = open(iptables_file_path,'w')
		cfgfile.write(filecontent)
		cfgfile.close()
		removeDuplicate(iptables_file_path)
		module.exit_json(changed=True, res= 'Security Iptables rule  is added in ' + ''.join(platform.dist()))

	
	if 'centos-7' in flavour or 'redhat-7' in flavour:
		rc=0;
		if module.params.get('destlist') is  None and target in "ACCEPT":
			for port in portlist:
				rc=os.system("firewall-cmd --permanent --zone=" +zone+ " --add-port="+port+"/"+protocol)
				if rc != 0:
                                                module.fail_json(msg="please check the args for security module as shown in error")
		elif module.params.get('destlist') is  None and target not in "ACCEPT":
			for port in portlist:
                                rc=os.system("firewall-cmd --zone=" +zone+ " --permanent --add-rich-rule=\"rule family=ipv4 port protocol="+protocol+ " port=" +port+ " " +target.lower()+ "\" >/dev/null")
				if rc != 0:
                                                module.fail_json(msg="please check the args for security module as shown in error")
		else:
			for dest in destlist:
		        	for port in portlist:
					rc=os.system("firewall-cmd --zone=" +zone+ " --permanent --add-rich-rule=\"rule family=ipv4 source address=" +dest+ "/32 port protocol="+protocol+ " port=" +port+ " " +target.lower()+ "\" >/dev/null")
					if rc != 0:
						module.fail_json(msg="please check the args for security module as shown in error")
		if rc == 0:
	        	module.exit_json(changed=True, res= 'Security Firewalld rule is added in ' + ''.join(platform.dist()))


from ansible.module_utils.basic import *
import os
import platform
import re
firewall()

