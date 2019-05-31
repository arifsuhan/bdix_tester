function check_ping () {

	ping -q -c1 $1 > /dev/null
	 
	if [ $? -eq 0 ]
	then
		echo "(!)" $1 "is connected"
	else
		echo "(x)" $1 "is not connected"
	fi
}

function series_ip(){

	for ip in `seq 1 $1`
	do
	  check_ping 192.168.0.$ip
	done
}

function main(){

	echo "\n"
	series_ip $1
	echo "\n"

}

function rangeCheck()
{	
	echo "Enter IP Range:"
	read range_v
	main $range_v
}

function fromFileCheck()
{
	fileName="data/bdix_ip.csv"

	while read -r col1 col2
	do
	    check_ping $col1
	done < $fileName
}

#rangeCheck
fromFileCheck



