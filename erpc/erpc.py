import random
import requests
import json

from time import sleep


class ERPC:

    def __init__(self, host, port):
        self.url = "http://" + host + ":" + port + "/"
        self.id = random.randint(1, 10000)
        self.error = False

    def send(self, method, params):
        headers = {'content-type': 'application/json'}
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": self.id,
        }
#        print json.dumps(payload, sort_keys=True, separators=(',', ': '), indent=4)
        response = requests.post(self.url, data=json.dumps(payload), headers=headers).json()
        if "result" in response:
            return response["result"]
        else:
            self.error = response["error"]
            return False

    def getAccount(self):
        return self.send("eth_accounts", ["0"])

    def compileContract(self, code):
        return self.send("eth_compileSolidity", [code])

    def sendTransaction(self, params):
        return self.send("eth_sendTransaction", [params])

    def getTransactionReceipt(self, thash):
        return self.send("eth_getTransactionReceipt", [thash])

    def sha3(self, str):
        return self.send("web3_sha3", ['0x' + str.encode("hex")])

    def call(self, params):
        return self.send("eth_call", [params, "latest"])

    def blockNumber(self):
        return self.send("eth_blockNumber", [])

    def getStorageAt(self, params):
        return self.send("eth_getStorageAt", [params, "latest"])

    def getCode(self, params):
        return self.send("eth_getCode", [params, "latest"])

    def sendTransactionWait(self, params, wait=100):
        r = self.sendTransaction(params)
        tr = False
        for i in range(0, wait):
            response = self.getTransactionReceipt(r)
            if response is not None:
                tr = response
                break
            sleep(1)
        return tr, r
