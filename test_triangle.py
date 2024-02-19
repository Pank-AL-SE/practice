import unittest

def get_triangle_params(a,b,c):
    min_s, mead_s, max_s = sorted([a,b,c])
    is_triangle = True
    if max_s >= min_s + mead_s:
        is_triangle = False
        return is_triangle,None,None    
    if min_s == mead_s == max_s:
        isoscales = True
        equilateral = True
    elif (min_s == mead_s) or (max_s == mead_s):
        isoscales = True
        equilateral = False
    else:
        isoscales = False
        equilateral = False
    return is_triangle, isoscales, equilateral


class Test_get_triangle(unittest.TestCase):

    def test_negative(self):
        self.assertAlmostEqual(get_triangle_params(a = 0,b = 1,c = 0),(False,None,None))
        self.assertAlmostEqual(get_triangle_params(a = 0,b = 0,c = 0),(False,None,None))

    def test_class_eq(self):
        self.assertAlmostEqual(get_triangle_params(a = 2,b = 4,c = 5),(True,False,False))
        self.assertAlmostEqual(get_triangle_params(a = 2,b = 3,c = 3),(True,True,False))
        self.assertAlmostEqual(get_triangle_params(a = 2,b = 2,c = 2),(True,True,True))
        self.assertAlmostEqual(get_triangle_params(a = 6,b = 6,c = 11),(True,True,False))
    
    def test_eq_split(self):
        self.assertAlmostEqual(get_triangle_params(a = 3,b = 4,c = 5),(True,False,False))
        self.assertAlmostEqual(get_triangle_params(a = 6,b = 12,c = 13),(True,False,False))

        


         


        
#pep8     
        

   



if __name__ == '__main__':
    unittest.main()