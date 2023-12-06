def find_domain_and_range(function_name):
    if function_name == 'sin' or function_name == 'cos':
        domain = 'All real numbers'
        range_ = '[-1, 1]'
    elif function_name == 'tan':
        domain = 'All real numbers except π/2 + nπ, n ∈ Integer'
        range_ = 'All real numbers'
    elif function_name == 'cot':
        domain = 'All real numbers except nπ, n ∈ Integer'
        range_ = 'All real numbers'
    else:
        domain = 'Unknown'
        range_ = 'Unknown'

    return domain, range_

def find_asymptotes(function_name):
    if function_name == 'tan':
        asymptotes = ['π/2 + nπ, n ∈ Integer']
    elif function_name == 'cot':
        asymptotes = ['nπ, n ∈ Integer']
    else:
        asymptotes = []

    return asymptotes
