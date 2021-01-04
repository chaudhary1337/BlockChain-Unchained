# BlockChain-Unchained
BlockChains & Cryptography from Scratch

## Solidity
An Exploration into the world of smart contracts.
I have a stab at **building** Smart Contracts, which are under ```./Solidity/Build/```. Meanwhile also exploring the **exploits** and **vulnerabilities** found in Solidity: From ```Re-Entrancy``` exploits draining all the ether from a smart contract and ```Phishing Attacks``` to get *Priviledge Escalation*, upto catching other Hackers using ```HoneyPot``` retaliation.  

### Build
I explore the bit by bit building of Solidity Code, along with the best practices.

- **ContractFactory**: A contract that generates other contracts; also uses inheritance
- **Error**: Require, Assert, Revert
- **FullGasAhead**: Usage of Gas in Ethereum
- **FunMod**: Using Function Modifiers
- **GetSet**: Getter and Setter functions
- **HelloWorld**: The classic Hello World
- **Inderitance**: Deriving children contracts from parent contracts
- **MapsAndArrays**: Usage of maps (dicts) and arrays (lists)
- **Payable**: Sending and Receiving Ether
- **PureView**: Controlling the views using: Pure, View, Other
- **SigningAndVerification**: The heart of BlockChain; signing and verification using ECDSA
- **StructsAndEnums**: Self-Explanatory
- **Visibility**: Public, Private, Internal, External

Quick Note: `view != visibilities`

### Break
A list of all the Solidity Exploits:
- **Overflow** Attack
- **Underflow** Attack
- **ReEntrancy** Attack
- **Self-Desruction** Attack
- **Denial of Service (DoS)** Attack
- **Phishing** Attack
- **Hiding Malicious Code**
- **Honey Pot Retaliation**

I have also included the fixes for the attacks: [Exploits and Attacks Fixes](https://github.com/SmartyPants042/BlockChain-Unchained/tree/main/Solidity/Break)


## Cryptography
A head first dive into the cryptography used in the modern day technologies. I've explored RSA & ECC, both of which are already in use widely and have had substantial impact on the current Scuerity Systems. ECC is more powerful, and has seen numerous applications in blockchain. We explore one of the standards used in Bitcoin; `secp256k1`.

### RSA
decsription to be added

### ECC
Elliptic Curve Cryptography is much more efficient, in the number of bits required to effectively encrypt/decrypt, sign/verify information. 
