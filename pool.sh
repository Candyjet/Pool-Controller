#!/bin/sh
### BEGIN INIT INFO
# Provides:          pool.sh
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO

dir="/home/pi/src/Pool-Controller/webapp"
case "$1" in
    stop|status)
    kill `ps -ef | grep "python $dir/pool.py$" | awk '{ print $2 }'`
    ;;
    start|force-reload|restart|reload)
    kill `ps -ef | grep "python $dir/pool.py$" | awk '{ print $2 }'`
    /usr/bin/python $dir/pool.py
    ;;
esac
