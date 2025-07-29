data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False

    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.
for idx, dict in enumerate(data):
    if not all(key in dict for key in key_list):
            [dict.setdefault(key, 'unknow') for key in key_list if key not in dict]
        
    [print(f'{key} 은/는 {dict.get(key)}입니다.') for key in key_list]