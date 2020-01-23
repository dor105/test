
#!/bin/bash

echo -n "Enter the username: "
read username

printf "Enter the password:\n"
read -s password

for i in {1}
do
last="$(lastlog -u UserName)" #Username that the system knows
done

echo "Welcome $username now is $(date)"
echo "your Last login was $last"


: '
#!/bin/bash

counter=1
while [ $counter -le 10 ]
do
echo $counter
((counter++))
done
echo All done
'


