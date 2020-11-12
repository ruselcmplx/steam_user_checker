import os
from steam.webapi import WebAPI

steam_key = os.getenv('STEAM_KEY')
api = WebAPI(key=steam_key)

PERSONA_STATES = {
    0: 'оффлайн',
    1: 'онлайн',
    2: 'занят',
    3: 'ушел',
    4: 'спит',
    5: 'готов поторговаться',
    6: 'готов поиграть'
}


def get_user_data(name: str):
    try:
        data = api.call('ISteamUser.ResolveVanityURL',
                        vanityurl=name)
        steam_id = data['response']['steamid']
        if (steam_id):
            return get_user_data_by_id(steam_id)
    except:
        return None


def get_user_data_by_id(user_id: int):
    try:
        data = api.call('ISteamUser.GetPlayerSummaries',
                        steamids=user_id)
        steam_user = data['response']['players'][0]
        if (steam_user and 'personastate' in steam_user):
            return {
                'name': steam_user['personaname'],
                'status': PERSONA_STATES[steam_user['personastate']] or None,
                'avatar': steam_user['avatar']
            }
    except Exception:
        return None
