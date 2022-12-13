import csv
import boto3

# Replace the following with your own AWS access key ID and secret key
aws_access_key_id = "YOUR AWS KEY ID"
aws_secret_access_key = "YOUR AWS KEY"

# Create a boto3 client for the Amazon Comprehend API
comprehend_client = boto3.client("comprehend", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

def parse_csv(csv_file):
  # open the CSV file
  with open(csv_file, 'r') as f:
    # create a reader object, and determine, how fields are devided
    reader = csv.reader(f, delimiter=';')
    # loop through each row in the reader object
    
    for row in reader:
      # call the function on the third column of the current row
      text = row[9]
      #if you want to debug if you've got the right column, uncomment the folowing line
      #print(text)
      result = get_response(text)
      # add the result to the row
      row.append(result)
      # write the updated row to the output CSV file
      with open('output.csv', 'a') as output:
        writer = csv.writer(output)
        writer.writerow(row)

# define the function that will be called on each line
def get_response(text):
  response = comprehend_client.detect_sentiment(Text=text, LanguageCode="de")  

  # Get the result from comprehend. 
  return response['Sentiment']

# call the parse_csv function
parse_csv('your_csv.csv')