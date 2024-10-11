# Extracted from https://stackoverflow.com/questions/1732438/how-do-i-run-all-python-unit-tests-in-a-directory
"""
The given script is executing all the Unit Test of the project stored at the
path %relativePath2Src% currently fixed coded for the given project. 

Prerequired:
    - Anaconda should be install
    - For the current user, an enviornment called "mtToolsEnv" should exists
    - xmlrunner Library should be installed
"""

import sys
import os
import xmlrunner
from Repository import repository 

relativePath2Src="./../.."
pythonPath=r'"C:\Users\%USERNAME%\.conda\envs\YourConfig\python.exe"' 
outputTestReportFolder=os.path.dirname(os.path.abspath(__file__))+r'\test-reports' #subfolder in current file path

class UTTesting():
    """
    Class tto run all the UT of the project
    """
    def __init__(self):
        """
        Initiate instance

        Returns
        -------
        None.

        """
        self.projectRepository = repository() 
        self.UTfile = [] #List all file
    
    def retrieveAllUT(self):
        """
        Generate the list of UT file in the project

        Returns
        -------
        None.

        """
        print(os.path.realpath(relativePath2Src))
        self.projectRepository.retriveAllFilePaths(relativePath2Src)
        #self.projectRepository.printAllFile() #debug
        for file2scan in self.projectRepository.devfile:
            if file2scan.endswith("_UT.py"):
                self.UTfile.append(file2scan)
                print(self.projectRepository.devfilepath[file2scan]+'/'+file2scan)
                
    
    def runUT(self,UTtoRun):
        """
        Run a single UT

        Parameters
        ----------
        UTtoRun : String
            File Name of the UT

        Returns
        -------
        None.

        """
        print(UTtoRun)
        if UTtoRun in self.projectRepository.devfilepath:
            UTtoRunFolderPath=os.path.realpath(os.path.join(self.projectRepository.devfilepath[UTtoRun]))
            UTtoRunPath = os.path.join(UTtoRunFolderPath, UTtoRun)
        print(UTtoRunPath)
        
        #set the correct execution context & run the test
        os.system(" cd " + UTtoRunFolderPath + \
                  " & " + pythonPath + " " + UTtoRunPath + " " + outputTestReportFolder )
        
        
    def runAllUT(self):
        """
        Run all the UT contained in self
        The function "retrieveAllUT" sjould ahve been performed before

        Returns
        -------
        None.

        """
        for UTfile in self.UTfile:
            self.runUT(UTfile)
                
    
                
if __name__ == "__main__":
    undertest=UTTesting()
    undertest.retrieveAllUT()
    undertest.runAllUT()

import os

class repository():
    """
    Class that decribed folder and file in a repository 
    """
    def __init__(self):
        """
        Initiate instance

        Returns
        -------
        None.

        """
        self.devfile = [] #List all file
        self.devfilepath = {} #List all file paths

    def retriveAllFilePaths(self,pathrepo):
        """
        Retrive all files and their path in the class

        Parameters
        ----------
        pathrepo : Path used for the parsin

        Returns
        -------
        None.

        """
        for path, subdirs, files in os.walk(pathrepo):
            for file_name in files:
                self.devfile.append(file_name)
                self.devfilepath[file_name] = path
                
    def printAllFile(self):
        """
        Display all file with paths

        Parameters
        ----------
        def printAllFile : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        for file_loop in self.devfile:
            print(self.devfilepath[file_loop]+'/'+file_loop)

if __name__ == "__main__":
    import xmlrunner
    import sys
    
    if len(sys.argv) > 1:
        outputFolder = sys.argv.pop() #avoid conflic with unittest.main
    else:
        outputFolder = r'test-reports'
    print("Report will be created and store there: " + outputFolder)
    
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output=outputFolder))

