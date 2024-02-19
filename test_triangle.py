import unittest


def get_triangle_params(a,b,c):
    min_s, mead_s, max_s = sorted([a,b,c])
    is_triangle = True
    if max_s >= min_s + mead_s:
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

    def my_test(self):
        self.assertAlmostEqual(get_triangle_params(a = 1,b = 1,c = 1),(True,True,True))
        self.assertAlmostEqual(get_triangle_params(a = 1,b = 4,c = 1),(True, None, None))  

    def test_class_eq(self):
        pass

    def test_eq_split(self):
        pass   
   
        
#pep8     
        

   



if __name__ == '__main__':
    unittest.main()