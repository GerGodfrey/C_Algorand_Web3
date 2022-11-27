# Algo Builder dry run and TEAL debugger demo
Demostrates the Algo Builder dry run feature and TEAL debugger using the smart contracts created in [this](https://github.com/Algo-Foundry/stateful-sc) assignment.

## Setup instructions

### 1. Install packages
```
yarn install
```

### 2. Update environement variables
1. Copy `.env.example` to `.env`.
2. Update Algorand Sandbox credentials in `.env` file.

### 3. Use .env file
```
source .env
```

### 4. Deploy smart contract
```
yarn run algob deploy
```

### 5. Opt into smart contract
```
yarn run algob run scripts/actions/optIn.js
```

### 6. Debug app call for attack
```
yarn run algob run scripts/debug/attack_dryrun.js
```

The output json file can be found in ./assets folder.


### 7. Create message pack file for TEAL debugger
```
yarn run algob run scripts/debug/attack_debug.js
```

#### Debug using TEAL debugger
```
# Copy the generated file to sandbox container. Run the command in the sandbox directory.
./sandbox copyTo ../proyects/Developer/demo-debugger-dryrun/dryrun.msgp

# Run TEAL debugger
./sandbox tealdbg debug -d dryrun.msgp --remote-debugging-port 9392

# Inspect debug output in chrome
chrome://inspect/#devices
```