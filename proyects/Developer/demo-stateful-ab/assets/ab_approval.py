from pyteal import *

def game():
    '''
    Save application args when app is initialized
    '''
    # esto se corre primero al deployar el proyecto 
    handle_creation = Seq([
        App.globalPut(Bytes("GlobalText"), Txn.application_args[0]), #GUardamos el primer argumento
        App.globalPut(Bytes("GlobalInteger"), Btoi(Txn.application_args[1])), #Guardamos el segundo argumento
        Return(Int(1))
    ])

    '''
    Initialize account's local state during opt in
    '''
    handle_optin = Seq([
        Assert(App.optedIn(Txn.sender(), Txn.application_id())), #check if the transaction sender has. aalready opted
        App.localPut(Txn.sender(), Bytes("LocalText"), Bytes("welcome")), #guardamos los valores locales 
        App.localPut(Txn.sender(), Bytes("LocalInteger"), Int(0)),
        Return(Int(1))
    ])

    '''
    Application call to update Global State
    '''
    update_global = Seq([
        App.globalPut(Bytes("GlobalText"), Txn.application_args[1]), #actualizacion de información
        App.globalPut(Bytes("GlobalInteger"), Btoi(Txn.application_args[2])), #actualizamos el 3er elemento de los argumentos por GlobalInteger
        Return(Int(1))
    ])

    '''
    Application call to update account's local state with data from global state
    '''
    update_local = Seq([
        Assert(App.optedIn(Txn.sender(), Txn.application_id())),
        App.localPut(Txn.sender(), Bytes("LocalText"), App.globalGet(Bytes("GlobalText"))), #ponemos lo de global (SC) en local 
        App.localPut(Txn.sender(), Bytes("LocalInteger"), App.globalGet(Bytes("GlobalInteger"))),
        Return(Int(1))
    ])

    '''
    Creator function - inner transaction to send Algos to account via app call
    '''
    amountToSend = Btoi(Txn.application_args[1])
    
    send_algos = Seq([
        Assert(Txn.sender() == Global.creator_address()), # creator only function
        Assert(amountToSend <= Int(1000000)), # less than or equals to 1 Algo
        InnerTxnBuilder.Begin(),
        InnerTxnBuilder.SetFields({
            TxnField.type_enum: TxnType.Payment,
            TxnField.receiver: Txn.accounts[1], # Txn.accounts[0] belongs to app creator
            TxnField.amount: amountToSend,
        }),
        InnerTxnBuilder.Submit(),
        Return(Int(1))
    ])

    handle_noop = Seq(
        Cond(
            [Txn.application_args[0] == Bytes("UpdateGlobal"), update_global],
            [Txn.application_args[0] == Bytes("UpdateLocal"), update_local],
            [Txn.application_args[0] == Bytes("SendAlgos"), send_algos],
        )
    )

    handle_closeout = Return(Int(1))
    handle_updateapp = Return(Int(0))
    handle_deleteapp = Return(Int(0))

    program = Cond(
        [Txn.application_id() == Int(0), handle_creation],
        [Txn.on_completion() == OnComplete.OptIn, handle_optin],
        [Txn.on_completion() == OnComplete.CloseOut, handle_closeout],
        [Txn.on_completion() == OnComplete.UpdateApplication, handle_updateapp],
        [Txn.on_completion() == OnComplete.DeleteApplication, handle_deleteapp],
        [Txn.on_completion() == OnComplete.NoOp, handle_noop]
    )

    return program

if __name__ == "__main__":
    print(compileTeal(game(), mode=Mode.Application, version=6))