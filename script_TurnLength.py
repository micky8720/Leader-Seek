import xml.etree.ElementTree as E
root=E.parse("2009_04_28.txt.xml").getroot()  #Here enter the file name
count=1
count_data={}
males=['luke','ted','david','matthew','jake','rick','josh','tony','aaron','michael','nick','george','john']
females=['judith','tia','meg','vicky','eva','julie','rita','leah','caroline','cintihia','ariel','macy','lynn','rebecca','cinthia','mara','amy','michelle']
for document in root:
    for sentences in document:
        for sentence in sentences:
            for tags in sentence:
                if tags.tag == "tokens":
                    for token in tags:
                       # print (token.tag,token.attrib)
                        #print (token.attrib['id'])
                        for intoken in token:
                            if(intoken.tag=="word" and (intoken.text in males or intoken.text in females)):
                                previous=intoken.text
                            #elif(intoken.tag=="POS" and (intoken.text=="PRP" or intoken.text=="PRP$")):
                            elif (intoken.tag == "POS"):
                                 if previous != "" and (previous in count_data) and (previous in males or previous in females):
                                        #print (previous,"has",intoken.text)
                                        count_data[previous]=count_data[previous]+1
                                 else:
                                        count_data[previous]=1
                           # if(token.attrib['id']=='1' and intoken.tag == "POS"):
                               # print(intoken.tag,'=',intoken.text)
print (count_data)
