def handler(request, response):
    # Get the two numbers from the query parameters
    num1 = int(request.query.get('num1'))
    num2 = int(request.query.get('num2'))

    # Add the two numbers together
    result = num1 + num2

    # Return the result as a JSON object
    response.status_code = 200
    response.headers.set('Content-Type', 'application/json')
    response.set_json({
        'result': result
    })
