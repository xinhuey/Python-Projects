### --- populate 30 min arrays ---- ####
ary_2sea30min = []
ary_4sea30min = []
ary_Hstr30min = []
#mcnt = 800
#for i in range (0,11):
#   stg = str(mcnt)
#   ary_2sea30min.append(stg)
#   ary_4sea30min.append(stg)
#   ary_Hstr30min.append(stg)
#   ary_2sea30min.append("Available")
#   ary_4sea30min.append("Available")
#   ary_Hstr30min.append("Available")
#   mcnt = mcnt +100
###--------------------------------
###-- populate 60min arrays ---#####
ary_2sea60min = []
ary_4sea60min = []
ary_Hstr60min = []
#mcnt = 800
#for i in range (0,7):
#   stg = str(mcnt)
#   ary_2sea60min.append(stg)
#   ary_4sea60min.append(stg)
#   ary_Hstr60min.append(stg)
#   ary_2sea60min.append("Available")
#   ary_4sea60min.append("Available")
#   ary_Hstr60min.append("Available")
#   mcnt = mcnt +130
#   if ((mcnt%100) == 60):
#      mcnt = mcnt + 40
####-------------------------------- 
ty_Plane = ""
tm_Flight = 0
bk_Flight = 0
tm_Cont = True
### --- task 1 ----------
while (tm_Flight != 30 and tm_Flight != 60 and tm_Cont):
   try:
      tm_Flight = int(input("Length of Flight [30]mins/[60]mins/[0]mins to Exit: "))
   except ValueError:
      print ("Invalid Entry. Input an integer")
      print("")
      continue
   if (tm_Flight != 30 and tm_Flight != 60 and tm_Flight !=0):
      print ("Flight time must be 30 mins/60 mins/0 mins to exit")
      print ("")
   #disp_Cnt = 0
   #while (tm_Flight != 0 and disp_Cnt < 3):
   if (tm_Flight == 0):
      tm_Cont = False
   else:
      print ("Today's length of flight: ", tm_Flight)
      print ("Type of Plane and Flight Time Available are:")
  ### re-display
pln_bked = []
while tm_Cont:
   tm_slot = float(input("Check time slot availability"))
   disp_Cnt = 0
   while (disp_Cnt < 3 and tm_Flight == 30):
      if (disp_Cnt == 0):
         nme_Flight = "Type: 2 Seater Plane"
         ary_Comn = ary_2sea30min
      elif (disp_Cnt == 1):
         nme_Flight = "Type: 4 Seater Plane"
         ary_Comn = ary_4sea30min
      else:
         nme_Flight = "Type : Historic Plane"         
         ary_Comn = ary_Hstr30min
      disp_Cnt = disp_Cnt + 1
      
      print ("")
      print (nme_Flight)
      print ("Available:")
      ary_tm30 = [8.00,9.00,10.00,11.00,12.00,13.00,14.00,15.00,16.00,17.00,18.00]
      if len(ary_Comn) == 0 :
         print ("Seat Available")
      else:
         for i in range (0,len(ary_tm30)):
            s = 0
            print (s< len(ary_Comn))
         
            while (s< len(ary_Comn) and ary_Comn[s] != ary_tm30[i]):
               s = s + 1
               if (ary_Comn[s] == stg_Tme) :
                  pln_bked.append(disp_cnt)
                   
                  s = s + 1
               else:
                  print ("arycomn",ary_Comn[s],"arytm",ary_tm30[i])
      ty_Plane = input("Book Flight on plane :")
      bk_add = True
      if len(pln_bked) != 0:
         for m in range (0,len(pln_bked)):
            if ty_Plane == pln_bked[m]:
               print ("Sorry flight time already taken. Please choose again")
               bk_add = False
      if bk_add:
         if (ty_Plane == '2'  ):
            ary_2sea30min.append(tm_slot)
         elif (ty_Plane == '4' ):
            ary_4sea30min.append(tm_slot)
         else:
            ary_Hstr30min.append(tm_slot)
      print ("2",ary_2sea30min,"4", ary_4sea30min, "H",ary_Hstr30min)
       #bk_Flight = float(input("Book Flight Time: "))
       #ary_Comn[1]
         
               
         
      #print ("%5.2f"%(float(ary_Comn[0])/100),ary_Comn[1]," ","%5.2f"%(float(ary_Comn[2])/100),ary_Comn[3]
      #       ," ","%5.2f"%(float(ary_Comn[4])/100),ary_Comn[5]," ","%5.2f"%(float(ary_Comn[6])/100),ary_Comn[7]
      #       ," ","%5.2f"%(float(ary_Comn[8])/100),ary_Comn[9])
      #print ("%5.2f"%(float(ary_Comn[10])/100),ary_Comn[11]," ","%5.2f"%(float(ary_Comn[12])/100),ary_Comn[13]
      #       ," ","%5.2f"%(float(ary_Comn[14])/100),ary_Comn[15]," ","%5.2f"%(float(ary_Comn[16])/100),ary_Comn[17]
      #       ," ","%5.2f"%(float(ary_Comn[18])/100),ary_Comn[19])
      #print ("%5.2f"%(float(ary_Comn[20])/100),ary_Comn[21])
   
