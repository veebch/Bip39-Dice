import os
import sys
import hashlib

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
        if (self.size % 3 != 0):
            raise ValueError('Expecting 11 or 23 words')

    def _compute_entropy(self, phrase):
        self.entropy = 0
        for w in phrase:
            idx = self.worddict[w]
            self.entropy = (self.entropy << 11) + idx
        return self.entropy

    def _scan(self):
        checksum_bits = self.size // 3
        entropy_size = (self.size * 11 - checksum_bits) // 8 # Fixed entropy string length
        entropy_to_fill = 11 - checksum_bits
        entropy_base = self.entropy << (entropy_to_fill)

        for i in range(0, 2 ** entropy_to_fill):
            entropy_candidate = entropy_base | i
            entropy_str = (entropy_candidate).to_bytes(entropy_size, 'big')
            hash = (hashlib.sha256(entropy_str).digest()[0])
            checksum = hash >> (8 - checksum_bits)
            final_word_idx = (i << checksum_bits) + checksum
            checkword = self.wordlist[final_word_idx]
            print (checkword)


def main():
    m = Bip39Check('english')
    print("Enter the 23 words: ")
    phrase = sys.stdin.readline().split()
    m._check_size(phrase)
    m._compute_entropy(phrase)
    print("___________________________\nThese are your 8 candidate words, select any one of these for the 24th word.\n")
    m._scan()

if __name__ == '__main__':
    main()
