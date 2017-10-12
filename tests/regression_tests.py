import unittest
import filecmp
import os

class FixturesTest(unittest.TestCase):

    #------------------- setup and teardown ---------------------------
    @classmethod
    def setUpClass(cls):
        print('\nin set up - this takes about 80 secs')
	    # We should have fixtures (generated by write_fixtures) saved
	    # in tests/test_fixtures. To set up we run write_fixtures again
	    # to generate new files in a temporary (/tmp) folder.
	    # Later we will test that these files are identical to the old 
	    # ones
        from write_fixtures import write_fixtures
        write_fixtures('/tmp')
        # define paths to individual files for checking, relative to 
        # the folder write_fixtures has saved in
        cls.corrmat = '/corrmat_file.txt'
        cls.gm = '/network-analysis/GlobalMeasures_corrmat_file_COST010.csv'
        cls.lm = '/network-analysis/NodalMeasures_corrmat_file_COST010.csv'
        cls.rich = '/network-analysis/RICH_CLUB_corrmat_file_COST010.csv'
    
    @classmethod
    def tearDownClass(cls):
        import shutil
        print('\nin tear down - deleting files')
        # delete all files generated in setup
        shutil.rmtree(os.getcwd()+'/tmp')
        
    #--------------------------- Tests --------------------------------
    # Each of these tests checks that ourly newly generated version of
    # file_x matches the fixture version
    
    def test_corrmat_matches_fixture(self):
        # test new correlation matrix against fixture
        print('\ntesting new correlation matrix against fixture')
        self.assertTrue(filecmp.cmp(os.getcwd()+'/tmp'+self.corrmat,
                        os.getcwd()+'/tests/test_fixtures'+self.corrmat))

    def test_gm_against_fixture(self):
        # test new global measures against fixture
        print('\ntesting new global measures against fixture')
        self.assertTrue(filecmp.cmp(os.getcwd()+'/tmp'+self.gm,
                        os.getcwd()+'/tests/test_fixtures'+self.gm))
    
    def test_lm_against_fixture(self):
        # test new local measures against fixture
        print('\ntesting new local measures against fixture')
        self.assertTrue(filecmp.cmp(os.getcwd()+'/tmp'+self.lm,
                        os.getcwd()+'/tests/test_fixtures'+self.lm))
    
    def test_rich_against_fixture(self):
        # test rich club against fixture
        print('\ntesting rich club against fixture')
        self.assertTrue(filecmp.cmp(os.getcwd()+'/tmp'+self.rich,
                        os.getcwd()+'/tests/test_fixtures'+self.rich))  

if __name__ == '__main__':
    unittest.main()
