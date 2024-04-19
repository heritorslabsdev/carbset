import pandas as pd
import numpy as np


def remove_special_characters(string):
  """Removes all commas and other special characters from a string.

  Args:
    string: The string to remove special characters from.

  Returns:
    A string with all commas and other special characters removed.
  """

  # Create a list of all the characters to remove.
  special_characters = [",", ".", "!", "?", ":", ";", "-", "_", "/", "\\", "(", ")", "[", "]", "{", "}", "<", ">"]

  # Remove all of the special characters from the string.
  for character in special_characters:
    string = string.replace(character, "")

  # Return the string with all special characters removed.
  return string

def remove_data_with_low_credits_remaining_after_removing_special_characters(input_csv_file_path, output_csv_file_path):
  """Removes all commas and other special characters from the Total Credits Remaining and Total Credits Issued columns in a CSV file, and then removes all rows where the Total Credits Remaining value is lower than 10% of the Total Credits Issued value.

  Args:
    input_csv_file_path: The path to the input CSV file.
    output_csv_file_path: The path to the output CSV file.
  """

  # Read the input CSV file into a Pandas DataFrame.
  df = pd.read_csv(input_csv_file_path)

  # Remove all of the special characters from the Total Credits Remaining and Total Credits Issued columns.
  df["Total Credits Remaining"] = df["Total Credits Remaining"].apply(remove_special_characters)
  df["Total Credits Issued"] = df["Total Credits Issued"].apply(remove_special_characters)

  # Convert the Total Credits Remaining and Total Credits Issued columns to numeric values.
  df["Total Credits Remaining"] = pd.to_numeric(df["Total Credits Remaining"])
  df["Total Credits Issued"] = pd.to_numeric(df["Total Credits Issued"])

  # Calculate 10% of the total credit issued.
  df["10% of Total Credits Issued"] = df["Total Credits Issued"] * 0.1

  # Filter the DataFrame to only include rows where the credit remaining value is greater than or equal to 10% of the total credit issued.
  df_filtered = df[df["Total Credits Remaining"] >= df["10% of Total Credits Issued"]]

  # Write the filtered DataFrame to the output CSV file.
  df_filtered.to_csv(output_csv_file_path, index=False)

if __name__ == "__main__":
  # Specify the path to the input CSV file and the output CSV file.
  input_csv_file_path = "c:/Users/publi/Desktop/negative.csv"
  output_csv_file_path = "c:/Users/publi/Desktop/positive.csv"

  # Remove all of the commas and other special characters from the Total Credits Remaining and Total Credits Issued columns in the CSV file, and then remove all rows where the Total Credits Remaining value is lower than 10% of the Total Credits Issued value.
  remove_data_with_low_credits_remaining_after_removing_special_characters(input_csv_file_path, output_csv_file_path)
