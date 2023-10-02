from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string, 
  connect_args={
    "ssl": {
      "?ssl_ca": "/etc/ssl/cert.pem"
    }
  }
)

# with engine.connect() as conn:
#   result = conn.execute(text("select * from jobs"))
#   # Fetch all rows from the result as a list of dictionaries
#   rows = result.fetchall()
  
#   # Get the column names from the result
#   column_names = result.keys()
  
#   # Initialize an empty list to store the dictionaries
#   result_list = []
  
#   # Iterate through the rows and build dictionaries
#   for row in rows:
#     row_dict = {}
#     for col_name, value in zip(column_names, row):
#         row_dict[col_name] = value
#     result_list.append(row_dict)
  
# print(result_list)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    
  jobs = []
  column_names = result.keys()
  for row in result.all():
    row_dict = {}
    for col_name, value in zip(column_names, row):
      row_dict[col_name] = value
    jobs.append(row_dict)

  return jobs
