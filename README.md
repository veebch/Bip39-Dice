# Generate a Bitcoin Wallet Using Dice

![outline](images/rolls.png)



[![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UCz5BOU9J9pB_O0B8-rDjCWQ?label=YouTube&style=social)](https://www.youtube.com/channel/UCz5BOU9J9pB_O0B8-rDjCWQ)
## Overview

These tools guide you through **offline** dice-throwing generation of a 24 word seed for a Bitcoin Wallet. The first 23 words are generated using paper and the glorious randomness of dice. Because the 24th is a checksum word, it is calculated using the Python script [24thword.py](/24thword.py).

This repository contains a pdf and a few lines of python code. The pdf contains both the instructions for making your seed phrase and the [BIP39](https://www.halborn.com/blog/post/what-is-a-bip39) list (English in pdf and English and Japanese in code).

To get all the files you'll need, clone this repository with the command 

```
git clone https://github.com/veebch/Bip39-Dice.git
```
You now have a directory called `BIP39-Dice` that contains all the files you'll need.

## Step 1: First 23 Words

Print [this pdf](/BIP39DiceManualCalculator.pdf) and grab
- a pen, 
- a pocket calculator (optional and depending on your mental arithmetic skills),
- some dice.

You're now ready to generate the first 23 words. Follow the instructions in the  [pdf](/BIP39DiceManualCalculator.pdf).

## Step 2: The 24th Word

To determine the final 24th word, on an [**OFFLINE**](https://en.wikipedia.org/wiki/Air_gap_(networking)) machine, edit `rolls.txt` and replace the words with the 23 that you chose using dice. Then run:

`python3 24thword.py`

You will be given a list of 8 valid 24th words. Pick one of the 8 words (eg by rolling 3 dice using and using the method above to get a number between 1 and 8 (1+1+2+4)), write your chosen word with the other 23. This is a valid wallet seed, and you can use it with [Electrum](http://electrum.org) or some other wallet application.

If you don't have an airgapped (permanently offline) machine, you could use [seedsigner](https://github.com/SeedSigner/seedsigner).

For more information on how words become keys, see check: https://learnmeabitcoin.com/technical/mnemonic

## Step 3: Receiving/ Sending Funds

To receive money to the wallet. You'll need an address (derived from your xpub). To send, you'll need your private key. The keys you'll need to do both of these things can be derived using an offline version of the page https://iancoleman.io/bip39/ 

## Step 4: Storing Your Seed Phrase - Video

The words that you generated need to be stored in a secure way, here's a video of one method:

[![Alt text](/images/videoetch.png)](https://www.youtube.com/watch?v=RVYHCVpeyEA)

    
## Nothing is Original

The Python code for 24th word was based on [avsync/bip39chk](https://github.com/avsync/bip39chk)

## License

GPL 3.0
