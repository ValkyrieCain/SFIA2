from random import *
scpno=str(randint(1, 10000))
siteno=str(randint(1, 200))
oc=input("Safe, Euclid or Keter? ")
objectclass=oc.upper()
if objectclass=="SAFE":
	oc="s"
	lockerno=str(randint(1, 200))
if objectclass=="EUCLID":
	oc="e"
	containersize=str(randint(1, 20))
if objectclass=="KETER":
	oc="k"
locationlist=["Texas", "England", "Siberia", "France", "Maine", "Germany", 
"Italy", "Morocco", "Cuba", "Antarctica", "Sierra Lione", "South Africa", 
"Australia", "[REDACTED]", "█████████"]
ll=sample(locationlist, 1)
ll1=str(ll[0])
safeadjectivelist=["green", "round", "metallic", "black", "small", "circular", "white"]
sal=sample(safeadjectivelist, 2)
sal1=str(sal[0])
sal2=str(sal[1])
euclidadjectivelist=["1.5 meter tall", "round", "carnivorous"]
eal=sample(euclidadjectivelist, 2)
eal1=str(eal[0])
eal2=str(eal[1])
keteradjectivelist=["400 meters squared wide", "bright white"]
kal=sample(keteradjectivelist, 2)
kal1=str(kal[0])
kal2=str(kal[1])
safenounlist=["rock", "spoon", "███████ brand handheld games console", "shelf", "bowl of rice"]
snl=sample(safenounlist, 1)
snl1=str(snl[0])
euclidnounlist=["human of █████ descent", "███████", "sentient bicycle", "model train set"]
enl=sample(euclidnounlist, 1)
enl1=str(enl[0])
keternounlist=["pond", "building built in 19██", "nuclear bomb", "train", "████████"]
knl=sample(keternounlist, 1)
knl1=str(knl[0])
anomalycategorylist=["memetic", "xyz"]
acl=sample(anomalycategorylist, 1)
acl1=str(acl[0])
print("Item #: SCP-"+scpno)
if oc=="s":
	print("Object Class: Safe")
	print("Special Containment Procedures: SCP-"+scpno+" is to be held in storage locker #"+
		lockerno+" at Site "+siteno+".")
	print("Description: SCP-"+scpno+" is a "+sal1+", "+sal2+" "+snl1+". It is a "+
		acl1+" object that has the anomalous property of ____")
if oc=="e":
	print("Object Class: Euclid")
	print("Special Containment Procedures: SCP-"+scpno+" is to be held in a "+
		containersize+"m by"+containersize+"m by"+containersize+"m containment chamber at Site "+siteno+".")
	print("Description: SCP-"+scpno+" is a "+eal1+", "+eal2+" "+enl1+". It is a "+
		acl1+" object that has the anomalous property of ____")
if oc=="k":
	print("Object Class: Keter")
	print("Special Containment Procedures: SCP-"+scpno+" is contained on location in █████████, "+
		ll1+". Site "+siteno+" has been built around it.")
	print("Description: SCP-"+scpno+" is a "+kal1+", "+kal2+" "+knl1+". It is a "+
		acl1+" object that has the anomalous property of ____")