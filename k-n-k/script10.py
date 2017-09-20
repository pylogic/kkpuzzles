# -*- encoding=utf8 -*-
# ganben
# question source: http://philosophy.hku.hk/think/logic/knights.php  Hongkong University
from z3 import *

# A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.

# Q1

# You meet two inhabitants: Zoey and Mel.
# Zoey tells you that Mel is a knave.
#
# Mel says, “Neither Zoey nor I are knaves.”
# var declare
kt, kv= Ints('kt kv')
zoey, mel = Ints('zoey mel')
#check if zoey == 1 == kt;
s0 = Solver()
#s0.add(Distinct(zoey, mel))
#constrains 1, or 2 1 == kt, 2 == kv
s0.add(zoey>=1, zoey<=2)
s0.add(mel>=1,  mel<=2)
#add assume:
s0.add(zoey == 1, mel == 2)
#add sayings
s0.add(mel==2)
s0.add(Xor(mel <> 2, zoey <> 2)) #negation due to 2
r = s0.check()

if r == unsat:
    print('zoey mel <> 1 2')

else:
    print(s0.model())

#assume 2: zoey == 2 == kv
s1 = Solver()
#s1.add(Distinct(zoey, mel))
#constrains 1, or 2 1 == kt, 2 == kv
s1.add(zoey>=1, zoey<=2)
s1.add(mel>=1,  mel<=2)
#add assumes
s1.add(zoey ==2, mel ==1)
#add sayings
s1.add(mel <> 2) # negation due to 2
s1.add(mel <> 2, zoey <>2)
r = s1.check()
if r == unsat:
    print('zoey mel <> 2 1')
else:
    print(s1.model())


#Q2

