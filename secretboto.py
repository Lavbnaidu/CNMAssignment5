import boto3

# create an instance of the secretsmanager client
client = boto3.client('secretsmanager')

# create a new secret
response = client.create_secret(
    Name='my-secret',   # specify the name of the secret
    SecretString='{"username":"my-username","password":"my-password"}' # provide the secret as a JSON string
)

# print the ARN of the new secret
print(response['ARN'])