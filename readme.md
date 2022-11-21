# Pasos 


## Crear y Correr Nodo 

1) Correr docker 

2) Clonar el repositorio de https://github.com/algorand/sandbox 

3) Dentro de sandbox Correr ``` ./sandbox up ```. Para confirmar Podemos ver en el Docker la instancia corriendo.

4) Correr ```./sandbox goal account list```  Para ver las cuentas en el nodo demo:
    Existen dos tipos de cuentas: Online y Offline

5) Correr ```./sandbox test``` para ver cómo correr 

5) Extraer nemónico ```./sandbox goal account export --address YOUR_ACCOUNT_ADDRESS```

6) Ver la lista de las wallets ```./sandbox goal wallet list```

7) Más comando en : https://developer.algorand.org/

## Instalación de paquetes 

### Máquina 
* NodeJs 
* Python 3
    - Pyenv 
    - Pyteal 

### Proyectos

* Algosdk
```npm install algosdk ```

* Dotenv  
```npm install dotenv ```

* Crear un documento .env 
    - Correr ```source .env ```

## Correr un script 
```node name.js```

Desde el mismo portafolio correr yarn init y dejar todo en blanco 

3) Correr yarn add @algo-builder/algob@3.2.0
4) Inicializar el proyecto yarn run algob init .
5) Activar el virtualenv pipenv shell 
6) Correr pipenv run ( no lo hicimos)

Deploy los contratos 
    yarn run algob deploy

8) Cambiar algob.config 
9) Vismo como ocupar postman para las querys 

## LESSON 3 

(Falta abajo de la lección 10)

### Rekeying
Es mantener una llave pública, pero asegurándola con otra llave privada. Entonces para que salgan fondos de la primera cuenta deberán de estar firmados por la segunda.

Crear nueva cuenta : 
    ./sandbox goal account new alice

    Alice Key: 2T5BSXL4C2WMQFNNTAJD66F4ACZ5J27KZPPPTGELUW6BO7V46IH6FUBI44
    Tom Key: TD3W6ZKVSFLHP3R3FKB2F27I67LYVVO3NTY7FRBTCQAI33CCEMNJZAVMGQ

Mandar Tokens 
    ./sandbox goal clerk send --from 'public_key' --to 'name' --amount 100000

    ./sandbox goal clerk send --from BLBXRGMAPN4CWNNFMM6X3IC7BXV7BYCLO5OITIUSNTBRTY6KXJBG24EA5M --to alice --amount 1000000

Asegurar Doble
    ./sandbox goal clerk send --from 'name1' --to 'name1' --amount 0 --rekey-to 'publick key name2'

    ./sandbox goal clerk send --from alice --to alice --amount 0 --rekey-to TD3W6ZKVSFLHP3R3FKB2F27I67LYVVO3NTY7FRBTCQAI33CCEMNJZAVMGQ

    Ahora si intentamos mandar ALGOs de la cuenta de alice a tom, fallará.
    Entonces, esta TRX debe de ser confirmada por tom 

Crear un file de la transacción
    ./sandbox goal clerk send --from 'name1' --to 'name2' --amount 10000 --out send-single.txn

    ./sandbox goal clerk send --from alice --to tom --amount 10000 --out send-single.txn

Firmar una transacción 
    ./sandbox goal clerk sign --signer 'publick key name2' --infile send-single.txn --outfile send-single.stxn

    ./sandbox goal clerk sign --signer TD3W6ZKVSFLHP3R3FKB2F27I67LYVVO3NTY7FRBTCQAI33CCEMNJZAVMGQ --infile send-single.txn --outfile send-single.stxn

Atender la firma y TRX
    ./sandbox goal clerk rawsend --filename send-single.stxn

Asegurar Triple

### LINKS 

Demo accounts wallets :  https://github.com/Algo-Foundry/demo-accounts-wallets