# StephsQuiz2

https://gist.github.com/StephanieSunshine/04d4a4eee550b8dbbf30e5b4c6ae4ab1 

run this command to fix the data:

cat big_boss_list | perl -p -e 's/429 Too Many Requests\n//gs' | perl -p -e "s/}\n\{/}{/gs" | sed -e 's/}{/},{/' -e 'H;$!d;x;s/^\n//' -e 's/^/[/;s/$/]/' > fixed_big_boss_list

run parse.py to sort the data into the folders.

Done!

