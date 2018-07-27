import pandas

# LIFTOFF NOVEMBER 2017 STL
lo_stl_nov_2017 = pandas.read_csv("/home/paulmint/liftoff_data/csv/clean/lo_2017_nov_stl.csv", header=0, index_col=0)
# print(lo_stl_nov_2017.head(2))
# print(list(lo_stl_nov_2017.columns.values))

# LIFTOFF JANUARY 2018 STL
lo_stl_jan_2018 = pandas.read_csv("/home/paulmint/liftoff_data/csv/clean/lo_2018_jan_stl.csv", header=0, index_col=0)
# print(lo_stl_jan_2018.head(2))
# print(list(lo_stl_jan_2018.columns.values))

# LIFTOFF MARCH 2018 STL
lo_stl_march_2018 = pandas.read_csv("/home/paulmint/liftoff_data/csv/clean/lo_2018_march_stl.csv", header=0, index_col=0)
# print(lo_stl_jan_2018.head(2))
# print(list(lo_stl_jan_2018.columns.values))

# LIFTOFF MARCH 2018 KC
lo_kc_march_2018 = pandas.read_csv("/home/paulmint/liftoff_data/csv/clean/lo_2018_march_kc.csv", header=0, index_col=0)
# print(lo_stl_jan_2018.head(2))
# print(list(lo_stl_jan_2018.columns.values))

# LIFTOFF MARCH 2018 TAMPA
lo_tampa_march_2018 = pandas.read_csv("/home/paulmint/liftoff_data/csv/clean/lo_2018_march_tampa.csv", header=0, index_col=0)
# print(lo_stl_jan_2018.head(2))
# print(list(lo_stl_jan_2018.columns.values))


# WRITE CLEAN DATA
lo_data = pandas.concat([lo_stl_nov_2017, lo_stl_jan_2018, lo_stl_march_2018, lo_kc_march_2018, lo_tampa_march_2018], sort=True)

# ADDS status to lo_data WILL NEED TO BE MANUALLY ENTERED
# status can be one of: enrolled, completed, dropped, withdrawn, ghosted or "no record"
lo_data['status'] = "no record"
lo_data = lo_data.drop(['current_score', 'current_points', 'final_score', 'final_points'], axis=1)
lo_data["project_deployment"] = "NA"

sorted_columns = [
    'student',
    'email',
    'status',
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
    'online_profiles',
    'live_coding',
    'mock_interview',
    'project_planning',
    'project_setup',
    'project_review',
    'project_presentation',
    'project_deployment'
]

lo_data = lo_data.reindex(sorted_columns, axis=1)
print(lo_data.head(1))
print(lo_data.columns.values)

lo_data.to_csv("/home/paulmint/liftoff_data/csv/clean/merged/liftoff_data.csv")