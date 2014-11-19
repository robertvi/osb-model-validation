import os
import subprocess as sp

from ..common.inout import inform, trim_path
from backend import OMVBackend, BackendExecutionError


class BrianBackend(OMVBackend):
    
    name = "Brian"

    @staticmethod
    def is_installed(version):
        ret = True
        try:
            import brian
            inform("Brian is correctly installed...", indent=2)
            
        except Error as err:
            inform("Couldn't import Brian into Python: ", err, indent=1)
            ret = False
        return ret
        
    @staticmethod
    def install(version):
        from getbrian import install_brian
        home = os.environ['HOME']
        inform('Will fetch and install the latest Brian (version 1.x)', indent=2)
        install_brian()
        inform('Done...', indent=2)
        
    def run(self):
        try:
            inform("Running file %s with %s" % (trim_path(self.modelpath), self.name), indent=1)
            self.stdout = sp.check_output(['python', self.modelpath, '-nogui'],
                                          cwd=os.path.dirname(self.modelpath))
            self.returncode = 0
        except sp.CalledProcessError as err:
            self.returncode = err.returncode
            self.stdout = err.output
            raise BackendExecutionError
        except Exception as err:
            inform("Another error with running %s: "%self.name, err, indent=1)
            self.returncode = -1
            self.stdout = "???"


















