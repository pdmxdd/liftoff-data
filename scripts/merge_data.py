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

print(lo_data.head(1))
print(lo_data.columns.values)

lo_data.to_csv("/home/paulmint/liftoff_data/csv/clean/merged/liftoff_data.csv")