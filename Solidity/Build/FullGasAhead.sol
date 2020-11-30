pragma solidity ^0.7.0;

contract Gas{
    function getGasPrice() public returns (uint) { return tx.gasprice; }
    
    function fullGasAhead() public {
        uint i = 0;
        while(true){ i += 100; }
    }
}
