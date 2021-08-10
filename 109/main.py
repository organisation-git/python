import pandas as pd
import statistics
import csv

df = pd.read_csv("StudentsPerformance.csv")
read_list = df['reading score'].to_list()


read_mean = statistics.mean(read_list)
read_std_deviation = statistics.stdev(read_list)


# 1, 2, 3 standard deviation for read
read_first_std_deviation_start, read_first_std_deviation_end = read_mean-(read_std_deviation), read_mean+(read_std_deviation)
read_second_std_deviation_start, read_second_std_deviation_end = read_mean-(2*read_std_deviation), read_mean+(2*read_std_deviation)
read_third_std_deviation_start, read_third_std_deviation_end = read_mean-(3*read_std_deviation), read_mean+(3*read_std_deviation)

# percentage of data within 1, 2, 3 standard deviation for read
read_list_of_data_within_1_std_deviation = [result for result in read_list if result > read_first_std_deviation_start and result < read_first_std_deviation_end]
read_list_of_data_within_2_std_deviation = [result for result in read_list if result > read_second_std_deviation_start and result < read_second_std_deviation_end]
read_list_of_data_within_3_std_deviation = [result for result in read_list if result > read_third_std_deviation_start and result < read_third_std_deviation_end]
# print data for read and the weight

print(f"{len(read_list_of_data_within_1_std_deviation) * 100.0 / len(read_list)}% of data for read lies within 1 std dev")
print(f"{len(read_list_of_data_within_2_std_deviation) * 100.0 / len(read_list)}% of data for read lies within 2 std dev")
print(f"{len(read_list_of_data_within_3_std_deviation) * 100.0 / len(read_list)}% of data for read lies within 3 std dev")
