#!/bin/bash

function three() {
cd /usr/bin/
rm -f python
ln -s /usr/bin/python3.4 python
}
function two() {
cd /usr/bin/
rm -f python
ln -s /usr/bin/python2.7 python
}

case $1 in
2)
two
exit
;;
3)
three
exit
;;
*)
echo "参数错误"
esac
ll /usr/bin/python
