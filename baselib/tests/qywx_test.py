from baselib.qywx import QyWechat
obj = QyWechat("")


class TestSplitMsgByLine:
    def test_normal(self):
        msg = "hello\nworld"
        limit = 10
        expected = ["hello\n", "world"]
        assert obj.split_msg_by_line(msg, limit) == expected

    def test_single_line(self):
        msg = "hello world"
        limit = 10
        expected = ["hello worl", "d"]
        assert obj.split_msg_by_line(msg, limit) == expected

    def test_limit_larger_than_msg_len(self):
        msg = "hello\nworld"
        limit = 20
        expected = ["hello\nworld"]
        assert obj.split_msg_by_line(msg, limit) == expected

    def test_empty_msg(self):
        msg = ""
        limit = 10
        expected = [""]
        assert obj.split_msg_by_line(msg, limit) == expected

    def test_single_char_limit(self):
        msg = "hello\nworld"
        limit = 1
        expected = ["h", "e", "l", "l", "o", "\n", "w", "o", "r", "l", "d"]
        assert obj.split_msg_by_line(msg, limit) == expected


class TestCutMsg:
    def test_cut_msg_within_limit(self):
        msg = "Hello, World!"
        assert obj.cut_msg(msg, limit=20) == msg

    def test_cut_msg_exceed_limit(self):
        msg = "This is a very long message that exceeds the limit of 20 characters."
        assert obj.cut_msg(msg, limit=20) == "This is a very long me\n..."

    def test_cut_msg_with_custom_post_msg(self):
        msg = "This is a very long message that exceeds the limit of 20 characters."
        assert obj.cut_msg(msg, limit=20, post_msg=" [truncated]") == "This is a very long [truncated]"

    def test_cut_msg_with_unicode_characters(self):
        msg = "你好，世界！"
        assert obj.cut_msg(msg, limit=10) == msg

    def test_cut_msg_with_emoji(self):
        msg = "This is a message with an emoji 😊"
        assert obj.cut_msg(msg, limit=20) == "This is a message wit\n..."


class TestSplitMsg:
    test_obj = QyWechat("")

    def test_split_msg_normal(self):
        msg = "hello world"
        limit = 5
        expected = ["hello", " worl", "d"]
        assert self.test_obj.split_msg(msg, limit) == expected

    def test_split_msg_single_page(self):
        msg = "hello world"
        limit = 20
        expected = ["hello world"]
        assert self.test_obj.split_msg(msg, limit) == expected

    def test_split_msg_empty_msg(self):
        msg = ""
        limit = 10
        expected = [""]
        assert self.test_obj.split_msg(msg, limit) == expected

    def test_split_msg_limit_larger_than_msg_len(self):
        msg = "hello world"
        limit = 50
        expected = ["hello world"]
        assert self.test_obj.split_msg(msg, limit) == expected

    def test_split_msg_unicode(self):
        msg = "你好，世界"
        limit = 5
        expected = ["你好，", "世界"]
        assert self.test_obj.split_msg(msg, limit) == expected