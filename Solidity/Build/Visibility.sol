// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.7.0;

/*
Private - Self
Public - Self, Child, Other

Internal - Self, Child
External - Other
*/

contract Parent {
    function privateFun() private pure returns (string memory) {
        return "private string inside parent";
    }

    function publicFun() public pure returns (string memory) {
        return "public string inside parent";
    }

    function internalFun() internal pure returns (string memory) {
        return "Internal string inside parent";
    }

    function externalFun() external pure returns (string memory) {
        return "external string inside parent";
    }

    function publicCallsPrivate() public pure returns (string memory) {
        return privateFun();
    }

    function publicCallsInternal() public pure returns (string memory) {
        return internalFun();
    }

    // Does not compile!
    // External is not available in self or child contracts ...
    // function publicCallsExternal() pure public returns(string memory){
    //     return externalFun();
    // }

    // State variables
    string private privateVar = "my private variable";
    string internal internalVar = "my internal variable";
    string public publicVar = "my public variable";
    // State variables cannot be external so this code won't compile.
    // string external externalVar = "my external variable";
}

contract Child is Parent {
    //
    // error: Undeclared identifier
    // Cant see private!
    // function childCallPrivate() pure public returns (string memory){
    //     return privateFun();
    // }
    //
    //
    // Both of the below work. but, we do not need them!
    // WHY?
    // inheritance!
    // function childCallPublic() pure public returns (string memory){
    //     return publicFun();
    // }
    // function childCallInternal() pure public returns (string memory){
    //     return internalFun();
    // }
    //
    //
    // error: Undeclared identifier
    // Cant see external!
    // function childCallExternal() pure public returns (string memory){
    //     return externalFun();
    // }
    //
}
