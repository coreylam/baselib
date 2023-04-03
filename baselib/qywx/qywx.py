# -*- coding: utf-8 -*-
"""
@author     : coreylin
@createTime : 2018/12/22
"""
from baselib.py import urllib2
import json
import base64
import hashlib


class QyWechat(object):
    """ 企业微信处理类
    """
    font_tmpl = '<font color="{color}">{info}</font>'

    def __init__(
            self,
            key,
            proxy="",
            is_ssl=False,
            debug=False):
        # 在 init 中定义所有私有变量，方便查找，无特别意义
        self.key = None
        self.url = self.__proxy = None

        self.debug = debug
        self.set_proxy(proxy)
        self.set_ssl(is_ssl)
        self.update_key(key)

    def update_key(self, key):
        self.key = key
        self.url = "%s/cgi-bin/webhook/send?key=%s" % (self.domain, self.key)

    def set_ssl(self, is_ssl=False):
        if is_ssl:
            self.domain = "https://qyapi.weixin.qq.com"
        else:
            self.domain = "http://qyapi.weixin.qq.com"

    def set_proxy(self, proxy):
        self.__proxy = proxy

    def format_text(self, content, m_list=None, mm_list=None):
        """
        将输入文本转换为企业微信的请求格式
        :param content: 文本内容，最长不超过2048个字节，必须是utf8编码
        :param m_list:  userid的列表，提醒群中的指定成员(@某个成员)，
                        @all表示提醒所有人，如果开发者获取不到userid，可以使用mentioned_mobile_list
        :param mm_list: 手机号列表，提醒手机号对应的群成员(@某个成员)，@all表示提醒所有人
        :return:
        """
        if isinstance(m_list, str):
            m_list = [m_list]

        if isinstance(mm_list, str):
            mm_list = [mm_list]

        data = {
            "msgtype": "text",
            "text": {
                "content": content
            }
        }

        if m_list is not None and len(m_list) > 0:
            data["text"]["mentioned_list"] = m_list
        if mm_list is not None and len(mm_list) > 0:
            data["text"]["mentioned_mobile_list"] = m_list
        return data



    def format_image(self, base64_data, md5):
        data = {
            "msgtype": "image",
            "image": {
                "base64": base64_data,
                "md5": md5
            }
        }
        return data

    def format_news(self, title, target_url, desc=None, pic_url=None):
        data = {
            "msgtype": "news",
            "news": {
                "articles": [
                    {
                        "title": title,
                        "url": target_url
                    }
                ],

            }
        }
        if desc is not None:
            data["news"]["articles"][0]["description"] = desc
        if pic_url is not None:
            data["news"]["articles"][0]["picurl"] = pic_url
        return data

    def md5sum(self, filename):
        with open(filename, "rb") as f:
            fcont = f.read()
        f.close()
        fmd5 = hashlib.md5(fcont)
        return fmd5.hexdigest()

    def _send(self, data):
        """
        使用post方法，向企业微信发送消息
        :param data: 发送消息内容，为字典类型，通过get_xxx_data获得
        :return:企业微信返回的json消息，如：{u'errcode': 0, u'errmsg': u'ok'}
        """
        if len(self.__proxy) > 0:
            proxy = urllib2.ProxyHandler({'http': self.__proxy})
            opener = urllib2.build_opener(proxy)
            urllib2.install_opener(opener)
        post_json = json.dumps(data)
        if self.debug:
            print("url :{}, \ndata :{}".format(self.url, post_json))
            print("proxy : {}".format(self.__proxy))
        rsp = urllib2.urlopen(self.url, post_json.encode('utf-8')).read()
        if self.debug:
            print(rsp)
        return json.loads(rsp)

    def send_image(self, img_path):
        """ 发送图片
        :param img_path: 图片文件的本地路径
        :return: 企业微信返回的json消息，如：{u'errcode': 0, u'errmsg': u'ok'}
        """
        md5 = self.md5sum(img_path)
        with open(img_path, "rb") as f:
            # b64encode是编码，b64decode是解码
            base64_data = base64.b64encode(f.read())
        self.send(self.format_image(base64_data, md5))

    def send_news(self, data):
        pass

    def send_markdown(self, msg, limit=4096, multi_page=True, post_msg="\n..."):
        """ 发送 markdown 格式的数据
        :param msg: 发送的数据内容（markdown格式）
        :param limit: 分页参数，每条消息的最大长度（企业微信默认4096），超过该长度报错
        :param multi_page: 分页参数，消息内容超长的处理方法， True=分页， False=截断
        :param post_msg: 分页参数，选择截断时，加在消息末尾的补充信息
        :return:
        """
        def format_markdown(content, to_user=None, to_party=None,
                            to_tag=None, agentid=None, enable_duplicate_check=None,
                            duplicate_check_interval=None):
            """ 将输入markdown文本转换为企业微信的请求格式。
            """
            data = {
               "msgtype": "markdown",
               "markdown": {
                    "content": content
               }
            }
            if to_user is not None:
                data['touser'] = "|".join(to_user)
            if to_party is not None:
                data["toparty"] = " | ".join(to_party)
            if to_tag is not None:
                data["totag"] = " | ".join(to_tag)
            if agentid is not None:
                data["agentid"] = agentid
            if enable_duplicate_check is not None:
                data["enable_duplicate_check"] = enable_duplicate_check
            if duplicate_check_interval is not None:
                data["duplicate_check_interval"] = duplicate_check_interval
            return data
        if multi_page:
            msg_list = self.get_page_list(msg, limit)
        else:
            msg_list = [self.limit_msg_length(msg, limit, post_msg)]
        rsp_list = []
        for msg in msg_list:
            rsp_list.append(self._send(format_markdown(msg)))
        if len(rsp_list) == 1:
            return rsp_list[0]
        return rsp_list

    def send_text(self, data):
        pass

    def limit_msg_length(self, msg, limit=4096, post_msg="\n..."):
        """ 将 msg 长度限制在 limit 以内
            - 如果大于 limit， 则截断多余部分，并补充 post_msg
            - 如果小于等于 limit，则直接返回
        :param msg:
        :param limit:
        :param post_msg:
        :return:
        """
        msg_len = len(msg.encode("utf-8"))
        if msg_len <= limit:
            return msg
        post_msg_len = len(post_msg.encode("utf-8"))
        idx = 0
        for idx in range(len(msg)):
            if len(msg[:-1 - idx].encode("utf-8")) <= limit - post_msg_len:
                break
        return msg[:-1 - idx] + post_msg

    def split_lines(self, msg, limit=4096):
        msg_len = len(msg.encode("utf-8"))
        if msg_len <= limit:
            return msg
        lines = [""]
        line_no = 0
        for char in msg:
            if len(lines[line_no].encode("utf-8")) <= limit - len(char.encode("utf-8")):
                lines[line_no] += char
                continue
            lines.append(char)
            line_no += 1
        return lines

    def get_page_list(self, msg, limit=4096):
        """ 将数据按行分页
        :return: 返回分页后的数据列表
        """
        msg = msg.strip()
        msg_len = len(msg.encode("utf-8"))
        if msg_len < limit:
            return [msg]
        if len(msg.encode("utf-8"))/len(msg.split("\n")) > limit/10:
            return self.split_lines(msg)
        page_len = page_no = 0
        page_list = [""]
        for aline in msg.split("\n"):
            len_aline = len("{}\n".format(aline).encode("utf-8"))
            if page_len + len_aline <= limit:
                page_len += len_aline
                page_list[page_no] += "{}\n".format(aline)
                continue
            page_len = 0
            page_no += 1
            page_list.append("")
        return [i.strip() for i in page_list]


if __name__ == "__main__":
    def demo():
        key = ""  # robot key
        robot = QyWechat(key=key, is_ssl=True, debug=True)
        print(robot.send_markdown("hello"))

    demo()
