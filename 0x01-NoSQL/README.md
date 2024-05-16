# 0x01. NoSQL

## Learning Objectives

### General

- What NoSQL means
- What is difference between SQL and NoSQL
- What is ACID
- What is a document storage
- What are NoSQL types
- What are benefits of a NoSQL database
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB

| Task                            | File                                                   |
| ------------------------------- | ------------------------------------------------------ |
| 0. List all databases           | [0-list_databases](./0-list_databases)                 |
| 1. Create a database            | [1-use_or_create_database](./1-use_or_create_database) |
| 2. Insert document              | [2-insert](./2-insert)                                 |
| 3. All documents                | [3-all](./3-all)                                       |
| 4. All matches                  | [4-match](./4-match)                                   |
| 5. Count                        | [5-count](./5-count)                                   |
| 6. Update                       | [6-update](./6-update)                                 |
| 7. Delete by match              | [7-delete](./7-delete)                                 |
| 8. List all documents in Python | [8-all.py](./8-all.py)                                 |
| 9. Insert a document in Python  | [9-insert_school.py](./9-insert_school.py)             |
| 10. Change school topics        | [10-update_topics.py](./10-update_topics.py)           |
| 11. Where can I learn Python?   | [11-schools_by_topic.py](./11-schools_by_topic.py)     |
| 12. Log stats                   | [12-log_stats.py](./12-log_stats.py)                   |
| 13. Regex filter                | [100-find](./100-find)                                 |
| 14. Top students                | [101-students.py](./101-students.py)                   |
| 15. Log stats - new version     | [102-log_stats.py](./102-log_stats.py)                 |

## Tasks

### 0. List all databases

- Write a script that lists all databases in MongoDB.

### 1. Create a database

- Write a script that creates or uses the database `my_db`:

### 2. Insert document

_Write a script that inserts a document in the collection `school`:
_ The document must have one attribute `name` with value “Holberton school” \* The database name will be passed as option of `mongo` command

### 3. All documents

*Write a script that lists all documents in the collection `school`:
*The database name will be passed as option of `mongo` command

### 4. All matches

- Write a script that lists all documents with `name="Holberton school"` in the collection `school`:
  - The database name will be passed as option of `mongo` command

### 5. Count

- Write a script that displays the number of documents in the collection `school`:
  - The database name will be passed as option of `mongo` command

### 6. Update

- Write a script that adds a new attribute to a document in the collection `school`:
  *The script should update only document with `name="Holberton school"` (all of them)
  *The update should add the attribute `address` with the value “972 Mission street”
  \*The database name will be passed as option of `mongo` command

### 7. Delete by match

- Write a script that deletes all documents with `name="Holberton school"` in the collection `school`:
  - The database name will be passed as option of `mongo` command

### 8. List all documents in Python

- Write a Python function that lists all documents in a collection:
  - Prototype: `def list_all(mongo_collection):`
  - Return an empty list if no document in the collection
  - `mongo_collection` will be the `pymongo` collection object

### 9. Insert a document in Python

- Write a Python function that inserts a new document in a collection based on `kwargs`:
  - Prototype: `def insert_school(mongo_collection, **kwargs):`
  - `mongo_collection` will be the `pymongo` collection object
  - Returns the new `_id`

### 10. Change school topics

- Write a Python function that changes all topics of a school document based on the name:
  - Prototype: `def update_topics(mongo_collection, name, topics):`
  - `mongo_collection` will be the `pymongo` collection object
  - `name` (string) will be the school name to update
  - `topics` (list of strings) will be the list of topics approached in the school

### 11. Where can I learn Python?

- Write a Python function that returns the list of school having a specific topic:
  - Prototype: `def schools_by_topic(mongo_collection, topic):`
  - `mongo_collection` will be the `pymongo` collection object
  - `topic` (string) will be topic searched

### 12. Log stats

- Write a Python script that provides some stats about Nginx logs stored in MongoDB:
  _ Database: `logs`
  _ Collection: `nginx`
  _ Display (same as the example):
  _ first line: `x logs `where `x` is the number of documents in this collection
  _ second line: `Methods:`
  _ 5 lines with the number of documents with the `method` = `["GET", "POST", "PUT", "PATCH", "DELETE"]` in this order (see example below - warning: it’s a tabulation before each line)
  _ one line with the number of documents with:
  _ `method=GET` \* `path=/status`
  You can use this dump as data sample: [dump.zip](https://intranet.alxswe.com/rltoken/0szbpslKvH3RqKb_2HUeoQ)

The output of your script **must be exactly the same as the example**

### 13. Regex filter

- Write a script that lists all documents with `name` starting by `Holberton` in the collection `school`:
  - The database name will be passed as option of `mongo` command

### 14. Top students

- Write a Python function that returns all students sorted by average score:
  - Prototype: `def top_students(mongo_collection):`
  - `mongo_collection` will be the `pymongo` collection object
  - The top must be ordered
  - The average score must be part of each item returns with key = `averageScore`

### 15. Log stats - new version

- Improve `12-log_stats.py` by adding the top 10 of the most present IPs in the collection `nginx` of the database `logs`:
  - The IPs top must be sorted (like the example below)
  ````94778 logs
  Methods:
  	method GET: 93842
  	method POST: 229
  	method PUT: 0
  	method PATCH: 0
  	method DELETE: 0```
  ````
