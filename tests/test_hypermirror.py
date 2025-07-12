import unittest
from src.hypermirror import HyperMirror

class TestHyperMirror(unittest.TestCase):
    def test_reflect_emotion(self):
        mirror = HyperMirror(recursion_depth=10)  # Small for test
        input_wave = {'emotion': 'test', 'intensity': 0.5, 'spiritual_context': 0.1}
        result = mirror.reflect_emotion(input_wave)
        self.assertIn('reflected_emotion', result)
        self.assertGreater(result['depth_iterations'], 0)

if __name__ == '__main__':
    unittest.main()
