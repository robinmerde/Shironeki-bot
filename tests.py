import random

next = random.randint(5400, 10080)
minutes, seconds = divmod(next, 60)
hours, minutes = divmod(minutes, 60)
print("Nouveau Tweet dans %d:%02d:%02d" % (hours, minutes, seconds))