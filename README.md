# Experimental work - Concatenated index
---
This repository is used for experimental work for "Infrastruktura za podatke velikog obujma" course on Faculty of informatics and Digital Technologies. It covers bencmarking of read requests response time with and without concatenated index.  The complete Django web app source code and neccessary Docker files are given which are described later.

# Description for using
---
After downloading the .zip file (and extracting it and opening it in your text editor) from Github or after cloning it in your text editor, open the terminal and move to the root folder that contains extracted files (You can try ls command to see if Dockerfile is in it).
```
cd yourPath/rootFolder
```
If you already are in the root folder (where the Dockerfile is located), build your docker image with:
```
docker build -t yourchosenname .
```

and then run the container with:
```
docker run -p 8000:8000 yourchosenname
```
After running the container, the app should be available on URL:
```
http://localhost:8000
```
The home page contains a short description on how to benchmark this model, but you can also find some instructions over here:
 1. The homepage contains three buttons for each type of queries (without, with concat. index, with part of concat. index and with concat. index with wrong order of columns).
 2. To test response times You can click on a button (check if your browser is loading) and wait that you get forwarded to the page with JSON response with summary of ab test.
 3. You can get back to the home page with the left arrow integrated in Your browser (normal "go back" button/action).
 4. You can compare different read response times by clicking on different buttons on for different indexes.

#### **HELP OR ADDITIONAL INFORMATION**
 If you have trouble with starting the test you should look at errors which appear in the terminal where You started the app.
 If the error is appearing because You do not have ab installed or if you want to try ab requests in your own terminal, You should install it:
 ### Debian based Linux
    ```
    sudo apt-get install apache2-utils
    ```
 ### Arch based Linux
    ```
    sudo pacman -S apache-tools 
    or just 
    sudo pacman -S apache

 ### Alpine based Linux
    ```
    apk add apache2-utils
    ```
 **I used ab command with -n 1000 and -c 3 parameters.**

Here are examples of URLs for every type of index that you could test and send ab requests to in Your own terminal:
* http://127.0.0.1:8000/withoutIndex/?naziv=bread&cijena=1.99&datum_kreiranja=1973-11-21
* http://127.0.0.1:8000/withIndex/?naziv=eggs&cijena=9.99&datum_kreiranja=1999-03-23
* http://127.0.0.1:8000/withPartIndex/?naziv=milk&cijena=2.99&datum_kreiranja=2009-06-23
* http://127.0.0.1:8000/withWrongIndex/?naziv=eggs&cijena=9.99&datum_kreiranja=1996-03-12

If You want You could also try to send Your own requests by going to URL:
```
http://localhost:8000/admin
```
and login with username: admin, password: admin data, and try to do a request for data You choose based on the given URLs before.
