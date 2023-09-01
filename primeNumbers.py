import math

def generateNPrimes(numPrimes: int) -> [int]:
    primes = [2]
    count = 2
    while True:
        if len(primes) == numPrimes:
            return primes
        count+=1
        if 0 in map(lambda p: count%p, primes):
            continue
        primes.append(count)

def generatePrimesUntil(stopNum: int) -> [int]:
    primes = [2]
    for count in range(3,stopNum+1):
        if 0 in map(lambda p: count%p, primes):
            continue
        primes.append(count)
    return primes

def isPrime(num: int) -> bool:
    stopNum = math.floor(num**0.5)
    primes = generatePrimesUntil(stopNum)
    return False if (0 in map(lambda p: num%p, primes)) else True

def main() -> None:
    pass

if __name__ == '__main__':
    main()
