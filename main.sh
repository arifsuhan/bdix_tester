
function check_ping () {

	ping -q -c1 $1 > /dev/null

	#printf '\342\234\224\n'
	#echo "\xE2\x9C\x94  existing"
	#echo "\xE2\x9D\x8C missing"

	if [ $? -eq 0 ]
	then
		#echo "(!)" "$2 $3 $4" "is connected"
		echo "\xE2\x9C\x94  $2 $3 $4"
	else
		#echo "(x)" "$2 $3 $4" "is not connected"
		echo "\xE2\x9D\x8C  $2 $3 $4"
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

fromFileCheck



