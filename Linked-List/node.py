linked_list = {
    'value': 10,
    'next': {
        'value': 12,
        'next': {
            'value': 13,
            'next': None,
        }
    }
}

print(linked_list['next']['next'])
