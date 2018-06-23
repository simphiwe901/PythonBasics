# program which determines the winner due to the distance by prompting the user
# Simphiwe Mchunu
# 24 July 2015

def main():
    #print("***** Long Jump Information System *****")
    names = []
    m = 1
    space = ''
    competitor = "abc"
    #print("Please enter the names of competitors. (Press enter when done.)")
    while competitor != space:
        dictn = {}
        att = []
        list_names = []
        competitor = input("Competitor no. {}:\n".format(m))
        end = ""
        names.append(competitor)
        m +=1
        if competitor == space:
            print("Please enter the distances for each competitor.")
            for competitor in names:
                z = 1
                #print("Competitor {}:".format(competitor))
                for i in range(3):
                    attempt = input("Attempt {}:\n".format(z))
                    list_names.append(attempt)
                    att.append(attempt)
                    z +=1
                    if attempt == "Foul":
                        attepmt = 0
                        dictn[competitor] = 0
                        if dictn[competitor] ==0:
                            s = "No Jump"

                    else:
                        maxn=max(att)
                        dictn[competitor] = maxn
                #print(dictn)
                #print(list_names)

main()
