from scripts.helper_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    deploy_mocks,
    get_account,
)
from brownie import config, network, FundMe, MockV3Aggregator


def deploy_fund_me():
    account = get_account()
    verify = config["networks"][network.show_active()].get("verify")

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    # pass the price feed address
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=verify,
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
