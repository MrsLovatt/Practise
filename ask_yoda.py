from easygui import *
import random

yoda_answers = ["Train yourself to let go of everything of everything you fear to lose", "You must unlearn what you have learned", "Difficult to see. Always in motion is the future...", "Through the Force, things you will see", "Always pass on what you ahve learned", "Looking? Found someone you have, eh?", "Yes, a Jedi's strength flows from the Force. But be aware of the dark side.", "You will find only what you bring in.", "Patience you must have my young Padawan.", "Do or do not. There is not try."]#creates a list
yoda = random.choice(yoda_answers)#randomly choses from the list ' yoda_answers'
enterbox("Question:n\What should I do today?n\n\Yoda says:n\" + yoda )
         
