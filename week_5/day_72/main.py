import pandas as pd

pd.options.display.float_format = '{:,.2f}'.format

df = pd.read_csv('salaries_by_college_major.csv')

clean_df = df.dropna()

highest_salary_index = clean_df['Starting Median Salary'].idxmax()
highest_salary = clean_df['Starting Median Salary'].max()
highest_salary_major = clean_df['Undergraduate Major'][highest_salary_index]
# highest_salary_major = clean_df.loc[highest_salary]

print(f"The highest starting salary is as a {highest_salary_major} at {highest_salary}\n")
# highest mid-career salary
highest_mid_career_salary_index = clean_df['Mid-Career Median Salary'].idxmax()
highest_mid_career_salary = clean_df['Mid-Career Median Salary'].max()
highest_mid_career_salary_major = clean_df['Undergraduate Major'][highest_mid_career_salary_index]

print(f"the highest mid career salary is {highest_mid_career_salary_major} at {highest_mid_career_salary}\n")

# lowest starting salary
lowest_start_salary = clean_df['Starting Median Salary'].min()
lowest_start_salary_index = clean_df['Starting Median Salary'].idxmin()
lowest_start_major = clean_df['Undergraduate Major'][lowest_start_salary_index]

print(f"The lowest starting salary is {lowest_start_major} at {lowest_start_salary}\n")

#lowest Risk majors
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)

low_risk = clean_df.sort_values('Spread')
print("\nThe majors with the lowest risk")
print(low_risk[['Undergraduate Major', 'Spread']].head())

#degrees with the greatest spread
high_risk = clean_df.sort_values('Spread', ascending=False)
print("\nThe majors with the greatest risk")
print(high_risk[['Undergraduate Major', 'Spread']].head())

#degree with the highest potential
highest_potential_salary = clean_df['Mid-Career 90th Percentile Salary'].max()
highest_potential_salary_index = clean_df['Mid-Career 90th Percentile Salary'].idxmax()
highest_potential_major = clean_df['Undergraduate Major'][highest_potential_salary_index]

print(f"\nThe degree with the highest potential earning is {highest_potential_major}\nat a mid career 90th Percentile salary of {highest_potential_salary}")

group = clean_df.groupby('Group').count()
print(group)

mean = clean_df.groupby('Group').mean(numeric_only=True)
print(mean)


