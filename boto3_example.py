import boto3
from botocore.config import Config

my_config = Config(
    region_name='eu-west-1'
)


runtime = boto3.client('runtime.sagemaker', config = my_config)
# sage = boto3.client('sagemaker', config = my_config)

# print(sage.list_endpoints())
response = runtime.invoke_endpoint(
    EndpointName="mnist-ei-traced",
    ContentType='image/jpeg',
    Body="payload"
)
