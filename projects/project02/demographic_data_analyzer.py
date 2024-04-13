import pandas as pd


def calculate_demographic_data(print_data=True):
  # Read data from file
  csv_file_path = './adult.data.csv'
  df = pd.read_csv(csv_file_path)

  # How many of each race are represented in this dataset?
  # This should be a Pandas series with race names as the index labels.
  race_count = df['race'].value_counts()

  # What is the average age of men?
  men = df[df['sex'] == 'Male']
  average_age_men = men['age'].mean()
  average_age_men = round(average_age_men, 1)

  # What is the percentage of people who have a Bachelor's degree?
  education = df['education']
  percentage_education = education.value_counts(normalize=True) * 100
  percentage_bachelors = percentage_education['Bachelors']
  percentage_bachelors = round(percentage_bachelors, 1)

  # What percentage of people with advanced education
  # (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
  # What percentage of people without advanced education make more than 50K?

  # with and without `Bachelors`, `Masters`, or `Doctorate`
  higher_education = df.loc[df['education'].isin(
      ['Bachelors', 'Masters', 'Doctorate'])]
  higher_education = round(higher_education, 1)

  lower_education = df.loc[~df['education'].
                           isin(['Bachelors', 'Masters', 'Doctorate'])]
  lower_education = round(lower_education, 1)

  # percentage with salary >50K
  higher_ed_salary = higher_education['salary']
  higher_ed_percentage = higher_ed_salary.value_counts(normalize=True) * 100
  higher_education_rich = higher_ed_percentage['>50K']
  higher_education_rich = round(higher_education_rich, 1)

  lower_ed_salary = lower_education['salary']
  lower_ed_percentage = lower_ed_salary.value_counts(normalize=True) * 100
  lower_education_rich = lower_ed_percentage['>50K']
  lower_education_rich = round(lower_education_rich, 1)

  # What is the minimum number of hours a person works per week
  # (hours-per-week feature)?
  min_work_hours = df['hours-per-week'].min()

  # What percentage of the people who work the minimum number of hours per week
  # have a salary of >50K?
  num_min_workers = df.loc[df['hours-per-week'] == 1]

  min_workers_salary = num_min_workers['salary']
  min_workers_percentage = min_workers_salary.value_counts(
      normalize=True) * 100
  rich_percentage = min_workers_percentage['>50K']

  # What country has the highest percentage of people that earn >50K?
  countries = df.groupby('native-country')['salary'].value_counts(
      normalize=True).unstack().fillna(0)
  countries_rich = countries['>50K'] * 100
  countries_rich_series = pd.Series(countries_rich)

  highest_earning_country = countries_rich_series.idxmax()
  highest_earning_country_percentage = countries_rich.max()
  highest_earning_country_percentage = round(
      highest_earning_country_percentage, 1)

  # Identify the most popular occupation for those who earn >50K in India.
  india = df[df['native-country'] == 'India']
  india_rich = india[india['salary'] == '>50K']
  india_rich_occupations = india_rich['occupation'].value_counts()
  top_IN_occupation = india_rich_occupations.idxmax()

  # DO NOT MODIFY BELOW THIS LINE

  if print_data:
    print("Number of each race:\n", race_count)
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(
        f"Percentage with higher education that earn >50K: {higher_education_rich}%"
    )
    print(
        f"Percentage without higher education that earn >50K: {lower_education_rich}%"
    )
    print(f"Min work time: {min_work_hours} hours/week")
    print(
        f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
    )
    print("Country with highest percentage of rich:", highest_earning_country)
    print(
        f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
    )
    print("Top occupations in India:", top_IN_occupation)

  return {
      'race_count': race_count,
      'average_age_men': average_age_men,
      'percentage_bachelors': percentage_bachelors,
      'higher_education_rich': higher_education_rich,
      'lower_education_rich': lower_education_rich,
      'min_work_hours': min_work_hours,
      'rich_percentage': rich_percentage,
      'highest_earning_country': highest_earning_country,
      'highest_earning_country_percentage': highest_earning_country_percentage,
      'top_IN_occupation': top_IN_occupation
  }