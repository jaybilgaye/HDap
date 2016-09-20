# Variables

This files contains the list of the global variables used in playbooks. Modify this file to set the cluster configuration
The following table will describe all the variables:
### all file (Default file)

* Common variables which will be required for playbooks  

|       Variable      |                                                  Description                                                  |
|:-------------------:|:-------------------------------------------------------------------------------------------------------------:|
|     ANSIBLE_USER    | User who has a sudo access on all target hosts; ex: hadoop                                                                |
|        DOMAIN       | whether installation uses intranet or internet; Acceptable values: local(for intranet repositories), internet |
|       CLUSTER       | Name of Hadoop cluster; ex: Cluster1                                                                                        |
|       FLAVOUR       | Which flavour of Hadoop you want to install; Acceptable values: cdh, hdp, bi                                  |
|     HA_NAMENODE     | want to configure namenode high availibilty; Acceptable values: true, false                                   |
| HA_RESOURCE_MANAGER | want to configure resource manager high availibilty; Acceptable values: true, false                           |
|     NAMESERVICE     | name of the nameservice for namenode HA; ex: nameservice1                                                                       |

* Variables need to be changed only when domain is local (intranet)  

|  Variable  |              Description              |
|:----------:|:-------------------------------------:|
| NTP_SERVER | Internal time server IP for time sync; ex:10.0.0.4 |
|   OS_REPO  | URL of OS repository file; ex: http://mirror.centos.org/centos/7/CentOS-Base.repo             |

* Variables need to be changed only for Cloudera when flavour is cdh  

|      Variable      |                                                                Description                                                                |
|:------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------:|
|       CDH_VER      | Cloudera version which you want to install; ex: 5.8.0                                                                                     |
| CM_BASE_URL | Base URL of CM repo; ex: http://archive.cloudera.com/cm5/redhat/7/x86_64/cm/5.8.0/                                                        |
|  CDH_PARCELS_REPO  | URL of parcels for CDH and KAFKA; ex: http://archive.cloudera.com/cdh5/parcels/5.8.0/,http://archive.cloudera.com/kafka/parcels/2/        |
|    DEBIAN_CM_KEY   | Path of CM archive.key for pub-key verification when OS is Ubuntu; ex: http://archive.cloudera.com/cm5/ubuntu/trusty/amd64/cm/archive.key |

* Variables need to be changed only for Ambari(HDP/BI) when flavour is hdp or bi
  
|      Variable     |                                                          Description                                                         |
|:-----------------:|:----------------------------------------------------------------------------------------------------------------------------:|
|    AMBARI_REPO    | Base URL of Ambari repo; ex: http://public-repo-1.hortonworks.com/ambari/centos6/2.x/updates/2.2.1.0                         |
|      LOG_DIR      | Log dir for all services; ex: /var/log                                                                                       |
| DATANODE_DATA_DIR | Data dir of datanodes; ex: /data/hadoop/                                                                                     |
|      JAVA_URL     | URL of Java tar only when domain is local; ex: http://www.oracle.com/java/jdk-7u71-linux-x64.tar.gz |

* Variables need to be changed only for Hortonworks when flavour is hdp  

|    Variable    |                                                        Description                                                       |
|:--------------:|:------------------------------------------------------------------------------------------------------------------------:|
|     HDP_VER    | HDP major version; ex: 2.4                                                                                               |
|  HDP_UTILS_VER | HDP utils version; ex: 1.1.0.20                                                                                          |
|    HDP_REPO    | Base URL of HDP repo, if domain is local; ex: http://public-repo-1.hortonworks.com/HDP/centos7/2.x/updates/2.4.0.0       |
| HDP_UTILS_REPO | Base URL of HDP utils repo, if domain is local; ex: http://public-repo-1.hortonworks.com/HDP-UTILS-1.1.0.20/repos/centos7 |

* Variables need to be changed only for BigInsights when flavour is bi  

|    Variable   |                                                               Description                                                              |
|:-------------:|:--------------------------------------------------------------------------------------------------------------------------------------:|
|     BI_VER    | BI major version; ex: 4.2                                                                                                              |
|   BI_IOP_VER  | BI IOP version; ex: 1.2                                                                                                                |
|    BI_REPO    | Base URL of BI repo, if domain is local; ex: https://ibm-open-platform.ibm.com/repos/IOP/rhel/7/x86_64/4.2.x/Updates/4.2.0.0_20160721/ |
| BI_UTILS_REPO | Base URL of BI IOP utils repo, if domain is local; ex: https://ibm-open-platform.ibm.com/repos/IOP-UTILS/rhel/7/x86_64/1.2/             |

### passwords.yml file  

* Variables need to be changed only when you want to change default password of below variables  

|         Variable        |                           Description                           |
|:-----------------------:|:---------------------------------------------------------------:|
| HIVE_METASTORE_PASSWORD | password for hive metastore database; by default password: hive |
|    SENTRY_DB_PASSWORD   | password for sentry database; by default password: sentry       |

For editing the above file call: **ansible-vault edit passwords.yml** Password for vault is: **vault**
