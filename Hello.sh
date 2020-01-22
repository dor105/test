#!/bin/bash

echo -n "Enter the username: "
read username

printf "Enter the password:\n"
read -s password


echo "hello $username " "Today is $(date)"
