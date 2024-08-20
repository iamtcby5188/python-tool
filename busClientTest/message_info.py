__all__ = ['msg_startQuery']
taskId = '2c9485a48eb7ba94018ee65d633215f6'
orderId = '63504110-fcb8-11ee-904a-9fea2a90e2ec-41192'
startTime =1713357936564.0
endTime =1713357940772.0
filepath = r'D:\Data\QiyeWei\WXWork\1688851290782214\Cache\File\2024-04\aa\log_task_2c94869e8eeb90b6018eeb994711001e_2b03d960-fca5-11ee-96f2-f96629f15ab3-81147.cubedb'
msg_startQuery = {
    "header": {
        "cmd_code": 0x07100003,
        "req_id": 2140000100,
        "origin_id": 0,
        "projectUuid": ""
    },
    "result": {
        "err_code": 0,
        "err_msg": ""
    },
    "params": {
        # "taskId": taskId,
        # "orderId": orderId,
        "filePath" : filepath
    },
    "userdata": {}
}

msg_QueryPage = {
    "header": {
        "cmd_code": 0x07100004,
        "req_id": 2140000100,
        "origin_id": 0,
        "projectUuid": ""
    },
    "result": {
        "err_code": 0,
        "err_msg": ""
    },
    "params": {
        "taskId": taskId,
        "orderId": orderId,
        "page": 1,
        "size": 100,
        "filter": {
            "startTime": startTime,
            "endTime": endTime,
        },
        "query": {
            "logLevel": 3,
            "keyword": "a"
        }
    },
    "userdata": {}
}

msg_QueryIndex = {
    "header": {
        "cmd_code": 0x07100008,
        "req_id": 2140000100,
        "origin_id": 0,
        "projectUuid": ""
    },
    "result": {
        "err_code": 0,
        "err_msg": ""
    },
    "params": {
        "taskId": taskId,
        "orderId": orderId,
        "keywordNum": 2,
        "size": 100,
        "filter": {
            "startTime": startTime,
            "endTime": endTime,
        },
        "query": {
            "logLevel": None,
            "keyword": "计次循环"
        }
    },
    "userdata": {}
}

msg_mallocApp = {
    "header": {
        "cmd_code": 0x00010008,
        "req_id": 2140000100,
        "origin_id": 0,
        "projectUuid": ""
    },
    "result": {
        "err_code": 0,
        "err_msg": ""
    },
    "params": {
        "appType": 256,
        "resType": 10
    },
    "userdata": {}
}
