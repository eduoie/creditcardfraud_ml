## 1. Data generation

A Lambda function will be created to generate the data.

Given that you cannot install packages in Python for Lambda, we will resort to generate the layers.

1. Run get_layer_packages.sh to obtain a zip file with the required dependencies (check links below for more information on these steps)
2. Upload it to Lambda as a layer
3. Create a bucket to store the data
4. Allow Lambda execution role to access the S3 bucket: [instructions](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-execution-role-s3-bucket/) and [permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket.html)
5. Create a Lambda function and add `simulated_data_generation.py`, use `lambda_data_generation.py` for the main function. It is a modified version of the notebook code to generate simulated card transactions so it is compatible with AWS Lambda and S3.
6. Configure the function to allow to run for several minutes (around 5?)
7. Compute requirements seem to be too high for Lambda to process them on time. It is a better idea to use other service such as Batch. Given that is more complex, I will leave it for future iterations if needed and just upload the generated data locally to proceed further.

**References and links:**

https://stackoverflow.com/questions/36054976/pandas-aws-lambda

[How to Install Pandas on AWS Lambda Function](https://www.youtube.com/watch?v=1UDEp90S9h8)

https://medium.com/@qtangs/creating-new-aws-lambda-layer-for-python-pandas-library-348b126e9f3e

How to structure folders:
https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html#configuration-layers-path

Invoking lambda functions:
https://aws.amazon.com/blogs/architecture/understanding-the-different-ways-to-invoke-lambda-functions/

# 2. Feature engineering

