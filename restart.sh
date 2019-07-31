#!/bin/bash
#author: hubery
#	获取进程数
proc_num()                                              # 计算进程数  
{  
    num=`ps -ef | grep $1 | grep -v "grep" | wc -l`
    return $num  
}

#	获取后台进程pid
proc_id_runserver()                                               # 进程号  
{  
    pid=`ps -ef | grep 'runserver' | grep -v grep | awk '{print $2}'`  
}

#	获取前端进程pid
proc_id_npm()                                               # 进程号  
{  
    pid=`ps -ef | grep 'npm' | grep -v grep | awk '{print $2}'`  
}


proc_id_runserver
if [ -n "$pid" ];
	then
		m=""
		m=`echo $pid | awk '{print $1}'`
		n=""
		n=`echo $pid | awk '{print $2}'`
		command=`kill -9 $m`
		command=`kill -9 $n`
fi

proc_id_npm
if [ -n "$pid" ];
	then
		m=""
		m=`echo $pid | awk '{print $1}'`
		command=`kill -9 $m`
fi

nohup python /home/phonetest/gale/TesterRunner/manage.py runserver 0:8000 >/home/phonetest/gale/TesterRunner/TestRunner.INFO 2>&1 &

cd /home/phonetest/gale/frontend/
nohup npm run dev > run.INFO 2>&1 &
echo "restart the TestRunner service."