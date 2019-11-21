#!/bin/bash
msg=$1
curl -X POST \
  https://chatapi.viber.com/pa/send_message \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 7a4fcff7-10b0-4cb5-b06b-05d9fe586032' \
  -H 'X-Viber-Auth-Token: 47a8013822e7d11d-ab56199efb157593-cc8056c2033cd3e5' \
  -d '{
   "receiver":"16bW64OueOdsT4IsZMreXg==",
   "min_api_version":1,
   "sender":{
      "name":"SMS Bot",
      "avatar":""
   },
   "tracking_data":"tracking data",
   "type":"text",
   "text":"'"$msg"'"
}' > /dev/null 2>&1
