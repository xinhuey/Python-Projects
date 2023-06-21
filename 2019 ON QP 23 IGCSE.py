#Task 1, 2, 3
tile_descrpary=['Small Black Granite','Small Grey Marble   ','Small Powder Blue   ','Medium Sunset Yellow','Medium Berry Red    ','Medium Glitter Purple','Large Oak Wood Effect','Large Black Granite','Large Bamboo Effect','Extra-Large White Marble']
priceperbox_ary=[19.5,25.95,35.75,12.5,11,52.95,65,58.98,85,62.75]
idcode_ary=['001','002','003','004','005','006','007','008','009','010']
total_area=0
max_numwalls=4
print('ID','','  Tile description','\t','   Price per box $')
for i in range(0,len(idcode_ary)):
    print(idcode_ary[i],'',tile_descrpary[i],'\t',priceperbox_ary[i])
ask_cust=str(input('Would you like to continue[Y/N]:'))
while ask_cust=='Y':
    while (True):
        wall_count=0
        try:
            num_walls=int(input('How many walls would you like to tile?(Max:4 walls):'))
        except ValueError:
            print('Only Integers are accepted, please re-enter')
    while num_walls > max_numwalls and num_walls <=0:
        print('Only 4 walls can be tiled. Please Re-enter')
        num_walls=int(input('How many walls would you like to tile?(Max:4 walls):'))
    print (num_walls)
    for u in range(0,num_walls):
        wall_count=wall_count+1
        print('Enter dimensions for WALL',wall_count)
        while (True):
            try:
                height_input=float(input('Enter height of the wall: '))
                while height_input <=0:
                    print('Invalid height. Re-Enter')
                    height_input=float(input('Enter height of the wall: '))
            except ValueError:
                print('Only Integers are accepted, please re-enter')
            while height_input <=0:
                print('Invalid height. Re-Enter')
                height_input=float(input('Enter height of the wall: '))
        while (True):
            try:
                width_input=float(input('Enter width of the wall: '))
            except ValueError:
                print('Only Integers are accepted, please re-enter')
            while width_input <=0:
                print('Invalid width.Re-Enter.')
                width_input=float(input('Enter width of the wall: '))
        area_wall=height_input*width_input
        total_area=total_area+area_wall
        print('')
    tile_chosen=str(input('Enter ID code of tile chosen: '))
    while tile_chosen not in idcode_ary:
        print('Invalid ID code. Re-Enter.')
        tile_chosen=str(input('Enter ID code of tile chosen: '))
    waste_percentinput=float(input('Enter the percentage for wastage: '))
    index_tile=idcode_ary.index(tile_chosen)
    price_tile=priceperbox_ary[index_tile]
    total_waste=(waste_percentinput/100)*(total_area)
    total_cost=round(total_area+total_waste)*price_tile
    print('Number of boxes of tiles needed before wastage is:',(total_area))
    print('SUMMARY')
    print('The total area of the wall is: ' ,total_area)
    print('The total number of boxes needed after wastage:', round((total_area+total_waste)))
    print('Total cost is $',round(total_cost))
    print('Total damaged boxes of tiles: ',round(total_waste))
    print('')
    ask_cust=str(input('Would you like to continue[Y/N]:'))
       
