# Problem-5: Portfolio Management
portfolio = {
    'accounts': ['SBI', 'IOB'],
    'shares': ['HDFC', 'ICICI', 'TM', 'TCS'],
    'ornaments': ['10 gm gold', '1 kg silver']
}

# a) Add a key 'MF' with values 'Relaince' and 'ABSL'
portfolio['MF'] = ['Relaince', 'ABSL']

# b) Set 'accounts' to ['Axis', 'BOB']
portfolio['accounts'] = ['Axis', 'BOB']

# c) Sort 'shares' key
portfolio['shares'].sort()

# d) Delete 'ornaments' key
del portfolio['ornaments']

print(portfolio)
