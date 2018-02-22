import requests
import json

SourceFile          = open('source.txt', "r")
SourceLines         = list(SourceFile)

print('----------------------------------------------------------------')
print('-------------------------Savalan YouTube Solution---------------')
print('----------------------------------------------------------------')
print('Link Numbers: \t\t' + str(len(SourceLines)))
i                   = 0
while i < len(SourceLines):
    print('================================================================')
    result              = requests.get('https://www.saveitoffline.com/process/?url=' + SourceLines[i] + '&type=json')
    response            = json.loads(result.text)
    Urls                = response['urls']
    print('Title: \t\t\t' + response['title'])
    #Filter Out The Files Without Sound or Files Witch Are
    # Not in 'mp4' Formant:
    j                   = 0
    k                   = 0
    VUrls               = []
    while j < len(Urls):
        if 'no sound' not in Urls[j]['label'] and 'mp4' in Urls[j]['label']:
            VUrls.append(Urls[j])
        j += 1
    #Find The Highest Resolution Available:
    Resos               = []
    j                   = 0
    print('Availables: \t\t' + str(len(VUrls)))
    while j < len(VUrls):
        Resos.append(int(VUrls[j]['label'][:3]))
        MaxRes = max(Resos)
        j += 1
    print('Max Res Possible: \t' + str(MaxRes) + "p")
    #Write Down The Link Url For The File With Highest Resolution
    j                   = 0
    link                = 'No Link'
    while j < len(VUrls):
        if str(MaxRes) in VUrls[j]['label']:
            link = VUrls[j]['id']
        j += 1
    ResultFile          = open('result' + ''+ '.txt','a')
    ResultFile.write(link + '\n')
    ResultFile.close()
    print('Link: \t\t\t' + link)
    i += 1
    
print('================================================================')
print('Processing Links Finished')
input("Press Enter to continue...")
