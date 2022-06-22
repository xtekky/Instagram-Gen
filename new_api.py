import requests

headers = {
    'authority': 'www.facebook.com',
    'accept': '*/*',
    'accept-language': 'en',
    'cache-control': 'no-cache',
    'origin': 'https://www.instagram.com',
    'pragma': 'no-cache',
    'referer': 'https://www.instagram.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
}

response = requests.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&input_token&origin=1&redirect_uri=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Femailsignup%2F&sdk=joey&wants_cookie_data=true', headers=headers)


#----------------------------------------------------------------


cookies = {
    'csrftoken': 'pCxzOjlYS12pQ4knokE0W9axzLR1RCem',
    'mid': 'YrOGswALAAFJ3HA4e_mjCgzdyCKN',
    'ig_did': 'F3C03963-BF21-43B8-93B1-89E458329F49',
}

headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'csrftoken=pCxzOjlYS12pQ4knokE0W9axzLR1RCem; mid=YrOGswALAAFJ3HA4e_mjCgzdyCKN; ig_did=F3C03963-BF21-43B8-93B1-89E458329F49',
    'origin': 'https://www.instagram.com',
    'pragma': 'no-cache',
    'referer': 'https://www.instagram.com/accounts/emailsignup/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'x-asbd-id': '198387',
    'x-csrftoken': 'pCxzOjlYS12pQ4knokE0W9axzLR1RCem',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '2d77870e0d45',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    '__d': 'dis',
}

data = {
    'q': '[{"page_id":"vp4g8j","app_id":"936619743392459","device_id":"F3C03963-BF21-43B8-93B1-89E458329F49","frontend_env":"c1f","posts":[["qex:expose",{"universe_id":"e42bb34173aaba74caf60de2dabb1e9e","device_id":"F3C03963-BF21-43B8-93B1-89E458329F49"},1655934900401,0]],"trigger":"falco","send_method":"ajax"}]',
    'ts': '1655934901624',
}

response = requests.post('https://www.instagram.com/ajax/bz', params=params, cookies=cookies, headers=headers, data=data)


#------------------------------------------------


cookies = {
    'csrftoken': 'pCxzOjlYS12pQ4knokE0W9axzLR1RCem',
    'mid': 'YrOGswALAAFJ3HA4e_mjCgzdyCKN',
    'ig_did': 'F3C03963-BF21-43B8-93B1-89E458329F49',
}

headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'csrftoken=pCxzOjlYS12pQ4knokE0W9axzLR1RCem; mid=YrOGswALAAFJ3HA4e_mjCgzdyCKN; ig_did=F3C03963-BF21-43B8-93B1-89E458329F49',
    'origin': 'https://www.instagram.com',
    'pragma': 'no-cache',
    'referer': 'https://www.instagram.com/accounts/emailsignup/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'x-asbd-id': '198387',
    'x-csrftoken': 'pCxzOjlYS12pQ4knokE0W9axzLR1RCem',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'access_token': '936619743392459|3cdb3f896252a1db29679cb4554db266',
    'message': '{"app_id":"936619743392459","app_ver":"1.0.0","data":[{"time":1655934900.4,"name":"javascript_web_error","extra":{"appId":"936619743392459","access_token":null,"ancestor_hash":"3pkjb3","bundle_variant":"es6","clientTime":"1655934900","column":"14799","componentStackFrames":[],"extra":[],"frontend_env":"c1f","guardList":[],"line":"4","loggingFramework":"ig_web","messageFormat":"Initialized FB-Error From IG Web","messageParams":[],"name":"FBLogger","sample_weight":"1","script":"https://www.instagram.com/static/bundles/es6/ConsumerLibCommons.js/cfdddb9df230.js","stackFrames":[{"column":"14799","identifier":"Fe.$FBLogMessage1","line":"4","script":"https://www.instagram.com/static/bundles/es6/ConsumerLibCommons.js/cfdddb9df230.js"},{"column":"15387","identifier":"Fe.info","line":"4","script":"https://www.instagram.com/static/bundles/es6/ConsumerLibCommons.js/cfdddb9df230.js"},{"column":"442","identifier":"t","line":"2","script":"https://www.instagram.com/static/bundles/es6/ConsumerLibCommons.js/cfdddb9df230.js"},{"column":"1487","identifier":"e.entrypointReady","line":"2","script":"https://www.instagram.com/static/bundles/es6/ConsumerLibCommons.js/cfdddb9df230.js"},{"column":"3586","identifier":"","line":"1","script":"https://www.instagram.com/static/bundles/es6/Consumer.js/870110ca04ef.js"},{"column":"1343","identifier":"c","line":"281","script":"https://www.instagram.com/accounts/emailsignup/"},{"column":"895","identifier":"i","line":"281","script":"https://www.instagram.com/accounts/emailsignup/"},{"column":"390","identifier":"r","line":"281","script":"https://www.instagram.com/accounts/emailsignup/"},{"column":"22","identifier":"","line":"1327","script":"https://www.instagram.com/static/bundles/es6/Consumer.js/870110ca04ef.js"}],"type":"info","page_time":"400","project":"ig_web","push_phase":"c2","rollout_hash":"2d77870e0d45","server_revision":null,"spin":null,"svn_rev":"undefined","additional_client_revisions":[],"taalOpcodes":[2,2],"version":"3","xFBDebug":[],"windowLocationURL":"https://www.instagram.com/accounts/emailsignup/","loggingSource":"FBLOGGER","ancestors":[],"clientWeight":"1","page_position":"1"}},{"time":1655934900.489,"name":"instagram_web_osp_event","extra":{"frontend_env":"c1f","rollout_hash":"2d77870e0d45"}},{"time":1655934900.511,"name":"instagram_web_logged_out_impression","extra":{"rollout_hash":"2d77870e0d45","frontend_env":"c1f","app_id":"936619743392459","module":"signupPage","referrer":null,"referrer_domain":"","url":"/accounts/emailsignup/","original_referrer":null,"original_referrer_domain":"","objid":"/accounts/emailsignup/"}},{"time":1655934900.512,"name":"instagram_web_interaction_perf_events","extra":{"eventType":"asyncSwitch","orig":"","origId":"","dest":"signupPage","destId":"/accounts/emailsignup/","frontend_env":"c1f","timeTaken":28}},{"time":1655934900.547,"name":"instagram_web_osp_event","extra":{"frontend_env":"c1f","rollout_hash":"2d77870e0d45"}},{"time":1655934900.699,"name":"instagram_web_login","extra":{"event_name":"fb_status_received","fbconnect_status":"logged_out","frontend_env":"c1f","login_identifier_type":null,"path":"/accounts/emailsignup/","platform":"desktop","rollout_hash":"2d77870e0d45"}},{"time":1655934900.715,"name":"instagram_web_registration","extra":{"event_name":"form_load","fbconnect_status":"logged_out","frontend_env":"c1f","module":"loginPage","platform":"desktop","rollout_hash":"2d77870e0d45"}},{"time":1655934900.731,"name":"instagram_web_client_perf_events","extra":{"redirects":0,"dns":0,"connect":0,"request":179,"response":119,"network":191,"domInteractive":176,"domContentLoaded":176,"domComplete":430,"loadEvent":431,"displayDone":732,"timeToInteractive":543,"firstPaint":221,"firstContentfulPaint":221,"reactReady":280,"reactRender":3,"bundle_variant":"es6","frontend_env":"c1f","module":"LoginAndSignupPage","objid":"/accounts/emailsignup/","objtype":"url","pigeon_reserved_keyword_module":"LoginAndSignupPage","pigeon_reserved_keyword_obj_id":"/accounts/emailsignup/","pigeon_reserved_keyword_obj_type":"url","referrer":null,"referrer_domain":"","rollout_hash":"2d77870e0d45"}},{"time":1655934900.731,"name":"instagram_web_client_connection_info","extra":{"effectiveType":"4g","connectionType":"unknown","downlink":10000,"rtt":50,"objtype":"url","objid":"/accounts/emailsignup/"}}],"log_type":"client_event","seq":1,"session_id":"1818d6958b0-664580","device_id":"F3C03963-BF21-43B8-93B1-89E458329F49","claims":[]}',
}

response = requests.post('https://www.instagram.com/logging/falco', cookies=cookies, headers=headers, data=data)


#----------------------------------------------------------------


headers = {
    'authority': 'graph.instagram.com',
    'accept': '*/*',
    'accept-language': 'en',
    'cache-control': 'no-cache',
    'origin': 'https://www.instagram.com',
    'pragma': 'no-cache',
    'referer': 'https://www.instagram.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'x-asbd-id': '198387',
}




data = {
    'access_token': '936619743392459|3cdb3f896252a1db29679cb4554db266',
    'message': '{"app_id":"936619743392459","app_ver":"1.0.0","data":[{"time":1655934900.511,"name":"instagram_web_client_events","extra":{"event_type":"page_view","mid":"YrOGswALAAFJ3HA4e_mjCgzdyCKN","rollout_hash":"2d77870e0d45","frontend_env":"c1f","app_id":"936619743392459","page_id":"signupPage_email","referrer":null,"referrer_domain":"","original_referrer":null,"original_referrer_domain":""},"module":"signupPage","obj_type":"url","obj_id":"/accounts/emailsignup/"},{"time":1655934900.544,"name":"instagram_web_time_spent_navigation","extra":{"rollout_hash":"2d77870e0d45","frontend_env":"c1f","app_id":"936619743392459","event":"load","client_time":1655934900543,"time_spent_id":"vp4g8j","extra_data":{},"dest_endpoint":"loginPage","referrer":null,"referrer_domain":"","url":"/accounts/emailsignup/","original_referrer":null,"original_referrer_domain":""}},{"time":1655934900.621,"name":"instagram_web_time_spent_bit_array","extra":{"rollout_hash":"2d77870e0d45","frontend_env":"c1f","app_id":"936619743392459","tos_id":"vp4g8j","start_time":1655934900,"tos_array":[1,0],"tos_len":1,"tos_seq":0,"tos_cum":1,"log_time":1655934900620,"referrer":null,"referrer_domain":"","url":"/accounts/emailsignup/","original_referrer":null,"original_referrer_domain":""}},{"time":1655934901.622,"name":"device_status","extra":{"locale":"en"}}],"log_type":"client_event","seq":0,"session_id":"1818d6958b0-664580","device_id":"F3C03963-BF21-43B8-93B1-89E458329F49","claims":[]}',
}

response = requests.post('https://graph.instagram.com/logging_client_events', headers=headers, data=data)


data = {
    'access_token': '936619743392459|3cdb3f896252a1db29679cb4554db266',
    'message': '{"app_id":"936619743392459","app_ver":"1.0.0","data":[{"time":1655934908.143,"name":"instagram_web_time_spent_bit_array","extra":{"rollout_hash":"2d77870e0d45","frontend_env":"c1f","app_id":"936619743392459","tos_id":"vp4g8j","start_time":1655934908,"tos_array":[1,0],"tos_len":1,"tos_seq":2,"tos_cum":7,"log_time":1655934908142,"referrer":null,"referrer_domain":"","url":"/accounts/emailsignup/","original_referrer":null,"original_referrer_domain":""}}],"log_type":"client_event","seq":3,"session_id":"1818d6958b0-664580","device_id":"F3C03963-BF21-43B8-93B1-89E458329F49","claims":["0"]}',
}

response = requests.post('https://graph.instagram.com/logging_client_events', headers=headers, data=data)


#--------------------------------------------


cookies = {
    'csrftoken': 'pCxzOjlYS12pQ4knokE0W9axzLR1RCem',
    'mid': 'YrOGswALAAFJ3HA4e_mjCgzdyCKN',
    'ig_did': 'F3C03963-BF21-43B8-93B1-89E458329F49',
}

headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'csrftoken=pCxzOjlYS12pQ4knokE0W9axzLR1RCem; mid=YrOGswALAAFJ3HA4e_mjCgzdyCKN; ig_did=F3C03963-BF21-43B8-93B1-89E458329F49',
    'origin': 'https://www.instagram.com',
    'pragma': 'no-cache',
    'referer': 'https://www.instagram.com/accounts/emailsignup/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'x-asbd-id': '198387',
    'x-csrftoken': 'pCxzOjlYS12pQ4knokE0W9axzLR1RCem',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '2d77870e0d45',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1655934918:ARFQAM7RB3rDM2FNOeZtneVHPiKcsynAqF/6BA4y22FFEGIABw0S8ugMQIH6dQIQnoWBRVJCXTPLBnCEc3mTEgG8Twd6KNqi7NkDr6NpZv9v9qIPfe/1eZoA0K8K9sMZojdHhAtQ+34FsFrIycSh',
    'email': 'fesexa4678@mahazai.com',
    'username': 'fkahdia',
    'first_name': 'zefefzf zef',
    'opt_into_one_tap': 'false',
}

response = requests.post('https://www.instagram.com/accounts/web_create_ajax/attempt/', cookies=cookies, headers=headers, data=data)

#DRYUN PASSED == TRUE


#----------------------------------------------------------------


cookies = {
    'csrftoken': 'pCxzOjlYS12pQ4knokE0W9axzLR1RCem',
    'mid': 'YrOGswALAAFJ3HA4e_mjCgzdyCKN',
    'ig_did': 'F3C03963-BF21-43B8-93B1-89E458329F49',
}

headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'csrftoken=pCxzOjlYS12pQ4knokE0W9axzLR1RCem; mid=YrOGswALAAFJ3HA4e_mjCgzdyCKN; ig_did=F3C03963-BF21-43B8-93B1-89E458329F49',
    'origin': 'https://www.instagram.com',
    'pragma': 'no-cache',
    'referer': 'https://www.instagram.com/accounts/emailsignup/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'x-asbd-id': '198387',
    'x-csrftoken': 'pCxzOjlYS12pQ4knokE0W9axzLR1RCem',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '2d77870e0d45',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    '__d': 'dis',
}

data = {
    'q': '[{"page_id":"vp4g8j","app_id":"936619743392459","device_id":"F3C03963-BF21-43B8-93B1-89E458329F49","frontend_env":"c1f","posts":[["ods:incr",{"key":"web.password_encrypt.attempt"},1655934918090,0],["ods:incr",{"key":"web.password_encrypt.success"},1655934918110,0]],"trigger":"falco","send_method":"ajax"}]',
    'ts': '1655934919149',
}

response = requests.post('https://www.instagram.com/ajax/bz', params=params, cookies=cookies, headers=headers, data=data)



#------------------------------------------------



cookies = {
    'csrftoken': 'pCxzOjlYS12pQ4knokE0W9axzLR1RCem',
    'mid': 'YrOGswALAAFJ3HA4e_mjCgzdyCKN',
    'ig_did': 'F3C03963-BF21-43B8-93B1-89E458329F49',
}

headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'csrftoken=pCxzOjlYS12pQ4knokE0W9axzLR1RCem; mid=YrOGswALAAFJ3HA4e_mjCgzdyCKN; ig_did=F3C03963-BF21-43B8-93B1-89E458329F49',
    'origin': 'https://www.instagram.com',
    'pragma': 'no-cache',
    'referer': 'https://www.instagram.com/accounts/emailsignup/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'x-asbd-id': '198387',
    'x-csrftoken': 'pCxzOjlYS12pQ4knokE0W9axzLR1RCem',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'access_token': '936619743392459|3cdb3f896252a1db29679cb4554db266',
    'message': '{"app_id":"936619743392459","app_ver":"1.0.0","data":[{"time":1655934909.509,"name":"instagram_client_password_encryption_payload_sent","extra":{"encrypt_request_uuid":"81afe22e-8248-4d31-b6da-f4fc472bfe92","has_encrypted_params":false,"has_plaintext_params":false,"referrer_uri":"https://www.instagram.com/accounts/emailsignup/","request_uri":"/accounts/web_create_ajax/attempt/","tag":"#PWD_INSTAGRAM_BROWSER","version":10}},{"time":1655934910.51,"name":"instagram_client_password_encryption_payload_sent","extra":{"encrypt_request_uuid":"d27c09df-5e23-4b43-9dcf-0822fea5af22","has_encrypted_params":false,"has_plaintext_params":false,"referrer_uri":"https://www.instagram.com/accounts/emailsignup/","request_uri":"/accounts/web_create_ajax/attempt/","tag":"#PWD_INSTAGRAM_BROWSER","version":10}},{"time":1655934910.738,"name":"instagram_web_resource_transfer_size_events","extra":{"frontend_env":"c1f","full_page_load":false,"module":"signupPage","resource_type":"script","resources_count":"3","transfer_size":"107705"}},{"time":1655934910.738,"name":"instagram_web_resource_transfer_size_events","extra":{"frontend_env":"c1f","full_page_load":false,"module":"signupPage","resource_type":"img","resources_count":"3","transfer_size":"20597"}},{"time":1655934910.807,"name":"instagram_client_password_encryption_payload_sent","extra":{"encrypt_request_uuid":"d394992f-04bc-49d9-ac4b-a41550e9ee3a","has_encrypted_params":false,"has_plaintext_params":false,"referrer_uri":"https://www.instagram.com/accounts/emailsignup/","request_uri":"/accounts/web_create_ajax/attempt/","tag":"#PWD_INSTAGRAM_BROWSER","version":10}},{"time":1655934911.982,"name":"instagram_client_password_encryption_payload_sent","extra":{"encrypt_request_uuid":"3a10279e-2dc9-49f6-a3c2-7e73f6a2472b","has_encrypted_params":false,"has_plaintext_params":false,"referrer_uri":"https://www.instagram.com/accounts/emailsignup/","request_uri":"/accounts/web_create_ajax/attempt/","tag":"#PWD_INSTAGRAM_BROWSER","version":10}},{"time":1655934914.032,"name":"instagram_client_password_encryption_payload_sent","extra":{"encrypt_request_uuid":"a3a57ae5-dc15-4a7a-a83f-f8c57457a7ad","has_encrypted_params":false,"has_plaintext_params":false,"referrer_uri":"https://www.instagram.com/accounts/emailsignup/","request_uri":"/accounts/web_create_ajax/attempt/","tag":"#PWD_INSTAGRAM_BROWSER","version":10}},{"time":1655934918.09,"name":"instagram_client_password_encryption_encrypt_attempt","extra":{"encrypt_instance_uuid":"fdc01c55-d2fc-4b2c-859b-0e0e285921f8","encrypt_request_uuid":"bca13865-26cc-4273-824b-44bdac137dbe","key":"6a9d39334a7f31a51d67d383a1814ab0ebc7c799b6983c166f833fcabaf5543d","key_id":17,"tag":"#PWD_INSTAGRAM_BROWSER","version":10}},{"time":1655934918.11,"name":"instagram_client_password_encryption_encrypt_success","extra":{"encrypt_instance_uuid":"fdc01c55-d2fc-4b2c-859b-0e0e285921f8","encrypt_request_uuid":"bca13865-26cc-4273-824b-44bdac137dbe","key":"6a9d39334a7f31a51d67d383a1814ab0ebc7c799b6983c166f833fcabaf5543d","key_id":17,"tag":"#PWD_INSTAGRAM_BROWSER","version":10}},{"time":1655934918.111,"name":"instagram_client_password_encryption_payload_sent","extra":{"encrypt_request_uuid":"bca13865-26cc-4273-824b-44bdac137dbe","has_encrypted_params":true,"has_plaintext_params":false,"referrer_uri":"https://www.instagram.com/accounts/emailsignup/","request_uri":"/accounts/web_create_ajax/attempt/","tag":"#PWD_INSTAGRAM_BROWSER","version":10}}],"log_type":"client_event","seq":4,"session_id":"1818d6958b0-664580","device_id":"F3C03963-BF21-43B8-93B1-89E458329F49","claims":["0"]}',
}

response = requests.post('https://www.instagram.com/logging/falco', cookies=cookies, headers=headers, data=data)


#----------------------------------------------------------------



headers = {
    'authority': 'graph.instagram.com',
    'accept': '*/*',
    'accept-language': 'en',
    'cache-control': 'no-cache',
    'origin': 'https://www.instagram.com',
    'pragma': 'no-cache',
    'referer': 'https://www.instagram.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'x-asbd-id': '198387',
}

data = {
    'access_token': '936619743392459|3cdb3f896252a1db29679cb4554db266',
    'message': '{"app_id":"936619743392459","app_ver":"1.0.0","data":[{"time":1655934920.351,"name":"instagram_web_client_events","extra":{"event_type":"action","event_name":"validationAttempt","mid":"YrOGswALAAFJ3HA4e_mjCgzdyCKN","rollout_hash":"2d77870e0d45","frontend_env":"c1f","app_id":"936619743392459","platform":"windows_nt_10","type":"email","referrer":null,"referrer_domain":"","original_referrer":null,"original_referrer_domain":""},"module":null,"obj_type":"url","obj_id":"/accounts/emailsignup/"},{"time":1655934920.7,"name":"instagram_web_client_events","extra":{"event_type":"action","event_name":"validationSuccess","mid":"YrOGswALAAFJ3HA4e_mjCgzdyCKN","rollout_hash":"2d77870e0d45","frontend_env":"c1f","app_id":"936619743392459","platform":"windows_nt_10","type":"email","referrer":null,"referrer_domain":"","original_referrer":null,"original_referrer_domain":""},"module":null,"obj_type":"url","obj_id":"/accounts/emailsignup/"}],"log_type":"client_event","seq":5,"session_id":"1818d6958b0-664580","device_id":"F3C03963-BF21-43B8-93B1-89E458329F49","claims":["0"]}',
}

response = requests.post('https://graph.instagram.com/logging_client_events', headers=headers, data=data)


#------------------------------------------------------------------------------



cookies = {
    'csrftoken': 'pCxzOjlYS12pQ4knokE0W9axzLR1RCem',
    'mid': 'YrOGswALAAFJ3HA4e_mjCgzdyCKN',
    'ig_did': 'F3C03963-BF21-43B8-93B1-89E458329F49',
}

headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'csrftoken=pCxzOjlYS12pQ4knokE0W9axzLR1RCem; mid=YrOGswALAAFJ3HA4e_mjCgzdyCKN; ig_did=F3C03963-BF21-43B8-93B1-89E458329F49',
    'origin': 'https://www.instagram.com',
    'pragma': 'no-cache',
    'referer': 'https://www.instagram.com/accounts/emailsignup/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'x-asbd-id': '198387',
    'x-csrftoken': 'pCxzOjlYS12pQ4knokE0W9axzLR1RCem',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '2d77870e0d45',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'day': '6',
    'month': '5',
    'year': '1999',
}

response = requests.post('https://www.instagram.com/web/consent/check_age_eligibility/', cookies=cookies, headers=headers, data=data)



#------------------------------------------------------------------------------



cookies = {
    'csrftoken': 'pCxzOjlYS12pQ4knokE0W9axzLR1RCem',
    'mid': 'YrOGswALAAFJ3HA4e_mjCgzdyCKN',
    'ig_did': 'F3C03963-BF21-43B8-93B1-89E458329F49',
}

headers = {
    'authority': 'i.instagram.com',
    'accept': '*/*',
    'accept-language': 'en',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'csrftoken=pCxzOjlYS12pQ4knokE0W9axzLR1RCem; mid=YrOGswALAAFJ3HA4e_mjCgzdyCKN; ig_did=F3C03963-BF21-43B8-93B1-89E458329F49',
    'origin': 'https://www.instagram.com',
    'pragma': 'no-cache',
    'referer': 'https://www.instagram.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'x-asbd-id': '198387',
    'x-csrftoken': 'pCxzOjlYS12pQ4knokE0W9axzLR1RCem',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '2d77870e0d45',
}

data = {
    'device_id': 'YrOGswALAAFJ3HA4e_mjCgzdyCKN',
    'email': 'fesexa4678@mahazai.com',
}

response = requests.post('https://i.instagram.com/api/v1/accounts/send_verify_email/', cookies=cookies, headers=headers, data=data)



#--------------------------------------------------

headers = {
    'authority': 'graph.instagram.com',
    'accept': '*/*',
    'accept-language': 'en',
    'cache-control': 'no-cache',
    'origin': 'https://www.instagram.com',
    'pragma': 'no-cache',
    'referer': 'https://www.instagram.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'x-asbd-id': '198387',
}

data = {
    'access_token': '936619743392459|3cdb3f896252a1db29679cb4554db266',
    'message': '{"app_id":"936619743392459","app_ver":"1.0.0","data":[{"time":1655934940.618,"name":"instagram_web_time_spent_bit_array","extra":{"rollout_hash":"2d77870e0d45","frontend_env":"c1f","app_id":"936619743392459","tos_id":"vp4g8j","start_time":1655934940,"tos_array":[1,0],"tos_len":1,"tos_seq":4,"tos_cum":29,"log_time":1655934940618,"referrer":null,"referrer_domain":"","url":"/accounts/emailsignup/","original_referrer":null,"original_referrer_domain":""}}],"log_type":"client_event","seq":9,"session_id":"1818d6958b0-664580","device_id":"F3C03963-BF21-43B8-93B1-89E458329F49","claims":["0"]}',
}

response = requests.post('https://graph.instagram.com/logging_client_events', headers=headers, data=data)


#------------------------------------------------


cookies = {
    'csrftoken': 'pCxzOjlYS12pQ4knokE0W9axzLR1RCem',
    'mid': 'YrOGswALAAFJ3HA4e_mjCgzdyCKN',
    'ig_did': 'F3C03963-BF21-43B8-93B1-89E458329F49',
}

headers = {
    'authority': 'i.instagram.com',
    'accept': '*/*',
    'accept-language': 'en',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'csrftoken=pCxzOjlYS12pQ4knokE0W9axzLR1RCem; mid=YrOGswALAAFJ3HA4e_mjCgzdyCKN; ig_did=F3C03963-BF21-43B8-93B1-89E458329F49',
    'origin': 'https://www.instagram.com',
    'pragma': 'no-cache',
    'referer': 'https://www.instagram.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'x-asbd-id': '198387',
    'x-csrftoken': 'pCxzOjlYS12pQ4knokE0W9axzLR1RCem',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '2d77870e0d45',
}

data = {
    'code': '129807',
    'device_id': 'YrOGswALAAFJ3HA4e_mjCgzdyCKN',
    'email': 'fesexa4678@mahazai.com',
}

response = requests.post('https://i.instagram.com/api/v1/accounts/check_confirmation_code/', cookies=cookies, headers=headers, data=data)


#----------------------------------------------------------------



cookies = {
    'csrftoken': 'pCxzOjlYS12pQ4knokE0W9axzLR1RCem',
    'mid': 'YrOGswALAAFJ3HA4e_mjCgzdyCKN',
    'ig_did': 'F3C03963-BF21-43B8-93B1-89E458329F49',
}

headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'csrftoken=pCxzOjlYS12pQ4knokE0W9axzLR1RCem; mid=YrOGswALAAFJ3HA4e_mjCgzdyCKN; ig_did=F3C03963-BF21-43B8-93B1-89E458329F49',
    'origin': 'https://www.instagram.com',
    'pragma': 'no-cache',
    'referer': 'https://www.instagram.com/accounts/emailsignup/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'x-asbd-id': '198387',
    'x-csrftoken': 'pCxzOjlYS12pQ4knokE0W9axzLR1RCem',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '2d77870e0d45',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1655934963:ARFQAKbDxzhHMQ9HhdoJsBAWHuU5sgHk4/FOxpezRVWQoVdgESrdnDopczM4QSArV4WBpvu2/gET2B2A6XpdSL0+QLU5XItiTsfzAGNF8D1VAhxs0BS/Yc1Am4mlXCsUroUhxDhNhCYczkNkd8qM',
    'email': 'fesexa4678@mahazai.com',
    'username': 'fkahdia',
    'first_name': 'zefefzf zef',
    'month': '5',
    'day': '6',
    'year': '1999',
    'client_id': 'YrOGswALAAFJ3HA4e_mjCgzdyCKN',
    'seamless_login_enabled': '1',
    'tos_version': 'eu',
    'force_sign_up_code': 'EukT8NBm',
}

response = requests.post('https://www.instagram.com/accounts/web_create_ajax/', cookies=cookies, headers=headers, data=data)

