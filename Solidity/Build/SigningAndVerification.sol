// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.7.0;

/*
LOGICAL DETAILS
Signing and Verifying is at the heart of what makes a blockchain secure.
In the below contract, we have functions to:
1. getTransactionHash: hash trasaction details
- `to` - to whom this trasaction ether has to be sent
- `amount` - the amount to be sent to `to`
- `message` - the message description
- `nonce` - prevents replay attacks by choosing an arbitary number
2. getSignedTransactionHash: signing the hash
3. verify:
- finds the hash of the publically available transaction
- gets it signed by the `_signer`
- recovers the signer using 4
4. recoverSigner: uses splitSignature and then ec-recover to get signer.
ec-recover uses `v` as recovery id and `r`, `s` from ECDSA to recover the signer
5. splitSignature splits the signature into `r`, `s`, `v` using inline assembly

ALL SOURCES:
Primary Source: https://solidity-by-example.org/signature/
r,s,v: https://ethereum.stackexchange.com/questions/15766/what-does-v-r-s-in-eth-gettransactionbyhash-mean
ec-recover: https://ethereum.stackexchange.com/questions/75903/ecrecover-in-c

EXTRA INFORMATION:
Using ECDSA: https://github.com/SmartyPants042/BlockChain-Unchained/blob/main/Cryptography/ECC/ECDSA.py
*/

contract SignAndVerify {
    // returns a hash of the receiver address, the amount, the string message and the nonce.
    function getTransactionHash(
        address _to,
        uint _amount,
        string memory _message,
        uint _nonce
    ) 
    pure public returns (bytes32) {
        return keccak256(abi.encodePacked(_to, _amount, _message, _nonce));
    }
    
    // @params: _messageHash is the hash of transaction details
    // returns the signed hash message
    function getSignedTransactionHash(bytes32 _messageHash) public pure returns (bytes32) {
        /* 
            Signature is produced by signing a keccak256 hash with the following format:
            "\x19Ethereum Signed Message\n" + len(msg) + msg
            
            in our case, len is always 32, since that is what keccak256 is;
            recall: 256 bits = 32 bytes!
        */
        return keccak256(abi.encodePacked("\x19Ethereum Signed Message:\n32", _messageHash));
    }
    
    function verify(
        address _signer,
        address _to,
        uint _amount,
        string memory _message,
        uint _nonce,
        bytes memory signature
    ) public pure returns (bool) {
        // hashing the transaction details
        bytes32 transactionHash = getTransactionHash(_to, _amount, _message, _nonce);
        // getting the transaction signed by the `_signer`
        bytes32 signedTransactionHash = getSignedTransactionHash(transactionHash);
    
        // recovers signer from the signed transaction hash. checks equality
        return recoverSigner(signedTransactionHash, signature) == _signer;
    }
    
    // helper function to access ecrecover
    function recoverSigner(
        bytes32 _signedTransactionHash, 
        bytes memory _signature
    ) public pure returns (address) {
        // getting r, s from ECDSA and v as recovery id
        // source: https://ethereum.stackexchange.com/questions/15766/what-does-v-r-s-in-eth-gettransactionbyhash-mean
        (bytes32 r, bytes32 s, uint8 v) = splitSignature(_signature);

        // here's some quick implementation on ecrecover
        // https://ethereum.stackexchange.com/questions/75903/ecrecover-in-c
        return ecrecover(_signedTransactionHash, v, r, s);
    }
    
    // the below is taken directly from:
    // source: https://solidity-by-example.org/signature/
    function splitSignature(bytes memory sig) public pure returns (bytes32 r, bytes32 s, uint8 v)
    {
        // 32 bytes (r) + 32 bytes (s) + 1 byte (uint8)
        require(sig.length == 65, "invalid signature length");
        
        // inline assembly!
        assembly {
            /*
            First 32 bytes stores the length of the signature

            add(sig, 32) = pointer of sig + 32
            effectively, skips first 32 bytes of signature

            mload(p) loads next 32 bytes starting at the memory address p into memory
            */

            // first 32 bytes, after the length prefix
            r := mload(add(sig, 32))
            
            // second 32 bytes
            s := mload(add(sig, 64))
            
            // final byte (first byte of the next 32 bytes)
            v := byte(0, mload(add(sig, 96)))
        }
        // implicitly return (r, s, v)
    }
}
