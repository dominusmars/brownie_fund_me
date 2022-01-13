from sqlite3.dbapi2 import Error
from scripts.helper_functions import LOCAL_BLOCKCHAIN_DEPLOYMENTS, get_account
from scripts.deploy import deploy_fund_me
from brownie import network, accounts, exceptions
import pytest


def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entreance_fee = fund_me.getEntranceFee() + 100
    tx = fund_me.fund({"from": account, "value": entreance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entreance_fee
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_DEPLOYMENTS:
        pytest.skip("only for local testing")
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
