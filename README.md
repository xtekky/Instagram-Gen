## Request (1) [Registration]

### Method
```js
POST
```
### Endpoint
```js
  https://www.instagram.com/accounts/web_create_ajax/attempt/?hl=fr
```
### Headers
```js
  :authority: www.instagram.com
  :method: POST
  :path: /accounts/web_create_ajax/attempt/?hl=fr
  :scheme: https
  accept: */*
  accept-encoding: gzip, deflate, br
  accept-language: en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3
  content-length: 381
  content-type: application/x-www-form-urlencoded
  cookie: ds_user_id=8476891723; csrftoken=qLUVZrX3gHCJkuu9cOJ2qp5mgkBOBKMW; mid=YnjUGQALAAFKDNv5oPrKa8NEUUek; ig_did=205A0AA6-6D58-43BE-897B-CF0E2BAC77F3; shbid="5002\0548476891723\0541684261030:01f7f18f86d8b819470ca19f2f2074007a63ceb431fe505a6892757b56f539677ab4d27f"; shbts="1652725030\0548476891723\0541684261030:01f7adc7c9bd8c4207d791d190b7b4555a40204a52e9454e4ca18faa6b96196f930408b7"
  origin: https://www.instagram.com
  referer: https://www.instagram.com/accounts/emailsignup/?hl=fr
  sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"
  sec-ch-ua-mobile: ?0
  sec-ch-ua-platform: "Windows"
  sec-fetch-dest: empty
  sec-fetch-mode: cors
  sec-fetch-site: same-origin
  user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36
  x-asbd-id: 198387
  x-csrftoken: qLUVZrX3gHCJkuu9cOJ2qp5mgkBOBKMW
  x-ig-app-id: 936619743392459
  x-ig-www-claim: 0
  x-instagram-ajax: 808d16d2325b
  x-requested-with: XMLHttpRequest
```

### Payload
```js
  enc_password: #PWD_INSTAGRAM_BROWSER:10:1652864114:AehQALNdAFuzJ+Hx2nZ257w8EWQQcRTph24KXrBIMYSeHhpWObspeM4/trFhUdNz5tCa2gEeQcUIPCyC9TaPcmr989uSMIR/tIvXpaGMfu6efuAclp+LJKbTsQZMOWNVc/lf1O/ZB5j+cLY6JavO
  email: jejago7907@duetube.com
  username: fezehfeh34dedzd
  first_name: Ziduhf
  client_id: YnjUGQALAAFKDNv5oPrKa8NEUUek
  seamless_login_enabled: 1
  opt_into_one_tap: false
```

### Response
```js
{"account_created":false,"dryrun_passed":true,"username_suggestions":["jejago7907","ziduhf5","ziduhf18","ziduhf371","ziduhf2709","ziduhf6","ziduhf60","ziduhf458","ziduhf3430","ziduhf30"],"status":"ok"}
```

## Request (2) [Age Verification]

### Method
```js
POST
```
### Endpoint
```js
  https://www.instagram.com/web/consent/check_age_eligibility/?hl=fr
```
### Headers
```js
  :authority: www.instagram.com
  :method: POST
  :path: /web/consent/check_age_eligibility/?hl=fr
  :scheme: https
  accept: */*
  accept-encoding: gzip, deflate, br
  accept-language: en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3
  content-length: 24
  content-type: application/x-www-form-urlencoded
  cookie: ds_user_id=8476891723; csrftoken=qLUVZrX3gHCJkuu9cOJ2qp5mgkBOBKMW; mid=YnjUGQALAAFKDNv5oPrKa8NEUUek; ig_did=205A0AA6-6D58-43BE-897B-CF0E2BAC77F3; shbid="5002\0548476891723\0541684261030:01f7f18f86d8b819470ca19f2f2074007a63ceb431fe505a6892757b56f539677ab4d27f"; shbts="1652725030\0548476891723\0541684261030:01f7adc7c9bd8c4207d791d190b7b4555a40204a52e9454e4ca18faa6b96196f930408b7"
  origin: https://www.instagram.com
  referer: https://www.instagram.com/accounts/emailsignup/?hl=fr
  sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"
  sec-ch-ua-mobile: ?0
  sec-ch-ua-platform: "Windows"
  sec-fetch-dest: empty
  sec-fetch-mode: cors
  sec-fetch-site: same-origin
  user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36
  x-asbd-id: 198387
  x-csrftoken: qLUVZrX3gHCJkuu9cOJ2qp5mgkBOBKMW
  x-ig-app-id: 936619743392459
  x-ig-www-claim: 0
  x-instagram-ajax: 808d16d2325b
  x-requested-with: XMLHttpRequest
```

### Payload
```js
  day: 11
  month: 3
  year: 1993
```

### Response
```js
{"eligible_to_register":true,"parental_consent_required":false,"is_supervised_user":false,"status":"ok"}
```

### Request (3) [Email Verification]

### Method
```js
POST
```
### Endpoint
```js
  https://i.instagram.com/api/v1/accounts/send_verify_email/?hl=fr
```
### Headers
```js
  :authority: i.instagram.com
  :method: POST
  :path: /api/v1/accounts/send_verify_email/?hl=fr
  :scheme: https
  accept: */*
  accept-encoding: gzip, deflate, br
  accept-language: en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3
  content-length: 69
  content-type: application/x-www-form-urlencoded
  cookie: ds_user_id=8476891723; csrftoken=qLUVZrX3gHCJkuu9cOJ2qp5mgkBOBKMW; mid=YnjUGQALAAFKDNv5oPrKa8NEUUek; ig_did=205A0AA6-6D58-43BE-897B-CF0E2BAC77F3; shbid="5002\0548476891723\0541684261030:01f7f18f86d8b819470ca19f2f2074007a63ceb431fe505a6892757b56f539677ab4d27f"; shbts="1652725030\0548476891723\0541684261030:01f7adc7c9bd8c4207d791d190b7b4555a40204a52e9454e4ca18faa6b96196f930408b7"
  origin: https://www.instagram.com
  referer: https://www.instagram.com/
  sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"
  sec-ch-ua-mobile: ?0
  sec-ch-ua-platform: "Windows"
  sec-fetch-dest: empty
  sec-fetch-mode: cors
  sec-fetch-site: same-site
  user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36
  x-asbd-id: 198387
  x-csrftoken: qLUVZrX3gHCJkuu9cOJ2qp5mgkBOBKMW
  x-ig-app-id: 936619743392459
  x-ig-www-claim: 0
  x-instagram-ajax: 808d16d2325b
```

### Payload
```js
  device_id: YnjUGQALAAFKDNv5oPrKa8NEUUek
  email: jejago7907@duetube.com
```

### Response
```js
{"email_sent":true,"title":"Consultez vos e-mails","body":"Suivez le lien du message que nous avons envoyé à \u003cpii.types.GeneralUseEmail object at 0x7fbf4aeaaac0\u003e pour vérifier votre adresse e-mail et nous aider à confirmer que vous en êtes bien le propriétaire.","status":"ok"}
```

## Request (3) [confirmation Code]

### Method
```js
POST
```
### Endpoint
```js
  https://i.instagram.com/api/v1/accounts/check_confirmation_code/?hl=fr
```
### Headers
```js
  :authority: i.instagram.com
  :method: POST
  :path: /api/v1/accounts/check_confirmation_code/?hl=fr
  :scheme: https
  accept: */*
  accept-encoding: gzip, deflate, br
  accept-language: en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3
  content-length: 81
  content-type: application/x-www-form-urlencoded
  cookie: ds_user_id=8476891723; csrftoken=qLUVZrX3gHCJkuu9cOJ2qp5mgkBOBKMW; mid=YnjUGQALAAFKDNv5oPrKa8NEUUek; ig_did=205A0AA6-6D58-43BE-897B-CF0E2BAC77F3; shbid="5002\0548476891723\0541684261030:01f7f18f86d8b819470ca19f2f2074007a63ceb431fe505a6892757b56f539677ab4d27f"; shbts="1652725030\0548476891723\0541684261030:01f7adc7c9bd8c4207d791d190b7b4555a40204a52e9454e4ca18faa6b96196f930408b7"
  origin: https://www.instagram.com
  referer: https://www.instagram.com/
  sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"
  sec-ch-ua-mobile: ?0
  sec-ch-ua-platform: "Windows"
  sec-fetch-dest: empty
  sec-fetch-mode: cors
  sec-fetch-site: same-site
  user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36
  x-asbd-id: 198387
  x-csrftoken: qLUVZrX3gHCJkuu9cOJ2qp5mgkBOBKMW
  x-ig-app-id: 936619743392459
  x-ig-www-claim: 0
  x-instagram-ajax: 808d16d2325b
```

### Payload
```js
  code: 475891
  device_id: YnjUGQALAAFKDNv5oPrKa8NEUUek
  email: jejago7907@duetube.com
```

### Response
```js
  {"signup_code":"OeXMozwn","status":"ok"}
```

## Request (4) [Confirm account]

### Method
```js
POST
```
### Endpoint
```js
  https://www.instagram.com/accounts/web_create_ajax/attempt/?hl=fr
```
### Headers
```js
  :authority: www.instagram.com
  :method: POST
  :path: /accounts/web_create_ajax/attempt/?hl=fr
  :scheme: https
  accept: */*
  accept-encoding: gzip, deflate, br
  accept-language: en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3
  content-length: 376
  content-type: application/x-www-form-urlencoded
  cookie: ds_user_id=8476891723; csrftoken=qLUVZrX3gHCJkuu9cOJ2qp5mgkBOBKMW; mid=YnjUGQALAAFKDNv5oPrKa8NEUUek; ig_did=205A0AA6-6D58-43BE-897B-CF0E2BAC77F3; shbid="5002\0548476891723\0541684261030:01f7f18f86d8b819470ca19f2f2074007a63ceb431fe505a6892757b56f539677ab4d27f"; shbts="1652725030\0548476891723\0541684261030:01f7adc7c9bd8c4207d791d190b7b4555a40204a52e9454e4ca18faa6b96196f930408b7"
  origin: https://www.instagram.com
  referer: https://www.instagram.com/accounts/emailsignup/?hl=fr
  sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"
  sec-ch-ua-mobile: ?0
  sec-ch-ua-platform: "Windows"
  sec-fetch-dest: empty
  sec-fetch-mode: cors
  sec-fetch-site: same-origin
  user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36
  x-asbd-id: 198387
  x-csrftoken: qLUVZrX3gHCJkuu9cOJ2qp5mgkBOBKMW
  x-ig-app-id: 936619743392459
  x-ig-www-claim: 0
  x-instagram-ajax: 808d16d2325b
  x-requested-with: XMLHttpRequest
```

### Payload
```js
  enc_password: #PWD_INSTAGRAM_BROWSER:10:1652864242:AehQAGP7nUO2Kv8YQH80legF1COzYZsMXWnrdI6EfAdCCqN5xgpCcGupqDF/ICaO4VPD4p0ifhYPM1PDNVECbQ+ms0uOGvtxc0xmkSArcNFSnCTabEXaRcxrg9WpMXRvpEgunfUtUujQ00XSQcWY
  email: jejago7907@duetube.com
  username: fezehfeh34dedzd
  first_name: Ziduhf
  client_id: YnjUGQALAAFKDNv5oPrKa8NEUUek
  seamless_login_enabled: 1
  force_sign_up_code: OeXMozwn
```

### Response
```js
  {"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"Nous limitons la fréquence de certaines actions que vous pouvez effectuer sur Instagram afin de protéger notre communauté. Si vous pensez que nous avons commis une erreur, faites-le-nous savoir.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Nous contacter","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}
```





