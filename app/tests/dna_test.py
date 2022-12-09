import unittest
from source.dna_to_rna import convert_dna_to_rna

# To run from docker: docker-compose run web python tests/dna_test.py


class TestDNAToRna(unittest.TestCase):

    def test_dna_string_1(self):
        """Test for DNA sequence"""
        data = 'ATTTGGCTACTAACAATCTA'
        expected = 'AUUUGGCUACUAACAAUCUA'
        actual = convert_dna_to_rna(data)
        if actual == expected:
            print('DNA Test_string_1 Passed')

        self.assertTrue(actual == expected, f'Should be: {expected}')

    def test_dna_string_2(self):
        """Test for DNA sequence"""
        data = 'GTTGTAATGGCCTACATTA'
        expected = 'GUUGUAAUGGCCUACAUUA'
        actual = convert_dna_to_rna(data)
        if actual == expected:
            print('DNA Test_string_2 Passed')

        self.assertTrue(actual == expected, f'Should be: {expected}')

    def test_dna_string_3(self):
        """Test for DNA sequence"""
        data = 'CAGGTGGTGTTGTTCAGTT'
        expected = 'CAGGUGGUGUUGUUCAGUU'
        actual = convert_dna_to_rna(data)
        if actual == expected:
            print('DNA Test_3 Passed')

        self.assertTrue(actual == expected, f'Should be: {expected}')

    def test_dna_string_4(self):
        """Test for DNA sequence"""
        data = 'GCTAACTAAC'
        expected = 'GCUAACUAAC'
        actual = convert_dna_to_rna(data)
        if actual == expected:
            print('DNA Test_string_4 Passed')

        self.assertTrue(actual == expected, f'Should be: {expected}')

    def test_dna_string_5(self):
        """Test for DNA sequence"""
        data = 'GCTAACTAAC'
        expected = 'GCUAACUAAC'
        actual = convert_dna_to_rna(data)
        if actual == expected:
            print('DNA Test_string_5 Passed')

        self.assertTrue(actual == expected, f'Should be: {expected}')

    def test_dna_string_6(self):
        """Test for DNA sequence"""
        data = 'GCTAACTAACATCTTTGGCACTGTT'
        expected = 'GCUAACUAACAUCUUUGGCACUGUU'
        actual = convert_dna_to_rna(data)
        if actual == expected:
            print('DNA Test_string_6 Passed')

        self.assertTrue(actual == expected, f'Should be: {expected}')

    def test_dna_string_7(self):
        """Test for DNA sequence"""
        data = 'CCCGTCCTTGATTGGCTTGAAGAGAAGTTT'
        expected = 'CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU'
        actual = convert_dna_to_rna(data)
        if actual == expected:
            print('DNA Test_string_7 Passed')

        self.assertTrue(actual == expected, f'Should be: {expected}')

    def test_digits (self):
        """Test for integer input that returns an error"""
        data = 123
        expected = 'Please provide DNA sequence in "ACGT" format'
        actual = convert_dna_to_rna(data)
        if actual == expected:
            print(f'DNA test_digits Passed')
        self.assertTrue(actual == expected, f'Should be: {expected}')

    def test_none (self):
        """Test for None input that returns an error"""
        data = None
        expected = 'Please provide DNA sequence in "ACGT" format'
        actual = convert_dna_to_rna(data)
        if actual == expected:
            print(f'DNA test_none Passed')
        self.assertTrue(actual == expected, f'Should be: {expected}')



if __name__ == '__main__':
    unittest.main()