from brownie import MockV3Aggregator, accounts, network, config
# from web3 import Web3

LOCAL_BLOCKCHAIN_DEPLOYMENTS = ["development", "ganache-local"]
FOCKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]


DECIMALS = 8
STARTING_PRICE = 20000000000

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_DEPLOYMENTS or network.show_active() in FOCKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is ${network.show_active()}")
    print("Deploying Mock...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print("Mocks deployed successfully")
    return MockV3Aggregator[-1].address
