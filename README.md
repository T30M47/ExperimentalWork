# Experimental work - Concatenated index
---
This repository is used for experimental work for "Infrastruktura za podatke velikog obujma" course on Faculty of informatics and Digital Technologies. It covers bencmarking of read request response times with and without concatenated index based on the number of rows in a table, cardinality of chosen columns and different queries. The complete Django web app source code and neccessary Docker files are given which are described later.

# Description for using
---

**The recommended way to use this repo is to clone it, because just downloading the .zip file has extra steps which will be described later!***

1. Firstly, create an empty folder and open it in Your text editor (I used VS Code)
2. Open the terminal in Your text editor while in the empty folder You just created.
3. Clone the repo with:
```
git clone https://github.com/T30M47/ExperimentalWork.git
```

**If You decide to dowload the zip file of the code, you have to do some extra steps:**
1. After extracting the folder, open it in Your text editor.
2. Download the "db.sqlite3" file separately (Chose the file in this repo and click "*Download Raw*")
3. Put the downloaded raw file of the database in downloaded mysite folder (replace the old one with this downloaded one)
4. This is needed, because this file is put on GitHub with git lfs for uploading large files and without this steps, You will not have a working database file, but just a text file with a pointer to it.


After You prepared the folder and Your environment, go in the terminal in Your text editor and go to the root folder if You are not in it (root folder is the folder where the Dockerfile is located).
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
 1. The homepage contains buttons for comparing response times of conacatenated indexes (without, with concat. index, with part of concat. index and with concat. index with wrong order of columns).
 2. To test response times You can click on a button (check if your browser is loading) and wait that you get forwarded to the page with JSON response with summary of the ab test.
 3. You can get back to the home page with the left arrow integrated in Your browser (normal "go back" button/action).
 4. You can compare different read response times by clicking on different buttons for comparing different relationships between indexes based on the number of rows and different carinalities of chosen columns.
 5. You can compare the mean of "Time per request" in ab result or percentiles over 90.
 6. If You want to use Your own ab tests on URLs, I recommend You read the descriptions of URLs below (not needed for just using GUI and buttons).

#### **HELP OR ADDITIONAL INFORMATION**
 If you have trouble with starting the test you should look at errors which appear in the terminal where You started the app.
 If the error is appearing because You do not have ab installed (Dockerfile should install it) or if you want to try ab requests in your own terminal, You should install it:
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

## **Run the benchmark on different data and examples (if You want)**
---
### Descriptions of URLs
* withoutIndex/ - for testing queries on table with no index and small cardinality of columns naziv and cijena (query containing naziv, cijena, datum_kreiranja)
  
* withIndex/ - for testing queries on table with normal full index and small cardinality of columns naziv and cijena (query containing naziv, cijena, datum_kreiranja on which index is created)
  
* withPartIndex/ - for testing queries on table with part index and small cardinality of columns naziv and cijena (query containing naziv, cijena, datum_kreiranja while the index is only on naziv and cijena)
  
* withWrongIndex/ - for testing queries on table with wrong index - opposite order of columns than normal index and small cardinality of columns naziv and cijena (query containing only naziv and cijena)
  
* withoutIndexLessRows/ - for testing queries on table with no index and a small amount of rows (query containing naziv, cijena, datum_kreiranja)
  
* withIndexLessRows/ - for testing queries on table with normal full index and a small amount of rows (query containing naziv, cijena, datum_kreiranja on which index is created)
  
* withIndexBigCard/ - for testing queries on table with normal full index and big cardinality of columns naziv and cijena (query containing naziv, cijena, datum_kreiranja on which index is created)
  
* withPartIndexBigCard/ - for testing queries on table with part index and big cardinality of columns naziv and cijena (query containing naziv, cijena, datum_kreiranja while the index is only on naziv and cijena)
  
* withWrongIndexBigCard/ - for testing queries on table with wrong index - opposite order of columns than normal index and big cardinality of columns naziv and cijena (query containing only naziv and cijena)
  
* withIndexDate/ - for testing queries on table with normal full index and small cardinality of columns naziv and cijena (query containing only naziv and cijena)
  
* withIndexBigDate/ - for testing queries on table with normal full index and big cardinality of columns naziv and cijena (query containing only naziv and cijena)
  
* withWrongIndexFull/ - for testing queries on table with wrong index - opposite order of columns than normal index and small cardinality of columns naziv and cijena (query containing naziv, cijena, datum_kreiranja on which index is created)

* withWrongIndexBigCardFull/ - for testing queries on table with wrong index - opposite order of columns than normal index and big cardinality of columns naziv and cijena (query containing naziv, cijena, datum_kreiranja on which index is created)

**I used the ab command with -n 1000 and -c 3 parameters and this is hard-coded in my code (main/views.py).**
```
ab -n 1000 -c 3 "yourURL"
```
**For results I used mean of "Time per request" and above 90 percentiles**

Here is an example of URLs for comparison of index usage on small and big tables that you could test and send ab requests to in Your own terminal:

**For comparing with and without index based on size of table (100 and 100000 rows):**

100 Rows, there should be no significant difference:
* http://127.0.0.1:8000/withoutIndexLessRows/?naziv=bread&cijena=1.99&datum_kreiranja=1993-09-13
* http://127.0.0.1:8000/withIndexLessRows/?naziv=eggs&cijena=9.99&datum_kreiranja=2022-03-14

VS

100000 rows, now the index should help a lot:
* http://127.0.0.1:8000/withoutIndex/?naziv=milk&cijena=2.99&datum_kreiranja=1989-03-15
* http://127.0.0.1:8000/withIndex/?naziv=eggs&cijena=9.99&datum_kreiranja=1996-03-13

In that way, You can also test other situations...

If You want to change the amount of data in tables, You should go to:
```
mysite/main/management/commands/setup_test_data.py
```
and change the neccessary constant in the beggining of the file (e.g NUM_PROIZVODBEZINDEKSA) and open a new terminal while the container is still running and run the command:
```
./manage.py setup_test_data
```
But this way, all the data in the database will change and You will have to change Your queries, so You should go to:
```
http://localhost:8000/admin
```
and login with username: admin, password: admin data, and try to do a request for data You choose based on the given URLs before.

*You should also look at which URL queries all columns from index or just a part of them from descriptions of URLs.*
