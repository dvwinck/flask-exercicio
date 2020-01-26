from flask import Flask, jsonify, request
from flask_restful import Api,  Resource
import json

app = Flask(__name__)

@app.route('/')
def primes():
    primes =[]
    seq = 0
    for cont in range (300000):
        
        if isPrime(cont):
            primes.append([seq, cont])
            seq = seq+1
    return json.dumps(primes)


def isPrime(n):
    cont = int(n/2)

    for i in range(3,cont,2):
        if n% (i) == 0:
            return False ;
    return n >=2;


if __name__ == "__main__":
    app.run(debug=True)