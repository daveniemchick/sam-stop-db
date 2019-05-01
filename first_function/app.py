import boto3
import json
import os



# Global variables are reused across execution contexts (if available)
session = boto3.Session()
key_string = "exceeding the maximum allowed time"
RDS = boto3.client('rds')

def lambda_handler(event, context):
    """
        AWS Lambda handler
        Parameters
        ----------
        context: object, required
            Lambda Context runtime methods and attributes

        Attributes
        ----------

        context.aws_request_id: str
            Lambda request ID
        context.client_context: object
            Additional context when invoked through AWS Mobile SDK
        context.function_name: str
            Lambda function name
        context.function_version: str
            Function version identifier
        context.get_remaining_time_in_millis: function
            Time in milliseconds before function times out
        context.identity:
            Cognito identity provider context when invoked through AWS Mobile SDK
        context.invoked_function_arn: str
            Function ARN
        context.log_group_name: str
            Cloudwatch Log group name
        context.log_stream_name: str
            Cloudwatch Log stream name
        context.memory_limit_in_mb: int
            Function memory

            https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

        event: dict, required

        Returns
        ------

    """

    try:

        message = event['Records'][0]['Sns']['Message']['Event Message']
        dbinstance = event['Records'][0]['Sns']['Message']['Source ID']
        if key_string in message:
            return stop_db(dbinstance)
        else:
            return message

    except:
        return "There was an error!"

def stop_db(dbinstance):

    response = RDS.stop_db_instance(DBInstanceIdentifier=dbinstance)
    return response
