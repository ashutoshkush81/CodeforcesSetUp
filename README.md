# CodeforcesSetUp
## How to make user code snippets for Vscode/Sublime Text/Atom
(I'm creating user snippets in vscode but you can perform similar steps for other editor also).
- Opne vscode settings
- Select user snippets
- Select new global snippets file (If you want to use it globally)
- Enter name of your file
- Go to website 'snippet-generator.app'
- Select language as Description(Write name of language)
- Select name of snippets as Tab Trigger. (***)
- Enter your code.
- Copy code from 'copy snippet' button.
- Come back to vscode , now delete everything except first semicolon({})
- Paste and save the snippets.
- Now u can easly use you snippets as (***).

## Making both scipt executable fromm any place and also declare their alias
Note - Move your script into the usr/local/bin folder
```
alias c='clear'

function run() {

        python3 ~/../../usr/local/bin/./test.py $1
        
}

function cf(){

        cd cp/codeforces
        
        ~/../../usr/local/bin/codeforces.sh $1 $2 $3
        
        cd $1
        
}
```
## About test.py
This is use for download test cases from codeforces and compare with your output with actual output.
If both are equal then it' will show accepted otherwise it will show wrong answer promte.

### What are the arguments req. to run test.py?
alias for test.py is run and argument req is 'name_of_your_file'.cpp

You don't need to write .cpp

ex. run name_of_your_file

I have declare alias of test.py as 

## About codeforces.sh

This is used for create a new folder where it create as file and echo link for all problem into the file corresponding file.

## What are the arguments req. to run codeforces.sh

total 3 arguments req
- Name of folder
- link of codeforces contest
- no of file you want to create (by default it is 4).
ex. cf div2-635 1337 5

## Lib. req to run all script.
- python3
- g++
- beautiful soup
- cprint
