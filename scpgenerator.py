from random import *
scpno=str(randint(1, 10000))
siteno=str(randint(1, 200))
oc=input("Safe, Euclid or Keter? ")
objectclass=oc.upper()
if objectclass=="SAFE":
	oc="s"
	lockerno=str(randint(1, 200))
elif objectclass=="EUCLID":
	oc="e"
	containersize=str(randint(1, 20))
elif objectclass=="KETER":
	oc="k"
elif objectclass=="TEST":
	oc="t"
else:
	oc="spelling"
locationlist=["Texas", "England", "Siberia", "France", "Maine", "Germany", 
"Italy", "Morocco", "Cuba", "Antarctica", "Sierra Lione", "South Africa", 
"Australia", "[REDACTED]", "█████████"]
ll=sample(locationlist, 1)
safeadjectivelist=["green", "round", "metallic", "black", "small", "circular", "white"]
sal=sample(safeadjectivelist, 1)
euclidadjectivelist=["1.5 meter tall", "round", "carnivorous"]
eal=sample(euclidadjectivelist, 1)
keteradjectivelist=["400 meters squared wide", "bright white"]
kal=sample(keteradjectivelist, 1)
safenounlist=["rock", "spoon", "███████ brand handheld games console", "shelf", "bowl of rice"]
snl=sample(safenounlist, 1)
euclidnounlist=["human of █████ descent", "███████", "sentient bicycle", "model train set"]
enl=sample(euclidnounlist, 1)
keternounlist=["pond", "building built in 19██", "nuclear bomb", "train", "████████"]
knl=sample(keternounlist, 1)
anomalycategorylist=["a memetic", "an antimemetic", "an autonomous"]
acl=sample(anomalycategorylist, 1)
if oc=="s":
	print("Item #: SCP-"+scpno)
	print("Object Class: Safe")
	print("Special Containment Procedures: SCP-"+scpno+" is to be held in storage locker #"+
		lockerno+" at Site "+siteno+".")
	print("Description: SCP-"+scpno+" is a "+sal[0]+" "+snl[0]+". It is "+
		acl[0]+" object that has the anomalous property of ____")
if oc=="e":
	print("Item #: SCP-"+scpno)
	print("Object Class: Euclid")
	print("Special Containment Procedures: SCP-"+scpno+" is to be held in a "+
		containersize+"m by "+containersize+"m by "+containersize+"m containment chamber at Site "+siteno+".")
	print("Description: SCP-"+scpno+" is a "+eal[0]+" "+enl[0]+". It is "+
		acl[0]+" object that has the anomalous property of ____")
if oc=="k":
	print("Item #: SCP-"+scpno)
	print("Object Class: Keter")
	print("Special Containment Procedures: SCP-"+scpno+" is contained on location in █████████, "+
		ll[0]+". Site "+siteno+" has been built around it.")
	print("Description: SCP-"+scpno+" is a "+kal[0]+" "+knl[0]+". It is "+
		acl[0]+" object that has the anomalous property of ____")
if oc=="spelling":
	print("Object Class incorrectly inputted. Please try again.")
if oc=="t":
	oc="t"