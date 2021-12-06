# Project

The goal of this project is to put into production a credit card fraud detection system (based on generated data) using the AWS stack.

The code and methodology have been obtained from the [Machine Learning for Credit Card Fraud detection - Practical handbook](https://fraud-detection-handbook.github.io/) online book, and it will be adapted to work in a production-like environment.

## First phase

The first part of the process is to get acquainted with the book concepts and proceed to generate data according to the specifications, doing feature engineering, splitting data, and finally train some machine learning models using this generated data according to the book.

From the beginning, Docker will be used to host a Conda environment, so results can be reproduced easily on the cloud or where needed without depending on any local computer dependencies.

## Second phase

Move the code to AWS and reproduce the data generation, feature engineering and model training using a diverse set of AWS services, such as available AWS ML algorithms or bring-your-own-algorithm. I will try using a smaller image (trying to minimize it and avoid using Conda) and/or use SageMaker notebooks.

Will also include a data store to better reflect how a real system would work in practice.

## Third phase

Deploy and serve the model in *production* (using generated data). It is yet to be determined if it will be real-time or batch; it will also depend on how costly is to run it.

## Fourth phase

Will include:

- Introducing drift using the data generator. How to proceed with model monitoring and maintenance according to available AWS services is yet TBD.

- **Maybe**: Use Spark through EMR to do the data preprocessing part.


# References and credit

The original work is from [Machine Learning Group (Université Libre de Bruxelles - ULB).](https://mlg.ulb.ac.be/wordpress/) and I have adapted it from [here](https://fraud-detection-handbook.github.io/fraud-detection-handbook/index.html).

Code released under a [GNU GPL v3.0 license](https://www.gnu.org/licenses/gpl-3.0.en.html)