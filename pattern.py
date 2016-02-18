#fixme: what to do re recipe names used more than once?
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

def extract_dragontear_oil(quantity=1,indent=0):
	build_tree("Extract Dragontear Oil",quantity,indent)
	indent += 1
	dragontear(quantity*4,indent)

def dragontear(quantity=1,indent=0):
	build_tree("Dragontear",quantity,indent)

def ancientbloom_oil(quantity=1,indent=0):
	build_tree("Ancientbloom Oil",quantity,indent)
	indent += 1
	ancientbloom(quantity*4,indent)

def extract_kingsbloom_oil(quantity=1,indent=0):
	build_tree("Extract Kingsbloom Oil",quantity,indent)
	indent += 1
	kingsbloom(quantity*5,indent)

def kingsbloom(quantity=1,indent=0):
	build_tree("Kingsbloom",quantity,indent)

def extract_angelflower_oil(quantity=1,indent=0):
	build_tree("Extract Angelflower Oil",quantity,indent)
	indent += 1
	angelflower(quantity*5,indent)

def angelflower(quantity=1,indent=0):
	build_tree("Angelflower",quantity,indent)
