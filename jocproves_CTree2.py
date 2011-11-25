# -*- coding:utf-8  -*-
import inspect ## No se si funcionarà en tots els pythons?!?

print "Comprovant CTree:",

# Comprovació de la declaració de la classe:
################################################################################
try:
	CTree = __import__("CTree")
	reload(CTree)
except:
	raise ValueError, """CTree: No s'ha trobat l'arxiu "CTree.py" (Comproveu el nom de l'arxiu que ha de ser exactament igual)."""

try:
	if len(inspect.getargspec(CTree.CTree.Build)[0]) != 2: raise ValueError, """CTree: a Build() se li passa un paràmetre, la seva capçalera ha de ser exactament: "def Build(self,file):" """
except AttributeError:
	raise ValueError, """CTree: No s'ha trobat la funció Build(). La capçalera d'aquesta ha de ser exactament: "def Build(self,file):" """

try:
	if len(inspect.getargspec(CTree.CTree.AddData)[0]) != 2: raise ValueError, """CTree: a AddData() se li passa un paràmetre, la seva capçalera ha de ser exactament: "def AddData(self,features):" """
except AttributeError:
	raise ValueError, """CTree: No s'ha trobat la funció AddData(). La capçalera d'aquesta ha de ser exactament: "def AddData(self,features):" """

try:
	if len(inspect.getargspec(CTree.CTree.GetDataClass)[0]) != 2: raise ValueError, """CTree: a GetDataClass() se li passa un paràmetre, la seva capçalera ha de ser exactament: "def GetDataClass(self,features):" """
except AttributeError:
	raise ValueError, """CTree: No s'ha trobat la funció GetDataClass(). La capçalera d'aquesta ha de ser exactament: "def GetDataClass(self,features):" """

try:
	if len(inspect.getargspec(CTree.CTree.parser)[0]) != 5: raise ValueError, """CTree: a parser() se li passen quatre paràmetres, la seva capçalera ha de ser exactament: "def parser (self,fileList,lin,prof,nodeact):" """
except AttributeError:
	raise ValueError, """CTree: No s'ha trobat la funció parser(). La capçalera d'aquesta ha de ser exactament: "def parser (self,fileList,lin,prof,nodeact):" """

try:
	if len(inspect.getargspec(CTree.CTree.addDataRecursive)[0]) != 4: raise ValueError, """CTree: a addDataRecursive() se li passen tres paràmetres, la seva capçalera ha de ser exactament: "def addDataRecursive(self, features, featurenum, nodeact):" """
except AttributeError:
	raise ValueError, """CTree: No s'ha trobat la funció addDataRecursive(). La capçalera d'aquesta ha de ser exactament: "def addDataRecursive(self, features, featurenum, nodeact):" """

## Comprovació del funcionament de la classe:
################################################################################
tr = CTree.CTree()

tr.Build('db.xml')
##Provem parser

rep=0
shel=0
fro=0
ins=0
mam=0
bird=0
for ii in tr._CTree__root.getChilds():
    if ii.getData().count('reptile')>0:
        rep+=1
    if ii.getData().count('shellfish')>0:
        shel+=1
    if ii.getData().count('frog')>0:
        fro+=1
    if ii.getData().count('insect')>0:
        ins+=1
    if ii.getData().count('mammal')>0:
        mam+=1
    if ii.getData().count('bird')>0:
        bird+=1

if rep<1:raise ValueError, """CTree: Error al parser=> Reptile no trobat"""
if shel<1:raise ValueError, """CTree: Error al parser=> Shellfish no trobat"""
if fro<1:raise ValueError, """CTree: Error al parser=> Frog no trobat"""
if ins<1:raise ValueError, """CTree: Error al parser=> Insect no trobat"""
if mam<1:raise ValueError, """CTree: Error al parser=> Mammal no trobat"""
if bird<1:raise ValueError, """CTree: Error al parser=> Brid no trobat"""


## Provem GetDataClass
pitviper=['reptile','no','no','yes','0','no','yes','yes','yes','yes','yes','no','no','no','yes','no','no']
seasnake=['reptile','no','no','yes','0','no','yes','no','yes','yes','yes','yes','no','no','no','no','no']
slowworm=['reptile','no','no','yes','0','no','no','yes','yes','yes','yes','no','no','no','yes','no','no']
tuatara=['reptile','no','no','yes','4','no','no','yes','yes','yes','yes','no','no','no','yes','no','no']
scorpion=['shellfish','no','no','yes','8','no','yes','yes','no','no','yes','no','no','no','no','no','no']
piranha=['fish','no','no','yes','0','yes','no','no','yes','yes','yes','yes','no','no','yes','no','no']
catfish=['fish','no','no','yes','0','yes','no','no','yes','yes','yes','yes','no','no','yes','no','no']
seahorse=['fish','no','no','yes','0','yes','no','no','yes','yes','no','yes','no','no','yes','no','no']
haddock=['fish','no','no','yes','0','yes','no','no','yes','yes','no','yes','no','no','yes','no','no']
sole=['fish','no','no','yes','0','yes','no','no','yes','yes','no','yes','no','no','yes','no','no']
seawasp=['shellfish','no','no','no','0','no','yes','no','no','no','yes','yes','no','no','yes','no','no']
slug=['shellfish','no','no','no','0','no','no','yes','no','no','no','no','no','no','yes','no','no']
worm=['shellfish','no','no','no','0','no','no','yes','no','no','no','no','no','no','yes','no','no']
clam=['shellfish','no','no','no','0','no','no','no','no','no','yes','no','no','no','yes','no','no']
starfish=['shellfish','no','no','no','5','no','no','no','no','no','yes','yes','no','no','yes','no','no']
crab=['shellfish','no','no','no','4','no','no','no','no','no','yes','yes','no','no','yes','no','no']
crayfish=['shellfish','no','no','no','6','no','no','no','no','no','yes','yes','no','no','yes','no','no']
lobster=['shellfish','no','no','no','6','no','no','no','no','no','yes','yes','no','no','yes','no','no']
carp=['fish','no','yes','yes','0','yes','no','no','yes','yes','no','yes','no','no','yes','no','no']
stingray=['fish','yes','no','yes','0','yes','yes','no','yes','yes','yes','yes','no','no','yes','no','no']
pike=['fish','yes','no','yes','0','yes','no','no','yes','yes','yes','yes','no','no','yes','no','no']
tuna=['fish','yes','no','yes','0','yes','no','no','yes','yes','yes','yes','no','no','yes','no','no']
dogfish=['fish','yes','no','yes','0','yes','no','no','yes','yes','yes','yes','no','no','yes','no','no']
newt=['frog','no','no','yes','4','no','no','yes','yes','yes','yes','yes','no','no','yes','no','no']
frog=['frog','no','no','no','4','no','no','yes','yes','yes','yes','yes','no','no','yes','no','no']
toad=['frog','no','no','no','4','no','no','yes','yes','yes','no','yes','no','no','yes','no','no']
honeybee=['insect','no','yes','no','6','no','yes','yes','no','no','no','no','yes','no','yes','no','yes']
ladybird=['insect','no','no','no','6','no','no','yes','no','no','yes','no','yes','no','yes','no','no']
moth=['insect','no','no','no','6','no','no','yes','no','no','no','no','yes','no','yes','no','yes']
housefly=['insect','no','no','no','6','no','no','yes','no','no','no','no','yes','no','yes','no','yes']
gnat=['insect','no','no','no','6','no','no','yes','no','no','no','no','yes','no','yes','no','no']
flea=['insect','no','no','no','6','no','no','yes','no','no','no','no','no','no','yes','no','no']
termite=['insect','no','no','no','6','no','no','yes','no','no','no','no','no','no','yes','no','no']
pussycat=['mammal','yes','yes','yes','4','no','no','yes','yes','yes','yes','no','no','yes','no','no','yes']
sealion=['mammal','yes','no','yes','2','yes','no','yes','yes','yes','yes','yes','no','yes','no','no','yes']
wallaby=['mammal','yes','no','yes','2','no','no','yes','yes','yes','no','no','no','yes','no','no','yes']
mink=['mammal','yes','no','yes','4','no','no','yes','yes','yes','yes','yes','no','yes','no','no','yes']
antelope=['mammal','yes','no','yes','4','no','no','yes','yes','yes','no','no','no','yes','no','no','yes']
deer=['mammal','yes','no','yes','4','no','no','yes','yes','yes','no','no','no','yes','no','no','yes']
oryx=['mammal','yes','no','yes','4','no','no','yes','yes','yes','no','no','no','yes','no','no','yes']
giraffe=['mammal','yes','no','yes','4','no','no','yes','yes','yes','no','no','no','yes','no','no','yes']
elephant=['mammal','yes','no','yes','4','no','no','yes','yes','yes','no','no','no','yes','no','no','yes']
buffalo=['mammal','yes','no','yes','4','no','no','yes','yes','yes','no','no','no','yes','no','no','yes']
platypus=['mammal','yes','no','yes','4','no','no','yes','yes','no','yes','yes','no','yes','yes','no','yes']
seal=['mammal','yes','no','no','0','yes','no','yes','yes','yes','yes','yes','no','yes','no','no','yes']
gorilla=['mammal','yes','no','no','2','no','no','yes','yes','yes','no','no','no','yes','no','no','yes']
aardvark=['mammal','yes','no','no','4','no','no','yes','yes','yes','yes','no','no','yes','no','no','yes']
bear=['mammal','yes','no','no','4','no','no','yes','yes','yes','yes','no','no','yes','no','no','yes']
hamster=['mammal','no','yes','yes','4','no','no','yes','yes','yes','no','no','no','yes','no','no','yes']
cavy=['mammal','no','yes','no','4','no','no','yes','yes','yes','no','no','no','yes','no','no','yes']
vampire=['mammal','no','no','yes','2','no','no','yes','yes','yes','no','no','yes','yes','no','no','yes']
fruitbat=['mammal','no','no','yes','2','no','no','yes','yes','yes','no','no','yes','yes','no','no','yes']
squirrel=['mammal','no','no','yes','2','no','no','yes','yes','yes','no','no','no','yes','no','no','yes']
opossum=['mammal','no','no','yes','4','no','no','yes','yes','yes','yes','no','no','yes','no','no','yes']
mole=['mammal','no','no','yes','4','no','no','yes','yes','yes','yes','no','no','yes','no','no','yes']
vole=['mammal','no','no','yes','4','no','no','yes','yes','yes','no','no','no','yes','no','no','yes']
hare=['mammal','no','no','yes','4','no','no','yes','yes','yes','no','no','no','yes','no','no','yes']
penguin=['bird','yes','no','yes','2','no','no','yes','yes','no','yes','yes','no','no','yes','yes','no']
vulture=['bird','yes','no','yes','2','no','no','yes','yes','no','yes','no','yes','no','yes','yes','no']
rhea=['bird','yes','no','yes','2','no','no','yes','yes','no','yes','no','no','no','yes','yes','no']
swan=['bird','yes','no','yes','2','no','no','yes','yes','no','no','yes','yes','no','yes','yes','no']
flamingo=['bird','yes','no','yes','2','no','no','yes','yes','no','no','no','yes','no','yes','yes','no']
ostrich=['bird','yes','no','yes','2','no','no','yes','yes','no','no','no','no','no','yes','yes','no']
chicken=['bird','no','yes','yes','2','no','no','yes','yes','no','no','no','yes','no','yes','yes','no']
dove=['bird','no','yes','yes','2','no','no','yes','yes','no','no','no','yes','no','yes','yes','no']
parakeet=['bird','no','yes','yes','2','no','no','yes','yes','no','no','no','yes','no','yes','yes','no']
skua=['bird','no','no','yes','2','no','no','yes','yes','no','yes','yes','yes','no','yes','yes','no']
skimmer=['bird','no','no','yes','2','no','no','yes','yes','no','yes','yes','yes','no','yes','yes','no']
gull=['bird','no','no','yes','2','no','no','yes','yes','no','yes','yes','yes','no','yes','yes','no']
crow=['bird','no','no','yes','2','no','no','yes','yes','no','yes','no','yes','no','yes','yes','no']
hawk=['bird','no','no','yes','2','no','no','yes','yes','no','yes','no','yes','no','yes','yes','no']
kiwi=['bird','no','no','yes','2','no','no','yes','yes','no','yes','no','no','no','yes','yes','no']
duck=['bird','no','no','yes','2','no','no','yes','yes','no','no','yes','yes','no','yes','yes','no']
lark=['bird','no','no','yes','2','no','no','yes','yes','no','no','no','yes','no','yes','yes','no']
wren=['bird','no','no','yes','2','no','no','yes','yes','no','no','no','yes','no','yes','yes','no']
pheasant=['bird','no','no','yes','2','no','no','yes','yes','no','no','no','yes','no','yes','yes','no']
sparrow=['bird','no','no','yes','2','no','no','yes','yes','no','no','no','yes','no','yes','yes','no']



if (tr.GetDataClass(mink).count('mink')!=1): raise ValueError, """CTree: Error al GetDataClass=>mink"""
if (tr.GetDataClass(platypus).count('platypus')!=1): raise ValueError, """CTree: Error al GetDataClass=>platypus"""
if (tr.GetDataClass(seal).count('seal')!=1): raise ValueError, """CTree: Error al GetDataClass=>seal"""
if (tr.GetDataClass(gorilla).count('gorilla')!=1): raise ValueError, """CTree: Error al GetDataClass=>gorilla"""
if (tr.GetDataClass(hamster).count('hamster')!=1): raise ValueError, """CTree: Error al GetDataClass=>hamster"""
if (tr.GetDataClass(cavy).count('cavy')!=1): raise ValueError, """CTree: Error al GetDataClass=>cavy"""
if (tr.GetDataClass(squirrel).count('squirrel')!=1): raise ValueError, """CTree: Error al GetDataClass=>squirrel"""
if (tr.GetDataClass(penguin).count('penguin')!=1): raise ValueError, """CTree: Error al GetDataClass=>penguin"""
if (tr.GetDataClass(vulture).count('vulture')!=1): raise ValueError, """CTree: Error al GetDataClass=>vulture"""
if (tr.GetDataClass(rhea).count('rhea')!=1): raise ValueError, """CTree: Error al GetDataClass=>rhea"""
if (tr.GetDataClass(swan).count('swan')!=1): raise ValueError, """CTree: Error al GetDataClass=>swan"""
if (tr.GetDataClass(flamingo).count('flamingo')!=1): raise ValueError, """CTree: Error al GetDataClass=>flamingo"""
if (tr.GetDataClass(ostrich).count('ostrich')!=1): raise ValueError, """CTree: Error al GetDataClass=>ostrich"""
if (tr.GetDataClass(kiwi).count('kiwi')!=1): raise ValueError, """CTree: Error al GetDataClass=>kiwi"""
if (tr.GetDataClass(duck).count('duck')!=1): raise ValueError, """CTree: Error al GetDataClass=>duck"""
if (tr.GetDataClass(pitviper).count('pitviper')!=1): raise ValueError, """CTree: Error al GetDataClass=>pitviper"""
if (tr.GetDataClass(seasnake).count('seasnake')!=1): raise ValueError, """CTree: Error al GetDataClass=>seasnake"""
if (tr.GetDataClass(slowworm).count('slowworm')!=1): raise ValueError, """CTree: Error al GetDataClass=>slowworm"""
if (tr.GetDataClass(tuatara).count('tuatara')!=1): raise ValueError, """CTree: Error al GetDataClass=>tuatara"""
if (tr.GetDataClass(scorpion).count('scorpion')!=1): raise ValueError, """CTree: Error al GetDataClass=>scorpion"""
if (tr.GetDataClass(seawasp).count('seawasp')!=1): raise ValueError, """CTree: Error al GetDataClass=>seawasp"""
if (tr.GetDataClass(clam).count('clam')!=1): raise ValueError, """CTree: Error al GetDataClass=>clam"""
if (tr.GetDataClass(starfish).count('starfish')!=1): raise ValueError, """CTree: Error al GetDataClass=>starfish"""
if (tr.GetDataClass(crab).count('crab')!=1): raise ValueError, """CTree: Error al GetDataClass=>crab"""
if (tr.GetDataClass(carp).count('carp')!=1): raise ValueError, """CTree: Error al GetDataClass=>carp"""
if (tr.GetDataClass(stingray).count('stingray')!=1): raise ValueError, """CTree: Error al GetDataClass=>stingray"""
if (tr.GetDataClass(newt).count('newt')!=1): raise ValueError, """CTree: Error al GetDataClass=>newt"""
if (tr.GetDataClass(frog).count('frog')!=1): raise ValueError, """CTree: Error al GetDataClass=>frog"""
if (tr.GetDataClass(toad).count('toad')!=1): raise ValueError, """CTree: Error al GetDataClass=>toad"""
if (tr.GetDataClass(honeybee).count('honeybee')!=1): raise ValueError, """CTree: Error al GetDataClass=>honeybee"""
if (tr.GetDataClass(ladybird).count('ladybird')!=1): raise ValueError, """CTree: Error al GetDataClass=>ladybird"""
if (tr.GetDataClass(gnat).count('gnat')!=1): raise ValueError, """CTree: Error al GetDataClass=>gnat"""
if (tr.GetDataClass(pussycat).count('pussycat')!=1): raise ValueError, """CTree: Error al GetDataClass=>pussycat"""
if (tr.GetDataClass(sealion).count('sealion')!=1): raise ValueError, """CTree: Error al GetDataClass=>sealion"""
if (tr.GetDataClass(wallaby).count('wallaby')!=1): raise ValueError, """CTree: Error al GetDataClass=>wallaby"""
if (tr.GetDataClass(['bird','yes','no','yes','20','yes','no','yes','yes','no','yes','yes','no','no','yes','yes','no'])is not None): raise ValueError, """CTree: Error al GetDataClass, GetDAtaClass() ha de tornar None si no troba l'animal"""

##provem d'afegir una branca de la mateixa mida
try:
    tr.AddData(['mammal','yes','yes','yes','8','no','no','yes','yes','no','no','yes','no','no','yes','yes','no','orfix'])
except:
    raise ValueError, """CTree: AddData no funciona correctament"""
if (tr.GetDataClass(['mammal','yes','yes','yes','8','no','no','yes','yes','no','no','yes','no','no','yes','yes','no']).count('orfix')!=1): raise ValueError, """CTree: Error al GetDataClass"""

##Afegim una de mida diferent i més petita (ho ha d'acceptar)
try:
    tr.AddData(['I','you','he','she','it','we','you','they'])
except:
    raise ValueError, """CTree: AddData no funciona correctament"""
if (tr.GetDataClass(['I','you','he','she','it','we','you']).count('they')!=1): raise ValueError, """GetDataClass"""

##Afegim una de mida diferent i més gran (ho ha d'acceptar)
try:
    tr.AddData(['mammal','yes','yes','javier','marcal','no','no','yes','yes','ED','no','yes','no','no','yes','jocdeproves','animals','yes','robots','no','pilots','orfix','quecoiesunorfix'])
except:
    raise ValueError, """CTree: AddData no funciona correctament"""
if (tr.GetDataClass(['mammal','yes','yes','javier','marcal','no','no','yes','yes','ED','no','yes','no','no','yes','jocdeproves','animals','yes','robots','no','pilots','orfix']).count('quecoiesunorfix')!=1): raise ValueError, """CTree: Error al GetDataClass"""


print "[Correcte]"
