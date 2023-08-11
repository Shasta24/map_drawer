from random import *

XX = 640            # horizontal size of the map
YY = 480            # vertical size of the map
max_height = 250    # Max hight value and depth value on the map, recommanded is 250
K = 100             # K value sets the size of the islands

def static_noise_filtering(MAP, K):
    '''
    MAP - Double nested list
    K - int 
    '''
    for l in range(0,K):
        for i in range(0,XX):
            for j in range(0,YY):
                MAP[i][j] = ( 4 * MAP[i][j] + MAP[i][(j+YY-1)%YY] + MAP[i][(j+1)%YY] + MAP[(i+XX-1)%XX][j] + MAP[(i+1)%XX][j] +
                0.5 * MAP[(i+XX-1)%XX][(j+YY-1)%YY] + 0.5 * MAP[(i+XX-1)%XX][(j+1)%YY] + 0.5 * MAP[(i+1)%XX][(j+YY-1)%YY] + 0.5 * MAP[(i+1)%XX][(j+1)%YY] ) / 10
    return MAP

def set_min_max_value(MAP):
    '''
    MAP - Double nested list
    '''
    #min-max search
    minimum = MAP[0][0]
    maximum = MAP[0][0]
    for row in range (0, len(MAP)):
        if minimum > min(MAP[row]):
            minimum = min(MAP[row])
        if maximum < max(MAP[row]):
            maximum = max(MAP[row])
    #set values
    for i in range(0,len(MAP)):
        for j in range(0,len(MAP[i])):
            MAP[i][j] = round( (MAP[i][j]-minimum) / (maximum-minimum)*(max_height*2) - max_height )
    return MAP

def main():
    seed()
    MAP = []

    #radnom matrix
    for i in range(0,XX):
        row = []
        for j in range(0,YY):
            row.append(random()) 
        MAP.append(row)

    MAP = static_noise_filtering(MAP, K)
    MAP = set_min_max_value(MAP)

    #write into file
    f = open("map.txt", "w")
    f.write(str(XX)+ " " + str(YY) + "\n")
    for row in MAP:
        for number in row:
            f.write(str(number)+" ")
        f.write("\n")
    f.close()

if __name__ == "__main__":
    main()
