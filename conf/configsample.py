
NICK = 'marjutest'
PASSWORD = 'marjupassword'
SERVER = "some.server.org"
PORT = 6667

OWNER_NICK="nick"
OWNER_PASS="pass"

GOOGLE_KEY = '?key=yourGoogleKeyHere'
GOOGLE_CX = '&cx=yourGoogleCxHere'

FML_KEY = 'yourFmlKeyHere'

marjutest = {}
marjutest["name"] = "#marjutest"
marjutest["folder"] = "marjutest"
marjutest["logging"] = True
marjutest["ai"] = True
marjutest["quoting"] = True
marjutest["seen"] = True

mingikanal = {}
mingikanal["name"] = "#minukanal"
mingikanal["folder"] = "minukanal"
mingikanal["logging"] = False
mingikanal["ai"] = True
mingikanal["quoting"] = True
mingikanal["seen"] = False

channels = {
    marjutest["name"]: marjutest,
    mingikanal["name"]: mingikanal,
}