# CS172 Final Project

#### Team member 1 - Raajitha Rajkumar 862015848
#### Team member 2 - Russell Brown 862024798
#### Team member 3 - Jason Tang 862046859

## DESIGN

#####  For this project, we have a main.py that generates everything for the user. This main.py program welcomes the user and asks for an input for URLs to crawl. That is when the program calls the crawler and shows all the URLs being crawled. After this, our main.py calls our ElasticSearch file which has all the ES commands which the program generates and asks the user for an index name. The index is developed and bulk loads all the crawled data. The main.py then generates a terminal search which the user can search a term for their score and the docs the term shows up in. The user can also find the term in the text to see where it is generated. Our main.py does all this functionality for the user and that is how the program operates. 

## HOW TO COMPILE

#### Before running the project, make sure you have all the Python modules installed. You may need to run these commands after intalling Python:

```python
$ pip3 install --upgrade pip
```
```python
$ pip3 install flask
```
```python
$ pip3 install requests
```
```python
$ pip3 install beautifulsoup4
```
```python
$ pip3 install elasticsearch
```

### To run this Project, copy the following command:

```python
$ python3 main.py
```
### Anything that is not in that format will result in an error. 

[LINK TO DEMO](https://www.youtube.com/watch?v=O0p6m5bCUI8)

