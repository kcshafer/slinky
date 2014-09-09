import ConfigParser

def build_credentials(username, password, production):
    cp = ConfigParser.ConfigParser()
    f = open('auth.ini', 'w')
    
    cp.add_section('credentials')
    cp.set('credentials', 'username', username)
    cp.set('credentials', 'password', password)
    cp.set('credentials', 'production', production)

    cp.write(f)
    f.close()

def retrieve_credentials():
    cp = ConfigParser.ConfigParser()
    cp.read('auth.ini')
    c = 'credentials'
    u = 'username'
    p = 'password'
    r = 'production'
    return cp.get(c, u), cp.get(c, p), cp.get(c, r)