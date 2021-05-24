from utility import FileLoader as fileLoader
import glob
from utility import PropertyReader as pr

allyamlfiles = glob.glob(pr.getYourProperty("../source.properties","yamlsource"))

def read_yaml(file):
    with open(file,'r') as f:
        doc= fileLoader.safe_load(f)
        info = doc['info']
        location= info ['city']
        matchday= info ['dates']
        teams =info ['teams']
        print('This match was happened between ' + teams[0] +' and '+teams[1]+' at '+ location[0] +' on ' + str(matchday[0]))

for file in allyamlfiles:
    read_yaml(file)



