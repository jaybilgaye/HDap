# Hosts

This file contains the information about the IP address of all hosts in the hadoop cluster. The host file is divided into two section: one for Ambari hadoop installation for HDP or BI and another one for Cloudera hadoop.

### Ambari_hosts
* List of hosts which will be required for installing hadoop cluster of hortanworks or BigInsights over ambari.  
* By default, all services will be installed randomly on the nodes and all clients will be installed on each node. If you want to specify namenode or resource manager services explicitly on some specific node than define the optional variable for that service as shown in below table:  

|          Variable          |                                                 Description                                                 | Required |
|:--------------------------:|:-----------------------------------------------------------------------------------------------------------:|:--------:|
|         ODP_hadoop         | List of all nodes of hadoop cluster                                                                         | Yes      |
|        ambari-server       | IP of the node over which ambari-server need to install                                                     | Yes      |
| ODP_namenode               | IP of the node in which you want to install namenode                                                        | No       |
| ODP_resourcemanager        | IP of the node in which you want to install resourcemanager                                                 | No       |
| ODP_standbynamenode        | IP of the node in which you want to install standby namenode if HA_NAMENODE variable is true               | No       |
| ODP_standbyresourcemanager | IP of the node in which you want to install standby resourcemanager if HA_RESOURCE_MANAGER variable is true | No       |

### Cloudera_hosts  

* List of hosts which will be required for installing hadoop cluster of cloudera over cloudera-manager. 
* By default, only HDFS, YARN and Zookeeper services will be installed on the nodes and all gateway will be installed on each node. If you want HDFS, YARN and Zookeeper on some specific node or need some other services over cluster than define the optional variables for that service as shown in below table: 

|        Variable        |                                                                                                  Description                                                                                                  | Required |
|:----------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------:|
|     cloudera_master    | IP of the node over which cloudera-manager need to install                                                                                                                                                    | Yes      |
|      hadoop_hosts      | List of all nodes of hadoop cluster                                                                                                                                                                           | Yes      |
|       hive_nodes       | IP of the node if  you want to install hive server                                                                                                                                                            | No       |
|      spark_on_yarn     | IP of the node if you want to install spark                                                                                                                                                                   | No       |
|          oozie         | IP of the node if you want to install oozie                                                                                                                                                                   | No       |
|          hbase         | IP of the node if you want to install hbase                                                                                                                                                                   | No       |
|        datanodes       | IP of the node in which you want to install datanodes                                                                                                                                                         | No       |
|          solr          | IP of the node if you want to install solr                                                                                                                                                                    | No       |
|          sqoop         | IP of the node if you want to install sqoop2                                                                                                                                                                  | No       |
|          flume         | IP of the node if you want to install flume                                                                                                                                                                   | No       |
|        namenode        | IP of the node in which you want to install namenode                                                                                                                                                          | No       |
|     resourcemanager    | IP of the node in which you want to install resourcemanager                                                                                                                                                   | No       |
|       secondarynn      | IP of the node in which you want to install secondary namenode                                                                                                                                                | No       |
|        zookeeper       | IP of the node in which you want to install zookeeper                                                                                                                                                         | No       |
|           hue          | IP of the node if you want to install hue                                                                                                                                                                     | No       |
|         impala         | IP of the node if you want to install impala                                                                                                                                                                  | No       |
|           kms          | IP of the node if you want to install kms                                                                                                                                                                     | No       |
|       ks_indexer       | IP of the node if you want to install ks_indexer                                                                                                                                                              | No       |
|         sentry         | IP of the node if you want to install sentry                                                                                                                                                                  | No       |
|          kafka         | IP of the node if you want to install kafka, and also define comma separated list for parcel of kafka in CDH_PARCELS_REPO variable                                                                                    | No       |
|       journalnode      | IP of the nodes on which you want to install journalnodes, if you want to configure namenode high availability, journal nodes should be on 3 or more odd number of nodes. And HA_NAMENODE variable should be true | No       |
|     standbynamenode    | IP of the node on which you want to install standby namenode, if you want to configure namenode high availability. And HA_NAMENODE variable should be true                                                        | No       |
| standbyresourcemanager | IP of the node on which you want to install standby resource manager, if you want to configure resource manager high availability. And HA_RESOURCE_MANAGER variable should be true                                | No       |

