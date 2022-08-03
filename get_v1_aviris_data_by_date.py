# import requests module
import requests

'''
For SHIFT data, for a singular date, there are multiple flight paths, all of which 
have files that are required to make a Zarr archive. For L1 files, we need the igm,
igm.hdr, rdn, & rdn.hdr files. For L2a files, we need rfl & rfl.hdr.
'''

def get_L1(flight_path, date):
    # Making a get request
    r = requests.get(igm_url, allow_redirects=True)
    open(f'{flight_path}_igm', 'wb').write(r.content)

    r = requests.get(igm_hdr_url, allow_redirects=True)
    open(f'{flight_path}_igm.hdr', 'wb').write(r.content)

    r = requests.get(rdn_url, allow_redirects=True)
    open(f'{flight_path}_rdn_v2aa1_clip', 'wb').write(r.content)

    r = requests.get(rdn_hdr_url, allow_redirects=True)
    open(f'{flight_path}_rdn_v2aa1_clip.hdr', 'wb').write(r.content)
    
def get_L2(flight_path, date):
    # Making a get request       
    r = requests.get(rfl_url, allow_redirects=True)
    open(f'{flight_path}_rfl', 'wb').write(r.content)

    r = requests.get(rfl_hdr_url, allow_redirects=True)
    open(f'{flight_path}_rfl.hdr', 'wb').write(r.content)

def get_all(flight_path, date):
    # Making a get request
    r = requests.get(igm_url, allow_redirects=True)
    open(f'{flight_path}_igm', 'wb').write(r.content)

    r = requests.get(igm_hdr_url, allow_redirects=True)
    open(f'{flight_path}_igm.hdr', 'wb').write(r.content)

    r = requests.get(rdn_url, allow_redirects=True)
    open(f'{flight_path}_rdn_v2aa1_clip', 'wb').write(r.content)

    r = requests.get(rdn_hdr_url, allow_redirects=True)
    open(f'{flight_path}_rdn_v2aa1_clip.hdr', 'wb').write(r.content)

    r = requests.get(rfl_url, allow_redirects=True)
    open(f'{flight_path}_rfl', 'wb').write(r.content)

    r = requests.get(rfl_hdr_url, allow_redirects=True)
    open(f'{flight_path}_rfl.hdr', 'wb').write(r.content)

date = input("Enter date of format YYYYMMDD: ")
flight_path = input("Enter flight path of format angYYYYMMDDtHHNNSS, or 'all' for all flight paths: ")
data = input("Downloading 'all' L1 and L2a data. Respond 'all' to: ")

igm_url = f"https://avng.jpl.nasa.gov/pub/SHIFT/v1/{date}/L1/igm/{flight_path}_igm"
rdn_url = f"https://avng.jpl.nasa.gov/pub/SHIFT/v1/{date}/L1/rdn/{flight_path}_rdn_v2aa1_clip"
rfl_url = f"https://avng.jpl.nasa.gov/pub/SHIFT/v1/{date}/L2a/{flight_path}_rfl"

igm_hdr_url = f"https://avng.jpl.nasa.gov/pub/SHIFT/v1/{date}/L1/igm/{flight_path}_igm.hdr"
rdn_hdr_url = f"https://avng.jpl.nasa.gov/pub/SHIFT/v1/{date}/L1/rdn/{flight_path}_rdn_v2aa1_clip.hdr"
rfl_hdr_url = f"https://avng.jpl.nasa.gov/pub/SHIFT/v1/{date}/L2a/{flight_path}_rfl.hdr"

data_20220224 = [
    'ang20220224t195402',
    'ang20220224t200332',
    'ang20220224t201928',
    'ang20220224t203333',
    'ang20220224t204803',
    'ang20220224t210144',
    'ang20220224t211618',
    'ang20220224t213004',
    'ang20220224t214423',
    'ang20220224t215759',
    'ang20220224t221356',
    'ang20220224t223027',
]
data_20220228 = [
'ang20220228t183924',
'ang20220228t185150',
'ang20220228t185720',
'ang20220228t190702',
'ang20220228t192104',
'ang20220228t193333',
'ang20220228t194708',
'ang20220228t195958',
'ang20220228t201833',
'ang20220228t202944',
'ang20220228t204228',
'ang20220228t205624',
'ang20220228t210940',
]
data_20220308 = [
    'ang20220308t183206',
    'ang20220308t184127',
    'ang20220308t185140',
    'ang20220308t190523',
    'ang20220308t191151',
    'ang20220308t192816',
    'ang20220308t194253',
    'ang20220308t195648',
    'ang20220308t201508',
    'ang20220308t202617',
    'ang20220308t204043',
    'ang20220308t205512',
    'ang20220308t211733',
    'ang20220308t213310',
    'ang20220308t214629'
]
data_20220316 = [
    'ang20220316t183443',
    'ang20220316t184402',
    'ang20220316t185139',
    'ang20220316t190239',
    'ang20220316t191705',
    'ang20220316t193240',
    'ang20220316t194717',
    'ang20220316t200240',
    'ang20220316t202123',
    'ang20220316t203318',
    'ang20220316t204811',
    'ang20220316t210303',
    'ang20220316t211819'
]
data_20220318 = [
    'ang20220318t193410',
    'ang20220318t194010',
]
data_20220322 = [
    'ang20220322t192924',
    'ang20220322t193854',
    'ang20220322t194447',
    'ang20220322t195241',
    'ang20220322t200335',
    'ang20220322t201228',
    'ang20220322t202643',
    'ang20220322t203801',
    'ang20220322t204749',
    'ang20220322t205950',
    'ang20220322t210856',
    'ang20220322t212712',
    'ang20220322t215548',
    'ang20220322t220619',
    'ang20220322t221256'
]
data_20220405 = [
    'ang20220405t185108',
    'ang20220405t190223',
    'ang20220405t191148',
    'ang20220405t193603',
    'ang20220405t192935',
    'ang20220405t194236',
    'ang20220405t195821',
    'ang20220405t201359',
    'ang20220405t202743',
    'ang20220405t204007',
    'ang20220405t205228',
    'ang20220405t210448',
    'ang20220405t211706',
    'ang20220405t212916',
    'ang20220405t214144',
    'ang20220405t215533',
]
data_20220412 = [
    'ang20220412t185410',
    'ang20220412t190510',
    'ang20220412t192034',
    'ang20220412t193109',
    'ang20220412t194550',
    'ang20220412t195932',
    'ang20220412t201217',
    'ang20220412t202627',
    'ang20220412t203940',
    'ang20220412t205405',
    'ang20220412t210701',
    'ang20220412t212151',
    'ang20220412t215642'
]
data_20220420 = [
    'ang20220420t182836',
    'ang20220420t181856',
    'ang20220420t183824',
    'ang20220420t184735',
    'ang20220420t190012',
    'ang20220420t191418',
    'ang20220420t192635',
    'ang20220420t194128',
    'ang20220420t195351',
    'ang20220420t200950',
    'ang20220420t202328',
    'ang20220420t204018',
    'ang20220420t205737',
    'ang20220420t211130',
    'ang20220420t211746',
    'ang20220420t212903'
]
data_20220429 = [
    'ang20220429t182823',
    'ang20220429t183922',
    'ang20220429t185945',
    'ang20220429t191122',
    'ang20220429t193717',
    'ang20220429t195134',
    'ang20220429t202217',
    'ang20220429t204250',
    'ang20220429t205711',
    'ang20220429t212438',
    'ang20220429t213801',
    'ang20220429t215742'
]
data_20220503 = [
    'ang20220503t181259',
    'ang20220503t182413',
    'ang20220503t183508',
    'ang20220503t184753',
    'ang20220503t190109',
    'ang20220503t191752',
    'ang20220503t193029',
    'ang20220503t194326',
    'ang20220503t195633',
    'ang20220503t200956',
    'ang20220503t202310',
    'ang20220503t203611',
    'ang20220503t205420',
    'ang20220503t210356'
]
data_20220511 = [
    'ang20220511t182038',
    'ang20220511t183056',
    'ang20220511t183825',
    'ang20220511t184946',
    'ang20220511t190344',
    'ang20220511t191813',
    'ang20220511t193135',
    'ang20220511t194610',
    'ang20220511t195950',
    'ang20220511t201348',
    'ang20220511t202703',
    'ang20220511t204152',
    'ang20220511t205951',
    'ang20220511t211351',
    'ang20220511t212317',
    'ang20220511t214730'
]
data_20220512 = [
    'ang20220512t164509',
    'ang20220512t170130',
    'ang20220512t171026',
    'ang20220512t172553',
    'ang20220512t173907',
    'ang20220512t175232',
    'ang20220512t180531',
    'ang20220512t181806',
    'ang20220512t183012',
    'ang20220512t184259',
    'ang20220512t185806',
    'ang20220512t190633'
]
data_20220517 = [
    'ang20220517t184026',
    'ang20220517t184913',
    'ang20220517t185532',
    'ang20220517t190513',
    'ang20220517t193145',
    'ang20220517t194445',
    'ang20220517t195833',
    'ang20220517t201603',
    'ang20220517t202642',
    'ang20220517t204021',
    'ang20220517t212527',
    'ang20220517t213427'
]
data_20220529 = [
    'ang20220529t184338',
    'ang20220529t185311',
    'ang20220529t190009',
    'ang20220529t191254',
    'ang20220529t193259',
    'ang20220529t194556',
    'ang20220529t200210',
    'ang20220529t201722',
    'ang20220529t203308',
    'ang20220529t204600',
    'ang20220529t210007',
    'ang20220529t211333',
    'ang20220529t214201',
    'ang20220529t220336',
    'ang20220529t220943',
    'ang20220529t222033'
]

if date == '20220224' or '20220228' or '20220308' or '20220316' or '20220318' or '20220322' or '20220405' or '20220412' or '20220420' or '20220429' or  '20220503' or '20220511' or '20220512' or '20220517' or '20220529' and flight_path == 'all':
    if date == '20220318':
        for flight_path in data_20220318:
            get_all(flight_path, date)
    elif date == '20220224':
        for flight_path in data_20220224:
            get_all(flight_path, date)
    elif date == '20220228':
        for flight_path in data_20220228:
            get_all(flight_path, date)
    elif date == '20220308':
        for flight_path in data_20220308:
            get_all(flight_path, date)
    elif date == '20220316':
        for flight_path in data_20220316:
            get_all(flight_path, date)
    elif date == '20220322':
        for flight_path in data_20220322:
            get_all(flight_path, date)
    elif date == '20220405':
        for flight_path in data_20220405:
            get_all(flight_path, date)
    elif date == '20220412':
        for flight_path in data_20220412:
            get_all(flight_path, date)
    elif date == '20220420':
        for flight_path in data_20220420:
            get_all(flight_path, date)
    elif date == '20220429':
        for flight_path in data_20220429:
            get_all(flight_path, date)
    elif date == '20220503':
        for flight_path in data_20220503:
            get_all(flight_path, date)
    elif date == '20220511':
        for flight_path in data_20220511:
            get_all(flight_path, date)
    elif date == '20220512':
        for flight_path in data_20220512:
            get_all(flight_path, date)
    elif date == '20220517':
        for flight_path in data_20220517:
            get_all(flight_path, date)
    elif date == '20220529':
        for flight_path in data_20220529:
            get_all(flight_path, date)

# elif date == '20220308' or '20220316' and flight_path != 'all' and data == 'L1':
#     get_L1(flight_path, date)

# elif date == '20220308' or '20220316' and flight_path != 'all' and data == 'L2':
#     get_L2(flight_path, date)

# elif date == '20220308' or '20220316' and flight_path != 'all' and data == 'all':
#         get_all(flight_path, date)
else:
    print("Data not found") # will add additional dates later as they become available
    exit