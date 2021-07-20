if [ -z "$1" ]; then echo "usage: $0 <shift value>"; exit 1; fi

if [ -z "$(diff <(cat test.txt | python untitled.py encrypt $1 | python untitled.py decrypt $1) test.txt)" ]; then echo 'works'; else echo "doesn't work"; fi
