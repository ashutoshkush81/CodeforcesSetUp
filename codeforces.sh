#! /bin/bash

name_of_folder=$1
link_of_contest=$2
no_of_file=${3:-4}
#Choosing dafault number of file as 4.


# function to  Convert interger into character
chr() {
  printf \\$(printf '%03o' $1)
}

#Go to your directory where u want to create new folder for contest
mkdir $name_of_folder

# On your favorite code editor.
# I'm using vscode as my default editor
code -n .

for (( i=0; i<$no_of_file; i++))
do
        file_name=$(expr "$i" + 1).cpp
        touch $file_name
        echo "//   https://codeforces.com/contest/$2/problem/$(chr $(expr "$i" + 65))"  >> $file_name
        # Place your default code as you want
        code $file_name
done

clear
echo "Welcome to codeforces"
echo "Good luck and High Rating"
cd $name_of_folder
