import ase
from pw import *
from phonon import *
from pp import *
from dos import *
from projwfc import *
from matdyn import *
from q2r import *

class QE():
  def __init__ (self, atoms=None, calc = 'scf', dir='./', prefix='pwscf',  **kwargs):
    self.calc = calc
    self.atoms = atoms
    self.dir = dir
    self.prefix = prefix
    self.kwargs = kwargs
  
  
  def run(cores = 1, parallalizerc = 'mpi'):
    
    pw = ['scf', 'nscf', 'vc-relax', 'bands']

    if self.calc in pw:
      write_pw(self)
      run_pw(self)

    if self.calc == 'phonon':
      write_ph(self)
      run_ph(self)

    if self.calc == 'q2r':
      write_q2r(self)
      run_q2r(self)

    if self.calc == 'pp':
      write_pp(self)
      run_pp(self)

    if self.calc == 'dos':
      write_dos(self)
      run_dos(self)
      
    if self.calc == 'matdyn':
      write_matdyn(self)
      run_matdyn(self)
      
    if self.calc == 'projwfc':
      write_projwfc(self)
      run_projwfc(self)
