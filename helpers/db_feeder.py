import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

from helpers.models import Drug, PubMed, Clinical_Trials


# Create an SQLAlchemy engine and session
engine = create_engine("postgresql://postgres:coco@localhost:5432/postgres")
Session = sessionmaker(bind=engine)
session = Session()

# Define an SQLAlchemy model for the database table
Base = declarative_base()


class PubMedTable(Base):
    __tablename__ = "pubmed"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    date = Column(String)
    journal = Column(String)


class ScientificTable(Base):
    __tablename__ = "scientific"
    id = Column(String, primary_key=True)
    scientific_title = Column(String)
    date = Column(String)
    journal = Column(String)


class DrugsTable(Base):
    __tablename__ = "drugs"
    atccode = Column(String, primary_key=True)
    drug = Column(String)


# Create the tables in the database
Base.metadata.create_all(engine)


def populate_table(table, file, model):

    # Read data from the CSV file into a Pandas DataFrame
    df = pd.read_csv(file)
    list_of_dicts = df.to_dict(orient="records")
    # Iterate over the DataFrame and insert data into the database
    for row in list_of_dicts:
        data = model(**row)
        try:
            # Validate the data using the Pydantic model
            data_dict = data.model_dump()
            database_row = table(**data_dict)
            session.add(database_row)
            session.commit()
        except Exception as e:
            print(f"Error: {e}")
            session.rollback()
    print("done!")
    return


tables = [DrugsTable, PubMedTable, ScientificTable]
files = ["curated_drugs.csv", "curated_pubmed.csv", "curated_clinical_trials.csv"]
models = [Drug, PubMed, Clinical_Trials]

for table, file, model in zip(tables, files, models):
    populate_table(table=table, file=file, model=model)
# Close the database session
session.close()
