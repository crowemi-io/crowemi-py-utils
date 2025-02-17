import unittest
from datetime import datetime
from crowemi_model.log import LogMessage, LogLevel


class TestLogMessage(unittest.TestCase):

    def test_log_message_initialization(self):
        log_message = LogMessage(**{
            "app": "test_app",
            "message": "test_message",
            "level": LogLevel.INFO.value,
            "created_at": datetime.now(),
            "session": "test_session",
            "path": None
        })

        self.assertEqual(log_message.app, "test_app")
        self.assertEqual(log_message.message, "test_message")
        self.assertEqual(log_message.level, LogLevel.INFO.value)
        self.assertIsInstance(log_message.created_at, datetime)

    def test_log_message_logging(self):
        log_message = LogMessage(**{
            "app": "test_app",
            "message": "test_message",
            "level": LogLevel.INFO.value,
            "created_at": datetime.now(),
            "session": "test_session"
        })



if __name__ == '__main__':
    unittest.main()