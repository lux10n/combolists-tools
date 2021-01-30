iconv -c -t utf-8 $1 > $1"_tmp"
mv $1"_tmp" $1
