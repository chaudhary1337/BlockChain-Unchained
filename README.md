# BlockChain-Unchained
BlockChains & Cryptography from Scratch

## Solidity
An Exploration into the world of smart contracts.
I have a stab at **building** Smart Contracts, which are under ```./Solidity/Build/```. Meanwhile also exploring the **exploits** and **vulnerabilities** found in Solidity: From ```Re-Entrancy``` exploits draining all the ether from a smart contract and ```Phishing Attacks``` to get *Priviledge Escalation*, upto catching other Hackers using ```HoneyPot``` retaliation.  

### Build
I explore the bit by bit building of Solidity Code, along with Solidity Best Practices.

0. Hello World
1. Getters and Setters
2. Gas
3. Modifier: Pure, View, Other
4. Inderitance
5. Function Modifiers
6. Visibilities: Public, Private, Internal, External
7. Error: Require, Assert, Revert
8. Maps and Arrays Usage
9. Structs and Enums usage
10. Payable: Sending and Receiving Ether

### Break
A list of all the Solidity Exploits:
- Overflow Attack
- Underflow Attack
- ReEntrancy Attack
- Self-Desruction Attack
- Denial of Service (DoS) Attack
- Phishing Attack
- Hiding Malicious Code
- Honey Pot Retaliation

I have also included the fixes for the attacks: [Exploits and Attacks Fixes](https://github.com/SmartyPants042/BlockChain-Unchained/tree/main/Solidity/Break)


## Cryptography
A head first dive into the cryptography used in the modern day technologies. I've explored RSA & ECC, both of which are already in use widely and have had substantial impact on the current Scuerity Systems. ECC is even more powerful, and has seen numerous applications in blockchain. We explore one of the standards used in Bitcoin; `secp256k1`.

### RSA
decsription to be added

### ECC
Elliptic Curve Cryptography is much more efficient, in the number of bits required to effectively encrypt/decrypt, sign/verify information. 
