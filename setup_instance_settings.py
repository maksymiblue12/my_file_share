from os.path import exists

if (exists("options.txt")):
	quit()
data={}

settings="""
autoJump:false
enableVsync:false
fov:1.0
fovEffectScale:0.0
darknessEffectScale:0.0
graphicsPreset:"custom"
fullscreen:true
gamma:1000.0
guiScale:2
maxFps:60
narrator:0
renderDistance:16
simulationDistance:12
screenEffectScale:0.0
vignette:false
operatorItemsTab:true
showSubtitles:true
bobView:false
darkMojangStudiosBackground:true
damageTiltStrength:0.0
highContrastBlockOutline:true
narratorHotkey:false
lang:en_us
advancedItemTooltips:true
tutorialStep:none
skipMultiplayerWarning:true
joinedFirstServer:true
menuBackgroundBlurriness:0
soundCategory_music:0.0
"""

for i in settings.strip().split("\n"):
	k,v=i.split(":")
	if (k.startswith("#")):
		continue
	data[k]=v

with open("options.txt","w") as f:
	for k,v in data.items():
		f.write(f"{k}:{v}\n")