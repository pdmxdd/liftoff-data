import pandas
import os
# TODO: read in all LO CSVs
'''
headers = ["student", "canvas_user_id", "email",
           "attendance_class_1",
           "attendance_class_2",
           "attendance_class_3",
           "attendance_class_4",
           "attendance_class_5",
           "attendance_class_6",
           "attendance_class_7",
           "attendance_class_8",
           "code_of_conduct",
           "liftoff_agreement",
           "assignment_repository_setup",
           "project_outline",
           "project_planning",
           "online_profiles",
           "project_setup",
           "live_coding",
           "mock_interview",
           "proejct_presentation",
           "project_review"
           ]
'''
"""
good_cols = [0, 1, 3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
"""
lo_stl_nov_2017 = pandas.read_csv("/home/paulmint/liftoff_data/csv/liftoff_2017_novemeber_stl.csv", skiprows=[1], header=0, index_col=1)
lo_stl_jan_2018 = pandas.read_csv("/home/paulmint/liftoff_data/csv/liftoff_2018_january_stl.csv", skiprows=[1], header=0, index_col=1)
lo_kc_march_2018 = pandas.read_csv("/home/paulmint/liftoff_data/csv/liftoff_2018_march_stl.csv", skiprows=[1], header=0, index_col=1)
lo_stl_march_2018 = pandas.read_csv("/home/paulmint/liftoff_data/csv/liftoff_2018_march_stl.csv", skiprows=[1], header=0, index_col=1)
lo_tampa_march_2018 = pandas.read_csv("/home/paulmint/liftoff_data/csv/liftoff_2018_march_stl.csv", skiprows=[1], header=0, index_col=1)

# print(lo_stl_nov_2017.head(5))
# print(lo_stl_jan_2018.head(5))
# print(lo_kc_march_2018.head(5))
# print(lo_stl_march_2018.head(5))
# print(lo_tampa_march_2018.head(5))

# STL NOV DATA
print("-" * 40)
print("STL NOV 2017 DATA")
print(lo_stl_nov_2017.columns.values)

# TODO: clean data
nov_class_bad_cols = [
    'SIS User ID',
    'Section',
    '🐣 Class 1 Prep (3468)',
    '🐣 Class 2 Prep  (3470)',
    '🐣 Class 3 Prep (3472)',
    '🐣 Class 4 Prep (3474)',
    '🐣 Class 5 Prep (3476)',
    'Attend a Meetup (3624)',
    '🐣 Class Prep Current Points',
    '🐣 Class Prep Final Points',
    '🐣 Class Prep Current Score',
    '🐣 Class Prep Final Score',
    '🐥 Class Current Points',
    '🐥 Class Final Points',
    '🐥 Class Current Score',
    '🐥 Class Final Score',
    '🐹 Assignments Current Points',
    '🐹 Assignments Final Points',
    '🐹 Assignments Current Score',
    '🐹 Assignments Final Score'
]

lo_stl_nov_2017 = lo_stl_nov_2017.drop(nov_class_bad_cols, axis=1)
lo_stl_nov_2017["Class 7"] = 'NA'
lo_stl_nov_2017["Class 8"] = "NA"

# print(lo_stl_nov_2017.head(5))


# TODO: write clean data

nov_class_final_col_names = [
    'student',
    'email',
    'class_1_attendance',
    'class_2_attendance',
    'class_3_attendance',
    'class_4_attendance',
    'class_5_attendance',
    'class_6_attendance',
    'code_of_conduct',
    'liftoff_agreement',
    'assignment_repository_setup',
    'project_outline',
    'project_planning',
    'online_profiles',
    'project_setup',
    'live_coding',
    'mock_interview',
    'project_presentation',
    'project_review',
    'current_points',
    'final_points',
    'current_score',
    'final_score',
    'class_7_attendance',
    'class_8_attendance'
]

# TODO: write out to a new csv that's all cleaned up so we can merge them together
lo_stl_nov_2017.to_csv("/home/paulmint/liftoff_data/csv/clean/lo_2017_nov_stl.csv", header=nov_class_final_col_names)

print("-" * 40)
print("STL Jan 2018 DATA")

# clean data
jan_class_bad_cols = [
    'SIS User ID',
    'Section',
    'Class Prep Current Points',
    'Class Prep Final Points',
    'Class Prep Current Score',
    'Class Prep Final Score',
    'Class Current Points',
    'Class Final Points',
    'Class Current Score',
    'Class Final Score',
    'Assignments Current Points',
    'Assignments Final Points',
    'Assignments Current Score',
    'Assignments Final Score'
]

lo_stl_jan_2018 = lo_stl_jan_2018.drop(jan_class_bad_cols, axis=1)
lo_stl_jan_2018["code_of_conduct"] = "NA"
lo_stl_jan_2018["liftoff_agreement"] = "NA"
print(lo_stl_jan_2018.head(5))
print(list(lo_stl_jan_2018.columns.values))

# write clean data
jan_class_final_col_names = [
    'student',
    'email',
    'mock_interview',
    'live_coding',
    'online_profiles',
    'assignment_repository_setup',
    'project_planning',
    'project_outline',
    'project_setup',
    'project_review',
    'project_presentation',
    'class_1_attendance',
    'class_2_attendance',
    'class_3_attendance',
    'class_4_attendance',
    'class_5_attendance',
    'class_6_attendance',
    'class_7_attendance',
    'class_8_attendance',
    'current_points',
    'final_points',
    'current_score',
    'final_score',
    'code_of_conduct',
    'liftoff_agreement'
]
# write clean data
lo_stl_jan_2018.to_csv("/home/paulmint/liftoff_data/csv/clean/lo_2018_jan_stl.csv", header=jan_class_final_col_names)

print("-" * 40)
print("KC March 2018 DATA")
print(list(lo_kc_march_2018.columns.values))

# clean data
kc_march_class_bad_cols = [
    'SIS User ID',
    'Section',
    'Class Prep Current Points',
    'Class Prep Final Points',
    'Class Prep Current Score',
    'Class Prep Final Score',
    'Class Current Points',
    'Class Final Points',
    'Class Current Score',
    'Class Final Score',
    'Assignments Current Points',
    'Assignments Final Points',
    'Assignments Current Score',
    'Assignments Final Score',
    'Project Review 2 (5326)',
    'Liftoff to Ready for Placement Survey (5439)'
]

lo_kc_march_2018 = lo_kc_march_2018.drop(kc_march_class_bad_cols, axis=1)
print(len(list(lo_kc_march_2018.columns.values)))
print(list(lo_kc_march_2018.columns.values))

#print(list(lo_kc_march_2018.columns.values))


# write clean data
kc_march_final_col_names = [
    'student',
    'email',
    'class_1_attendance',
    'class_2_attendance',
    'class_3_attendance',
    'class_4_attendance',
    'class_5_attendance',
    'class_6_attendance',
    'class_7_attendance',
    'class_8_attendance',
    'code_of_conduct',
    'liftoff_agreement',
    'assignment_repository_setup',
    'project_outline',
    'project_planning',
    'live_coding',
    'project_setup',
    'online_profiles',
    'project_review',
    'mock_interview',
    'project_presentation',
    'current_points',
    'final_points',
    'current_score',
    'final_score'
]

lo_kc_march_2018.to_csv("/home/paulmint/liftoff_data/csv/clean/lo_2018_march_kc.csv", header=kc_march_final_col_names)

# STL MARCH DATA
print("-" * 40)
print("STL MARCH 2018 DATA")
print(list(lo_stl_march_2018.columns.values))

# clean data
stl_march_class_bad_cols = [
    'SIS User ID',
    'Section',
    'Class Prep Current Points',
    'Class Prep Final Points',
    'Class Prep Current Score',
    'Class Prep Final Score',
    'Class Current Points',
    'Class Final Points',
    'Class Current Score',
    'Class Final Score',
    'Assignments Current Points',
    'Assignments Final Points',
    'Assignments Current Score',
    'Assignments Final Score',
    'Project Review 2 (5326)',
    'Liftoff to Ready for Placement Survey (5439)'
]

lo_stl_march_2018 = lo_stl_march_2018.drop(stl_march_class_bad_cols, axis=1)

print(list(lo_stl_march_2018.columns.values))

# write clean data
stl_march_final_col_names = [
    'student',
    'email',
    'class_1_attendance',
    'class_2_attendance',
    'class_3_attendance',
    'class_4_attendance',
    'class_5_attendance',
    'class_6_attendance',
    'class_7_attendance',
    'class_8_attendance',
    'code_of_conduct',
    'liftoff_agreement',
    'assignment_repository_setup',
    'project_outline',
    'project_planning',
    'live_coding',
    'project_setup',
    'online_profiles',
    'project_review',
    'mock_interview',
    'project_presentation',
    'current_points',
    'final_points',
    'current_score',
    'final_score'
]

lo_stl_march_2018.to_csv("/home/paulmint/liftoff_data/csv/clean/lo_2018_march_stl.csv", header=stl_march_final_col_names)


# TAMPA MARCH DATA
print("-" * 40)
print("TAMPA MARCH 2018 DATA")

print(list(lo_tampa_march_2018.columns.values))

# CLEAN DATA
tampa_march_class_bad_cols = [
    'SIS User ID',
    'Section',
    'Class Prep Current Points',
    'Class Prep Final Points',
    'Class Prep Current Score',
    'Class Prep Final Score',
    'Class Current Points',
    'Class Final Points',
    'Class Current Score',
    'Class Final Score',
    'Assignments Current Points',
    'Assignments Final Points',
    'Assignments Current Score',
    'Assignments Final Score',
    'Project Review 2 (5326)',
    'Liftoff to Ready for Placement Survey (5439)'
]

lo_tampa_march_2018 = lo_tampa_march_2018.drop(tampa_march_class_bad_cols, axis=1)

print(list(lo_tampa_march_2018.columns.values))

# WRITE CLEAN DATA
tampa_march_final_col_names = [
    'student',
    'email',
    'class_1_attendance',
    'class_2_attendance',
    'class_3_attendance',
    'class_4_attendance',
    'class_5_attendance',
    'class_6_attendance',
    'class_7_attendance',
    'class_8_attendance',
    'code_of_conduct',
    'liftoff_agreement',
    'assignment_repository_setup',
    'project_outline',
    'project_planning',
    'live_coding',
    'project_setup',
    'online_profiles',
    'project_review',
    'mock_interview',
    'project_presentation',
    'current_points',
    'final_points',
    'current_score',
    'final_score'
]

lo_tampa_march_2018.to_csv("/home/paulmint/liftoff_data/csv/clean/lo_2018_march_tampa.csv", header=tampa_march_final_col_names)

# TODO: READ IN ALL CLEANED DATA and merge them
'''
print(lo_stl_nov_2017.info())
print(lo_stl_nov_2017['Student'])

# TODO: combine all CSVs into one new DataFrame
lo_data = pandas.concat([lo_stl_nov_2017, lo_stl_jan_2018, lo_stl_march_2018, lo_kc_march_2018, lo_tampa_march_2018])
print(lo_data['Student'])

# TODO: write out a new CSV that can be easily imported into SQL
lo_data.to_csv("liftoff_data.csv")
'''