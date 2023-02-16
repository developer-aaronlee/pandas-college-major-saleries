import pandas as pd

df = pd.read_csv("salaries_by_college_major.csv")

top_5_rows = df.head()
# print(top_5_rows)

rows_and_columns = df.shape
# print(rows_and_columns)

column_names = df.columns
# print(column_names)

nan_values = df.isna()
# print(nan_values)

last_5_rows = df.tail()
# print(last_5_rows)

clean_df = df.dropna()
# print(clean_df.tail())

starting_median_salary = clean_df["Starting Median Salary"]
# print(starting_median_salary)
highest_starting_salary = clean_df["Starting Median Salary"].max()
# print(highest_starting_salary)

highest_starting_salary_index = clean_df["Starting Median Salary"].idxmax()
# print(highest_starting_salary_index)
# highest_starting_salary_major = clean_df['Undergraduate Major'].loc[43]
highest_starting_salary_major = clean_df['Undergraduate Major'][43]
# print(highest_starting_salary_major)

highest_starting_salary_row = clean_df.loc[43]
# print(highest_starting_salary_row)

highest_mid_salary = clean_df["Mid-Career Median Salary"].max()
# print(highest_mid_salary)
highest_mid_salary_index = clean_df["Mid-Career Median Salary"].idxmax()
# print(highest_mid_salary_index)
highest_mid_salary_major = clean_df["Undergraduate Major"].loc[8]
# print(highest_mid_salary_major)

lowest_starting_salary = clean_df["Starting Median Salary"].min()
# print(lowest_starting_salary)
lowest_starting_salary_index = clean_df["Starting Median Salary"].idxmin()
# print(lowest_starting_salary_index)
lowest_starting_salary_major = clean_df["Undergraduate Major"][49]
# print(lowest_starting_salary_major)

lowest_mid_salary = clean_df["Mid-Career Median Salary"].min()
# print(lowest_mid_salary)
lowest_mid_salary_index = clean_df["Mid-Career Median Salary"].idxmin()
# print(lowest_mid_salary_index)
lowest_mid_salary_major = clean_df["Undergraduate Major"][18]
# print(lowest_mid_salary_major)

# mid_salary_difference = clean_df["Mid-Career 90th Percentile Salary"] - clean_df["Mid-Career 10th Percentile Salary"]
mid_salary_difference = clean_df["Mid-Career 90th Percentile Salary"].subtract(clean_df["Mid-Career 10th Percentile Salary"])
# print(mid_salary_difference)

clean_df.insert(1, "Spread", mid_salary_difference)
# print(clean_df.head())

# clean_df.drop("Spread", axis=1)
# print(clean_df.columns)

# low_risk = clean_df.sort_values(by="Spread", ascending=True)
# print(low_risk[["Undergraduate Major", "Spread"]].head())

# high_potential = clean_df.sort_values(by="Mid-Career 90th Percentile Salary", ascending=False)
# print(high_potential[["Undergraduate Major", "Mid-Career 90th Percentile Salary"]].head())

# greatest_spread = clean_df.sort_values(by="Spread", ascending=False)
# print(greatest_spread[["Undergraduate Major", "Spread"]].head())

# total_majors = clean_df.groupby("Group").count()
# print(total_majors)

pd.options.display.float_format = "{:,.2f}".format

group_avg_salary = clean_df.groupby("Group").mean(numeric_only=True)
print(group_avg_salary)

