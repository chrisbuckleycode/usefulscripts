# Summary

- From a list of your subreddits (pre-formatted) and each record `"*DIV*"` separated.
- Python script to convert it to a tilde-separated-values file
- Convert it to tab-separated-values file with command below
- In sqlite3: create a db, create a table, import the tsv file, perform a simple query of subreddits sorted by no. of subscribers descending value

# Usage

```shell
sudo apt install sqlite3

$ cat output.csv | tr '~' '\t' > modified_input.tsv
$ sqlite3 my_database.db
SQLite version 3.35.4 2021-04-02 15:20:15
Enter ".help" for usage hints.

sqlite> .mode tabs
sqlite> .read table_create.sql
sqlite> .import modified_input.tsv my_table
sqlite> .read query_subs_most_subscribed.sql
sqlite> .exit
```

# Remarks
- Sample input.txt provided

# Future Ideas
- Create db in Python
