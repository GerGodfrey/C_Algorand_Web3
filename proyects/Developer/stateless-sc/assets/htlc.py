
# STATELESS CONTRACT

import sys
sys.path.insert(0,'.')

from algobpy.parse import parse_params
from pyteal import *

def htlc(acc1_addr, acc2_addr, hash, timeout):

    basic_checks = And(
        Txn.type_enum() == TxnType.Payment,
        Txn.rekey_to() == Global.zero_address(),
        Txn.close_remainder_to() == Global.zero_address(),
        Txn.fee() <= Int(1000)
    )

    rcv_cond = And(
        basic_checks,
        Sha256(Arg(0)) == Bytes("base64", hash)
    )

    timeout_cond = And(
        basic_checks,
        Txn.first_valid() > Int(timeout)
    )

    program = Cond(
        [Txn.receiver() == Addr(acc2_addr), rcv_cond],
        [Txn.receiver() == Addr(acc1_addr), timeout_cond]
    )

    return program

if __name__ == "__main__":
    # Default receiver address used if params are not supplied when deploying this contract
    params = {
        "acc1": "2T5BSXL4C2WMQFNNTAJD66F4ACZ5J27KZPPPTGELUW6BO7V46IH6FUBI44",
        "acc2": "TD3W6ZKVSFLHP3R3FKB2F27I67LYVVO3NTY7FRBTCQAI33CCEMNJZAVMGQ",
        "hash": "QzYhq9JlYbn2QdOMrhyxVlNtNjeyvyJc/I8d8VAGfGc=",
        "timeout": 3001
    }

    # Overwrite params if sys.argv[1] is passed
    if(len(sys.argv) > 1):
        params = parse_params(sys.argv[1], params)

    print(compileTeal(htlc(
        params["acc1"], 
        params["acc2"], 
        params["hash"], 
        params["timeout"]), mode=Mode.Signature, version=6))