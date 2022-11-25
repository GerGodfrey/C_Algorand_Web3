const { executeTransaction, convert } = require("@algo-builder/algob");
const { types } = require("@algo-builder/web");
const helper = require('./helper.js');

async function run(runtimeEnv, deployer) {
    const acc1 = deployer.accountsByName.get("acc1");

    // get app info
    const approvalFile = "ab_approval.py";
    const clearStateFile = "ab_clearstate.py";
    const app = deployer.getApp(approvalFile, clearStateFile);

    // app call to update global state of the contract
    const appCallArgs = [convert.stringToBytes("UpdateGlobal"), convert.stringToBytes("acc1"), convert.uint64ToBigEndian(10)];
    await executeTransaction(deployer, {
        type: types.TransactionType.CallApp,
        sign: types.SignType.SecretKey,
        fromAccount: acc1,
        appID: app.appID,
        payFlags: { totalFee: 1000 },
        appArgs: appCallArgs,
    });

    // read global state after
    console.log(await helper.readGlobalStateWithoutAlgoBuilder(deployer.algodClient, app.appID));
}

module.exports = { default: run };
