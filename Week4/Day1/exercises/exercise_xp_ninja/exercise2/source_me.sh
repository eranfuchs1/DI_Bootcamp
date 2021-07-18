if [ -x "$(command -v python3)" ];
then
	alias py="python3"
elif [ -x "$(command -v python)" ];
then
	if grep '3\.[0-9]\.[0-9]' $(python -V) &> /dev/null
	then
		alias py="python"
	fi
fi

#$ source ./source_me.sh
