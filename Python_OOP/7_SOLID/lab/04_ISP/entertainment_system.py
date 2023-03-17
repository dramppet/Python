class Powerable:
    def plug_in_power(self):
        ...

class RCAConnectCable:
    def connect_by_device_via_rca_cable(self):
        ...

class HDMIConnectedCable:
    def connect_by_device_via_hdmi_cable(self):
        ...

class EthernetConnectedCable:
    def connect_by_device_via_ethernet_cable(self):
        ...


class Television(HDMIConnectedCable, RCAConnectCable, Powerable):
    def connect_to_dvd(self, dvd_player):
        self.connect_by_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_by_device_via_hdmi_cable(game_console)


class DVDPlayer(HDMIConnectedCable, Powerable):
    def connect_to_tv(self, television):
        self.connect_by_device_via_hdmi_cable(television)


class GameConsole(HDMIConnectedCable, EthernetConnectedCable, Powerable):
    def connect_to_tv(self, television):
        self.connect_by_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_by_device_via_ethernet_cable(router)


class Router(EthernetConnectedCable, Powerable):
    def connect_to_tv(self, television):
        self.connect_by_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_by_device_via_ethernet_cable(game_console)
