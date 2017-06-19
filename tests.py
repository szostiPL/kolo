import unittest

class TestDrawingMethods(unittest.TestCase):
    
    def test_create_line(self):
        x = (1,1)
        y = (2,2)
        line = create_line(x,y)
        self.assertEqual(line, [(1,1),(2,2),(3,3),(4,4)])
    
    def test_create_square(self):
        square = create_square()
        self.assertEqual(square, [(0,0),(4,0),(0,4),(4,4)])

if __name__ == "__main__":
    unittest.main()