# 0x00. AirBnB clone - The console

## About the project

[![project diagram][project-diagram]](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221025%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221025T053349Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=72959cebe454c817e1212b291f7a401cfafbb90a4e4282454d3275520d1422a9)


The console is a project which is based on the creation of a data model which allows you to create, update and destroy objects/instances of the model through a command interpreter. And also store aand persist(you wont have to pay attention (take care) of how your objects are stored) objects to a file (JSON file).


## How to Run the console

the console should work like this in interactive mode:
``
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
``
But also in non-interactive mode:
``
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
``

# Complete it later
