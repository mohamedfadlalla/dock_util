import os
import shutil

def DockAffinity(file):
    with open(file) as f:    
        for line in f.readlines():
            if line.startswith('DOCKED: USER    Estimated Free Energy of Binding'):
                affinity = float(line.split('=')[1].strip().replace('[', '').replace('kcal/mol',''))
                name = file[:-4]
                print(name)
                print(affinity)
                return name, affinity

def DockPoses(file):
    with open(file) as f:    
        for line in f.readlines():
            if line.startswith('DOCKED:'):
                affinity = float(line.split('=')[1].strip().replace('[', '').replace('kcal/mol',''))
                name = file[:-4]
                print(name)
                print(affinity)
                return name, affinity

def WriteResults(direcotry):
    lst = os.listdir(directory)
    lst = [x for x in lst if x.endswith('.dlg')]

    os.chdir(directory)
    with open('results.csv', 'w') as r:
        r.write('id, affinity\n')
        for file in lst:
            name, affinity = DockPoses(file)
            # break
            r.write(f'{name},{affinity}\n')

def WriteResults_Vina(direcotry):
    def DockPoses(file):
        affs = []
        with open(file) as f:    
            for line in f.readlines():
                if line.startswith('REMARK minimizedAffinity'):
                    affinity = float(line.split()[2])
                    name = file[:-4]
                    print(name)
                    affs.append(affinity)

        return name, min(affs)


    lst = os.listdir(direcotry)
    lst = [x for x in lst if x.endswith('.pdb')]

    os.chdir(direcotry)
    with open('results.csv', 'w') as r:
        r.write('id, affinity\n')
        for file in lst:
            name, affinity = DockPoses(file)
            # break
            r.write(f'{name},{affinity}\n')



direcotry = r'C:\Users\Andylau\Desktop\Diabetes Insilico\MD'
os.chdir(direcotry)
for file in os.listdir(direcotry):
    os.mkdir(file.split('.')[0])
    shutil.copy(file,file.split('.')[0])