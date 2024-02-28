# Bip39 Offline Mnemonic Generator

![outline](images/rolls.png)



[![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UCz5BOU9J9pB_O0B8-rDjCWQ?label=YouTube&style=social)](https://www.youtube.com/channel/UCz5BOU9J9pB_O0B8-rDjCWQ)

## Generate a Bitcoin Wallet using Dice

These tools guide you through **offline** generation of a full 24 word seed for a secure Bitcoin Wallet. The first 23 words are generated using paper and the glorious randomness of dice. Because the 24th is a checksum word, it is calculated using the script `24thword.py`.

This repository contains a pdf and a few lines of python code. The pdf contains both the instructions for making your seed phrase and the [BIP39](https://www.halborn.com/blog/post/what-is-a-bip39) list (English in pdf and English and Japanese in code). 

## Step 1: First 23 words

- Print the pdf,  
- grab a pen, 
- a pocket calculator (optional),
- some dice
You're now ready to generate the first 23 words. Follow the instructions in the  [pdf](/BIP39DiceManualCalculator.pdf).

## Step 2: The 24th word

To determine the final 24th word, on an [**OFFLINE**](https://en.wikipedia.org/wiki/Air_gap_(networking)) machine, edit `rolls.txt` and replace the words with the 23 that you chose using dice. Then run:

`python3 24thword.py`

You will be given a list of 8 valid 24th words. Pick one (eg by rolling 3 dice using and using the method above to get a number between 1 and 8), write your chosen word with the other 23. This is a valid wallet seed, and you can use it with [Electrum](http://electrum.org) or some other wallet application.

If you don't have an airgapped (permanently offline) machine, you could use [seedsigner](https://github.com/SeedSigner/seedsigner).

For more information you may check: https://learnmeabitcoin.com/technical/mnemonic

## Step 3: Receiving/ Sending

To receive money to the wallet. You'll need an address (derived from your xpub). To send, you'll need your private key. The keys you'll need to do both of these things can be derived using an offline version of the page https://iancoleman.io/bip39/ 

## Step 4: Storing your seed - Video

The code that you generated needs to be stored in a secure way, here's  a video of one (of many) possible methods:

[![Electro Etching](http://img.youtube.com/vi/RVYHCVpeyEA/0.jpg)](http://www.youtube.com/watch?v=RVYHCVpeyEA "Electro Etching a Seed Phrase")


## Nothing is Original

Code for 24th word was based on [avsync/bip39chk](https://github.com/avsync/bip39chk)

## License

GPL 3.0
