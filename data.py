import statistics as st
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import csv

df = pd.read_csv("data.csv")
reading_score = df["reading score"].to_list()
writing_score = df["writing score"].to_list()

#statistics for reading score
reading_mean = st.mean(reading_score)
reading_median = st.median(reading_score)
reading_mode = st.mode(reading_score)
print("Mean, Median and Mode of reading score is {}, {} and {} respectively"
      .format(reading_mean, reading_median, reading_mode))

reading_std_deviation = st.stdev(reading_score)

#calculating range for 1st 2nd and 3rd std_dev

r_f_stdev_start, r_f_stdev_end = reading_mean-reading_std_deviation,reading_mean+reading_std_deviation
r_s_stdev_start, r_s_stdev_end = reading_mean-(2*reading_std_deviation),reading_mean+(2*reading_std_deviation)
r_t_stdev_start, r_t_stdev_end = reading_mean-(3*reading_std_deviation),reading_mean+(3*reading_std_deviation)

reading_list_of_data_within_1_std_deviation = [result for result in reading_score if result 
                                              > r_f_stdev_start and
                                                result < r_f_stdev_end]

reading_list_of_data_within_2_std_deviation = [result for result in reading_score if result 
                                              > r_s_stdev_start and
                                                result < r_s_stdev_end]

reading_list_of_data_within_3_std_deviation = [result for result in reading_score if result 
                                              > r_t_stdev_start and
                                                result < r_t_stdev_end]

print("{}% of data for reading score lies within 1 standard deviation".format
      (len(reading_list_of_data_within_1_std_deviation)*100.0/len(reading_score)))

print("{}% of data for reading score lies within 2 standard deviation".format
     (len(reading_list_of_data_within_2_std_deviation)*100.0/len(reading_score)))

print("{}% of data for reading score lies within 3 standard deviation".format
      (len(reading_list_of_data_within_3_std_deviation)*100.0/len(reading_score)))


#statistics for writing score
writing_mean = st.mean(writing_score)
writing_median = st.median(writing_score)
writing_mode = st.mode(writing_score)
print("Mean, Median, Mode of writing score is {}, {} and {} respectively"
      .format(writing_mean, writing_median, writing_mode))
writing_std_deviation = st.stdev(writing_score)

w_f_stdev_start, w_f_stdev_end = writing_mean-writing_std_deviation,writing_mean+writing_std_deviation
w_s_stdev_start, w_s_stdev_end = writing_mean-(2*writing_std_deviation),writing_mean+(2*writing_std_deviation)
w_t_stdev_start, w_t_stdev_end = writing_mean-(3*writing_std_deviation),writing_mean+(3*writing_std_deviation)

writing_list_of_data_within_1_std_deviation = [result for result in writing_score if result 
                                              > w_f_stdev_start and
                                                result < w_f_stdev_end]

writing_list_of_data_within_2_std_deviation = [result for result in writing_score if result 
                                              > w_s_stdev_start and
                                                result < w_s_stdev_end]

writing_list_of_data_within_3_std_deviation = [result for result in writing_score if result 
                                              > w_t_stdev_start and
                                                result < w_t_stdev_end]

print("{}% of data for writing score lies within 1 standard deviation".format
      (len(writing_list_of_data_within_1_std_deviation)*100.0/len(writing_score)))

print("{}% of data for writing score lies within 2 standard deviation".format
      (len(writing_list_of_data_within_2_std_deviation)*100.0/len(writing_score)))

print("{}% of data for writing score lies within 3 standard deviation".format
      (len(writing_list_of_data_within_3_std_deviation)*100.0/len(writing_score)))













