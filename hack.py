class Hack:
    def __init__(self, path_to_file):
        values = {}

        with open(path_to_file, "r") as f:
            for line in f.readlines():
                s_line = line.split()
                values[s_line[0]] = s_line[2]

        self._validate(values)

        self.host = values["host"]
        self.ip = values["ip"]
        self.port = int(values["port"])
        self.password = int(values["password"])


    def _validate(self, raw):
        self.validate_host(raw["host"])
        self.validate_ip(raw["ip"])
        self.validate_port(raw["port"])
        self.validate_password(raw["password"])

    def validate_host(self, host):
        for num in host.split("."):
            if int(num) < 0 or int(num) > 255:
                raise Exception("Invalid HOST")

    def validate_ip(self, ip):
        for num in ip.split("."):
            if int(num) < 0 or int(num) > 255:
                raise Exception("Invalid IP")

    def validate_port(self, port):
        if int(port) < 1024 or int(port) > 9999:
            raise Exception("Invalid PORT")

    def validate_password(self, password):
        try:
            int(password)
        except:
            raise Exception("Invalid PASSWORD")

    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, host):
        self.validate_host(host)
        self.__host = host

    @property
    def ip(self):
        return self.__ip

    @ip.setter
    def ip(self, ip):
        self.validate_ip(ip)
        self.__ip = ip

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        self.validate_port(port)
        self.__port = port

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.validate_password(password)
        self.__password = password

hack = Hack('data.txt')
hack.host = '192.1.1.0'
print(hack.host)
hack.ip = '192.2.0.2'
print(hack.ip)
hack.port = '7777'
print(hack.port)
hack.password = '12131415'
print(hack.password)