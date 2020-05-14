from sportsreference.ncaaf.roster import Player

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

#Create each player based on the player class through each Player's player_id
TLawrence = Player('trevor-lawrence-1')
JFields = Player('justin-fields-2')
SEhlinger = Player('sam-ehlinger-1')
SHowell = Player('sam-howell-1')
JDaniels = Player('jayden-daniels-1')

#Set the previous season (This can be adjusted to current season while in mid season)
TLawrence('2019')
JFields('2019')
SEhlinger('2019')
SHowell('2019')
JDaniels('2019')

#Calculate the players touchdown efficiency rate
TLawTDperPA = float(TLawrence.passing_touchdowns)/float(TLawrence.attempted_passes)
JFieTDperPA = float(JFields.passing_touchdowns)/float(JFields.attempted_passes)
SEhlTDperPA = float(SEhlinger.passing_touchdowns)/float(SEhlinger.attempted_passes)
SHowTDperPA = float(SHowell.passing_touchdowns)/float(SHowell.attempted_passes)
JDanTDperPA = float(JDaniels.passing_touchdowns)/float(JDaniels.attempted_passes)


#Display the Players and their stats
print ("Player Name| Touchdowns | Pass attempts | Touchdown per Pass attempt")
print(TLawrence.name, TLawrence.passing_touchdowns, TLawrence.attempted_passes, "{:10.4f}".format(TLawTDperPA))
print(JFields.name, JFields.passing_touchdowns, JFields.attempted_passes, "{:10.4f}".format(JFieTDperPA))
print(SEhlinger.name, SEhlinger.passing_touchdowns, SEhlinger.attempted_passes, "{:10.4f}".format(SEhlTDperPA))
print(SHowell.name, SHowell.passing_touchdowns, SHowell.attempted_passes, "{:10.4f}".format(SHowTDperPA))
print(JDaniels.name, JDaniels.passing_touchdowns, JDaniels.attempted_passes, "{:10.4f}".format(JDanTDperPA))

#Plot some of the Quarterbacks' data (In this case, the touchdown efficiency rate)
objects = (TLawrence.name, JFields.name, SEhlinger.name, SHowell.name, JDaniels.name)
y_pos = np.arange(len(objects))
performance = [TLawTDperPA,JFieTDperPA,SEhlTDperPA,SHowTDperPA,JDanTDperPA]

plt.bar(y_pos, performance, width=0.8, align='center', alpha=1)
plt.xticks(y_pos, objects)
plt.ylabel('Touchdowns per Pass Attempt')
plt.title('My NCAA Quarterbacks')

plt.show()




