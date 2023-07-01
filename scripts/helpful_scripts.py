from brownie import network, config, accounts, MockV3Aggregator

DECIMALS = 8
STARTING_PRICE = 200000000000

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"Contract deployed to {network.show_active()}")
    print(f"Deploying the mocks!")
    MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print(f"Mocks Deployed")
