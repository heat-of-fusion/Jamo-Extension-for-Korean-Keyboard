# Dictionary to convert jaums to double-jaum.
double_jaum_dict = {
    'ㄱㄱ': 'ㄲ',
    'ㄱㅅ': 'ㄳ',
    'ㄴㅈ': 'ㄵ',
    'ㄴㅎ': 'ㄶ',
    'ㄷㄷ': 'ㄸ',
    'ㄹㄱ': 'ㄺ',
    'ㄹㅁ': 'ㄻ',
    'ㄹㅂ': 'ㄼ',
    'ㄹㅅ': 'ㄽ',
    'ㄹㅌ': 'ㄾ',
    'ㄹㅍ': 'ㄿ',
    'ㄹㅎ': 'ㅀ',
    'ㅂㅂ': 'ㅃ',
    'ㅂㅅ': 'ㅄ',
    'ㅅㅅ': 'ㅆ',
    'ㅈㅈ': 'ㅉ'
}

# Dictionary to convert moums to double-moum
double_moum_dict = {
    'ㅗㅏ': 'ㅘ',
    'ㅗㅐ': 'ㅙ',
    'ㅗㅣ': 'ㅚ',
    'ㅜㅔ': 'ㅞ',
    'ㅜㅓ': 'ㅝ',
    'ㅜㅣ': 'ㅟ',
    'ㅡㅣ': 'ㅢ',
    'ㅑㅣ': 'ㅒ',
    'ㅣㅕ': 'ㅒ',
    'ㅕㅣ': 'ㅖ',
    'ㅏㅣ': 'ㅐ',
    'ㅣㅓ': 'ㅐ',
    'ㅓㅣ': 'ㅔ',
}

# Dictionary to decompose double-moum to moums
moum_decomp_dict = dict(zip(list(double_moum_dict.values()), list(double_moum_dict.keys())))