const { executeTransaction, convert, readAppGlobalState } = require("@algo-builder/algob");
const { types } = require("@algo-builder/web");

async function run(runtimeEnv, deployer) {
    const master = deployer.accountsByName.get("master");
    const approvalFile = "game_approval.py";
    const clearStateFile = "game_clearstate.py";

    /**
     * Create Application
     * 
     * Global Ints
     * 1. Health
     * 2. MaxDamage
     * Global Bytes
     * 1. Mvp
     * Local Ints
     * 1. Damage
     */
    const monsterHealth = 5;
    await deployer.deployApp(
        approvalFile,
        clearStateFile,
        {
            sender: master,
            localInts: 1,
            localBytes: 0,
            globalInts: 2, //numero de espacios necesarios 
            globalBytes: 1,
            appArgs: [convert.uint64ToBigEndian(monsterHealth)],
        },
        { totalFee: 1000 }
    );

    // get app info
    const gameApp = deployer.getApp(approvalFile, clearStateFile);
    console.log(gameApp);
    const gameAppAddress = gameApp.applicationAccount;
    console.log("app account address:", gameAppAddress);

    let globalState = await readAppGlobalState(deployer, master.addr, gameApp.appID);
    console.log(globalState);

    // fund account with 20 algos
    await executeTransaction(deployer, {
        type: types.TransactionType.TransferAlgo,
        sign: types.SignType.SecretKey,
        fromAccount: master,
        toAccountAddr: gameAppAddress,
        amountMicroAlgos: 2e7, //20 algos
        payFlags: { totalFee: 1000 },
    });

    // get app account balance
    let appAccount = await deployer.algodClient.accountInformation(gameAppAddress).do();
    console.log(appAccount);
}

module.exports = { default: run };
