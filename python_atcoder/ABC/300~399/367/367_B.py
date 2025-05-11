X = input()
if '.' in X:
    X = X.rstrip('0')
    if X.endswith('.'):
        X = X[:-1]

print(X)