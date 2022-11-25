const { executeTransaction, convert, readAppGlobalState } = require("@algo-builder/algob");
const { types } = require("@algo-builder/web");
const helper = require('./actions/helper.js');
const algosdk = require("algosdk");

async function run(runtimeEnv, deployer) {
    const master = deployer.accountsByName.get("master");
    
    // deploy app
    const approvalFile = "ab_approval.py";
    const clearStateFile = "ab_clearstate.py";

    /**
     * Create Application
     * 
     * Global Ints
     * 1. GlobalText
     * Global Bytes
     * 1. GlobalInteger
     * Local Ints
     * 1. LocalInteger
     * Local Bytes
     * 1. LocalText
     */

    // Aqui estan los argumentos de la aplicacion
    const deployAppArgs = [convert.stringToBytes("Hello"), convert.uint64ToBigEndian(5)];

    // Aqui se deploya nuestra aplicacion y despues Algo BBuilder nos ayuda para 
    // obtener la aplicacion basada en los python files ( el TED o esa kk )
    await deployer.deployApp(
        approvalFile,
        clearStateFile,
        {
            sender: master,
            localInts: 1, //especificamos el storage de las variables. 
            localBytes: 1,
            globalInts: 1, // primer vairbale para global 
            globalBytes: 1, // segunda variable para global
            appArgs: deployAppArgs,
        },
        { totalFee: 1000 }
    );

    // get app info
    const app = deployer.getApp(approvalFile, clearStateFile);

    // fund contract with some algos to handle inner txn
    await executeTransaction(deployer, {
        type: types.TransactionType.TransferAlgo,
        sign: types.SignType.SecretKey,
        fromAccount: master,
        toAccountAddr: app.applicationAccount,
        amountMicroAlgos: 2e7, //20 algos
        payFlags: { totalFee: 1000 },
    });

    // READ GLOBAL STATE

    // using helper function from AB
    const globalState = await readAppGlobalState(deployer, master.addr, app.appID);
    console.log(globalState);

    // without AB
    const globalState2 = await helper.readGlobalStateWithoutAlgoBuilder(deployer.algodClient, app.appID);
    console.log(globalState2);
}

module.exports = { default: run };
