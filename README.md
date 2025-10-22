# ELevate-labs-task1
Task 1 - Data Cleaning and Preprocessing
Overview

This project performs data cleaning and preprocessing on the Customer Personality Analysis dataset (marketing_campaign.csv). The dataset is prepared for further analysis or modeling by handling missing values, standardizing text, and correcting data types.

Dataset:

Name: Customer Personality Analysis

Source: Kaggle

File: marketing_campaign.csv (tab-separated)

--Steps Performed

1.Load Dataset

Read CSV file using pandas.

Checked initial shape and column info.

2.Identify and Handle Missing Values

Checked missing values per column.

Removed rows containing null values using dropna().

3.Remove Duplicate Rows

Ensured dataset uniqueness using drop_duplicates().

4.Standardize Text Values

Trimmed spaces and converted all text to lowercase.

Standardized categorical columns like:

    marital_status (e.g., "together" → "married")

    education (e.g., "2n cycle" → "secondary")

5.Convert Date Formats

       Converted Dt_Customer column to datetime format.

6.Rename Columns

Lowercased column names and replaced spaces with underscores.

7.Check and Fix Data Types

Converted numeric columns to appropriate types:

     year_birth → integer

    income → float

8.Save Cleaned Dataset

Saved the cleaned data as cleaned_customer_personality.csv.

Output:

Cleaned Dataset: cleaned_customer_personality.csv


🔧 Libraries Used

pandas – for data manipulation and cleaning.
