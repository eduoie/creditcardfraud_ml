##################################
# Code for the AWS Lambda function
##################################

import json

import pandas as pd
import numpy as np
import datetime

from io import StringIO
import boto3
import simulated_data_generation

s3 = boto3.resource('s3')
bucket_name = "creditcardfraud-project"
s3_path = "simulated_data/data"


def lambda_handler(event, context):
    customer_profiles_table, terminal_profiles_table, transactions_df = \
        simulated_data_generation.generate_dataset(n_customers=2500,
                                                   n_terminals=5000,
                                                   nb_days=5,  # 183
                                                   start_date="2018-04-01",
                                                   r=5)

    transactions_df = simulated_data_generation.add_frauds(customer_profiles_table, terminal_profiles_table,
                                                           transactions_df)
    print('transactions_df shape: ', transactions_df.shape)

    start_date = datetime.datetime.strptime("2018-04-01", "%Y-%m-%d")

    for day in range(transactions_df.TX_TIME_DAYS.max() + 1):
        transactions_day = transactions_df[transactions_df.TX_TIME_DAYS == day].sort_values('TX_TIME_SECONDS')
        date = start_date + datetime.timedelta(days=day)
        filename_output = date.strftime("%Y-%m-%d") + '.csv'

        csv_buffer = StringIO()
        transactions_day.to_csv(csv_buffer)
        s3.Bucket(bucket_name).put_object(Key=s3_path + filename_output, Body=csv_buffer.getvalue())

    return {
        'statusCode': 200,
        'body': 'written files'
    }
