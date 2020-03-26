# 自定义token接口返回值
import uuid

from django.http import JsonResponse
from qiniu import put_file


def jwt_response_payload_handler(token, user=None, request=None):
    """为返回的结果添加用户相关信息"""

    return {
        'token': token,
        'user_id': user.id,
        'username': user.username,
        'avatar': user.avatar
    }


import qiniu

QINIU_ACCESS_KEY = "93NNWRp2HIr1DFHC5g0n0CjlPBkb-52_M0UyprRl"
QINIU_SECRET_KEY = 'GfFUtl-P9vNHNJXft4hHPqWAaJz3dRsIZM7UPuml'
QINIU_BUCKET_NAME = 'youtuba'
CLOUDHOST = 'http://cdn.wuzhongyin.com/'
LOCALDIR = './static/'
q = qiniu.Auth(QINIU_ACCESS_KEY, QINIU_SECRET_KEY)


def upload(file):
    # 指定要上传至的七牛云的空间

    filename = file['name']
    print(filename)

    # 上传到七牛后保存的文件名
    keyname = str(uuid.uuid4()) + '.' + filename.split('.')[1]
    print(keyname)

    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(QINIU_BUCKET_NAME, keyname, 3600)
    print(token)

    # # 保存文件到本地服务器，如果不想缓存到本地可以不写
    file = file['img']

    # /static/xx.png 路径名
    localfilepath = LOCALDIR + keyname

    with open(localfilepath, 'wb') as fp:
        for c in file.chunks():
            fp.write(c)
    #  要上传到七牛云的图片名
    ret, info = put_file(token, keyname, localfilepath)
    print('七牛云存储')
    print(info)
    print(ret)
    assert ret['key'] == keyname
    assert ret['hash'] == qiniu.etag(localfilepath)

    # # 此处要写加入数据库代码
    src = CLOUDHOST + keyname  # 七牛云的图片地址，传给前台并写入数据库
    print(src)
    return {"srcaddr": src}
