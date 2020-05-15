stringarray=('test' 'some thing' 'very long long long string' 'blah')
numberarray=(1 22 7777 8888888888)
anotherfieldarray=('other' 'mixed' 456 'data')
array_size=4

# for((i=0;i<array_size;i++))
# do
#     echo ${stringarray[$i]} $'\x1d' ${numberarray[$i]} $'\x1d' ${anotherfieldarray[$i]}
# done | column -t -s$'\x1d'


for((i=0;i<array_size;i++))
do
    echo ${numberarray[$i]}
done | column -t -s$'\x1d'


# echo "             Multiplication Table"
# echo "----+-------------------------------------"
# echo "    | ok "
# echo "----+-------------------------------------"
# for y in {0..9}
# do  echo " $y  | $y "
#     echo "----+-------------------------------------"
# done | column -t -s$'\x1d'

# $(cat "data/bdix_ip.csv" | wc -l)

# csv_length=$(cat "data/bdix_ip.csv" | wc -l)
# array_size="$(echo "${csv_length}" | tr -d '[:space:]')"
# echo "${array_size}"