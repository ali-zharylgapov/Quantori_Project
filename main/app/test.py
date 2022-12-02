import unittest

from dna_to_rna import convert_dna_to_rna
from rna_to_protein import convert_rna_to_protein


class TestDNAToRna(unittest.TestCase):

    def test_1(self):
        data = 'ATTTGGCTACTAACAATCTA'
        expected = 'AUUUGGCUACUAACAAUCUA'
        actual = convert_dna_to_rna(data)
        if actual == expected:
            print('DNA Test_1 Passed')

        self.assertTrue(actual == expected, f'Should be {expected}')

    def test_2(self):
        data = 'GTTGTAATGGCCTACATTA'
        expected = 'GUUGUAAUGGCCUACAUUA'
        actual = convert_dna_to_rna(data)
        if actual == expected:
            print('DNA Test_2 Passed')

        self.assertTrue(actual == expected, f'Should be {expected}')

    def test_3(self):
        data = 'CAGGTGGTGTTGTTCAGTT'
        expected = 'CAGGUGGUGUUGUUCAGUU'
        actual = convert_dna_to_rna(data)
        if actual == expected:
            print('DNA Test_3 Passed')

        self.assertTrue(actual == expected, f'Should be {expected}')

    def test_4(self):
        data = 'GCTAACTAAC'
        expected = 'GCUAACUAAC'
        actual = convert_dna_to_rna(data)
        if actual == expected:
            print('DNA Test_4 Passed')

        self.assertTrue(actual == expected, f'Should be {expected}')

    def test_5(self):
        data = 'GCTAACTAAC'
        expected = 'GCUAACUAAC'
        actual = convert_dna_to_rna(data)
        if actual == expected:
            print('DNA Test_5 Passed')

        self.assertTrue(actual == expected, f'Should be {expected}')

    def test_6(self):
        data = 'GCTAACTAACATCTTTGGCACTGTT'
        expected = 'GCUAACUAACAUCUUUGGCACUGUU'
        actual = convert_dna_to_rna(data)
        if actual == expected:
            print('DNA Test_6 Passed')

        self.assertTrue(actual == expected, f'Should be {expected}')

    def test_7(self):
        data = 'CCCGTCCTTGATTGGCTTGAAGAGAAGTTT'
        expected = 'CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU'
        actual = convert_dna_to_rna(data)
        if actual == expected:
            print('DNA Test_7 Passed')

        self.assertTrue(actual == expected, f'Should be {expected}')


class TestRNAtoProtein(unittest.TestCase):

    def test_1(self):
        data = 'AUUUGGCUACUAACAAUCUA'
        expected = 'IWLLTI'
        actual = convert_rna_to_protein(data)
        if actual == expected:
            print('RNA Test_1 Passed')

        self.assertTrue(actual == expected, f'Should be {expected}')

    def test_2(self):
        data = 'GUUGUAAUGGCCUACAUUA'
        expected = 'VVMAYI'
        actual = convert_rna_to_protein(data)
        if actual == expected:
            print('RNA Test_2 Passed')

        self.assertTrue(actual == expected, f'Should be {expected}')

    def test_3(self):
        data = 'CAGGUGGUGUUGUUCAGUU'
        expected = 'QVVLFS'
        actual = convert_rna_to_protein(data)
        if actual == expected:
            print('RNA Test_3 Passed')

        self.assertTrue(actual == expected, f'Should be {expected}')

    def test_4(self):
        data = 'GCUAACUAAC'
        expected = 'AN.'
        actual = convert_rna_to_protein(data)
        if actual == expected:
            print('RNA Test_4 Passed')

        self.assertTrue(actual == expected, f'Should be {expected}')

    def test_5(self):
        data = 'GCUAACUAACAUCUUUGGCACUGUU'
        expected = 'AN.HLWHC'
        actual = convert_rna_to_protein(data)
        if actual == expected:
            print('RNA Test_5 Passed')

        self.assertTrue(actual == expected, f'Should be {expected}')

    def test_6(self):
        data = 'UAUGAAAAACUCAAA'
        expected = 'YEKLK'
        actual = convert_rna_to_protein(data)
        if actual == expected:
            print('RNA Test_6 Passed')

        self.assertTrue(actual == expected, f'Should be {expected}')

    def test_7(self):
        data = 'CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU'
        expected = 'PVLDWLEEKF'
        actual = convert_rna_to_protein(data)
        if actual == expected:
            print('RNA Test_7 Passed')

        self.assertTrue(actual == expected, f'Should be {expected}')


if __name__ == '__main__':
    unittest.main()
