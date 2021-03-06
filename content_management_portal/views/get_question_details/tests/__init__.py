# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "get_question_details"
REQUEST_METHOD = "get"
URL_SUFFIX = "coding_questions/{question_id}/v1/"

from .test_case_01 import TestCase01GetQuestionDetailsAPITestCase

__all__ = [
    "TestCase01GetQuestionDetailsAPITestCase"
]
