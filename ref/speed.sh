

example="www.google.com"
# ping -c 4 $example | tail -1 | awk '{print $4}'| cut -d '/' -f 2
# ping -c 4 $example | tail -1 | awk -F '/' '{print $5}' $@ > /dev/null

speed=$(ping -c 4 $example | tail -1 | awk '{print $4}'| cut -d '/' -f 2)

echo $a