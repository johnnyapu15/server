from web3 import Web3, HTTPProvider
from solc import compile_files

ip = 'localhost'
port = '8545'
rpcUrl = 'http://' + ip + ":" + port

w3 = Web3(HTTPProvider(rpcUrl))

# contract_id = Web3.toChecksumAddress("")

# contract_code = ''
# compiled = compile_files(contract_code)
# interface = compiled["<stdin>:##contractName##"]

# contract = w3.eth.contract(
#     abi= contract_interface['abi'],
#     bytecode= contract_interface['bin'],
#     bytecode_runtime= contract_interface['bin-runtime']
#     )

# instance = contract(contract_id)



def isParticipated(_tournament_code, _account):
    t = True
    # t = 블록체인에서
    # 해당 토너먼트 코드의 참여자중에 계정이 있는지
    # 확인()
        # try:
        #     t = instance.transact({"from": Web3.toChecksumAddress(_account).isParticipated(_tournament_code)
        # except ValueError as v:
        #     return "오류: 관리자에게 문의하세요.<br>" + str(v) 
    
    return t