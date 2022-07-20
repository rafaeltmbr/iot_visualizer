from random import shuffle

class DeviceSecret:
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'

    def generate(size: int = 16) -> str:
        char_list = list(DeviceSecret.alphabet)
        shuffle(char_list)
        return ''.join(char_list)[:size]