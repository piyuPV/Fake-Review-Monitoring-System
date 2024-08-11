# Fake-Review-Monitoring-System
In this project, we are monitoring if the given review is Fake or Genuine using a text data and Spam model.
We are using Spam detection machine learning model 
Saving data in v.h5 and senti_model_rf.h5 file using those hdfs files in app.py(Streamlit) file to access the model.

v.h5 is provided for senti_model_rf.h5 run the jupyter notebook and save the model 

customer_data.txt is the data file which includes the verified customer name and bill numbers
To add new a function is added in app.py to add more customers.

if a customer is not in that data and try to add review will result as fake review.

![image](https://github.com/user-attachments/assets/20b75978-20de-436b-8d3b-36843660d9ab)
