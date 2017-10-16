CC=./sc-compile
DEPLOY=./sc-push
TEST=./sc-test

FILES=./examples/state.sol
TESTS=./examples/state.def
CONTRACT=Test
ABI=$(CONTRACT).abi
PORT=8545

all: compile push test

compile:
	$(CC) $(FILES)

push:
	$(DEPLOY) -c Test.abi -t $(TESTS) -p $(PORT)

test:
	$(TEST) -n $(CONTRACT) -t $(TESTS) -p $(PORT)
