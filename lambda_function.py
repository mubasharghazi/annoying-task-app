import json
import boto3

bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

def lambda_handler(event, context):
    try:
        # Parse body from API Gateway
        if 'body' in event and event['body']:
            body = json.loads(event['body'])
            user_text = body.get('text', '')
        else:
            user_text = event.get('text', '')

        if not user_text:
            return {
                'statusCode': 400,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST'
                },
                'body': json.dumps({'error': 'Please provide text to extract tasks.'})
            }

        prompt = f"""
You are an executive productivity assistant. Analyze the text below and return:
1. Executive Summary (3 clear bullet points)
2. Action Items Checklist (tasks with assigned owners if mentioned)
3. Priority Rating (High, Medium, or Low)

Text to process:
{user_text}
"""

        # Using Amazon Nova Lite Model (Fast & fully accessible)
        request_body = json.dumps({
            "inferenceConfig": {
                "max_new_tokens": 1000,
                "temperature": 0.3
            },
            "messages": [
                {
                    "role": "user",
                    "content": [{"text": prompt}]
                }
            ]
        })

        response = bedrock.invoke_model(
            modelId="us.amazon.nova-lite-v1:0",
            body=request_body
        )

        response_body = json.loads(response.get('body').read())
        output_text = response_body['output']['message']['content'][0]['text']

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({'result': output_text})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({'error': str(e)})
        }