def FizzBuzz(input, set_range = 25):
    """Calculate FizzBuzz"""

    for i in range(1, set_range+1):
        output = ''

        for multiple in input:
            if i % multiple == 0:
                output += input[multiple]

        if output == '':
            output = i

        print(f'Wow! {i} is really {output}!')
    
information = {3: 'Fizz', 5: 'Buzz'}

FizzBuzz(information, 100)
