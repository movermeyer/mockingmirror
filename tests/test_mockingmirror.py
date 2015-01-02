import unittest
import mockingmirror

class TestMirror(unittest.TestCase):

    def setUp(self):
        self.mirror, self.mock = mockingmirror.mirror()

    def test_setting_attribute_adds_attribute_to_mock(self):
        self.mirror.an_attribute = 42
        self.assertEqual(self.mock.an_attribute, 42)

    def test_missing_attribute_throws(self):
        with self.assertRaises(AttributeError):
            self.mock.a_missing_attribute

    def test_getting_attribute_creates_mock(self):
        self.mirror.an_attribute
        self.mock.an_attribute

    def test_mocks_are_not_callable(self):
        self.mirror.not_callable
        with self.assertRaises(TypeError):
            self.mock.not_callable()

    def test_calling_mirrors_makes_the_mock_callable(self):
        self.mirror.callable()
        self.mock.callable()

    def test_setting_return_value(self):
        self.mirror.a_method_with_return_value()[:] = 42
        self.assertEqual(self.mock.a_method_with_return_value(), 42)

    def test_setting_side_effect(self):
        @self.mirror.a_method_with_side_effect()
        def side_effect():
            return 42
        self.assertEqual(self.mock.a_method_with_side_effect(), 42)

    def test_setting_return_value_unsets_side_effect(self):
        @self.mirror.a_method()
        def side_effect():
            return "from_side_effect"
        self.assertEqual(self.mock.a_method(), "from_side_effect")

        self.mirror.a_method()[:] = "from_return_value"
        self.assertEqual(self.mock.a_method(), "from_return_value")
