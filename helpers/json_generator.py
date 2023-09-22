from sqlalchemy import create_engine, text
import json

# Create an SQLAlchemy engine
engine = create_engine("postgresql://postgres:coco@localhost:5432/postgres")

# Define the SQL query
sql_query = text(
    """
    SELECT
    d.drug AS drug,
    ARRAY_AGG(
        JSONB_BUILD_OBJECT(
            'title', s.scientific_title,
            'journal', s.journal,
            'date', s.date
        )
    ) AS scientific_titles,
    ARRAY_AGG(
        JSONB_BUILD_OBJECT(
            'scientific_title', p.title,
            'journal', p.journal,
            'date', p.date
        )
    ) AS pubmed_titles
FROM
    drugs AS d
LEFT JOIN
    scientific AS s ON s.scientific_title ILIKE '%' || d.drug || '%'
LEFT JOIN
    pubmed AS p ON p.title ILIKE '%' || d.drug || '%'
GROUP BY
    d.drug;

"""
)


def generate_json():
    # Create a database connection and execute the query
    with engine.connect() as connection:
        result = connection.execute(sql_query)

        with open("output.ndjson", "w") as f:
            # Fetch and write the results
            for row in result:
                drug, scientific_titles, pubmed_titles = row
                data = {
                    "drug": drug,
                    "clinical_trials": scientific_titles,
                    "pubmed_titles": pubmed_titles,
                }
                json.dump(data, f)
                f.write("\n")


if __name__ == "__main__":
    generate_json()
