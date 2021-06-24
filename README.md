# Bip39 Offline Mnemonic Generator

![outline](images/rolls.png)

This is a pdf containing the instructions and the English BIP39 list for offline generation of the first 23 words of a 24 word BIP39 mnemonic for a Bitcoin Wallet.

## What now?

To determine the final 24th word, on an OFFLINE machine, edit `rolls.txt` and replace the words that you chose using dice. Then run:

`python3 24thword.py`

You will be given a list of 8 valid 24th words. Pick one (no need to tell the program which), write it with the other 23. This is a valid wallet seed, and you can use it with Electrum or some other 

## Thanks!

Code for 24th word was based on [avsync/bip39chk](https://github.com/avsync/bip39chk)

## License

GPL 3.0
