users_socket = dict()
users_by_user_id = dict()

ROUTES = {
    'FRONT': {
        'CONNECT': 'connect',
        'DISCONNECT': 'disconnect',
        'AUTH': 'auth',
        'USER': {
            'ALL': 'user:all'
        },
        'CHAT': {
            'STATUS': 'chat:status',
            'PARTICIPATED': 'chat:participated',
            'MESSAGE': {
                'HISTORY': 'chat:message:history',
                'NEW': 'chat:message:new'
            }
        }
    },
    'BACK': {
        'CONNECT': 'connect',
        'DISCONNECT': 'disconnect',
        'USER': {
            'INVITE': 'user:invite',
            'EXCLUDE': 'user:exclude'
        },
        'CHAT': {
            'CREATE': 'chat:create',
            'REMOVE': 'chat:remove',
            'INVITE': 'chat:invite',
            'CHANGE': 'chat:change',
            'MESSAGE': {
                'NEW': 'chat:message:new',
                'EDIT': 'chat:message:edit',
                'REMOVE': 'chat:message:remove',
            }
        },
    }
}
