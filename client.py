from urllib import parse, request
import json


def cut_via_api(sentence_to_send):
    textmod = {"sentence": sentence_to_send}
    textmod = json.dumps(textmod).encode(encoding='utf-8')
    # textmod = parse.urlencode(textmod).encode(encoding='utf-8')
    # print(textmod)
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                   "Content-Type": "application/json"}
    url = 'http://localhost:5000/cut/api/v1.0'
    req = request.Request(url=url, data=textmod, headers=header_dict)
    res = request.urlopen(req)
    res = res.read()
    # print(res)
    # print(res.decode(encoding='utf-8'))
    res_dict = eval(res.decode(encoding='utf-8'))
    result = res_dict['result']
    return result


if __name__ == "__main__":
    sentence = "改革开放四十周年庆典"
    print(cut_via_api(sentence))
