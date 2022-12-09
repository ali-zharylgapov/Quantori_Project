import unittest
from source.rna_to_protein import convert_rna_to_protein

# To run from docker: docker-compose run web python tests/rna_test.py


class TestRNAtoProtein(unittest.TestCase):

    def test_rna_string_1(self):
        """Test for RNA sequence"""
        data = 'AUUUGGCUACUAACAAUCUA'
        expected = 'IWLLTI'
        actual = convert_rna_to_protein(data)
        if actual == expected:
            print('RNA Test_string_1 Passed')

        self.assertTrue(actual == expected, f'Should be {expected}')

    def test_rna_string_2(self):
        """Test for RNA sequence"""
        data = 'GUUGUAAUGGCCUACAUUA'
        expected = 'VVMAYI'
        actual = convert_rna_to_protein(data)
        if actual == expected:
            print('RNA Test_string_2 Passed')

        self.assertTrue(actual == expected, f'Should be {expected}')

    def test_rna_string_3(self):
        """Test for RNA sequence"""
        data = 'CAGGUGGUGUUGUUCAGUU'
        expected = 'QVVLFS'
        actual = convert_rna_to_protein(data)
        if actual == expected:
            print('RNA Test_string_3 Passed')

        self.assertTrue(actual == expected, f'Should be {expected}')

    def test_rna_string_4(self):
        """Test for RNA sequence"""
        data = 'GCUAACUAAC'
        expected = 'AN.'
        actual = convert_rna_to_protein(data)
        if actual == expected:
            print('RNA Test_string_4 Passed')

        self.assertTrue(actual == expected, f'Should be {expected}')

    def test_rna_string_5(self):
        """Test for RNA sequence"""
        data = 'GCUAACUAACAUCUUUGGCACUGUU'
        expected = 'AN.HLWHC'
        actual = convert_rna_to_protein(data)
        if actual == expected:
            print('RNA Test_string_5 Passed')

        self.assertTrue(actual == expected, f'Should be {expected}')

    def test_rna_string_6(self):
        """Test for RNA sequence"""
        data = 'UAUGAAAAACUCAAA'
        expected = 'YEKLK'
        actual = convert_rna_to_protein(data)
        if actual == expected:
            print('RNA Test_string_6 Passed')

        self.assertTrue(actual == expected, f'Should be {expected}')

    def test_rna_string_7(self):
        """Test for RNA sequence"""
        data = 'CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU'
        expected = 'PVLDWLEEKF'
        actual = convert_rna_to_protein(data)
        if actual == expected:
            print('RNA Test_string_7 Passed')

        self.assertTrue(actual == expected, f'Should be {expected}')

    def test_rna_digits(self):
        """Test for digit input that returns an error"""
        data = 123
        expected = 'Please provide RNA sequence in "ACGU" format'
        actual = convert_rna_to_protein(data)
        if actual == expected:
            print('RNA test_rna_digits Passed')

        self.assertTrue(actual == expected, f'Should be {expected}')

    def test_rna_none(self):
        """Test for none input that returns an error"""
        data = None
        expected = 'Please provide RNA sequence in "ACGU" format'
        actual = convert_rna_to_protein(data)
        if actual == expected:
            print('RNA test_rna_none Passed')

        self.assertTrue(actual == expected, f'Should be {expected}')



if __name__ == '__main__':
    unittest.main()
