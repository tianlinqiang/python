a=1
while(($a<=300))
do
	cat /etc/passwd	> /home/ryan/python/06-多进程拷贝文件/test/$a.txt
	let "a++"
done
