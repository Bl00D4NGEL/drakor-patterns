"""
Pattern calculator for Drakor. Woefully incomplete.

No UI; to use, load into console (IDLE works well), call the function
for the desired pattern, and then print the pattern tree. See also
pattern-ui.py.

Pattern naming rules: drop all non-alphanumeric characters; replace 
spaces with underscore; in cases of mismatch between recipe name and 
resulting mat, use mat name (ex: use iron_nail NOT form_iron_nails.

Arguments have defaults, so only need to include 
if you want more than one of the top-level pattern or if you want extra 
indentation.

For patterns that produce more than 1 of an item (like nails, shingles,
and powders), the amount of needed ingredients is rounded up.

For patterns where the same name is used more than once (such as with 
the Durability Runes), append the starting pattern level. So, the first
Durability Rune (Common+) - which has a level range of 1-8 - would be
durability_rune_common_1, while the second one - with a range of 8-15 - 
would be durability_rune_common_8.
"""

from math import ceil						#for multi-output rounding

#Any items related to infrastructure (building the pattern tree, etc.).
pattern_tree = []

def build_tree(mat_name,quantity,indent):
	pattern_tree.append({'name':mat_name,'quan':quantity,'indent':indent})


#Only patterns below here.
"""
def ?(quantity=1,indent=0):
	build_tree("?",quantity,indent)
	indent += 1
	?(quantity,indent)
	?(ceil(quantity/?.0),indent)

"""



""" ANCIENT RESEARCH 
"""

def primitive_writings(quantity=1, indent=0):
	build_tree("Primitive Writings", quantity, indent)
	
def aged_etching(quantity=1, indent=0):
	build_tree("Aged Etching", quantity, indent)
	
def primitive_reference(quantity=1, indent=0):
	build_tree("Primitive Reference", quantity, indent)
	
def primitive_rune(quantity=1, indent=0):
	build_tree("Primitive Rune", quantity, indent)
	
def primitive_parchment(quantity=1, indent=0):
	build_tree("Primitive Parchment", quantity, indent)

def aged_writings(quantity=1, indent=0):
	build_tree("Aged Writings", quantity, indent)
	
def intricate_etching(quantity=1, indent=0):
	build_tree("Intricate Etching", quantity, indent)

def aged_reference(quantity=1, indent=0):
	build_tree("Aged Reference", quantity, indent)

def aged_etching(quantity=1, indent=0):
	build_tree("Aged Etching", quantity, indent)
	
def elemental_rune(quantity=1, indent=0):
	build_tree("Elemental Rune", quantity, indent)
		
def elemental_parchment(quantity=1, indent=0):
	build_tree("Elemental Parchment", quantity, indent)
	
def ancient_etching(quantity=1, indent=0):
	build_tree("Ancient Etching", quantity, indent)
	
def pristine_writings(quantity=1, indent=0):
	build_tree("Pristine Writings", quantity, indent)
	
def complex_etching(quantity=1, indent=0):
	build_tree("Complex Etching", quantity, indent)
	
def pristine_reference(quantity=1, indent=0):
	build_tree("Pristine Reference", quantity, indent)
	
def pristine_rune(quantity=1, indent=0):
	build_tree("Pristine Rune", quantity, indent)
	
def preserved_parchment(quantity=1, indent=0):
	build_tree("Preserved Parchment", quantity, indent)
	
def primeval_writings(quantity=1, indent=0):
	build_tree("Primeval Writings", quantity, indent)
	
def elaborate_etching(quantity=1, indent=0):
	build_tree("Elaborate Etching", quantity, indent)
	
def primeval_reference(quantity=1, indent=0):
	build_tree("Primeval Reference", quantity, indent)
	
def primeval_rune(quantity=1, indent=0):
	build_tree("Primeval Rune", quantity, indent)
	
def primeval_parchment(quantity=1, indent=0):
	build_tree("Primeval Parchment", quantity, indent)

""" ANCIENT RESEARCH END
"""


""" LOGGING
"""
def light_birch(quantity=1,indent=0):
	build_tree("Light Birch",quantity,indent)

def black_spruce(quantity=1,indent=0):
	build_tree("Black Spruce",quantity,indent)

def wild_cherry(quantity=1,indent=0):
	build_tree("Wild Cherry",quantity,indent)
	
def black_ash(quantity=1,indent=0):
	build_tree("Black Ash",quantity,indent)

def red_cedar(quantity=1,indent=0):
	build_tree("Red Cedar",quantity,indent)
	
def white_pine(quantity=1,indent=0):
	build_tree("White Pine",quantity,indent)

def silver_maple(quantity=1,indent=0):
	build_tree("Silver Maple",quantity,indent)

def bigtooth_aspen(quantity=1,indent=0):
	build_tree("Bigtooth Aspen",quantity,indent)

def hemlock(quantity=1,indent=0):
	build_tree("Hemlock",quantity,indent)	

def sharkwood(quantity=1, indent=0):
	build_tree("Sharkwood", quantity, indent)
	
def walnut(quantity=1, indent=0):
	build_tree("Walnut", quantity, indent)

def dark_cherry(quantity=1, indent=0):
	build_tree("Dark Cherry", quantity, indent)

"""LOGGING END
"""

""" FISHING
"""

def eel(quantity=1, indent=0):
	build_tree("Eel", quantity, indent)
	
def pike(quantity=1, indent=0):
	build_tree("Pike", quantity, indent)
	
def trout(quantity=1, indent=0):
	build_tree("Trout", quantity, indent)
	
def salmon(quantity=1, indent=0):
	build_tree("Salmon", quantity, indent)
	
def delvrak(quantity=1, indent=0):
	build_tree("Delvrak", quantity, indent)
	
def gilgrash(quantity=1, indent=0):
	build_tree("Gilgrash", quantity, indent)
	
def pickerel(quantity=1, indent=0):
	build_tree("Pickerel", quantity, indent)
		
def sunray(quantity=1, indent=0):
	build_tree("Sunray", quantity, indent)
		
def fire_goby(quantity=1, indent=0):
	build_tree("Fire Goby", quantity, indent)
		
def shadow_fish(quantity=1, indent=0):
	build_tree("Shadow Fish", quantity, indent)
		
def halibut(quantity=1, indent=0):
	build_tree("Halibut", quantity, indent)
		
def flounder(quantity=1, indent=0):
	build_tree("Flounder", quantity, indent)
		
def catfish(quantity=1, indent=0):
	build_tree("Catfish", quantity, indent)
		
def perch(quantity=1, indent=0):
	build_tree("Perch", quantity, indent)
		
def rockfish(quantity=1, indent=0):
	build_tree("Rockfish", quantity, indent)
		
def lancetail(quantity=1, indent=0):
	build_tree("Lancetail", quantity, indent)
		
def spiny_piranha(quantity=1, indent=0):
	build_tree("Spiny Piranha", quantity, indent)
		
def mackerel(quantity=1, indent=0):
	build_tree("Mackerel", quantity, indent)
		
def trunkfish(quantity=1, indent=0):
	build_tree("Trunkfish", quantity, indent)
		
def lionfish(quantity=1, indent=0):
	build_tree("Lionfish", quantity, indent)
		
def ghostfish(quantity=1, indent=0):
	build_tree("Ghostfish", quantity, indent)
		
def herring(quantity=1, indent=0):
	build_tree("Herring", quantity, indent)
		
def icefish(quantity=1, indent=0):
	build_tree("Icefish", quantity, indent)
		
def angelfish(quantity=1, indent=0):
	build_tree("Angelfish", quantity, indent)
		
def fangtooth(quantity=1, indent=0):
	build_tree("Fangtooth", quantity, indent)

""" FISHING END
"""

""" GATHERING
"""

def goldenbush(quantity=1, indent=0):
	build_tree("Goldebush", quantity, indent)
	
def pixieroot(quantity=1, indent=0):
	build_tree("Pixieroot", quantity, indent)
	
def apple(quantity=1, indent=0):
	build_tree("Apple", quantity, indent)
	
def large_egg(quantity=1, indent=0):
	build_tree("Large Egg", quantity, indent)
	
def spiritherb(quantity=1, indent=0):
	build_tree("Spiritherb", quantity, indent)
	
def gorethistle(quantity=1, indent=0):
	build_tree("Gorethistle", quantity, indent)
	
def waterberry(quantity=1, indent=0):
	build_tree("Waterberry", quantity, indent)
	
def dogweed(quantity=1, indent=0):
	build_tree("Dogweed", quantity, indent)
	
def sandcreeper(quantity=1, indent=0):
	build_tree("Sandcreeper", quantity, indent)
	
def moonbeard(quantity=1, indent=0):
	build_tree("Moonbeard", quantity, indent)
	
def phantomlilly(quantity=1, indent=0):
	build_tree("Phantomlilly", quantity, indent)
	
def orange(quantity=1, indent=0):
	build_tree("Orange", quantity, indent)
	
def dark_honey(quantity=1, indent=0):
	build_tree("Dark Honey", quantity, indent)
	
def dark_cotton(quantity=1, indent=0):
	build_tree("Dark Cotton", quantity, indent)
	
def arcaneleaf(quantity=1, indent=0):
	build_tree("", quantity, indent)
	
def wolfsbane(quantity=1, indent=0):
	build_tree("Arcaneleaf", quantity, indent)
	
def ladyslipper(quantity=1, indent=0):
	build_tree("Ladyslipper", quantity, indent)
	
def banana(quantity=1, indent=0):
	build_tree("Banana", quantity, indent)
	
def giant_egg(quantity=1, indent=0):
	build_tree("Giant Egg", quantity, indent)
	
def liontail(quantity=1, indent=0):
	build_tree("Liontail", quantity, indent)
	
def devilweed(quantity=1, indent=0):
	build_tree("Devilweed", quantity, indent)
	
def ghoulweed(quantity=1, indent=0):
	build_tree("Ghoulweed", quantity, indent)
	
def spiderfoot(quantity=1, indent=0):
	build_tree("Spiderfoot", quantity, indent)
		
def vilegourd(quantity=1, indent=0):
	build_tree("Vilegourd", quantity, indent)
		
def apricot(quantity=1, indent=0):
	build_tree("Apricot", quantity, indent)
		
def devilpetal(quantity=1, indent=0):
	build_tree("Devilpetal", quantity, indent)
		
def medusaroot(quantity=1, indent=0):
	build_tree("Medusaroot", quantity, indent)
		
def ghostshroom(quantity=1, indent=0):
	build_tree("Ghostshroom", quantity, indent)
	
"""GATHERING END
"""

"""MINING
"""
		
def clay(quantity=1, indent=0):
	build_tree("Clay", quantity, indent)
			
def cobalt_ore(quantity=1, indent=0):
	build_tree("Cobalt Ore", quantity, indent)
			
def fire_clay(quantity=1, indent=0):
	build_tree("Fire Clay", quantity, indent)
			
def garnet(quantity=1, indent=0):
	build_tree("Garnet", quantity, indent)
			
def blackened_stone(quantity=1, indent=0):
	build_tree("Blackened Stone", quantity, indent)
			
def amber(quantity=1, indent=0):
	build_tree("Amber", quantity, indent)
			
def lava_rock(quantity=1, indent=0):
	build_tree("Lava Rock", quantity, indent)
			
def moonstone(quantity=1, indent=0):
	build_tree("Moonstone", quantity, indent)
			
def bloodstone_ore(quantity=1, indent=0):
	build_tree("Bloodstone Ore", quantity, indent)
			
def amethyst(quantity=1, indent=0):
	build_tree("Amethyst", quantity, indent)
			
def kaolinite(quantity=1, indent=0):
	build_tree("Kaolinite", quantity, indent)
			
def flame_pearl(quantity=1, indent=0):
	build_tree("Flame Pearl", quantity, indent)
			
def basalt(quantity=1, indent=0):
	build_tree("Basalt", quantity, indent)
			
def adamantite_ore(quantity=1, indent=0):
	build_tree("Adamantite Ore", quantity, indent)
				
def clear_opal(quantity=1, indent=0):
	build_tree("Clear Opal", quantity, indent)
				
def sun_opal(quantity=1, indent=0):
	build_tree("Sun Opal", quantity, indent)
				
def earthen_clay(quantity=1, indent=0):
	build_tree("Earthen Clay", quantity, indent)

""" MINING END
"""
	
def hard_clay_mixture(quantity=1,indent=0):
	build_tree("Hard Clay Mixture",quantity,indent)
	indent += 1
	shale_rock(quantity*10,indent)
	hard_clay(quantity*6,indent)

def hard_clay(quantity=1,indent=0):
	build_tree("Hard Clay",quantity,indent)

def iron_powder(quantity=1,indent=0):
	build_tree("Iron Powder",quantity,indent)
	indent += 1
	shale_rock(ceil(quantity/3.0),indent)
	iron_ore(ceil(quantity/3.0),indent)

def kingsflower_buff_superior(quantity=1,indent=0):
	build_tree("Kingsflower Buff (Superior+)",quantity,indent)
	indent += 1
	angelflower(quantity*2,indent)
	kingsbloom_oil(quantity*3,indent)

def silver_maple_handle(quantity=1,indent=0):
	build_tree("Silver Maple Handle",quantity,indent)
	indent += 1
	silver_maple(quantity*5,indent)

def silver_maple(quantity=1,indent=0):
	build_tree("Silver Maple",quantity,indent)

def wild_cherry_handle(quantity=1,indent=0):
	build_tree("Wild Cherry Handle",quantity,indent)
	indent += 1
	wild_cherry(quantity*2,indent)

def wild_cherry(quantity=1,indent=0):
	build_tree("Wild Cherry",quantity,indent)

def cotton(quantity=1,indent=0):
	build_tree("Cotton",quantity,indent)

def cotton_yarn(quantity=1,indent=0):
	build_tree("Cotton Yarn",quantity,indent)
	indent += 1
	cotton(quantity*5,indent)

def grilled_shrimp(quantity=1,indent=0):
	build_tree("Grilled Shrimp",quantity,indent)
	indent += 1
	shrimp(quantity*2,indent)

def shrimp(quantity=1,indent=0):
	build_tree("Shrimp",quantity,indent)

def common_random_enchant(quantity=1,indent=0):
	build_tree("Common Random Enchant",quantity,indent)
	indent += 1
	simple_dust(quantity*4,indent)

def superior_feet_enchant(quantity=1,indent=0):
	build_tree("Superior Feet Enchant",quantity,indent)
	indent += 1
	simple_dust(quantity*2,indent)
	arcane_powder(quantity,indent)

def random_superior_enchant(quantity=1,indent=0):
	build_tree("?",quantity,indent)
	indent += 1
	simple_dust(quantity*3,indent)
	arcane_powder(quantity*3,indent)

def kingsbloom_curse_superior(quantity=1,indent=0):
	build_tree("Kingsbloom Curse (Superior+)",quantity,indent)
	indent += 1
	egg(quantity,indent)
	kingsbloom_oil(quantity*5,indent)

def angel_dragon_toxin(quantity=1,indent=0):
	build_tree("Angel Dragon Toxin",quantity,indent)
	indent += 1
	shadow_essence(quantity,indent)
	dragontear_oil(quantity,indent)
	angelflower_oil(quantity*3,indent)

def shadow_essence(quantity=1,indent=0):
	build_tree("Shadow Essence",quantity,indent)

def angelflower_oil(quantity=1,indent=0):
	build_tree("Angelflower Oil",quantity,indent)
	indent += 1
	angelflower(quantity*5,indent)

def kingsbloom_oil(quantity=1,indent=0):
	build_tree("Kingsbloom Oil",quantity,indent)
	indent += 1
	kingsbloom(quantity*5,indent)

def iridium_ore(quantity=1,indent=0):
	build_tree("Iridium Ore",quantity,indent)

def quartz(quantity=1,indent=0):
	build_tree("Quartz",quantity,indent)

def iridium_bar(quantity=1,indent=0):
	build_tree("Iridium Bar",quantity,indent)
	indent += 1
	iridium_ore(quantity,indent)
	quartz(quantity*2,indent)

def iridium_nail(quantity=1,indent=0):
	build_tree("Iridium Nail",quantity,indent)
	indent += 1
	iridium_bar(ceil(quantity/15.0),indent)

def small_hemlock_building(quantity=1,indent=0):
	build_tree("Small Hemlock Building",quantity,indent)
	indent += 1
	hemlock_wall(quantity*4,indent)
	hemlock_roof(quantity,indent)
	hemlock_lumber(quantity*30,indent)
	iridium_nail(quantity*90,indent)

def hemlock_roof(quantity=1,indent=0):
	build_tree("Hemlock Roof",quantity,indent)
	indent += 1
	hemlock_lumber(quantity*100,indent)
	iridium_nail(quantity*220,indent)
	hemlock_shingle(quantity*340,indent)

def hemlock_shingle(quantity=1,indent=0):
	build_tree("Hemlock Shingle",quantity,indent)
	indent += 1
	hemlock(ceil(quantity/5.0),indent)

def hemlock_wall(quantity=1,indent=0):
	build_tree("Hemlock Wall",quantity,indent)
	indent += 1
	hemlock_lumber(quantity*100,indent)
	iridium_nail(quantity*180,indent)

def hemlock_lumber(quantity=1,indent=0):
	build_tree("Hemlock Lumber",quantity,indent)
	indent += 1
	hemlock(quantity,indent)

def hemlock(quantity=1,indent=0):
	build_tree("Hemlock",quantity,indent)

def copper_band(quantity=1,indent=0):
	build_tree("Copper Band",quantity,indent)
	indent += 1
	copper_powder(quantity*4,indent)
	pure_copper(quantity*2,indent)

def copper_powder(quantity=1,indent=0):
	build_tree("Copper Powder",quantity,indent)
	indent += 1
	copper_ore(ceil(quantity/3.0),indent)
	stone(ceil(quantity/3.0),indent)

def copper_bar(quantity=1,indent=0):
	build_tree("Copper Bar",quantity,indent)
	indent += 1
	copper_ore(quantity,indent)
	stone(quantity,indent)

def pure_copper(quantity=1,indent=0):
	build_tree("Pure Copper",quantity,indent)
	indent += 1
	copper_bar(8*quantity,indent)

def copper_ore(quantity=1,indent=0):
	build_tree("Copper Ore",quantity,indent)

def stone(quantity=1,indent=0):
	build_tree("Stone",quantity,indent)

def hemlock_container(quantity=1,indent=0):
	build_tree("Hemlock Container",quantity,indent)
	indent += 1
	iridium_nail(quantity*60,indent)
	hemlock_lumber(quantity*12,indent)
	hemlock_wall(quantity*6,indent)

def aspen_lumber(quantity=1,indent=0):
	build_tree("Aspen Lumber",quantity,indent)
	indent += 1
	bigtooth_aspen(quantity,indent)

def bigtooth_aspen(quantity=1,indent=0):
	build_tree("Bigtooth Aspen",quantity,indent)

def chromium_ore(quantity=1,indent=0):
	build_tree("Chromium Ore",quantity,indent)

def marble(quantity=1,indent=0):
	build_tree("Marble",quantity,indent)

def chromium_bar(quantity=1,indent=0):
	build_tree("Chromium Bar",quantity,indent)
	indent += 1
	chromium_ore(quantity,indent)
	marble(quantity*2,indent)

def chromium_nail(quantity=1,indent=0):
	build_tree("Chromium Nail",quantity,indent)
	indent += 1
	chromium_bar(ceil(quantity/15.0),indent)

def pine_lumber(quantity=1,indent=0):
	build_tree("Pine Lumber",quantity,indent)
	indent += 1
	white_pine(quantity,indent)

def white_pine(quantity=1,indent=0):
	build_tree("White Pine",quantity,indent)

def milkweed_line(quantity=1,indent=0):
	build_tree("Milkweed Line",quantity,indent)
	indent += 1
	milkweed(quantity*3,indent)

def milkweed(quantity=1,indent=0):
	build_tree("Milkweed",quantity,indent)

def smooth_birch_rod(quantity=1,indent=0):
	build_tree("Smooth Birch Rod",quantity,indent)
	indent += 1
	rough_birch_rod(quantity*2,indent)
	horsetail_sandpaper(quantity,indent)

def rough_birch_rod(quantity=1,indent=0):
	build_tree("Rough Birch Rod",quantity,indent)
	indent += 1
	light_birch(quantity*6,indent)

def light_birch(quantity=1,indent=0):
	build_tree("Light Birch",quantity,indent)

def horsetail_sandpaper(quantity=1,indent=0):
	build_tree("Horsetail Sandpaper",quantity,indent)
	indent += 1
	horsetail(ceil(quantity/3.0),indent)

def horsetail(quantity=1,indent=0):
	build_tree("Horsetail",quantity,indent)

def medium_pine_wall(quantity=1,indent=0):
	build_tree("Medium Pine Wall] x %d",quantity,indent)
	indent += 1
	aspen_lumber(quantity*35,indent)
	chromium_nail(quantity*200,indent)
	pine_lumber(quantity*50,indent)

def pine_container_wall(quantity=1,indent=0):
	build_tree("Pine Container Wall",quantity,indent)
	indent += 1
	chromium_nail(quantity*160,indent)
	pine_lumber(quantity*65,indent)

def pine_guild_container(quantity=1,indent=0):
	build_tree("Pine Guild Container",quantity,indent)
	indent += 1
	aspen_lumber(quantity*16,indent)
	chromium_nail(quantity*40,indent)
	medium_pine_wall(quantity*2,indent)
	pine_container_wall(quantity*4,indent)

def iron_nail(quantity=1,indent=0):
	build_tree("Iron Nail",quantity,indent)
	indent += 1
	iron_bar(ceil(quantity/15.0),indent)

def iron_bar(quantity=1,indent=0):
	build_tree("Iron Bar",quantity,indent)
	indent += 1
	iron_ore(quantity,indent)
	shale_rock(quantity,indent)

def iron_ore(quantity=1,indent=0):
	build_tree("Iron Ore",quantity,indent)

def shale_rock(quantity=1,indent=0):
	build_tree("Shale Rock",quantity,indent)

def pine_shingle(quantity=1,indent=0):
	build_tree("Pine Shingle",quantity,indent)
	indent += 1
	white_pine(ceil(quantity/5.0),indent)

def pine_guild_roof(quantity=1,indent=0):
	build_tree("Pine Guild Roof",quantity,indent)
	indent += 1
	black_ash(quantity*10,indent)
	iron_nail(quantity*1500,indent)
	limestone(quantity*220,indent)
	pine_shingle(quantity*1250,indent)

def black_ash(quantity=1,indent=0):
	build_tree("Black Ash",quantity,indent)

def limestone(quantity=1,indent=0):
	build_tree("Limestone",quantity,indent)

def pine_guild_wall(quantity=1,indent=0):
	build_tree("Pine Guild Wall",quantity,indent)
	indent += 1
	iron_nail(quantity*900,indent)
	limestone(quantity*120,indent)
	pine_lumber(quantity*250,indent)

def base_guild_wing_pine(quantity=1,indent=0):
	build_tree("Base Guild Wing (Pine)",quantity,indent)
	indent += 1
	aspen_lumber(quantity*14,indent)
	iron_nail(quantity*80,indent)
	pine_guild_roof(quantity,indent)
	pine_guild_wall(quantity*3,indent)

def pine_building_roof(quantity=1,indent=0):
	build_tree("Pine Building Roof",quantity,indent)
	indent += 1
	pine_lumber(quantity*60,indent)
	chromium_nail(quantity*200,indent)
	pine_shingle(quantity*300,indent)

def vendor_room(quantity=1,indent=0):
	build_tree("Vendor Room",quantity,indent)
	indent += 1
	iron_nail(quantity*100,indent)
	aspen_lumber(quantity*25,indent)
	pine_building_roof(quantity,indent)
	medium_pine_wall(quantity*3,indent)

def pine_building_wall(quantity=1,indent=0):
	build_tree("Pine Building Wall",quantity,indent)
	indent += 1
	chromium_nail(quantity*160,indent)
	pine_lumber(quantity*75,indent)

def polished_small_gem(quantity=1,indent=0):
	build_tree("Polished Small Gem",quantity,indent)
	indent += 1
	small_gem(quantity,indent)
	copper_powder(quantity*2,indent)

def small_gem(quantity=1,indent=0):
	build_tree("Small Gem",quantity,indent)

def polished_large_gem(quantity=1,indent=0):
	build_tree("Polished Large Gem",quantity,indent)
	indent += 1
	large_gem(quantity,indent)
	copper_powder(quantity*6,indent)

def large_gem(quantity=1,indent=0):
	build_tree("Large Gem",quantity,indent)
	indent += 1
	stone(quantity,indent)
	small_gem(quantity*3,indent)

def polished_large_agate(quantity=1,indent=0):
	build_tree("Polished Large Agate",quantity,indent)
	indent += 1
	copper_powder(quantity*6,indent)
	large_agate(quantity,indent)

def large_agate(quantity=1,indent=0):
	build_tree("Large Agate",quantity,indent)
	indent += 1
	stone(quantity*1,indent)
	agate(quantity*3,indent)

def agate(quantity=1,indent=0):
	build_tree("Agate",quantity,indent)

def enchanting_study(quantity=1,indent=0):
	build_tree("Enchanting Study",quantity,indent)
	indent += 1
	ancient_essence(quantity*16,indent)
	iron_nail(quantity*90,indent)
	aspen_lumber(quantity*35,indent)
	pine_building_wall(quantity,indent)
	pine_building_roof(quantity,indent)
	medium_pine_wall(quantity*2,indent)

def ancient_essence(quantity=1,indent=0):
	build_tree("Ancient Essence",quantity,indent)

def inscription_library(quantity=1,indent=0):
	build_tree("Inscription Library",quantity,indent)
	indent += 1
	iron_nail(quantity*90,indent)
	ancient_book(quantity*10,indent)
	archaic_rune(quantity*10,indent)
	aspen_lumber(quantity*35,indent)
	pine_building_wall(quantity,indent)
	pine_building_roof(quantity,indent)
	medium_pine_wall(quantity*2,indent)

def ancient_book(quantity=1,indent=0):
	build_tree("Ancient Book",quantity,indent)

def archaic_rune(quantity=1,indent=0):
	build_tree("Archaic Rune",quantity,indent)

def reinforced_pine_wall(quantity=1,indent=0):
	build_tree("Reinforced Pine Wall",quantity,indent)
	indent += 1
	limestone(quantity*160,indent)
	black_ash(quantity,indent)
	iron_nail(quantity*300,indent)
	pine_lumber(quantity*160,indent)

def alchemy_lab(quantity=1,indent=0):
	build_tree("Alchemy Lab",quantity,indent)
	indent += 1
	ancientbloom(quantity*20,indent)
	iron_nail(quantity*90,indent)
	aspen_lumber(quantity*30,indent)
	pine_building_wall(quantity,indent)
	pine_building_roof(quantity,indent)
	medium_pine_wall(quantity*2,indent)

def ancientbloom(quantity=1,indent=0):
	build_tree("Ancientbloom",quantity,indent)

def workshop(quantity=1,indent=0):
	build_tree("Workshop",quantity,indent)
	indent += 1
	black_ash(quantity*10,indent)
	iron_nail(quantity*100,indent)
	aspen_lumber(quantity*10,indent)
	pine_building_roof(quantity,indent)
	reinforced_pine_wall(quantity*3,indent)

def blacksmith(quantity=1,indent=0):
	build_tree("Blacksmith",quantity,indent)
	indent += 1
	golemite_ore(quantity*10,indent)
	iron_nail(quantity*100,indent)
	aspen_lumber(quantity*10,indent)
	pine_building_roof(quantity,indent)
	reinforced_pine_wall(quantity*3,indent)

def golemite_ore(quantity=1,indent=0):
	build_tree("Golemite Ore",quantity,indent)

def cedar_lumber(quantity=1,indent=0):
	build_tree("Cedar Lumber",quantity,indent)
	indent += 1
	red_cedar(ceil(quantity/2.0),indent)

def red_cedar(quantity=1,indent=0):
	build_tree("Red Cedar",quantity,indent)

def black_spruce_lumber(quantity=1,indent=0):
	build_tree("Black Spruce Lumber",quantity,indent)
	indent += 1
	black_spruce(ceil(quantity/2.0),indent)

def black_spruce(quantity=1,indent=0):
	build_tree("Black Spruce",quantity,indent)

def medium_cedar_wall(quantity=1,indent=0):
	build_tree("Medium Cedar Wall",quantity,indent)
	indent += 1
	iron_nail(quantity*180,indent)
	black_spruce_lumber(quantity*24,indent)
	cedar_lumber(quantity130,indent)

def medium_cedar_container(quantity=1,indent=0):
	build_tree("Medium Cedar Container",quantity,indent)
	indent += 1
	iron_nail(quantity*60,indent)
	cedar_lumber(quantity*24,indent)
	medium_cedar_wall(quantity*6,indent)

def guild_hall_bank(quantity=1,indent=0):
	build_tree("Guild Hall Bank",quantity,indent)
	indent += 1
	iron_nail(quantity*100,indent)
	medium_cedar_container(quantity*4,indent)
	aspen_lumber(quantity*14,indent)
	pine_building_roof(quantity,indent)
	reinforced_pine_wall(quantity*3,indent)

def huge_gem(quantity=1,indent=0):
	build_tree("Huge Gem",quantity,indent)
	indent += 1
	large_gem(quantity*3,indent)
	stone(quantity*6,indent)

def copper_ring_common(quantity=1,indent=0):
	build_tree("Copper Ring (Common+)",quantity,indent)
	indent += 1
	huge_gem(quantity,indent)
	copper_band(quantity,indent)

def tin_bar(quantity=1,indent=0):
	build_tree("Tin Bar",quantity,indent)
	indent += 1
	sandstone(quantity,indent)
	tin_ore(quantity,indent)

def sandstone(quantity=1,indent=0):
	build_tree("Sandstone",quantity,indent)

def tin_ore(quantity=1,indent=0):
	build_tree("Tin Ore]x%d",quantity,indent)

def thick_iron_bar(quantity=1,indent=0):
	build_tree("Thick Iron Bar",quantity,indent)
	indent += 1
	shale_rock(quantity*5,indent)
	iron_bar(quantity*5,indent)

def golemite_bar(quantity=1,indent=0):
	build_tree("Golemite Bar",quantity,indent)
	indent += 1
	copper_bar(quantity*2,indent)
	golemite_ore(quantity*3,indent)
	tin_bar(quantity*4,indent)
	iron_bar(quantity*4,indent)

def cast_iron_pot(quantity=1,indent=0):
	build_tree("Cast Iron Pot",quantity,indent)
	indent += 1
	thick_iron_bar(quantity*10,indent)
	golemite_bar(quantity*2,indent)

def birch_lumber(quantity=1,indent=0):
	build_tree("Birch Lumber",quantity,indent)
	indent += 1
	light_birch(ceil(quantity/2.0),indent)

def copper_nail(quantity=1,indent=0):
	build_tree("Copper Nail",quantity,indent)
	indent += 1
	copper_bar(ceil(quantity/15.0),indent)

def birch_container_wall(quantity=1,indent=0):
	build_tree("Birch Container Wall",quantity,indent)
	indent += 1
	birch_lumber(quantity*60,indent)
	copper_nail(quantity*200,indent)

def small_birch_container(quantity=1,indent=0):
	build_tree("Small Birch Container",quantity,indent)
	indent += 1
	birch_container_wall(quantity*6,indent)
	birch_lumber(quantity*16,indent)
	copper_nail(quantity*30,indent)

def cooking_hall(quantity=1,indent=0):
	build_tree("Cooking Hall",quantity,indent)
	indent += 1
	iron_nail(quantity*60,indent)
	aspen_lumber(quantity*30,indent)
	pine_building_wall(quantity,indent)
	pine_building_roof(quantity,indent)
	medium_pine_wall(quantity*2,indent)
	cast_iron_pot(quantity*4,indent)

def large_citrine(quantity=1,indent=0):
	build_tree("Large Citrine",quantity,indent)
	indent += 1
	shale_rock(quantity*2,indent)
	citrine(quantity*3,indent)

def citrine(quantity=1,indent=0):
	build_tree("Citrine",quantity,indent)

def huge_citrine(quantity=1,indent=0):
	build_tree("Huge Citrine",quantity,indent)
	indent += 1
	shale_rock(quantity*6,indent)
	large_citrine(quantity*3,indent)

def huge_malachite(quantity=1,indent=0):
	build_tree("Huge Malachite",quantity,indent)
	indent += 1
	slate(quantity*6,indent)
	large_malachite(quantity*3,indent)

def large_malachite(quantity=1,indent=0):
	build_tree("Large Malachite",quantity,indent)
	indent += 1
	slate(quantity*2,indent)
	malachite(quantity*3,indent)

def malachite(quantity=1,indent=0):
	build_tree("Malachite",quantity,indent)

def slate(quantity=1,indent=0):
	build_tree("Slate",quantity,indent)

def jewelry_room(quantity=1,indent=0):
	build_tree("Jewelry Room",quantity,indent)
	indent += 1
	iron_nail(quantity*100,indent)
	huge_citrine(quantity*3,indent)
	huge_malachite(quantity*5,indent)
	aspen_lumber(quantity*10,indent)
	pine_building_wall(quantity,indent)
	pine_building_roof(quantity,indent)
	reinforced_pine_wall(quantity*2,indent)

def party_cake(quantity=1,indent=0):
	build_tree("Party Cake",quantity,indent)
	indent += 1
	rosemary(quantity*50,indent)
	salt(quantity*12,indent)
	honey(quantity*15,indent)
	flax(quantity*25,indent)

def rosemary(quantity=1,indent=0):
	build_tree("Rosemary",quantity,indent)

def salt(quantity=1,indent=0):
	build_tree("Salt",quantity,indent)

def honey(quantity=1,indent=0):
	build_tree("Honey",quantity,indent)

def flax(quantity=1,indent=0):
	build_tree("Flax",quantity,indent)

def basic_book(quantity=1,indent=0):
	build_tree("Basic Book",quantity,indent)
	indent += 1
	midnight_ink(quantity*3,indent)
	basic_chapter(quantity*5,indent)

def midnight_ink(quantity=1,indent=0):
	build_tree("Midnight Ink",quantity,indent)
	indent += 1
	midnight_berry(ceil((quantity*3)/4.0),indent)
	squid(ceil(quantity/4.0),indent)
	egg(ceil((quantity*2)/4.0),indent)
	honey(ceil(quantity/4.0),indent)

def basic_chapter(quantity=1,indent=0):
	build_tree("Basic Chapter",quantity,indent)
	indent += 1
	basic_writings(quantity*7,indent)
	midnight_ink(quantity*2,indent)

def midnight_berry(quantity=1,indent=0):
	build_tree("Midnight Berry",quantity,indent)

def squid(quantity=1,indent=0):
	build_tree("Squid",quantity,indent)

def egg(quantity=1,indent=0):
	build_tree("Egg",quantity,indent)

def basic_writings(quantity=1,indent=0):
	build_tree("Basic Writings",quantity,indent)

def basic_reference_book(quantity=1,indent=0):
	build_tree("Basic Reference Book",quantity,indent)
	indent += 1
	midnight_ink(quantity*2,indent)
	basic_book(quantity,indent)
	basic_reference(quantity*6,indent)

def basic_reference(quantity=1,indent=0):
	build_tree("Basic Reference",quantity,indent)

def basic_formation(quantity=1,indent=0):
	build_tree("Basic Formation",quantity,indent)
	indent += 1
	basic_rune(quantity*3,indent)
	minor_etching(quantity*5,indent)

def basic_rune(quantity=1,indent=0):
	build_tree("Basic Rune",quantity,indent)

def minor_etching(quantity=1,indent=0):
	build_tree("Minor Etching",quantity,indent)

def basic_markings(quantity=1,indent=0):
	build_tree("Basic Markings",quantity,indent)
	indent += 1
	superb_etching(quantity,indent)
	basic_formation(quantity,indent)

def superb_etching(quantity=1,indent=0):
	build_tree("Superb Etching",quantity,indent)

def rough_parchment(quantity=1,indent=0):
	build_tree("Rough Parchment",quantity,indent)
	indent += 1
	basic_parchment(quantity*3,indent)

def basic_parchment(quantity=1,indent=0):
	build_tree("Basic Parchment",quantity,indent)

def common_weapon_enchant(quantity=1,indent=0):
	build_tree("Common Weapon Enchant",quantity,indent)
	indent += 1
	simple_dust(quantity*4,indent)

def simple_dust(quantity=1,indent=0):
	build_tree("Simple Dust",quantity,indent)

def weapon_enchant_rare(quantity=1,indent=0):
	build_tree("Weapon Enchant (Rare+)",quantity,indent)
	indent += 1
	arcane_powder(quantity*4,indent)
	mystic_essence(quantity*4,indent)

def arcane_powder(quantity=1,indent=0):
	build_tree("Arcane Powder",quantity,indent)

def mystic_essence(quantity=1,indent=0):
	build_tree("Mystic Essence",quantity,indent)

def dragontear_oil(quantity=1,indent=0):
	build_tree("Dragontear Oil",quantity,indent)
	indent += 1
	dragontear(quantity*4,indent)

def dragontear(quantity=1,indent=0):
	build_tree("Dragontear",quantity,indent)

def ancientbloom_oil(quantity=1,indent=0):
	build_tree("Ancientbloom Oil",quantity,indent)
	indent += 1
	ancientbloom(quantity*4,indent)

def kingsbloom(quantity=1,indent=0):
	build_tree("Kingsbloom",quantity,indent)

def angelflower(quantity=1,indent=0):
	build_tree("Angelflower",quantity,indent)
