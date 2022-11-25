const { executeTransaction, convert, readAppLocalState } = require("@algo-builder/algob");
const { types } = require("@algo-builder/web");
const helper = require('./helper.js');

async function run(runtimeEnv, deployer) {
    const master = deployer.accountsByName.get("master");
    const acc1 = deployer.accountsByName.get("acc1");

    // get app info
    const approvalFile = "ab_approval.py";
    const clearStateFile = "ab_clearstate.py";
    const app = deployer.getApp(approvalFile, clearStateFile);

    // receiver opt into the contract
    const appLocalState = await helper.readLocalStateWithoutAlgoBuilder(deployer.algodClient, acc1.addr, app.appID);
    if (appLocalState === undefined) {
        await deployer.optInAccountToApp(acc1, app.appID, { totalFee: 1000 }, {});
    }

    // read initial local state
    console.log(await readAppLocalState(deployer, acc1.addr, app.appID));
    console.log(await helper.readLocalStateWithoutAlgoBuilder(deployer.algodClient, acc1.addr, app.appID));

    // update local state
    const appCallArgs = [convert.stringToBytes("UpdateLocal")];
    await executeTransaction(deployer, {
        type: types.TransactionType.CallApp,
        sign: types.SignType.SecretKey,
        fromAccount: acc1,
        appID: app.appID,
        payFlags: { totalFee: 1000 },
        appArgs: appCallArgs,
    });

    // read local state after
    console.log(await helper.readLocalStateWithoutAlgoBuilder(deployer.algodClient, acc1.addr, app.appID));
}

module.exports = { default: run };
