from electrum.bitcoin import base_decode, base_encode, Hash, is_address
from electrum.exceptions import MissingHeader
from ..bitcoin import hash_encode
from electrum.util import inv_dict, read_json, bfh, to_bytes, BitcoinException
from .abstract_network import AbstractNet
from .auxpow_mixin import AuxPowMixin
from .stake_mixin import StakeMixin

class CheetahcoinMainnet(AbstractNet, StakeMixin):

    NAME = 'Cheetahcoin'
    NAME_LOWER = 'cheetahcoin'
    SHORT_CODE = 'CHTA'
    DATA_DIR = 'cheetahcoin'
    OPEN_ALIAS_PREFIX = 'chta'
    PAYMENT_URI_SCHEME = 'cheetahcoin'
    PAYMENT_REQUEST_PKI_TYPE = "dnssec+chta"
    APPLICATION_PAYMENT_REQUEST_TYPE = 'application/cheetahcoin-paymentrequest'
    APPLICATION_PAYMENT_TYPE = 'application/cheetahcoin-payment'
    APPLICATION_PAYMENT_ACK_TYPE = 'application/cheetahcoin-paymentack'
    BASE_UNITS = {'CHTA': 8, 'mCHTA': 5, 'uCHTA': 2, 'swartz': 0}
    BASE_UNITS_INVERSE = inv_dict(BASE_UNITS)
    BASE_UNITS_LIST = ['CHTA', 'mCHTA', 'uCHTA', 'swartz']
    TESTNET = False

    WIF_PREFIX = 0x80
    ADDRTYPE_P2PKH = 28
    ADDRTYPE_P2SH = 5
    XPRV_HEADERS = {
        'standard': 0x0488ade4,
    }
    XPRV_HEADERS_INV = inv_dict(XPRV_HEADERS)
    XPUB_HEADERS = {
        'standard': 0x0488b21e,
    }
    XPUB_HEADERS_INV = inv_dict(XPUB_HEADERS)
    BIP44_COIN_TYPE = 682

    GENESIS = "0000000090ae6bab6c2abd99179a7632b84f286f876def641dd35c3221eee7be"

    DEFAULT_PORTS = {'t': '10007', 's': '10008'}
    DEFAULT_SERVERS = read_json('servers/Cheetahcoin-Mainnet.json', {})
    CHECKPOINTS = read_json('checkpoints/Cheetahcoin-Mainnet.json', [])

    LN_REALM_BYTE = 0
    LN_DNS_SEEDS = []

    COINBASE_MATURITY = 100
    COIN = 100000000
    TOTAL_COIN_SUPPLY_LIMIT = 21000000000
    SIGNED_MESSAGE_PREFIX = b"\x18Cheetahcoin Signed Message:\n"

    DECIMAL_POINT_DEFAULT = 8 # CHTA
    
    TARGET_TIMESPAN = int(1 * 24 * 60 * 60)
    TARGET_SPACING = int(2 * 60)
    INTERVAL = int(TARGET_TIMESPAN / TARGET_SPACING)

    BLOCK_EXPLORERS = {
        'chtaexplorer.mooo.com': ('http://chtaexplorer.mooo.com:3002/', {'tx': '/tx/', 'addr': '/address/'}),
        'chta.mining4people.com': ('https://chta.mining4people.com/', {'tx': '/tx/', 'addr': '/address/'}),
    }


    @classmethod
    def get_target(cls, height: int, blockchain) -> int:
        index = height // 720 - 1
        if index == -1:
            return cls.MAX_TARGET

        # CHTA Blockchain is randomSpike on top of sha256 so that we dont have the info needed to
        # calculate the targets required
        return 0
