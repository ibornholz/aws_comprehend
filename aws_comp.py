#!/usr/bin/python3
# python file to ask amazon comprehend for sentiment
import boto3

# Replace the following with your own AWS access key ID and secret key
aws_access_key_id = "YOUR AWS KEYID"
aws_secret_access_key = "YOUR AWS KEY"

# Create a boto3 client for the Amazon Comprehend API
comprehend_client = boto3.client("comprehend", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Use the Amazon Comprehend API to analyze some text

text = "Danke, das haben Sie gut gemacht."
response = comprehend_client.detect_sentiment(Text=text, LanguageCode="de")

# Print the detected sentiment
print(response["Sentiment"])
