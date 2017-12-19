from blockcypher.constants import COIN_SYMBOL_ODICT_LIST

COIN_METADATA = {coin['coin_symbol']: coin for coin in COIN_SYMBOL_ODICT_LIST}

COIN_METADATA['bch'] = {
    'coin_symbol': 'bch',
    'vbypte_pubkey': 0
}