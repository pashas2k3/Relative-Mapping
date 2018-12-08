import json

'''
event: Is the event information passed in
context:
'''
def lambda_handler(event, context):
    '''
        Event:
        https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format
        Context:
        https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

        Returns
        ------
        API Gateway Lambda Proxy Output Format: dict
            'statusCode' and 'body' are required
        # api-gateway-simple-proxy-for-lambda-output-format
        https: // docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    '''
    try:
        body_dict = json.loads(event.body)

        result = relevant_fn(event.resource, event.httpMethod) (body_dict)
    except Exception as e:
        print ("Caught exception" + e)
        raise e

    return {
        "statusCode": 200,
        "body" : json.dumps({"result" : result})
    }


def relevant_fn(resource, httpMethod)
    from .controller import add_individual, get_relative_info, make_relation, find_relation
    if resource.contains('relative'):
        if httpMethod == 'POST':
            return add_individual
        elif httpMethod == 'GET':
            return get_relative_info
    elif resource.contains('relation'):
        if httpMethod == 'POST':
            return make_relation
        elif httpMethod == 'GET':
            return find_relation
