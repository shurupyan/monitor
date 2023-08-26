# How to configure the SpeetTest monitoring script on Keenetic router
* Install the `entware` 
[OPKG](https://help.keenetic.com/hc/en-us/articles/360000948719-OPKG) to the `KeeneticOS` following this 
[instruction](https://help.keenetic.com/hc/en-us/articles/360021888880-Installing-OPKG-Entware-in-the-router-s-internal-memory) 
* After that you can install the packages you need from the 
[repositoritory](http://bin.entware.net/mipssf-k3.4/Packages.html) and 
[additional repo](http://bin.entware.net/mipselsf-k3.4/keenetic/Packages.html)
* Install the `wget-ssl` package using the following command:
    

    opkg install wget-ssl

* Install the `cron` package using the following command:
    

    opkg install cron

* Create new service configuration file `/opt/etc/init.d/S10crond` with the following content:
    

    #!/bin/sh
    
    ENABLED=yes
    PROCS=crond
    ARGS="d -b -l 0 -L /opt/root/crontab.log"
    PREARGS=""
    DESC=$PROCS
    PATH=/opt/sbin:/opt/bin:/opt/usr/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
    
    . /opt/etc/init.d/rc.func

* Put the `monitor.sh` file into the home directory. Change the following line


    BACKEND_URL=${BACKEND_URL}
replacing `${BACKEND_URL}` with the real backend URL

* Run the `crontab -e` command to configure the periodic run of the monitoring process. 
Add the following line to the cron config:

        
        */5 * * * * /opt/root/monitor.sh

* Start cron service with the following command:


    /opt/etc/init.d/S10crond start

* You can check the status of the cron service by running the following command:


    /opt/etc/init.d/S10crond status

* Logs of the cron service wil be in file `~/crontab.log`
* Logs of the monitor.sh script will be in file `~/log.txt`

# TO DO:
*  Add the logs rotation, archiving, and deleting