import csv
import sqlite3
import pandas as pd
from django.db import models
from ecom.models import Project

df = pd.read_csv('positive.csv')
df = df.drop(28,index=1)
print(df)
# connection = sqlite3.connect('db.sqlite3')
# df.to_sql('ecom_project',connection,if_exist='replace',index=false)


# def transfer_csv_data_to_database(csv_file_path):
#     with open(csv_file_path, "r") as csv_file:
#         reader = csv.reader(csv_file)

#         # Skip the header row
#         next(reader)

#         for row in reader:
#             project = Project()
#             project.project_id = row[0]
#             project.project_name = row[1]
#             project.voluntary_registry = row[2]
#             project.voluntary_status = row[3]
#             project.scope = row[4]
#             project.type = row[5]
#             project.reduction_removal = row[6]
#             project.methodology_protocol = row[7]
#             project.region = row[8]
#             project.documents = row[9]
#             project.country = row[10]
#             project.state = row[11]
#             project.project_site_location = row[12]
#             project.project_developer = row[13]
#             project.total_credits_issued = row[14]
#             project.total_credits_retired = row[15]
#             project.total_credits_remaining = row[16]
#             project.ccb_certifications = row[17]
#             project.project_owner = row[18]
#             project.offset_project_operator = row[19]
#             project.authorized_project_designee = row[20]
#             project.verifier = row[21]
#             project.registry_arb = row[22]
#             project.project_listed = row[23]
#             project.project_registered = row[24]
#             project.project_type = row[25]
#             project.registry_documents = row[26]
#             project.project_website = row[27]

#             project.save()

# if __name__ == "__main__":
#     csv_file_path = "c:/Users/publi/Desktop/positive.csv"
#     transfer_csv_data_to_database(csv_file_path)
