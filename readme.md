# Pasos 


## Crear y Correr Nodo Sanbox 

1) Correr docker 
2) Clonar el repositorio de https://github.com/algorand/sandbox 
3) Dentro de sandbox Correr ``` ./sandbox up ```. Para confirmar Podemos ver en el Docker la instancia corriendo.
4) Correr ```./sandbox goal account list```  Para ver las cuentas en el nodo demo:
    Existen dos tipos de cuentas: Online y Offline
5) Correr ```./sandbox test``` para ver cómo correr 
6) Extraer nemónico ```./sandbox goal account export --address YOUR_ACCOUNT_ADDRESS```
7) Ver la lista de las wallets ```./sandbox goal wallet list```
8) Más comando en : https://developer.algorand.org/

### Otros comandos 

Datos 
    Alice Key: 2T5BSXL4C2WMQFNNTAJD66F4ACZ5J27KZPPPTGELUW6BO7V46IH6FUBI44
    Tom Key: TD3W6ZKVSFLHP3R3FKB2F27I67LYVVO3NTY7FRBTCQAI33CCEMNJZAVMGQ
    

1) Crear nueva cuenta  ``` ./sandbox goal account new alice```

2) Mandar Tokens  ```./sandbox goal clerk send --from 'public_key' --to 'name' --amount 100000```

3) Mandar Tokens 
    ```./sandbox goal clerk send --from 'public_key' --to 'name' --amount 100000```
./sandbox goal clerk send --from BLBXRGMAPN4CWNNFMM6X3IC7BXV7BYCLO5OITIUSNTBRTY6KXJBG24EA5M --to alice --amount 1000000

4) Asegurar Doble
    ``` ./sandbox goal clerk send --from 'name1' --to 'name1' --amount 0 --rekey-to 'publick key name2'```
./sandbox goal clerk send --from alice --to alice --amount 0 --rekey-to TD3W6ZKVSFLHP3R3FKB2F27I67LYVVO3NTY7FRBTCQAI33CCEMNJZAVMGQ
Ahora si intentamos mandar ALGOs de la cuenta de alice a tom, fallará. Entonces, esta TRX debe de ser confirmada por tom 

5) Crear un file de la transacción
    ``` ./sandbox goal clerk send --from 'name1' --to 'name2' --amount 10000 --out send-single.txn``` 
./sandbox goal clerk send --from alice --to tom --amount 10000 --out send-single.txn

6) Firmar una transacción 
    ```./sandbox goal clerk sign --signer 'publick key name2' --infile send-single.txn --outfile send-single.stxn```
./sandbox goal clerk sign --signer TD3W6ZKVSFLHP3R3FKB2F27I67LYVVO3NTY7FRBTCQAI33CCEMNJZAVMGQ --infile send-single.txn --outfile send-single.stxn

7) Atender la firma y TRX
    ```./sandbox goal clerk rawsend --filename send-single.stxn```

8)Asegurar Triple

## Crear y Correr Algo Builder 
1) ``` npm install --global yarn```

## Instalación de paquetes 

### Máquina 
* NodeJs 
* Python 3
    - Pyenv 
    - Pyteal
* #### Algo Builder 
1) ``` npm install --global yarn```
2) ```yarn init``` and put all questions in white 
3) Creae the framework ```yarn add @algo-builder/algob@3.2.0```
4) Run the proyect ``` yarn run algob init . ```
5) Copiar el archivo Pipfile en la raíz de la carpeta : https://github.com/scale-it/algo-builder/blob/master/Pipfile
6) Run ``` pipenv install ```
7) Activar el virtualenv ``` pipenv shell ```
8) Change the master account for the sandbox wallet 
8) Deploy SC ``` yarn run algob deploy ``` 
### Proyectos

* Algosdk
```npm install algosdk ```

* Dotenv  
```npm install dotenv ```

* Crear un documento .env 
    - Correr ```source .env ```

## Correr un script 
```node name.js```

## AlgoSigner 

Podemos crear y conectar una wallet. Para conocer los comandos hay que visitar : https://github.com/PureStake/algosigner

## Faucet Algorand Tesnet 
https://bank.testnet.algorand.network/

## LESSON 3 

(Falta abajo de la lección 10)

### Rekeying
Es mantener una llave pública, pero asegurándola con otra llave privada. Entonces para que salgan fondos de la primera cuenta deberán de estar firmados por la segunda.

### Mi Smart Coontract

1. https://testnet.algoexplorer.io/application/145541430

### LINKS 

Demo accounts wallets :  https://github.com/Algo-Foundry/demo-accounts-wallets :  https://github.com/PureStake/algosigner
PureStake : https://www.purestake.com/ya

Algorand SDK Funcrions : https://algorand.github.io/js-algorand-sdk/modules.html