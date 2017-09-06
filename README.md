# Coursera Dump

Parser [Coursera.org](https://www.coursera.org) courses.  
Find info about:
 
* Name
* Language
* Rating
* Start date
* Duration 

And generate .xlsx file with this data. 

# Install

```bash
pip3 -r requirements.txt
```

# How to use

```bash
python3 coursera.py
```
<h2>Args(not required)</h2>
-a(amount) - parser courses limit /by default is 5

-n(name) - output exel filename /by default devman

# Example

````bash
python3 -a=2 -n='test'
````

<h2>Result example</h2>
```bash
Success! devman.xlsx is done.
```
#Log
By default will write file log.log

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
