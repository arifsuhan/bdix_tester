
function check_ping () {

	ping -q -c1 -W1 $1 > /dev/null

	if [ $? -eq 0 ]
	then
		speed=$(ping -c 1 $1 | tail -1 | awk '{print $4}'| cut -d '/' -f 2)
		echo "\xE2\x9C\x93 $2 $3 $4 speed: $speed" | fmt -c -w "80"
	else
		echo "\xE2\x9C\x98 $2 $3 $4 " | fmt -c -w "80"
	fi

}

function fromFileCheck()
{	
	# data ref -> http://broadbandathome.com/ftp.html
	fileName="data/bdix_ip.csv"
	# fileName="data/test.csv"

	while IFS=',' read -r col1 col2
	do
	    check_ping $col1 $col2
	done < $fileName
}

cat 'data/logo.txt' | fmt -c -w "80"
echo ""
fromFileCheck





echo $a

