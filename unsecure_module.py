import boto3
from botocore.exceptions import NoCredentialsError

session = boto3.Session(
    aws_access_key_id="ABCDEFGHIJKLMNOPQRST",
    aws_secret_access_key="ABCDEFGHIJKLMNOPQRST",
    region_name="ap-northeast-2"
)
s3 = session.resource('s3')
dynamodb = session.resource('dynamodb')


def get_object_from_s3(bucket_name, object_key):
    try:
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        data = response['Body'].read()
        return data
    except NoCredentialsError:
        print("There is no Credentials.")
        return None


# DynamoDB에 데이터를 삽입하는 함수
# table_name: DynamoDB 테이블 이름
# data: S3 객체의 데이터
def put_data_to_dynamodb(table_name, data):
    try:
        response = dynamodb.put_item(
            TableName=table_name,
            Item={
                'PrimaryKey': {'S': 'YourPrimaryKeyValue'},  # Primary key의 값 설정
                'DataField': {'S': data.decode('utf-8')}  # 데이터 필드에 S3 객체의 데이터를 삽입
            }
        )
        return response
    except Exception as e:
        print("Error putting data to DynamoDB", str(e))

