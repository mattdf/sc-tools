import json
import collections
import erpc.abi as abi
import erpc.utils as utils


def JSONToOD(json_file):
    with open(json_file) as json_data:
        od = json.load(json_data, object_pairs_hook=collections.OrderedDict)

    return od


def callHash(scABI, fname):
    x = False
    for i in scABI:
        if i["name"] == fname and i["type"] == "function":
            x = i
            break
    if x is False:
        return ""
    args = []
    out = []
    for i in x["inputs"]:
        args.append(i["type"])

    for i in x["outputs"]:
        out.append(i["type"])

    return (x["name"] + "(" + ','.join(args) + ")", args, out, x["constant"])


def encodeParam(fsig, param, sig):
    return fsig[0:8] + abi.encode_abi(sig, param).encode("hex")


def hasConstructor(scABI):
    for i in scABI:
        if 'type' in i and i['type'] == 'constructor':
            types = []
            for x in i["inputs"]:
                types.append(x["type"])

            return types

    return False


def getEvents(scABI):
    events = []
    for i in scABI:
        if i["type"] == "event":
            args = []
            for j in i["inputs"]:
                args.append(j["type"])

            esig = i["name"] + "(" + ','.join(args) + ")"
            event = {
                "hash": '0x' + utils.sha3(esig).encode("hex"),
                "argsig": args,
                "name": esig
            }
            events.append(event)

    return events


def getLogs(events, response):
    result = dict()
    for log in response["logs"]:
        data = log["data"]
        topics = log["topics"]

        for event in events:
            if event["hash"] in topics:
                args = event["argsig"]
                if event["name"] not in result:
                    result[event["name"]] = []
                result[event["name"]].append(abi.decode_abi(args, data[2:].decode("hex")))

    return result


def printDict(d):
    print json.dumps(d, sort_keys=True, indent=4)
