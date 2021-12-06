## 1. Data generation

A Lambda function will be created to generate the data (the idea is to later use this function to generate additional data when the model is deployed)

Given that you cannot install packages in Python for Lambda, we will resort to generate the layers.

1. Run get_layer_packages.sh to obtain a zip file with the required dependencies (check links below for more information on these steps)
2. Upload it to Lambda as a layer
3. Create a bucket to store the data
4. Allow Lambda execution role to access the S3 bucket: [instructions](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-execution-role-s3-bucket/) and [permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket.html)
5. Create a Lambda function and add `simulated_data_generation.py`, use `lambda_data_generation.py` for the main function. It is a modified version of the notebook code to generate simulated card transactions so it is compatible with AWS Lambda and S3.
6. Configure the function to allow to run for several minutes (around 5?)
7. **Compute requirements seem to be too high for Lambda to process them on time**. It is a better idea to use other service such as Batch or SageMaker Processing. Given that is more complex, I will leave it for future iterations if needed and just upload the generated data locally to proceed further.

**References and links:**

[https://stackoverflow.com/questions/36054976/pandas-aws-lambda](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-introduction-notebook.html)

[How to Install Pandas on AWS Lambda Function](https://www.youtube.com/watch?v=1UDEp90S9h8)

[https://medium.com/@qtangs/creating-new-aws-lambda-layer-for-python-pandas-library-348b126e9f3e
](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-introduction-notebook.html)

How to structure folders:
[https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html#configuration-layers-path
](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-introduction-notebook.html)

Invoking lambda functions:
[https://aws.amazon.com/blogs/architecture/understanding-the-different-ways-to-invoke-lambda-functions/
](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-introduction-notebook.html)

# 2. Feature engineering

1. Created a notebook (used SageMaker Studio for this) to create a feature store. **Sagemaker needs an IAM role with attached policies for feature store and s3 (check video tutorial if needed.)**
2. Created a Data Wrangler job to explore the dataset and perform some transformations. (*make sure to stop the service when done, as it spawns a different instance for it*)
3. Decided to ingest and transform data using the notebook above instead for now.


**References and links**:

[https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-featurestore/feature_store_introduction.html](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-introduction-notebook.html)

[https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-introduction-notebook.html](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-introduction-notebook.html)

[https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_featurestore.html](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-introduction-notebook.html)

[Amazon SageMaker Feature Store Deep Dive Demo (YouTube)](https://www.youtube.com/watch?v=mHEUlPFT6xg)

[https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-athena-glue-integration.html](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-athena-glue-integration.html)

[https://aws.amazon.com/blogs/machine-learning/automate-feature-engineering-pipelines-with-amazon-sagemaker/](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-introduction-notebook.html)

[https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-notebooks.html](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-introduction-notebook.html)

[Feature store end to end WORKSHOP on github](https://github.com/aws-samples/amazon-sagemaker-feature-store-end-to-end-workshop)


# 3. Model training

1. Once the feature store is ready, the training set is prepared via an Athena SQL query.
2. A model is trained using the XGBoost algorithm from SageMaker.
3. 


**References and links**:

[https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-athena-glue-integration.html](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-athena-glue-integration.html)










