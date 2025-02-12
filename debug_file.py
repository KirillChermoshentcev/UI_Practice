data1 = ['Desktop', 'Notes', 'Commands', 'Angular', 'Veu', 'Downloads', 'Word File.doc', 'Excel File.doc']
data2 = ['desktop', 'notes', 'commands', 'angular', 'veu', 'downloads', 'wordFile', 'excelFile']

print(str(data1).replace(' ', '').replace('doc','').replace('.','').lower())
print(data2)

data1 = str(data1).replace(' ', '').replace('doc','').replace('.','').lower()
data2 = str(data2).replace(' ', '').lower()

assert data1 == data2
