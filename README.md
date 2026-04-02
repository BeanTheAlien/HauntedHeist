# Haunted Heist
Files from the indie game Haunted Heist.\
This repository was created by the Haunted Heist dev, [@BeanTheAlien](https://github.com/BeanTheAlien/).\
This is most of the build of the game.

# Other Info
This repo will provide info for many things, such as:
- Early access keys
- Game wiki
- Roadmap
- Sale dates
- ...and more

# Changelog
## 0.1.0 pre-alpha
- Started adding basic events

## 0.2.0 pre-alpha
- Added more complex events
- Updated to events linked to keys

## 0.3.0 pre-alpha
- Added UI widgets

## 0.3.1 pre-alpha
- Moved main screen to a separate level

## 0.3.2 pre-alpha
- Updated script to handle main screen

## 0.3.3 pre-alpha
- Updated widgets

## 0.4.0 pre-alpha
- Added AI enemies
- Enemies chase you
- Enemies ragdoll on death
- Enemies no longer have collision after death
- (bug) Enemies have extreme knockback
- (bug) Enemies have unrealistic vision
- Started patrol feature
- (roadmap) Jumpscare feature
- (roadmap) Roaming feature
- (bug) Chase, patrol, or roam enemy decision path required

## 0.4.3 pre-alpha
- Created beta patrol feature
- (roadmap) Random turning event
- (roadmap) Player death event

## 0.5.0 pre-alpha
- Beta random turning event released

## 0.6.0 pre-alpha
- Jim v1.0.0 finished and released
- (bug) Fix all events for enemies
- (roadmap) Total enemy rework to solve behavior bugs

## 0.4.0 pre-alpha
- Reversion required due to broken pawn sensing

## 0.4.7 pre-alpha
- Resolving previous content issues

## 0.5.3 pre-alpha
- Enemies now have proper tracking using a raycast and pawn sensing combination
- (bug) Enemy patrol continually repeats and overrides previous instructions

## 0.5.5 pre-alpha
- Enemies now have a work in progress basic action system

## 0.6.0 pre-alpha
- Re-added Jim v1.0.0

## 0.6.1 pre-alpha
- Fixed enemy patrol pathing
- (roadmap) Reworked random turn event

## 0.7.0 pre-alpha
- Released initial Beta death sequence

## 0.8.0 pre-alpha
- Released item interaction system
- (roadmap) Haunted items that trigger horde effect

## 0.8.1 pre-alpha
- Modified interaction to use standard fire for throwing, prevents fire while holding object

## 0.8.4 pre-alpha
- Player now has health
- Enemies now deal damage, 150 unit attack range, gain one attack chance every 3 seconds

## 0.8.5 pre-alpha
- Beta horde feature completed

## 0.8.6 pre-alpha
- Added some sounds
- Fixed some bugs
- Added new tank enemy

## 0.8.8 pre-alpha
- Added flashlight
- Added world manager

## 0.8.9 pre-alpha
- Added simple console system

## 0.8.10 pre-alpha
- Updated the console

## 0.8.11 pre-alpha
- Added noclip and flight

## 0.8.12 pre-alpha
- Added class-based destruction for console

## 0.8.13 pre-alpha
- Added more console commands

## 0.8.14 pre-alpha
- Added simple blood effect on screen when player is damaged
- (bug) Resolve blood screen removal on death

## 0.8.22 pre-alpha
- Fixed generation system
- Fixed render distance offload system
- Added random turning event for ghosts

## 0.8.23 pre-alpha
- Added wandering event for ghosts.

## 0.8.25 pre-alpha
- Fixed some errors.
- Added jump command to console.
- Added Shop level and Shop Radio.

## 0.8.26 pre-alpha
- Updated the model for Room1.

## 0.8.27 pre-alpha
- (bug) Enemy events are not working as intended.
- (bug) Room offload fails to destroy rooms.

## 0.8.28 pre-alpha
- Updated the shop.

## 0.8.29 pre-alpha
- Made various changes.

## 0.8.30 pre-alpha
- Added an ammunition system.

## 0.8.31 pre-alpha
- Raised the Tank health from 50 ⇒ 100.
- Raised Horde event spawn from 15 ⇒ 20 - 40.

## 0.9.0 pre-alpha
- Overhauled the room spawning system.

## 0.9.1 pre-alpha
- Added work in progress crowbar component.
- Started updating enemies to use enemy base.

## 0.9.2 pre-alpha
- Finished porting enemies to enemy base.
- Resolved some errors.

## 0.10.0 alpha
- Ported engine version from Unreal Engine 5.2 ⇒ Unreal Engine 5.6.
- Began overhaul on ghost AI system to State Tree.

## 0.10.1 alpha
- Added Big Boss actor.
- Crowbar correctly damages enemies.
- Added support for weapon switching.

## 0.10.2 alpha
- Continued development for weapon switching.
- Updated weapon switch to have a central weapon component instead of separate components.
- (bug) Weapon component does not properly deload skeletal meshes.
- Ported most weapon content to the central component.
- (roadmap) Medkit item to heal player after taking damage.

## 0.10.3 alpha
- (bug) Weapon component does not properly switch weapons.
- (bug) Pickups do not properly load weapons.

## 0.10.4 alpha
- Updated weapon component.

## 0.10.5 alpha
- Further development and patching for the inventory system.

## 0.10.6 alpha
- Changed development direction for inventory system to use has weapon booleans, weapon struct array and equip event with input for keys to map to equip indexes.
- (roadmap) The shotgun will have an iron sight because iron sights are badass.

## 0.10.7 alpha
- Input key maps to index, equip uses weapon struct array, ported some old variables over to Player, the attack event will now switch on the current equip index.

## 0.10.8 alpha
- Minor patch to use is valid index on equip check. Implemented to resolve future errors.

## 0.11.0 alpha
- Major update. Weapon inventory-style now functions. Crowbar does not position in the correct spot.
- (roadmap) Add specific weapon pickup triggers.

## 0.11.1 alpha
- Updated player logic to cancel reloading if fired, minor changes within testing of player holding object before continuing logic flows. Added shotgun and crowbar pickup.

## 0.11.2 alpha
- Overhauled room spawn system and applied a 430 unit gap between spawns.

## 0.11.3 alpha
- Added teleport trigger and red cube that summons rooms.

## 0.11.4 alpha
- Started fixing rooms, added props.

## 0.11.5 alpha
- Added Häuser/House (unfinished). Added prop/Bed.

## 0.11.6 alpha
- Updated house. Added spinning fish 10 hours media plate.

## 0.11.7 alpha
- Updated interacted event to provide a reference to the player, the hit component and the name of the hit bone.
- Added sofa. Interacting with the sofa will put you on top of it.

## 0.11.8 alpha
- Updated house and door. Added fridge.

## 0.11.9 alpha
- Added an oven.

## 0.11.10 alpha
- Added fall damage.

## 0.11.11 alpha
- Started adding WeatherManager.
- Added rain Niagara system to be implemented by WeatherManager.

## 0.11.12 alpha
- Implemented rain system.
- Updated WorldManager to add SetTimeStormy.

## 0.11.13 alpha
- Implemented medkit weapon.

## 0.11.14 alpha
- Added GetTime function for WorldManager.
- Started implementing graveyard.

## 0.11.15 alpha
- Worked on graveyard.
- (bug) Door does not open. Need to fix.

## 0.11.16 alpha
- Improvements to graveyard; made graveyard gate an actor.
- Fixed door not opening error.

## 0.11.17 alpha
- Added House1.

## 0.11.18 alpha
- Added Journal/JEntry, Journal/JournalUI.

## 0.12.0 alpha
- Finally changed the shotgun to a pellet-based system.

## 0.12.1 alpha
- Added velocity application per bullet impact.
- Added scream sound upon falling 50,0f.
- Fixed scream sound to be destroyed upon landing.
- Added swing sound to crowbar swing.
- Added Test Enemy Hit event for raycasts; changed content to use it.

## 0.12.2 alpha
- Started implementing Game Instance.
- Added Shop Upg spawning.

## 0.12.3 alpha
- Fixed ExtraBullet to call parent.
- Player goes to shop on death, added exit to shop.
