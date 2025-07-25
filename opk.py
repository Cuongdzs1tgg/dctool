s={'data': {'data': {'user': {'friendship_status': {'following': True, 'outgoing_request': False, 'text_post_app_pre_following': False}, 'id': '66516162781'}}}, 'extensions': {'is_final': True, 'server_metadata': {'request_start_time_ms': 1752381190204, 'time_at_flush_ms': 1752381191033}}, 'status': 'ok'}

if s.get('data') and s['data'].get('data') and \
       s['data']['data'].get('user') and \
       s['data']['data']['user'].get('friendship_status') and \
       s['data']['data']['user']['friendship_status'].get('following') == True:
        print("ok")
else:
    sys