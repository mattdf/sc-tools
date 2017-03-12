sc-tools by Matthew Di Ferrante

This repo contains a set of tools written in python to help develop, test and
deploy smart contracts under a unified interface that can be easily Makefile'd.

The project consists of three tools:
* sc-compile: Take a solidity contract and compile it down to a combined ABI +
  bytecode JSON file
* sc-push: deploy bytecode + ABI to the blockchain, and register/update the
  name and contract address in local "contracts.map" file
* sc-test: read local contracts.map file and take a tests file, and call into
  contract deployed by sc-push with given test cases

Example run (from Makefile):

```
$ ./sc-compile ./examples/state.sol
Generated Test.abi ...
Generated Test.test-skeleton ...

$./sc-push -c Test.abi -t ./examples/state.def -p 8881
Using account w/ address: 0xe564ab56ddfb3218fdf84dffe7e7a84f36b1bc8f
Received transaction hash 0x42ba6a85512d8235561a61bc6bdad4c3fa25df7617905565fcf8d20ef047191b
Contract address for  Test :  0x1216a17ab9e84aea8d777546f9d04fcca6bfd6f2
{
    "blockHash": "0xf36a8e0a37ef02c36b0c31a2f44389d0bbaeb1d31a27ee15f2a9d6606ae5e2f2",
    "blockNumber": "0x110b",
    "contractAddress": "0x1216a17ab9e84aea8d777546f9d04fcca6bfd6f2",
    "cumulativeGasUsed": "0x27387",
    "from": "0xe564ab56ddfb3218fdf84dffe7e7a84f36b1bc8f",
    "gasUsed": "0x27387",
    "logs": [],
    "root": "c393fd7eb73b5bf68cff8154fa82c78ae075b558858aff06c8b0b62c64c34362",
    "to": null,
    "transactionHash": "0x42ba6a85512d8235561a61bc6bdad4c3fa25df7617905565fcf8d20ef047191b",
    "transactionIndex": "0x0"

}
Updated map for Test

$ ./sc-test -n Test -t ./examples/state.def -p 8881
========= Testing setStore(int256) =========
Call setStore(int256)  will change blockchain state! Awaiting transaction receipt...
Current block:  4363
ABI Parameters: 0x51c8e02a0000000000000000000000000000000000000000000000000000000000000014
Gas cost:       29014
Event logs: ------
{
	"ShortStore(int256)": [
        20
    
	], 
	"StoreEvent(int256,int256)": [
        20, 
        320
    
	]

}
------------------
========= Testing multStore(int256) =========
Current block:  4365
ABI Parameters: 0xd78db6480000000000000000000000000000000000000000000000000000000000000005
ABI Result:     0x0000000000000000000000000000000000000000000000000000000000000064
JSON Result: -----
[
    100

]
------------------
Test 0 for multStore(int256) Passed!
========= Testing multStore(int256) =========
Current block:  4365
ABI Parameters: 0xd78db648000000000000000000000000000000000000000000000000000000000000000a
ABI Result:     0x00000000000000000000000000000000000000000000000000000000000000c8
JSON Result: -----
[
    200

]
------------------
Test 1 for multStore(int256) Passed!
========= Testing getStore() =========
Current block:  4365
ABI Parameters: 0xc2722ecc
ABI Result:     0x0000000000000000000000000000000000000000000000000000000000000014
JSON Result: -----
[
    20

]
------------------
Test 0 for getStore() Passed!
```
