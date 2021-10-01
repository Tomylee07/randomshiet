echo 'Hola mundo !!'

x=1

while [ $x -le 10 ]

do echo $x

	if [ $x -eq 5 ]
	then echo $x 'es la mitad'
	fi

 x=$(expr $x + 1)

done


