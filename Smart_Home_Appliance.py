class appliances:
    def status(self):
        print("Appliance is working fine.")

class fan(appliances):
    def status(self):
        print("fan is working fine")

class light(appliances):
    def status(self):
        print("light is working fine")

class AC(appliances):
    def status(self):
        print("AC is working fine")

fan = fan()
light= light()
AC = AC()

devices= [fan, light, AC]

for device in devices:
    device.status()