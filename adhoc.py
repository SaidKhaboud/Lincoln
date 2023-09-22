import json

# Create a dictionary to store the citation counts for each journal
journal_citations = {}

# Load the JSON data from the file
with open("output.ndjson", "r") as file:
    for line in file:
        data = json.loads(line)
        # Iterate through the data and count citations
        drug = data["drug"]
        pubmed_titles = data.get("pubmed_titles", [])
        clinical_trials = data.get("clinical_trials", [])
        journals = {
            article.get("journal", "Unknown")
            for article in pubmed_titles + clinical_trials
        }
        journals.discard("unknown")
        journals.discard(None)
        for journal in journals:
            if journal in journal_citations:
                journal_citations[journal] += 1
            else:
                journal_citations[journal] = 1

# Find the journal with the most citations
most_cited_journal = max(journal_citations, key=journal_citations.get)

# Print the most cited journal and its citation count
print(
    f"The most cited journal is '{most_cited_journal}' with {journal_citations[most_cited_journal]} citations."
)
