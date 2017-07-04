import unittest

from mygame.common.msg.message import Message


class MessageTest(unittest.TestCase):
    def test_init(self):
        message = Message('type')
        self.assertEqual(message.msg_type, 'type')
