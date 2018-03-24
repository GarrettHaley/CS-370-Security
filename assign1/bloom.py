import hashlib
import sys
import csv

class BloomFilter(set):

    def __init__(self, size, numHashes): 
        self.bit_array = list([False] * size)
        self.size = size
        self.numHashes = numHashes

    def add(self, item):
	hashType = ['md5', 'sha1', 'sha224', 'sha256', 'sha384']
        for i in range(self.numHashes):
	    Hash = getattr(hashlib,hashType[i])
            index = int(Hash(item).hexdigest(),16) % self.size
            self.bit_array[index] = True
        return self

    def contains(self, item):
        out = True
	j = 0
	hashType = ['md5', 'sha1', 'sha224', 'sha256', 'sha384']
        for i in range(self.numHashes):
	    Hash = getattr(hashlib,hashType[i])
            index = int(Hash(item).hexdigest(),16) % self.size
            if self.bit_array[index] == False:
                out = False
        return out

def parseFile(File):
        parsedData = []
        f = open(File,'r')
        for line in f:
            parsedData.append(line.strip())
        f.close()
        return parsedData

def writeResults(bloomFilter,inputPasswords,outputFile):
        f = open(outputFile,'w')
        for password in inputPasswords:
            if bloomFilter.contains(password):
                f.write('maybe\n')
            else:
                f.write('no\n')
        f.close()
def main():
    badPasswordsFile = sys.argv[2]
    inputPasswordFile = sys.argv[4]
    outputFile1 = sys.argv[6]
    outputFile2 = sys.argv[7]
    
    inputPasswords = parseFile(inputPasswordFile)
    badPasswords = parseFile(badPasswordsFile)
    bloom = BloomFilter(len(badPasswords)*8, 3)
    bloom2 = BloomFilter(len(badPasswords)*8,5)
    
    for password in badPasswords:
        bloom.add(password)
	bloom2.add(password)
    writeResults(bloom,inputPasswords,outputFile1)
    writeResults(bloom2,inputPasswords,outputFile2)
        
main()
