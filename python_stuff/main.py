import time
import textwrap
import random
from datetime import date
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

disp.fill(0)
disp.show()

width = disp.width
height = disp.height
image = Image.new("1", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

cake = Image.open("birthday.ppm").convert("1")

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = 0
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
font = ImageFont.load_default()
# font = ImageFont.truetype('AncientModernTales-a7Po.ttf', 20)

wrapper = textwrap.TextWrapper(width=20)


l = [
    "Star Trek Fact: Shari Lewis of Lamb Chop wrote a TOS episode",
    "Star Trek Fact: Mick Fleetwood played a fish alien in TNG and had to do 19 takes to say one line: 'Food'",
    "Star Trek Fact: Iggy Pop plays an alien Vorta named Yelgrun in DS9",
    "Star Trek Fact: Tribbles were originally going to be teddy bears",
    "Star Trek Fact: PADDs were inspired by Apple Newton",
    "Star Trek Fact: The Vulcan salute is inspired by a Jewish blessing",
    "Star Trek Fact: Star Trek was almost named Wagon to the Stars",
    "Star Trek Fact: Beam me up Scotty was never actually said",
    "Star Trek Fact: The Star Trek universe is home to over 800 alien species",
    "Star Trek Fact: The opening sequence of Star Trek: Deep Space Nine was inspired by the opening sequence for the film Blade Runner",
    "Star Trek Fact: The Bord was originally going to be called the Cyborg collective",
    "Star Trek Fact: Captain Jean-Luc Picard was originally going to be named Captain Erik Hanson",
    "Star Trek Fact: The transporter beam sound was created by rubbing an inflated balloon",
    "Star Trek Fact: The original Star Trek was filmed in black and white",
    "Star Trek Fact: The sound of the transporter beam was created by rubbing an inflated balloon against a microphone",
    "Star Trek Fact: Tribble fur made from hair clippings of Roddenberry's dog",
    "Star Trek Fact: Starfleet Academy never physically shown in any Star Trek shows or movies",
    "Star Trek Fact: Qo'noS, Klingon homeworld, named after real-life American Indian tribe",
    "Star Trek Fact: The replicator was inspired by an early computer program called COMIT",
    "Star Trek Fact: The PADDs (Personal Access Display Devices) were inspired by the Apple Newton",
    "Star Trek Fact: Data is Dr. Crusher's son's godfather in real life",
    "Star Trek Fact: There is an ATM in Quark's bar. It dispenses Federation credits, Bajoran litas, Cardassian leks, and Ferengi latinum",
    "Star Trek Fact: On TNG there is a series of conduits named GNDN, it stands for 'goes nowhere does nothing'",
    "Star Trek Fact: The DS9 episode 'The house of Quark' is the only Trek episode that features Gowron but not Worf",
    "Star Trek Fact: Morn was a tribute to Norm Peterson from Cheers. Morn is an anagram of Norm",
    "Star Trek Fact: At one point Star Trek accepted non-solicited (spec) scripts from anyone",
    "Star Trek Fact: Star Trek Picard used real life 3D printers as their replicator props",
    "Star Trek Fact: Rene Auberjonois (Odo) is related to Napoleon, a direct descendant of his younger sister",
    "Star Trek Fact: The Saurian Brandy prop is a bottle of George Dickel Tennessee Whisky from 1964",
    "Star Trek Fact: Some of James Doohan's ashes were smuggled aboard the Space Station and remain there to this day",
    "Star Trek Fact: The Mugatu was originally called the Gumatu",
    "Star Trek Fact: The entourage of the 14th Dalai Lama visited the TNG set",
    "Star Trek Fact: The original design for the Enterprise was upside down from the way we see it in the series",
    "Star Trek Fact: Gene Roddenberry wanted Troi to have three boobs",
    "Star Trek Fact: The math behind warp drive was worked out by Miguel Alcubierre in the mid 90s",
    "Star Trek Fact: The pronunciation of Data wasn't decided beforehand. It was left up to Patrick Stewart, since he was the first on camera to say the name (day-ta)",
    "Star Trek Fact: Dr. Richard Daystrom was also the star of Blackula and the King of Cartoons in Pee-wee",
    "Star Trek Fact: Odo was the french Chef in the Little Mermaid",
    "Star Trek Fact: Vulcan blood is green and so Leonard Nimoy's make up is a hand-mixed shade of green",
    "Star Trek Fact: The tankards used for Klingon bloodwine are actually measuring cups used in baking",
    "Star Trek Fact: There was friction between fans of Babylon 5 and DS9",
    "Star Trek Fact: Majel Barrett appearing on Babylon 5 as an alien prophetess",
    "Star Trek Fact: When Worf joined the cast, there was no intention from the start to have him engage in a relationship with Dax",
    "Star Trek Fact: The square glasses used in Quark's bar are actually candle holders turned upside down",
    "Star Trek Fact: DS9 is the only Star Trek television series not to have any human females as part of the main cast",
    "Star Trek Fact: Sisko's middle name is Lafayette",
    "Star Trek Fact: Mariska Hargitay (Law and Order: SVU) auditioned for the role of Jadzia Dax",
    "Star Trek Fact: Several paintings adorn the quarters of Sisko, Bashir, Dax and Kira. These were painted by Mark Allen Shepherd, who plays Morn, Quark's silent bar patron",
    "Star Trek Fact: DS9 takes place from 2369 to 2375",
    "Star Trek Fact: Geordi's visor was improvised on the first day of shooting, using chiefly a car air filter and a hair band",
    "Star Trek Fact: According to LeVar Burton, he would spend hours seated on the bridge set with little or no speaking, which would cause him to doze off",
    "Star Trek Fact: Patrick Stewart was so convinced that TNG would fail, that for the first 6 weeks of shooting he refused to unpack any of his suitcases",
    "Star Trek Fact: The Enterprise schematic has a mouse on a wheel in Engineering, seemingly powering the ship",
    "Star Trek Fact: Commander Data's storage capacity is 800 quadrillion bits or ~100,000 terabyte",
    "Star Trek Fact: The character of Geordi LaForge was originally conceived to be Jamaican. This plan was dropped, but Jamaican actress Madge Sinclair did appear as Geordi's mother",
]

e = [
    "Egg fact: The yolk and the whites have the same amount of protein",
    "Egg fact: Egg yolks naturally contain vitamin D because cholesterol is converted to Vit D when exposed to sunlight.",
    "Egg fact: Eggshells are made up of about 95% calcium carbonate (same material as chalk)",
    "Egg fact: Eggshells have about 17,000 pores which allow air to pass through to the embryo",
    "Egg fact: White-shelled eggs are laid by chickens with white earlobes, while brown-shelled eggs are laid by chickens with red earlobes.",
    "Egg fact: Eggs actually improve in flavor and texture as they age for a few days because carbon dioxide breaks down some of the proteins.",
    "Egg fact: Hard-boiled eggs spin easily, raw eggs wobble",
    "Egg fact: Eggs are a good source of choline",
    "Egg fact: Eggs can float in water due to the air pocket inside",
    "Egg fact: The yolk of an egg is one of the largest cells in the animal kingdom. The yolk is actually a single cell that is about 1/4 inch in diameter.",
    "Egg fact: Chickens that eat a lot of carotenoids will lay eggs with yolks that are a darker shade of yellow or orange.",
    "Egg fact: Cassowary egg shells are almost as hard as porcelain, and weigh almost 1.5lbs",
    "Egg fact: The average American eats about 290 eggs per year.",
    "Egg fact: The biggest chicken egg was 16oz, with a double yolk and double shell",
    "Egg fact: The most number of yolks in an egg was 9, reported by Diane Hainsworth of Hainsworth Poultry Farms, Mount Morris, New York",
    "Egg fact: Mohammed Muqbel (Yemen) created a stack of 4 eggs standing on end",
    "Egg fact: The most boiled eggs to be peeled and eaten in a minute is 6, achieved by Ashrita Furman (USA)",
    "Egg fact: The most eggs crushed by sitting in one minute is 72 eggs, achieved by Michaël Levillain (France)",
    "Egg fact: The most eggs crushed with a punch in one minute is 334 and was achieved by Ronald Sarchian (USA) in Tarzana, California",
    "Egg fact: Mohammed Muqbel balanced 888 eggs on his head, breaking his previous world record of 765 eggs.",
    "Egg fact: The world record hens egg toss (without breaking) was 323 ft.",
    "Egg fact: In 2017, Takeru Kobayashi from Japan devoured 126 hard-boiled eggs in just six minutes",
    "Egg fact: The extinct Madagascar elephant bird had eggs with 2.25 Gallon capacity",
    "Egg fact: The platypus is the world's first-known biofluorescent species of egg-laying mammal",
    "Egg fact: The greatest distance to carry an egg in one week (team) is 247.23 km (158.9 miles) achieved by St. Ewe Free Range Eggs South Team, in Cornwall, UK",
    "Egg fact: Eggs emitted from the oviduct before maturity are known as 'sports'",
    "Egg fact: The smallest egg laid by any bird is that of the vervain hummingbird",
    "Egg fact: The worlds largest egg scramble was 3,112 kg using 59,758 eggs, milk, onion, garlic and butter",
]
t = 10000  # initialized to large value to immediately branch
i = 0

delay = 5
# draw.bitmap([0, 0], cake, fill=255)
# d = date.today()
# if d.month==12 and d.day==3:
#     l.append('Happy birthday Jen')


def ds(s, coord):
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.multiline_text((x, coord), text=s, font=font, fill=255)
    disp.image(image)
    disp.show()


k = random.choice(l)
s = wrapper.fill(text=k)
nlines = s.count("\n")
while True:
    if t > (nlines + 3.5) * 10:
        t = 0
        k = random.choice(l)
        s = wrapper.fill(text=k)
        nlines = s.count("\n")
        ds(s, top - t)
        time.sleep(2)
    ds(s, top - t)
    time.sleep(0.1)
    t += 1
