from pyteal import *

"""Basic Counter Application"""

def approval_program():
    handle_creation = Seq([
        App.globalPut(Bytes("Count"), Int(0)),
        Return(Int(1))
    ])

    handle_optin = Return(Int(0))
    handle_closeout = Return(Int(0))
    handle_updateapp = Return(Int(0))
    handle_deleteapp = Return(Int(1))
    scratchCount = ScratchVar(TealType.uint64)

    add = Seq([
        scratchCount.store(App.globalGet(Bytes("Count"))), #cargamos el valor de count 
        App.globalPut(Bytes("Count"), scratchCount.load() + Int(1)), #le sumamos uno y después lo volvemos a guardar 
        Return(Int(1))
    ])

    deduct = Seq([
        scratchCount.store(App.globalGet(Bytes("Count"))),
         If(scratchCount.load() > Int(0),
             App.globalPut(Bytes("Count"), scratchCount.load() - Int(1)),
         ),
         Return(Int(1))
    ])

    handle_noop = Seq(
        Assert(Global.group_size() == Int(1)), #checa el tamaño de las trx
        Cond( #vemos que condición tiene el contrato add or deduct 
            [Txn.application_args[0] == Bytes("Add"), add], 
            [Txn.application_args[0] == Bytes("Deduct"), deduct]
        )
    )


    # verifica que exista una transacción y después define que tipo es
    # después manda a llamar la función que corresponde 
    program = Cond(
        [Txn.application_id() == Int(0), handle_creation],
        [Txn.on_completion() == OnComplete.OptIn, handle_optin],
        [Txn.on_completion() == OnComplete.CloseOut, handle_closeout],
        [Txn.on_completion() == OnComplete.UpdateApplication, handle_updateapp],
        [Txn.on_completion() == OnComplete.DeleteApplication, handle_deleteapp],
        [Txn.on_completion() == OnComplete.NoOp, handle_noop]
    )

    return compileTeal(program, Mode.Application, version=6)

# print out the results
print(approval_program())