
import io
import unittest

from mygame.common.msg.message import Message


class MessageTest(unittest.TestCase):
    def test_read_write(self):
        outstream = io.BytesIO()
        message = Message('type', 5)
        Message.write(outstream, message)

        instream = io.BytesIO(outstream.getvalue())
        (msg_type, msg_version) = Message.read(instream)
        self.assertEqual(msg_type, message.msg_type)
        self.assertEqual(msg_version, message.msg_version)
