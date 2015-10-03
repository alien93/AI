from Variable import *
from nonogramGraphics import *
from nonoState import *
from random import randint
from Module2.aStarGacProgram import *

#f = open('nono-rabbit.txt', 'r')
f = open('nono-sailboat.txt', 'r')
#f = open('nono-camel.txt', 'r')
#f = open('nono-heart-1.txt', 'r')
#f = open('test2.txt', 'r')
#f = open('nono-cat.txt', 'r')

#f = open('nono-telephone.txt', 'r')
#f = open('nono-chick.txt', 'r')


# while True:
#     prompt = input("Please type module number and press 'Enter': ")
#
#     if prompt == '1':
#         print("Module 1 selected")
#         break
#
#     elif prompt == '2':
#         print("Module 2 selected")
#         break
#     elif prompt == '3':
#         print("Module 1 selected")
#         break
#     else:
#         print("Module number not valid. Try again")
#
#
#
#
# while True:
#     prompt = input("Please type in the path to your file and press 'Enter': ")
#     try:
#         f = open(prompt + ".txt", 'r')
#     except FileNotFoundError:
#         print("Wrong file or file path")
#     else:
#         break

#print (f)

firstLine = f.readline()
values = ( firstLine.split( ) )

numberOfColumns= int(values[0])
numberOfRows= int(values[1])
print("")
print("numberOfRows: " + str(numberOfRows))
print("numberOfColumns: " + str(numberOfColumns))
print("")

rowsAndColumns = []
rows = []
columns = []

setDimensions( numberOfColumns, numberOfRows )

def createDomainRecursive(currentDomain,remaningPlaces, restrictions, returnList):
    for i in range(0,2): #Block can either be blank(0) or filled with the next block
        updatedDomain = currentDomain.copy()
        updatedRestrictions = restrictions.copy()

        if(i == 0): # Empty space here
            updatedDomain.append(0)
        else:
            for etTall in range(0,updatedRestrictions[0]):
                updatedDomain.append(1)
            updatedRestrictions.pop(0) #Removes the block

        if ((remaningPlaces == len(currentDomain) and len(updatedRestrictions) > 0) or remaningPlaces +1 < len(updatedDomain)):
            #Not a valid domain
            continue

        elif( len(updatedRestrictions) == 0): #Reached end of domain and the domain is valid. Returning it
            for index in range(0,(remaningPlaces+1) - len(updatedDomain)):
                updatedDomain.append(0)
            returnList.append(updatedDomain)
            #Domain created. Adding it to the list

        else:
            if(i == 1): #Adding the divider between blocks
                updatedDomain.append(0)
            if remaningPlaces > len(currentDomain): #Not done with the domain yet. We have to go deeper!
                createDomainRecursive(updatedDomain,remaningPlaces,updatedRestrictions,returnList)




#setDimensions(numberOfVertices)
constraints = []

for line in range(0,numberOfRows):
        vertLine = f.readline()

        values = ( vertLine.split( ) )
        intValues = []
        for v in range(0,len(values)):
            intValues.append(int(values[v]))
        index = line

        coord =  numberOfRows - line -1

        row = Variable(index,coord)

        constraints.append({})

        domene = []
        tempDomain = []

        createDomainRecursive(tempDomain,numberOfColumns-1,intValues,domene)

        row.domain = domene
        #print(domene)
        rowsAndColumns.append(row)
        for column in range(0,numberOfColumns):
            constraints[index][column + numberOfRows] = [[0,0], [1,1]]

print("Created all rows")

for line2 in range(0,numberOfColumns):
        vertLine = f.readline()
        values = ( vertLine.split( ) )
        intValues = []
        for v in range(0,len(values)):
            intValues.append(int(values[v]))
        index = line2 + numberOfRows

        coord = line2
        row = Variable(index,coord)

        constraints.append({})

        domene = []
        tempDomain = []

        createDomainRecursive(tempDomain,numberOfRows-1,intValues,domene)
        row.domain = domene
        rowsAndColumns.append(row)
        for row in range(0,numberOfRows):
            constraints[index][row] = [[0,0], [1,1]]


# if d2[var1.coord] == d1[var2.coord]:

print("Created all columns")
print("")

#for c in contraints:
    #print(c)

def drawNonoGramState(state):
    for var in range(0,numberOfRows):
        row = state.vertices[var]
        if row.isAssumed:
            for val in range(0,len(row.domain[0])):
                drawBox(val,var, row.domain[0][val])




#drawState()






#Initialization
#queue = []


#for line in range(0,numberOfRows + numberOfColumns):
#        queue.append(rowsAndColumns[line])

def nonoGramRevise(constraints, vertex1,vertex2):

        revised = False
        if constraints[vertex1.index][vertex2.index] is None:
                return False

        for d1 in vertex1.domain:
                domainChanged = False
                for d2 in vertex2.domain:
                        for const in constraints[vertex1.index][vertex2.index]:
                                if d1[vertex2.coord] == const[0] and d2[vertex1.coord] == const[1]:
                                    domainChanged = True

                if not domainChanged:
                        vertex1.domain.remove(d1)
                        revised = True

        return revised

#The Domain-Filtering Loop
# def domainFiltering(queue, stateVertices):
#
#         while len(queue) >= 1:
#
#                 todoReviseVertex = queue.pop(0)
#                 for const in contraints[todoReviseVertex.index]:
#                         neighbour = stateVertices[const]
#
#                         change = revise(todoReviseVertex,neighbour)
#                         if change:
#                                 for v5 in contraints[todoReviseVertex.index]:
#                                         if stateVertices[v5] not in queue:
#                                                 queue.append(stateVertices[v5])
#                                         #else:
#                                             #print(" hei hei he hei ih ihasd asdad a sd ")
#
#
#
# def generateSuccesorStates(vertices):
#         newStates = []
#
#         for vertex in vertices:
#                 if not vertex.isAssumed():
#                         for color in vertex.domain:
#                                 index = vertex.index
#                                 state = nonoState(vertices)
#                                 state.vertices[index].domain = [color]
#                                 state.lastModifiedVertex = state.vertices[index]
#                                 newStates.append(state)
#
#
#         return newStates



aStarGAC(3, rowsAndColumns, constraints, drawNonoGramState, nonoGramRevise)

# print("Running init")
# print("")
# #getWindow().getMouse()
# domainFiltering(queue,rowsAndColumns)
#
# print("Init done")
# #getWindow().getMouse()
# currentState = nonoState(rowsAndColumns)
#
#
# #getWindow().getMouse()
#
#
# drawState(currentState)
#
# if currentState.isFinished():
#     print("Solution found. No need for A*")
# else:
#     print("Done with init, but no solution yet. Running A*")
# while not currentState.isFinished():
# #for tall in range(0,100000):
#
#         #vert = vertices[tall]
#         #print("Doamin to " + str(tall) + " is " + str(vert.domain))
#
#
#         #color = vert.domain[0]
#         #vert.domain = [color]
#         newStates = generateSuccesorStates(currentState.vertices)
#         print("Lengden: " + str(len(newStates)))
#
#         #getWindow().getMouse()
#         if len(newStates) == 0:
#                 print("breaking")
#                 currentState = nonoState(rowsAndColumns)
#                 getWindow().getMouse()
#                 continue
#         currentState = newStates[randint(0,len(newStates)-1)]
#         canContinue = False
#
#         drawState(currentState)
#         vert = currentState.lastModifiedVertex
#         queue = []
#         for connectedVertex in contraints[vert.index]:
#                 if connectedVertex not in queue and not currentState.vertices[connectedVertex].isAssumed():
#                         queue.append(currentState.vertices[connectedVertex])
#
#
#
#
#
#
# #         domainFiltering(queue,currentState.vertices)
# #
#
# #Rerun
#
#
#
#
#         if currentState.isError():
#                 currentState = nonoState(rowsAndColumns)
#                 print("Going back a level")
#         elif currentState.isFinished():
#             print("Am i finished now?")
#             #getWindow().getMouse()
#
#
#         print("- ")





getWindow().getMouse()