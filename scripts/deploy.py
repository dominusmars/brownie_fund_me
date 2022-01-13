from brownie import FundMe, network, config
from scripts.helper_functions import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_DEPLOYMENTS,
)


def deploy_fund_me():
    account = get_account()
    # pass the fundme pricefeed
    # if on rinkeby then interal address
    if network.show_active() not in LOCAL_BLOCKCHAIN_DEPLOYMENTS:
        pricefeed = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        pricefeed = deploy_mocks()

    fund_me = FundMe.deploy(
        pricefeed,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    return fund_me


def main():
    deploy_fund_me()
