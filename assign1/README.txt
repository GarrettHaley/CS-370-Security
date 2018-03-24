############################################################################################

HOW TO RUN THE PROGRAM: python bloom.py -d dictionary.txt -i input.txt -o output3.txt output5.txt

############################################################################################
QUESTIONS:

a) What hash functions did you choose and why (Hint: Cryptographic or noncryptographic)?
What is the output range of the hash functions? What is the size
of the Bloom filter in each case? If you used a library for your hash function,
make sure to cite it.

I used pythons hashlib cryptographic library: https://docs.python.org/2/library/hashlib.html
 md5    -Output Range:  128 bits.
 sha1   -Output Range:  160 bits.
 sha224 -Output Range:  224 bits.
 sha256 -Output Range:  256 bits.
 sha384 -Output Range:  384 bits.
The size of the bloom filter is 8 times the size of the dictionary input for both the first bloom filter (3 hash functions) and second bloom filter (5 hash functions).
I chose to use cryptographic hash functions from the standard hashlib library simply because it was simple to implement (also, its worth noting cryptographic hashes have a lower
chance of producing collisions than noncryptographic hashes).

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

b) How long does it take for your Bloom Filter to check 1 password in each case?
Why does one perform better than other?

The following runtimes were collected on the school server:
 bloomFilter1 (3 hash functions)    - approx: 0.000014s (FASTEST)
 bloomFilter2 (5 hash functions)    - approx: 0.000016s
The reason that the first bloom filter performs faster is:
1. There are two less hash functions for the bloom filter to process.
2. The hash functions used in bloomFilter2 but not in bloomFilter1 are the slowest (sha256 and sha384).

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

c) What is the probability of False Positive in your Bloom Filter in each case? What
is the probability of False Negative in your Bloom Filter?

Chance of false negative: 0% -not possible!
false positive = (1-(1-1/m)^kb)^k where k = number of hashes (3 or 5), m = size of array (1,870,551), k = number of bad passwords in array (623,517).
False positive probability of bloomFilter1 (3 hash functions): 0.03057936207157
False positive probability of bloomFilter2 (5 hash functions): 0.02167922487598

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

d) How can you reduce the rate of False Positives? 

By increasing the size of the bloom filter and the number of hash functions used, we can reduce the probability of false positives.

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
