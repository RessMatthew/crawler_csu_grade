import requests


# 获取我的成绩响应
def getMyGradeResponseWithEdge():

    cookies = {
        '_ga': 'GA1.3.2145573915.1637496241',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%221807e7840c9650-04586c70a76f99c-2f26106e-1296000-1807e7840cae1f%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22%24device_id%22%3A%221807e7840c9650-04586c70a76f99c-2f26106e-1296000-1807e7840cae1f%22%7D',
        'BIGipServerpool_jwctest': '2085078474.20480.0000',
        'CSU_P2P_TOKEN': 'kJOIBNXhNSipfKplpisRIisiigieie',
        'JSESSIONID': '8F50AF2C8E87937271735A90506161ED',
        'JSESSIONID': '8F50AF2C8E87937271735A90506161ED',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_ga=GA1.3.2145573915.1637496241; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221807e7840c9650-04586c70a76f99c-2f26106e-1296000-1807e7840cae1f%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22%24device_id%22%3A%221807e7840c9650-04586c70a76f99c-2f26106e-1296000-1807e7840cae1f%22%7D; BIGipServerpool_jwctest=2085078474.20480.0000; CSU_P2P_TOKEN=kJOIBNXhNSipfKplpisRIisiigieie; JSESSIONID=8F50AF2C8E87937271735A90506161ED; JSESSIONID=8F50AF2C8E87937271735A90506161ED',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://csujwc.its.csu.edu.cn/jsxsd/framework/xsMain.jsp',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44',
    }

    params = {
        'Ves632DSdyV': 'NEW_XSD_WDCJ',
    }

    response = requests.get('http://csujwc.its.csu.edu.cn/jsxsd/kscj/cjcx_list', params=params, cookies=cookies,
                            headers=headers, verify=False)

    return response


def getMyGradeResponseWithChrome():
    cookies = {
        '_ga': 'GA1.3.2004897597.1655054997',
        'JSESSIONID': 'CBC6FA1D79351A7B8BAC2E37B394BC54',
        'BIGipServerpool_jwctest': '2017969610.20480.0000',
    }

    headers = {
        'Proxy-Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://csujwc.its.csu.edu.cn/jsxsd/framework/xsMain.jsp',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_ga=GA1.3.2004897597.1655054997; JSESSIONID=CBC6FA1D79351A7B8BAC2E37B394BC54; BIGipServerpool_jwctest=2017969610.20480.0000',
    }

    params = {
        'Ves632DSdyV': 'NEW_XSD_WDCJ',
    }

    response = requests.get('http://csujwc.its.csu.edu.cn/jsxsd/kscj/cjcx_list', params=params, cookies=cookies,
                            headers=headers, verify=False)

    return response
