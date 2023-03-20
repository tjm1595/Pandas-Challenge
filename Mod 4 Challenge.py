#!/usr/bin/env python
# coding: utf-8

# In[117]:


import pandas as pd


# In[118]:


school_data_load = "SchoolsComplete.csv"
student_data_load = "StudentsComplete.csv"


# In[119]:


school_data = pd.read_csv(school_data_load)
student_data = pd.read_csv(student_data_load)


# In[120]:


data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
data_complete.head()


# In[121]:


school_count = data_complete["school_name"].nunique()
school_count


# In[122]:


student_count = len(data_complete)
student_count


# In[123]:


total_budget = data_complete.groupby(["school_name"]).max()["budget"]
total_budgets = total_budget.sum()
total_budgets


# In[124]:


average_math_score = data_complete["math_score"].mean()
average_math_score


# In[125]:


average_reading_score = data_complete["reading_score"].mean()
average_reading_score


# In[126]:


passing_math_count = data_complete[(data_complete["math_score"] >= 70)].count()["student_name"]
passing_math_percentage = passing_math_count / float(student_count) * 100
passing_math_percentage


# In[127]:


passing_reading_count = data_complete[(data_complete["reading_score"] >= 70)].count()["student_name"]
passing_reading_percentage = passing_reading_count / float(student_count) * 100
passing_reading_percentage


# In[128]:


passing_scores_count = data_complete[
    (data_complete["math_score"] >= 70) & (data_complete["reading_score"] >= 70)
].count()["student_name"]
overall_pass_rate = passing_scores_count / float(student_count) * 100
overall_pass_rate


# In[129]:


district_summary = pd.DataFrame(
{"Number of Schools" : [15], "Number of Students" : [39170], "Total District Budget" : [24649428], "Avg. Math Score" : [78.98], "Avg. Reading Score" : [81.87], "% Passing Math" : [74.98], "% Passing Reading" : [85.8], "% Passsing Math & Reading" : [65.17]},
index = [0])
district_summary["Number of Students"] = district_summary["Number of Students"].map("{:,}".format)
district_summary["Total District Budget"] = district_summary["Total District Budget"].map("${:,.2f}".format)
district_summary.head()


# In[138]:


school_types = school_data.set_index(["school_name"])["type"]
school_types


# In[131]:


per_school_counts = student_data.groupby("school_name").count()["student_name"]
per_school_counts


# In[132]:


per_school_budget = data_complete.groupby(["school_name"]).mean()["budget"]
per_school_capita = per_school_budget / per_school_counts
per_school_capita


# In[18]:


per_school_math = data_complete.groupby(["school_name"]).mean()["math_score"]
per_school_math


# In[19]:


per_school_reading = data_complete.groupby(["school_name"]).mean()["reading_score"]
per_school_reading


# In[52]:


school_passing_math = per_school_math[per_school_math >= 70].count()
school_passing_math


# In[21]:


school_passing_reading = per_school_reading[per_school_reading >= 70].count()
school_passing_reading


# In[210]:


passing_math_and_reading = data_complete[
    (data_complete["reading_score"] >= 70) & (data_complete["math_score"] >= 70)
]

passing_math_df = data_complete[(data_complete["math_score"] >= 70)]
passing_math = passing_math_df.groupby(["school_name"]).count()["student_name"]


passing_reading_df = data_complete[(data_complete["reading_score"] >= 70)]
passing_reading = passing_reading_df.groupby(["school_name"]).count()["student_name"]

 


# In[212]:


per_school_passing_math = passing_math / per_school_counts * 100
per_school_passing_reading = passing_reading / per_school_counts * 100
overall_passing_rate = passing_math_and_reading.groupby(["school_name"]).count()["student_name"] / per_school_counts * 100


# In[214]:


# Create a DataFrame called `per_school_summary` with columns for the calculations above.
per_school_summary = pd.DataFrame({"School Type": school_types, "Total Students": per_school_counts, "Total School Budget": per_school_budget, "Per Student Budget": per_school_capita, "Avg Math Score": per_school_math, "Avg Reading Score": per_school_reading, "% Passing Math": per_school_passing_math, "% Passing Reading": per_school_passing_reading, "Overall Passing Rate": overall_passing_rate
}, index=['Bailey High School', 'Cabrera High School',  
'Figueroa High School',     
'Ford High School',         
'Griffin High School',    
'Hernandez High School',    
'Holden High School',       
'Huang High School',             
'Johnson High School',
'Pena High School',    
'Rodriguez High School',    
'Shelton High School',     
'Thomas High School',     
'Wilson High School',      
'Wright High School'])

# Formatting
per_school_summary["Total School Budget"] = per_school_summary["Total School Budget"].map("${:,.2f}".format)
#per_school_summary["Per Student Budget"] = per_school_summary["Per Student Budget"].map("${:,.2f}".format)

# Display the DataFrame
per_school_summary


# In[215]:


# Sort the schools by `% Overall Passing` in descending order and display the top 5 rows.
per_school_summary.sort_values('Overall Passing Rate', ascending=False)


# In[216]:


# Sort the schools by `% Overall Passing` in ascending order and display the top 5 rows.
per_school_summary.sort_values('Overall Passing Rate', ascending=True)


# In[217]:


# Use the code provided to separate the data by grade
ninth_graders = data_complete[(data_complete["grade"] == "9th")]
tenth_graders = data_complete[(data_complete["grade"] == "10th")]
eleventh_graders = data_complete[(data_complete["grade"] == "11th")]
twelfth_graders = data_complete[(data_complete["grade"] == "12th")]

# Group by "school_name" and take the mean of each.
ninth_graders_scores = ninth_graders.groupby(["school_name"]).mean()
tenth_graders_scores = tenth_graders.groupby(["school_name"]).mean()
eleventh_graders_scores = eleventh_graders.groupby(["school_name"]).mean()
twelfth_graders_scores = twelfth_graders.groupby(["school_name"]).mean()

# Use the code to select only the `math_score`.
ninth_grader_math_scores = ninth_graders_scores["math_score"]
tenth_grader_math_scores = tenth_graders_scores["math_score"]
eleventh_grader_math_scores = eleventh_graders_scores["math_score"]
twelfth_grader_math_scores = twelfth_graders_scores["math_score"]

# Combine each of the scores above into single DataFrame called `math_scores_by_grade`
#math_scores_by_grade = pd.concat([ninth_grader_math_scores, tenth_grader_math_scores, eleventh_grader_math_scores, twelfth_grader_math_scores], axis=1)
math_scores_by_grade = pd.DataFrame(
    {"9th Grade": ninth_grader_math_scores, 
     "10th Grade": tenth_grader_math_scores,
     "11th Grade": eleventh_grader_math_scores,
     "12th Grade": twelfth_grader_math_scores},
index=['Bailey High School', 'Cabrera High School',  
'Figueroa High School',     
'Ford High School',         
'Griffin High School',    
'Hernandez High School',    
'Holden High School',       
'Huang High School',             
'Johnson High School',
'Pena High School',    
'Rodriguez High School',    
'Shelton High School',     
'Thomas High School',     
'Wilson High School',      
'Wright High School'])

# Minor data wrangling
math_scores_by_grade.index.name = None

# Display the DataFrame
math_scores_by_grade


# In[218]:


# Use the code provided to separate the data by grade
ninth_graders = data_complete[(data_complete["grade"] == "9th")]
tenth_graders = data_complete[(data_complete["grade"] == "10th")]
eleventh_graders = data_complete[(data_complete["grade"] == "11th")]
twelfth_graders = data_complete[(data_complete["grade"] == "12th")]

# Group by "school_name" and take the mean of each.
ninth_graders_scores = ninth_graders.groupby(["school_name"]).mean()
tenth_graders_scores = tenth_graders.groupby(["school_name"]).mean()
eleventh_graders_scores = eleventh_graders.groupby(["school_name"]).mean()
twelfth_graders_scores = twelfth_graders.groupby(["school_name"]).mean()

# Use the code to select only the `reading_score`.
ninth_grader_reading_scores = ninth_graders_scores["reading_score"]
tenth_grader_reading_scores = tenth_graders_scores["reading_score"]
eleventh_grader_reading_scores = eleventh_graders_scores.mean()["reading_score"]
twelfth_grader_reading_scores = twelfth_graders_scores["reading_score"]

# Combine each of the scores above into single DataFrame called `reading_scores_by_grade`
reading_scores_by_grade = pd.DataFrame(
    {"9th Grade": ninth_grader_reading_scores, 
     "10th Grade": tenth_grader_reading_scores,
     "11th Grade": eleventh_grader_reading_scores,
     "12th Grade": twelfth_grader_reading_scores},
index=['Bailey High School', 'Cabrera High School',  
'Figueroa High School',     
'Ford High School',         
'Griffin High School',    
'Hernandez High School',    
'Holden High School',       
'Huang High School',             
'Johnson High School',
'Pena High School',    
'Rodriguez High School',    
'Shelton High School',     
'Thomas High School',     
'Wilson High School',      
'Wright High School'])
# Minor data wrangling
reading_scores_by_grade.index.name = None

# Display the DataFrame
reading_scores_by_grade


# In[233]:


# Establish the bins 
spending_bins = [0, 585, 630, 645, 680]
labels = ["<$585", "$585-630", "$630-645", "$645-680"]


# In[240]:


# Create a copy of the school summary since it has the "Per Student Budget" 
school_spending_df = per_school_summary.copy()
school_spending_df


# In[241]:


school_spending_df["Spending Ranges (Per Student)"] = pd.cut(school_spending_df["Per Student Budget"], spending_bins, labels=labels)


# In[254]:


spending_math_scores = school_spending_df.groupby(["Spending Ranges (Per Student)"]).mean()["Avg Math Score"]
spending_reading_scores = school_spending_df.groupby(["Spending Ranges (Per Student)"]).mean()["Avg Reading Score"]
spending_passing_math = school_spending_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Passing Math"]
spending_passing_reading = school_spending_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Passing Reading"]
overall_passing_spending = school_spending_df.groupby(["Spending Ranges (Per Student)"]).mean()["Overall Passing Rate"]


# In[247]:


spending_summary = pd.DataFrame({
    "Avg Math Scores": spending_math_scores,
    "Avg Reading Scores": spending_reading_scores,
    "% Passing Math": spending_passing_math,
    "% Passing Reading": spending_passing_reading,
    "Overall Passing %": overall_passing_spending}, 
index=["<$585", "$585-630", "$630-645", "$645-680"])
spending_summary


# In[245]:


size_bins = [0, 1000, 2000, 5000]
labels = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[246]:


per_school_summary["School Size"] = pd.cut(per_school_summary["Total Students"], size_bins, labels=labels)


# In[250]:


size_math_scores = per_school_summary.groupby(["School Size"]).mean()["Avg Math Score"]
size_reading_scores = per_school_summary.groupby(["School Size"]).mean()["Avg Reading Score"]
size_passing_math = per_school_summary.groupby(["School Size"]).mean()["% Passing Math"]
size_passing_reading = per_school_summary.groupby(["School Size"]).mean()["% Passing Reading"]
size_overall_passing = per_school_summary.groupby(["School Size"]).mean()["Overall Passing Rate"]


# In[252]:


size_summary = pd.DataFrame({
    "Avg Math Scores": size_math_scores,
    "Avg Reading Scores": size_reading_scores,
    "% Passing Math": size_passing_math,
    "% Passing Reading": size_passing_reading,
    "Overall Passing %": size_overall_passing}, 
index=["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"])
size_summary


# In[260]:


type_math_scores = per_school_summary.groupby(["School Type"]).mean()["Avg Math Score"]
type_reading_scores = per_school_summary.groupby(["School Type"]).mean()["Avg Reading Score"]
type_passing_math = per_school_summary.groupby(["School Type"]).mean()["% Passing Math"]
type_passing_reading = per_school_summary.groupby(["School Type"]).mean()["% Passing Reading"]
type_overall_passing = per_school_summary.groupby(["School Type"]).mean()["Overall Passing Rate"]


# In[261]:


type_summary = pd.DataFrame({
    "Avg Math Score": type_math_scores,
    "Avg Reading Score": type_reading_scores,
    "% Passing Math": type_passing_math, 
    "% Passing Reading": type_passing_reading,
    "% Overall Passing": type_overall_passing
}, index=["Charter", "District"])
type_summary


# In[ ]:




