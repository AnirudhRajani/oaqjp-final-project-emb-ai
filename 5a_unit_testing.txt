from EmotionDetection.emotion_detection import emotion_detector
import unittest

class test_cases(unittest.TestCase):

    def test_cases(self):
        results_1 = emotion_detector('I am glad this happened')['dominant_emotion']
        results_2 = emotion_detector('I am really mad about this')['dominant_emotion']
        results_3 = emotion_detector('I feel disgusted just hearing about this')['dominant_emotion']
        results_4 = emotion_detector('I am so sad about this')['dominant_emotion']
        results_5 = emotion_detector('I am really afraid that this will happen')['dominant_emotion']

        self.assertEqual(results_1, 'joy')
        self.assertEqual(results_2, 'anger')
        self.assertEqual(results_3, 'disgust')
        self.assertEqual(results_4, 'sadness')
        self.assertEqual(results_5, 'fear')

if __name__ == '__main__':
    unittest.main()