Ethereum ABI, Contract Creation and Interaction Overview
========================================================

This is a quick overview of the entire process that ethereum steps through when you create and interact with a contract. 

Creating Contracts
------------------

When creating a contract, you send the bytecode of the contract to the 0 address, but if the contract has a constructor, you must append the ABI-encoded arguments to the constructor at the end of the bytecode, without a function signature preceding them.

The contract can only be created through an eth_sendTransaction RPC call. The call will return a transaction hash, which you can use to request a transaction receipt through eth_getTransactionReceipt. Note that this returns immediately, even if the transaction receipt is unavailable, so you will need to poll. After the block where you have created the contract is deep enough, eth_getTransactionReceipt will return something like the following:
    
    {
        "blockHash": "0xed6b9c2b5c80d4b572bfcc9f51866eb7f33be7e2d458178562db26dc1de618dd",
        "blockNumber": "0x137e",
        "contractAddress": "0x4f63086fb08d6459b76f6a09b291a6da5c4ba188",
        "cumulativeGasUsed": "0x151bf",
        "from": "0x53b85e374cdfa5348f68468108be59711fe55861",
        "gasUsed": "0x151bf",
        "logs": [],
        "root": "8d4299367b56325082e10c845ad4e5628952b7ce45e8ad225efdd90d011fba98",
        "to": null,
        "transactionHash": "0xe87e1e6dca49578b060cbfc411f55e63bd4d72960854c0b4acf1a7f216c8b38a",
        "transactionIndex": "0x0"
    
    }
    

The "contractAddress" is what you will use to interact with the contract in the future.

Calling Methods on a Contract
-----------------------------

Calling constant methods that don't affect the blockchain state is done with eth_call, which expects, at a minimum, the contract address, the ABI-encoded parameter string, and the account you are calling the contract from. The response, if sucessful, will be an ABI-encoded parameter list. eth_call requires a block tag parameter, meaning, which block you want to target with your call. You can set this to "latest".

Calling a method that affects the blockchain state requires using eth_sendTransaction. The response is the same as above, you'll have to wait for eth_getTransactionReceipt before you can be sure that your transaction state change has been included into a block.

Either way, the encoded parameter string needs to be prefixed with a 4-byte identifier that signifies the address to jump into inside of the contract code. Normally, this is simply the first 4 bytes of the hash of a function signature i.e., keccak('main(uint256,int256)'). When hashing over the JSON RPC API, you must encode the string you're sending as a hex string first (i.e., '0x' + hello'.encode("hex")).

Ethereum ABI Encoding
---------------------

The ABI encoding is just a left padded, hex string of the argument value, in most cases. See the Ethereum ABI page for more info.
