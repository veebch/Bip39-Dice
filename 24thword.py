# The 24th Word - a tool for a fully offline wallet generation (run on an airgapped machine)

import os
import sys
import hashlib
import binascii

class Bip39Check(object):
    def __init__(self, language):
        self.radix = 2048
        self.worddict = {}
        self.wordlist = []

        counter = 0

        with open('%s/%s.txt' % (self._get_directory(), language), 'r') as file:
            for w in file.readlines():
                word = w.strip() if sys.version < '3' else w.strip()
                self.worddict[word] = counter
                self.wordlist.append(word)
                counter = counter + 1

        if(len(self.worddict) != self.radix):
            raise ValueError('Expecting %d words, not %d', self.radix, len(self.worddict))

    @classmethod
    def _get_directory(cls):
        return os.path.join(os.path.dirname(__file__), 'wordlist')

    def _check_size(self, phrase):
        self.size = len(phrase) + 1
        if (self.size != 24):
            raise ValueError('Expecting 23 words')

    def _compute_entropy(self, phrase):
        print("---------------------")
        self.entropy = 0
        for w in phrase:
            idx = self.worddict[w]
            print('Word "' + w + '", index at words list ' + str(idx + 1))
            self.entropy = (self.entropy << 11) + idx

        print('Entropy: ' + bin(self.entropy)[2:])
        return self.entropy

    def _scan(self):
        checksum_bits = self.size // 3
        entropy_to_fill = 11 - checksum_bits
        entropy_base = self.entropy << (entropy_to_fill)
        couldbe=[]

        print("---------------------")
        print('Candidates: ')
        for i in range(0, 2 ** entropy_to_fill):
            entropy_candidate = entropy_base | i
            print('Candidate ' + str(i+1))
            binary = bin(entropy_candidate)[2:]
            print(' > Binary:', binary)
            entropy_str = (entropy_candidate).to_bytes((entropy_candidate.bit_length() + 7) // 8, 'big')
            hash = (hashlib.sha256(entropy_str).digest()[0])
            checksum = hash >> (8 - checksum_bits)
            final_word_idx = (i << checksum_bits) + checksum
            checkword = self.wordlist[final_word_idx]
            couldbe.append(checkword)
        return couldbe


def main():

    # Read dice rolls, find words, and then generate a list of candidate 24th words
    with open('rolls.txt') as f:
        fullwordlist = f.read().splitlines()
    for i in range(len(fullwordlist)):
        fullwordlist[i].strip()

    m = Bip39Check('english')

    print("---------------------")
    phrase=fullwordlist
    print("23 words from dice rolls:\n")
    print(fullwordlist)
    m._check_size(phrase)
    m._compute_entropy(phrase)
    candidates=m._scan()

    print("---------------------")
    print ("Valid 24th words: ")
    print (candidates)
    print ("Pick one of these, write it down with the other 23")
    print ("You now have a valid bitcoin wallet seed. Restore it in the software of your choice")
     

if __name__ == '__main__':
    main()
