import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
connection_obj = sqlite3.connect('HarrisburgResources.db')

# Create a cursor object to interact with the database
cursor_obj = connection_obj.cursor()

# Drop the data Extractions table if it already exists (for clean setup)
cursor_obj.execute("DROP TABLE IF EXISTS DataExtractions")

# SQL query to create the table
table_creation_query = """
    CREATE TABLE DataExtractions (
        Resource VARCHAR(255),
        Summary VARCHAR(255),
        ExtractedData VARCHAR(255),
        MetaData VARCHAR(255)
    );
"""

# Execute the table creation query
cursor_obj.execute(table_creation_query)

# Confirm that the table has been created
print("Table is Ready")

# Close the connection to the database
connection_obj.close()