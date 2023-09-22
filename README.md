# Lincoln

## Data pipeline

### Preprocessing: (helpers/preprocessing.py)
For the preprocessing I used pandas, I removed the null values, normalized the date format and cleaned the text from non utf-8 characters. Also, for the drugs file I removed the lignes where the atccode doesn't follow the right format.

### Feeding the database: (helpers/db_feeder.py)
Being unable to run docker on my laptop, I setup a postgres db locally and fed the data to it using pydantic models and sqlalchemy. This also helps in adding a layer of data validation before inserting the data in the table.

### Data pipeline: (helpers/json_generator.py)
Since I was unable to setup docker on my laptop, the hyper-v backend wan't working, and when attempting to use the wsl2 based engine it takes too much ram and eventually crashes, so I only started the setup for airflow, but as you can see, with a prefilled database one simple query can do the trick, then you can use a Python operator to run the generate_json function, or on a larger scale, you can simple use something like a BigQueryInsertJobOperator to store the result of the query in a temporary table and then extract the table either locally or directly on GCS for example.

### Postprocessing: (adhoc.py)

Running this file will give you the journal mentioning the most drugs.

### Take it further:

To improve the performance of the code, first of all we'd need:
 - a database that's more equipped to handle large volumes of data (bigquery for example).
 - Setup airflow environment, add the deploy step in the jenkins and setup jenkins (if that's what we'll go with) and add a deployment configuration.
 - Use the generate_json or the query from within a dag, as I explained before, we'd need one operator to save the result of the query in a temporary table and another to extract the result either to a local folder or to an object store like GCS.
 - If the population of the database is also supposed to be handled by the dag, then I would have it done separately in a different dag, with one task for each table, using a PythonOperator to run the populate table function.

 ## SQL

 The queries for the first and second part of the test are in the sql1.sql and sql2.sql files respectively.

