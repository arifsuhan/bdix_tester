
function check_ping () {

	ping -q -c1 $1 > /dev/null

	if [ $? -eq 0 ];then
		echo "\xE2\x9C\x93 $2 $3 $4" | fmt -c -w "80"
	else
		echo "\xE2\x9C\x98 $2 $3 $4" | fmt -c -w "80"
	fi
}

function fromFileCheck()
{	
	# data ref -> http://broadbandathome.com/ftp.html
	fileName="data/bdix_ip.csv"

	while IFS=',' read -r col1 col2
	do
	    check_ping $col1 $col2
	done < $fileName
}

cat 'data/logo.txt' | fmt -c -w "80"
echo ""
fromFileCheck



