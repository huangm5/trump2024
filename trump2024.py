#becaure for push, it deletes new change
#20220823 --merging from x
# There is insufficient memory for the Java Runtime Environment to continue.
# Native memory allocation (mmap) failed to map 1048576 bytes for G1 virtual space
# An error report file with more information is saved as:
# C:\Users\Public\Documents\hs_err_pid6388.log
#where is this file? its right there ? hidden?
#20220609
#trump2024.py:2351 sleep 37281.17s
#rename working folder to start
#sihost or explorer may hold the folder to rename
#a dead situation happend, no cpu, sleeping?
#keep configable from sikuli /ok /revisit 1 month 3/28
#2D facets to 3D finding stories
#freq visit route
import math;

gtx1060="gtx1060";
inossem="inossem";

scenario=inossem;
class MakeSense:
    me={};
    OnChange={};
    def __getattr__(self,attr):
        return self.me[attr];
    def __setattr__(self,attr,value):
        if  bool(self.me.get(attr)) :
            if self.me[attr]==value:
                return;
        print "change ",attr;
        self.me[attr]=value;
        if  bool(self.OnChange.get(attr)) :
            self.OnChange[attr]();

global my;

try:
    my
    print("sure, it was defined.")
except NameError:
    print("well, it WASN'T defined after all!")
    my=MakeSense();        

def my_friend():
   if (my.lastStatus=='friend dialog' and random.random()>0.1):
       pass;
   else: 
       try:
            loc=my.ClientRegion.find(managed("1652298276529.png","my_friend"))
            print loc
            lastLoc=loc.getTarget(); 
            #was.png for inossem
            if my_friend_help()==0:
                sleep(20);
            return 0;
       except:
           pass;
   if (my.lastStatus=='friend home' and random.random()>0.1):
       pass;
   else: 
       print my_friend1()
   return 999;

import socket
print(socket.gethostname())

if socket.gethostname()=='Inossem':
    my.scenario=inossem;
else:
    my.scenario=gtx1060;

def my_blue_feeder():
    loc=find("1659095267480.png");
    if loc.getScore()>0.95:                                    
        type(Key.F5);
        sleep(3*60);
        my.need_splash=True;
                
def skipAds():
    click("1659010237092.png")
    click(Location(2684, 360));
    click(Location(2455, 286));

def buysellpoppy100():
  for i in range(6):
    loc=find("1658314287861.png")
    print loc #593 293
    click(Location(590, 289));sleep(3);
    click(Location(590, 338));sleep(1);
    click(Location(645, 475));sleep(1);
    click(Location(488, 516));sleep(1);
    loc=find("1658314178135.png");
    click(Location(739, 678));sleep(1);
    
    click(Location(1142, 269));sleep(1);
    click(Location(1038, 625));sleep(1);
    click(Location(936, 616));sleep(1);
    drag(Location(1035, 375));
    dropAt(Location(450, 438)); sleep(1)
    click(Location(514, 681));sleep(4);
    
    
cookieItemFulls={};

def my_connectionError():
    try:   
        loc=find(managed("1661290954532.png",'reconnect'))
        print loc,loc.getTarget().x,loc.y+loc.h*92/100
        sleep(10);
        loc=Location(loc.getTarget().x,loc.y+loc.h*92/100)
        print loc
        click(loc)
        sleep(1)
        click("1652488232002.png");
        sleep(1)
        #sleep(3*60);#splash
        return 0;
    except:
        return 999;
#my_connectionError();   

def sell_buy_poppy():
  for i in range(12):    
    poppy=Location(555,324)
    try:
        poppy=find("1658057886220.png").getTarget();
        print poppy# 555,324
        click(poppy);sleep(2)#Location(555, 326)
    except:
        pass;
    click(poppy.offset(0, 94));sleep(2)
    click(poppy.offset(600-542, 517-324));sleep(1)
    RemoveObject=find("1658057148093.png")
    #print RemoveObject,
    click(Location(494, 514))#,click stoned?
    mouseDown(Button.LEFT);sleep(0.2);mouseUp(Button.LEFT);sleep(1)
    Sell=find("1658057450850.png")
    click(Location(744, 676));sleep(1)
    click(Location(509, 476));sleep(1)
    click(Location(519, 573));sleep(1)
    Yes=find("1658057621555.png")
    click(Location(509, 684));sleep(4)

def cookie_item(item,title):
    if bool(cookieItemFulls.get(title)):
        return;
    try:
        loc=find(item);    
        print title,loc;#M[1369,267 250x158]@
        if loc.getScore()>0.85:
            loc1=Location(loc.x+loc.w*0.9,loc.y+loc.h*0.75)
            rg=Region(loc1.x-80,loc1.y-50,80*2,50*2)
            try:
                loc2=rg.find("1655843239458.png")
                print 'x0:',loc2 
                if loc2.getScore()<0.93:
                    raise Exception('bad score'); 
            except:        
                click(loc1);
                sleep(1);
                try:
                    loc2=find("1656888495630.png");
                    click(loc2.getTopRight());
                    cookieItemFulls[title]=True;
                except:
                    pass;
    except:
        pass;

import datetime;
cookieItems=[["1656276637754.png",'Jellybean Jam']
#            ,["1656996995975.png",'Butter']
            ,["1656997272926.png",'Wood']
            ,["1657059240407.png",'Shovel']
            ,["1656277184823.png",'Planter']
            ,["1656277384825.png",'Cream']
            ,["1656277517404.png",'Latte']
            ,["1656277609357.png",'Pillow']
            ,["1656277907046.png",'Candy Saw']    
        ,["1655844625187.png",'Suger Cube']            
            ,["1655860567350.png",'Toffe Jam']      
            ,["1656860612793.png",'Ring']      
            ,["1655947616537.png",'Stew']      
            ,["1656860737440.png",'Focaccia']      
            ,["1655947493149.png",'Toy']      
            ,["1655843769524.png",'Axe']      
            ,["1655860711815.png",'Candy Wool']
            ,["1656276970547.png",'Hearty Rye']];
#ci=cookieItems[2]
def cookie_wook():

    cookie_item("1655860761062.png",'Milk:');            
    cookie_item("1655862866954.png",'Basket:');    
    cookie_item("1655871263617.png",'Flower:');    
    for ci in cookieItems:
         cookie_item (ci[0],ci[1]);
    cookie_item("1655860632123.png",'Jelly Jam:');
    try:
        loc=find("1655844115185.png");    
        print 'JellyBean:',loc;#M[1369,267 250x158]@
        if loc.getScore()>0.85:
            loc1=Location(loc.x+loc.w*0.9,loc.y+loc.h*0.75)
            rg=Region(loc1.x-80,loc1.y-50,80*2,50*2)
            try:
                loc2=rg.find("1655843239458.png")
                print loc2 
                if loc2.getScore()<0.85:
                    raise Exception('bad score'); 
            except:        
                click(loc1);
                sleep(1);
    except:
        pass;
    try:
        loc=find("1655843068695.png");    
        print 'flour:',loc;#M[1369,267 250x158]@        
        loc1=Location(loc.x+loc.w*0.95,loc.y+loc.h*0.75)
        rg=Region(loc1.x-80,loc1.y-50,80*2,50*2)
        try:
            rg.find("1655843239458.png")
        except:        
            click(loc1);
            sleep(1);
    except:
        pass;
    click(Location(1012, 529)); #right       
    sleep(1);
#    click(Location(451, 530));#left
#    sleep(1);

def findOR(rgs,pics):
    for rg in rgs:
        for pic in pics:
            try:
                loc=rg.find(pic);
                return loc;
            except:
                pass;
def cookie_works():
    loc=findOR([Screen()],["1655859264104.png","1656038737775.png"])
    print loc
    if bool(loc):
        click(loc)
        sleep(3)
        click(loc)
        sleep(5)
    
        cookieItemFulls={};
    
        for j in range(2624):
            for i in range(31):
                cookie_wook();
                mouseMove(Location(0,0))
                sleep(0.5)         
                locMouse=Mouse.at();
                if not (locMouse.x<10 and locMouse.y<10):
                    break;
            if i<31-1:
                break;
            sleep(13)         
    #Shards: -20/29/6 -19/25?/5 -21/?/8  -17/18/4
    if False:
        #without mouse
        for j in range(222):
            for i in range(31):
                cookie_wook();
            print datetime.datetime.now();
            sleep(113)        
#print cookie_works();

def scale(rg,sc0):
   sc=Screen();#R[0,0 1920x1080]@S(0)
   return Region(rg.x*sc.w/sc0.w,rg.y*sc.h/sc0.h,rg.w*sc.w/sc0.w,rg.h*sc.h/sc0.h)
#print scale(Region(0,0,560,406),Region(0,0,1920,1080))
#print scale(Region(993,494,373,270),Region(0,0,1280,768))
#R[993,494 373x270]@S(0) for 1280x768



ClientRegions={
        gtx1060:Region(161,40,1598,998),
        inossem:Region(1,100,1200,625)
        };
print ClientRegions[scenario];
#print cr;
ClientRegion=ClientRegions[scenario];

def my_direct_ramp():
    wilds=["1653477061197.png"
            ,"1653477491528.png"
            ,"1653477522075.png"
            ,"1653689150137.png"
            ,"1653689444115.png"
            ,"1653689497145.png"
            ,"1653689553562.png"
            ,"1653689671914.png"
            ,"1653689768469.png"
            ,"1653689808007.png"
            ,"1653690885820.png"
            ,"1653690895113.png"
            ,"1653690950729.png"
            ,"1653690996752.png"
            ,"1653692223086.png"
            ];
    for i in range(len(wilds)):
        try:
            ClientRegion.find(managed(wilds[i],"wildtohome"));
            Log("wildtohome #{I}".format(I=i));
            drag(autoscale(Location(222, 574),inossem));
            dropAt(autoscale(Location(986, 275),inossem));
            return 0;
        except:
            pass;
    return 999;   
#my_direct_ramp();

def my_direct_ramp_right():
    wilds=[
           "1653689311325.png"
           ,"1653690020449.png"
            ,"1653690112052.png"
            ,"1653690145125.png"
            ,"1653690172479.png"
            ,"1653690198582.png"
            ,"1653690228711.png"
            ,"1653690269359.png"
            ,"1653690319577.png"
            ,"1653690353440.png"
            ,"1653690411321.png"
            ,"1653736497313.png"
            ,"1653736529591.png"
            ];
    for i in range(len(wilds)):
        try:
            ClientRegion.find(managed(wilds[i],"wildtohome"));
            Log("wildtohome #{I}".format(I=i));
            drag(autoscale(Location(917, 593),inossem));
            dropAt(autoscale(Location(208, 275),inossem));
            return 0;
        except:
            pass;
    return 999;   
#my_direct_ramp_right();

def my_direct_ramp_left():
    wilds=["1653691143390.png"
            ,"1653691234108.png"
            ];
    for i in range(len(wilds)):
        try:
            ClientRegion.find(managed(wilds[i],"wildtohome"));
            Log("wildtohome #{I}".format(I=i));
            drag(autoscale(Location(208, 275),inossem));
            dropAt(autoscale(Location(917, 593),inossem));
            return 0;
        except:
            pass;
    return 999;   
#my_direct_ramp_left();

def my_direct_water():
    try:
       auto_must(Region(1,212,129,497),inossem).click(managed("1653477759587.png","watermission")); 
       return 0;
    except:
        return 999;
#print my_direct_water();

import datetime;
t0=datetime.datetime(1,1,1);
lastClientRegion=t0;

def updateClientRegion():
    global ClientRegion,firstClientRegion,lastClientRegion;
    try:
        ds=[Region(0,0,313,318).find("1652230690072.png").getTarget(),
        Region(993,494,373,270).find("1652229805622.png").getTarget(),
        Region(766,0,494,360).find("1652229378603.png").getTarget()
               ]
            
        #print Region(21,50,1311,661)
        cs=[
                [Location(43,151),Location(1149,683),Location(982,132),Region(0,100,1184,624)],
                [Location(49,79),Location(1324,677),Location(1140,58),Region(0,24,1366,705)],
                [Location(68,102),Location(1289,663),Location(1118,81),Region(21,50,1311,661)]
        ];
        #print cs
        #from scipy import linalg
        #import numpy as np
        #np.array
        a=([[cs[0][1].x-cs[0][0].x,cs[0][1].y-cs[0][0].y,1],
            [cs[1][1].x-cs[1][0].x,cs[1][1].y-cs[1][0].y,1],
            [cs[2][1].x-cs[2][0].x,cs[2][1].y-cs[2][0].y,1]])
        bx=([cs[0][3].x-cs[0][0].x,cs[1][3].x-cs[1][0].x,cs[2][3].x-cs[2][0].x])
        by=([cs[0][3].y-cs[0][0].y,cs[1][3].y-cs[1][0].y,cs[2][3].y-cs[2][0].y])
        bw=([cs[0][3].w,cs[1][3].w,cs[2][3].w])
        print a
        print bw
        px=[-0.0334696913350688,  -0.005206396429899591,  -3.2127184827073263];
        py=[ 0.01859427296392711,  -0.10821866865005578,  -13.992934176273709];
        pw=[  1.154332465600595,  -0.198214949795463,  12.758646336928226];
        ph=[  0.034585347712904425,  1.1387132763108962,  -20.046857567869097];
        ac=a[1];
        pd=ph;
        #print ac[0]*pd[0]+ac[1]*pd[1]+pd[2];#+cs[1][0].y;
        #x=linalg.solve(a,b) #https://www.99cankao.com/algebra/unknwn3.php
        #print(x)
        #ds=[Location(53,91),Location(1293,652),Location(1122,70)];
        ac=[ds[1].x-ds[0].x,ds[1].y-ds[0].y]
        pd=ph
        h=ac[0]*pd[0]+ac[1]*pd[1]+pd[2];
        pd=pw
        w=ac[0]*pd[0]+ac[1]*pd[1]+pd[2];
        pd=px
        x=ac[0]*pd[0]+ac[1]*pd[1]+pd[2]+ds[0].x;
        pd=py
        y=ac[0]*pd[0]+ac[1]*pd[1]+pd[2]+ds[0].y;
        cr=Region(int(x),int(y),int(w),int(h))
#        print cr
#        print Region(8,37,1323,663)
        if ClientRegion!=cr :
            ClientRegion=cr;
            firstClientRegion=now;
        lastClientRegion=now;
        return cr;
    except:
        print "Failed: updateClientRegion  ";
    return ClientRegion;
updateClientRegion();
print ClientRegion;

global zoo,landmarks,Orig_Xs,Orig_Ys;
global lastLoc;

lastLoc=Location(0,0);
#location sense
Orig_X=0;
Orig_Y=0;
CenterX=0; #screen center to gate
CenterY=0;
DescX=0; #destination to gate
DescY=0;


LocCenter=ClientRegion.getCenter();
#Location(933, 503);//screen select region //can capture! 
def auto(rg,origin): #ClientRegions not ClientRegion
#    if(scenario==origin):
#        return rg;
    return auto_must(rg,origin);
    
def auto_must(rg,origin): #ClientRegions not ClientRegion
    cro=ClientRegions[origin];
    crs=ClientRegion;    #ClientRegions[scenario];    
    return Region(
    (rg.x-cro.x) *crs.w/cro.w+crs.x,
    (rg.y-cro.y) *crs.h/cro.h+crs.y,
    rg.w *crs.w/cro.w,
    rg.h *crs.h/cro.h);
#print auto(ClientRegions[gtx1060],gtx1060);
#print auto(ClientRegions[inossem],inossem);
ROI=[];        
def which_zoo_gtx1060():
    zoo='unknown';
    try:
        zoc=Region(249,75,38,71).find("1646455711214.png");
        zoo="Main";
        return zoo;
    except:
        pass;
    try:
        zoc=Region(249,75,38,71).find("1646455529709.png");
        zoo="Fir";
        return zoo;
    except:
        pass;
    try:
        zoc=Region(249,75,38,71).find("1646455590532.png");
        zoo="Terrarium";
        return zoo;
    except:
        pass;   
    return zoo;
#print which_zoo_gtx1060();
        
def which_zoo_inossem():
    zoo='unknown';
    zoc=None;
    AdvisorRegion=Region(0,0,306,300);
    try:
        zoc=AdvisorRegion.find("1646769583487.png");
        zoo="Main";
        return zoo;
    except:
        pass;
    try:
        zoc=AdvisorRegion.find(managed("1652374285038.png","fir"));
        print zoc;
        if zoc.score>0.85:
            zoo="Fir";
#            return zoo;
    except:
        pass;
    try:
        zoc3=AdvisorRegion.find("1648929649914.png");
        print zoc3;
        if bool(zoc):
            if zoc.score>zoc3.score:
                return zoo;
        if zoc3.score>0.85:
            zoo="Kujali";
            return zoo;
        zoc=zoc3;
    except:
        pass;
    try:
        zoc=AdvisorRegion.find("1646769787903.png");
        zoo="Terrarium";
        return zoo;
    except:
        pass;   
    try:
        zoc=Region(8,104,108,73).find(managed("1652374190639.png","somebody"));
        Log("in somebody houese, hope you can close");
        return zoo;
    except:
        pass;   
    return zoo;
#print which_zoo_inossem();
import os
def Log(str):
    os.system('echo '+str);



which_zoo1={gtx1060:which_zoo_gtx1060,inossem:which_zoo_inossem}[scenario];
oldzoo="unknown";

SetDestFir=0;
SetDestTerrarium=0;

def Hypnagogia(sc):
    if(sc<5):
        sleep(sc);
    else:
        now=datetime.datetime.now();
        togo = now+datetime.timedelta(seconds=sc-5);
        while now<togo:
            locMouse=Mouse.at();
            if locMouse.x<10 and locMouse.y<10:
                return;
            now1=now;
            ScanLandmarks();
            now=datetime.datetime.now();
            sk=(now-now1).total_seconds();
            sc-=sk;
            print(sk,"second killed",sc,"remain");            
        Log("Sleep short of {S}".format(S=sc));
        if(sc<0):
            pass;
#            Log("Sleep short of {S}".format(S=sc));
        else:
            sleep(sc);
            now=datetime.datetime.now();
            print(now);
            
#Hypnagogia(0.1);
#Hypnagogia(4);
#Hypnagogia(40);      

def my_click(loc,sleepy):
    global lastLoc;
    lastLoc=loc;
    mouseMove(lastLoc); 
    mouseDown(Button.LEFT);
    Hypnagogia(0.3);
    mouseUp(Button.LEFT);
    Hypnagogia(sleepy);
    return 0;

def autoscale(loc,origin): #ClientRegions not ClientRegion
    if(scenario==origin):
        if(ClientRegion==ClientRegions[origin]):        
            return loc;
    cro=ClientRegions[origin];
    crs=ClientRegion;
    return Location(
    (loc.x-cro.x) *crs.w/cro.w+crs.x,
    (loc.y-cro.y) *crs.h/cro.h+crs.y);

def my_friend_gonext():
    global lastLoc;
    Hypnagogia(2);
#    lastLoc=Location(564, 487);    #inossem, no use?
    try: 
       lastLoc=auto(Region(396,401,279,150),inossem).find(managed("1651154628086.png","1010"));
       print lastLoc; #score 0.79 faile
       if lastLoc.score>0.84:
           exclude=findBeast(auto(Region(396,401,279,150),inossem),"1653995763648.png","810");
           if exclude==Location(0,0) or exclude.score<lastLoc.score:
        #       click(Location(702, 483));
               lastLoc=lastLoc.offset(140,0);#ok for both
               click(lastLoc);
               Hypnagogia(2);    
               click(LocCenter);
               Hypnagogia(3);
        #       print LocCenter;#L[601,412]@S(0)
               click(autoscale(Location(304, 514),inossem));
               Hypnagogia(0.2);    
               click(autoscale(Location(511, 459),inossem));
               Hypnagogia(0.2);    
               click(autoscale(Location(698, 454),inossem));
               Hypnagogia(0.2);    
               click(autoscale(Location(881, 475),inossem));
               Hypnagogia(2);    
               lastLoc=autoscale(Location(746, 592),inossem); #Redeem
               click(lastLoc);
               Hypnagogia(1);    
    except:
        Hypnagogia(1);
    lastLoc=autoscale(Location(513, 585),inossem);
    try: 
       lastLoc=auto(Region(403,538,251,105),inossem).find(managed("1649620530268.png","Yes"));
    except:
        Log("my_friend_gonext missign Yes ");
#            Location(489, 580) # Yes to next friend
    click(lastLoc);
    sleep(12); #nothing to look at yet
#my_friend_gonext();


import glob
import shutil;
def managed(img, nametag):
#    img="1651154628086.png";nametag="1010";
    scenzoo=scenario+"/"+zoo;
    storepath=getBundlePath()+"\\"+scenzoo;
    if not os.path.exists(img):
        if not os.path.exists(getBundlePath()+"\\"+img):
#            list_of_files = glob.glob(folder_to_file+'/*')
            list_of_files = list_managed(img, nametag);
            if len(list_of_files)==0:
                Log("Sorry no file found for "+nametag+"="+img);
                return img;
            latest_file = max(list_of_files, key=os.path.getctime)
            print(latest_file)            
            return latest_file;
    folder_to_file=storepath+"\\"+nametag;
    path_to_file=folder_to_file+"\\"+img;
    file_exists = os.path.exists(path_to_file); 
    if not file_exists :
        try:
            os.makedirs(folder_to_file);
        except:
            pass;
        Log("shutil.copy {P}".format(P=path_to_file));
        shutil.copy(getBundlePath()+"/"+img, path_to_file);
    return img;
#zoo="Main";
#print managed("1651763228410.png", "1010");
#print managed("1651154628086.png", "1010");

def list_managed(img, nametag):
    paths=[];
    scenzoo=scenario+"/"+zoo;
    storepath=getBundlePath()+"\\"+scenzoo;
    folder_to_file=storepath+"\\"+nametag;
    path_to_file=folder_to_file+"\\"+img;
#    print folder_to_file;
    paths.append(folder_to_file);
    scenzoo=scenario+"/unknown";
    storepath=getBundlePath()+"\\"+scenzoo;
    folder_to_file=storepath+"\\"+nametag;
    path_to_file=folder_to_file+"\\"+img;
#    print folder_to_file;
    paths.append(folder_to_file);
    scenzoo=scenario;
    storepath=getBundlePath()+"\\"+scenzoo;
    folder_to_file=storepath+"\\"+nametag;
    path_to_file=folder_to_file+"\\"+img;
#    print folder_to_file;
    paths.append(folder_to_file);
    storepath=getBundlePath();
    folder_to_file=storepath+"\\"+nametag;
    path_to_file=folder_to_file+"\\"+img;
#    print folder_to_file;
    paths.append(folder_to_file);
    list_of_files=[];
    for path in paths:
        list_of_files.extend(glob.glob(path+'/*'))
    if len(list_of_files)==0:
        print("Sorry no file found for "+img);
        return list_of_files;
#    latest_file = max(list_of_files, key=os.path.getctime)
    list_of_files.sort(key=lambda x: -os.path.getctime(x));    
    return list_of_files;
#print list_managed("1649762735950.png","my_friend_exit");

def entering(zoo):
    if zoo==Terrarium:
        Hypnagogia(1);
        wheel(LocCenter,Button.WHEEL_DOWN,10);
        Hypnagogia(2);
    elif zoo==Main:
        drag(autoscale(Location(403, 651),inossem));
        dropAt(autoscale(Location(750, 136),inossem));
    
def my_friend_exit():    
    try:
        rg=auto(Region(1026,116,155,166),inossem);
        lastLoc=findBeast(rg,"1653518245883.png","my_friend_exit");
        if lastLoc!=Location(0,0):
        #    lastLoc=Location(1169, 133);
            mouseMove(lastLoc);
            mouseDown(Button.LEFT);
            Hypnagogia(0.3);           
            mouseUp(Button.LEFT);
            Hypnagogia(15);
            entering(zoo);
            return 0;
    except:
        #Log("my_friend_exit not found");
        return 999;
#my_friend_exit();

def my_friend_exit_all():
    try:    
        lastLoc=Region(1047,163,84,77).find("1648086212284.png");
        #    lastLoc=Location(1087, 191);
        mouseMove(lastLoc);
        mouseDown(Button.LEFT);
        Hypnagogia(0.3);
        mouseUp(Button.LEFT);
        Hypnagogia(15);
        entering(zoo);
        return 77;
    except:
        Log("my_friend_exit_all not found");
        pass;
#my_friend_exit_all();

def my_friend():
   try:
        lastLoc=ClientRegion.find(managed("1652298276529.png","my_friend")).getTarget(); 
        #was.png for inossem
        return 0;
   except:
       return 999;
#my_friend();

#ClientRegion=Region(5,36,1360,694);#for charlotte @ inossem
#scenario='new';
#meshnet="1651443957097.png";
#LocCenter=ClientRegion.getCenter();
zoo="Main"
#meshnet=managed("1651687266431.png","meshnet");#was 1645891158890.png for inossem
meshnet=managed("1653449826127.png","meshnet");#was 1645891158890.png for inossem
#print meshnet;
butarea={inossem:Region(291,444,477,310),
        gtx1060:Region(548,859,228,203)}[scenario];

def my_friend_meshnet():
       return findBeast(butarea,"1653449826127.png","meshnet"); 
#my_friend_meshnet();
#corco={inossem:Location(1110, 580),gtx1060:Location(1603, 823)}[scenario];
corco=autoscale(Location(1110, 580+20),inossem);
def my_friend1():
   #lastLoc=Location(0,0);
   try:
        lastLoc=my_friend_meshnet();
        if lastLoc!=Location(0,0):
            reachX=200;
            reachY=126;
            offsetY=40;
            #charlotte:
            if(scenario=="gtx1060"):
                reachX=270;
                reachY=150;
                offsetY=40;
            for i in range(21):
                click(lastLoc);
                Hypnagogia(0.1);
                if i>10:
                #meshnet continue exists in shadow, only a pop up can hel
                    try:
                        lastLoc=my_friend_meshnet();
                        print(lastLoc);#0.92
                        if lastLoc.getTarget()==Location(0,0):
                            break;
                        if lastLoc.score<0.85:
                            break;
                        try:
                            ({inossem:Region(515,333,397,343),
                            gtx1060:Region(954,641,390,329)}[scenario]).find(
                                   managed( "1652368662649.png","gohome"));
                            return my_friend_gonext(); 
                        except:
                            type(Key.ESC);
                            pass;
                    except:
                        break;
                loc=corco;
    #            loc=Location(1265, 610);#chalotte@inossem
                drag(loc);
                offs={inossem:[[-reachX,-reachY+offsetY],[-110,155+offsetY],[220,-220+offsetY]],
                        gtx1060:[[-reachX,-reachY+offsetY],[-140,195+offsetY],[270,-295+offsetY]]}[scenario];
                for off in offs:            
                    drag(LocCenter.offset(off[0],off[1]));
                dropAt(LocCenter);
            Hypnagogia(1.2);
            print "Rabbit gone";
            return my_friend_exit();#failed rabit?
   except:
       pass;
   try:
       #        "1645891351088.png"#inossem
       #"1652302078356.png"
        lastLoc=butarea.find(managed("1653446315434.png","ballon")).getTarget(); 
        for i in range(5):
            mouseMove(lastLoc);
            Hypnagogia(0.2);
            mouseDown(Button.LEFT);
            Hypnagogia(0.2);
            mouseUp(Button.LEFT);
            Hypnagogia(0.8);
            loc=corco;
#            loc=Location(1262, 574);#chaelotte@inossem
            mouseMove(loc);
            Hypnagogia(0.4);
            drag(loc);
            Hypnagogia(0.5);
            dropAt(LocCenter);
            Hypnagogia(0.2);
        Hypnagogia(2);
        return my_friend_gonext();
   except:
       pass;
   try:
#        rg=auto(Region(374,628,98,84),inossem);
         #       "1651444630312.png" #charlotte@inossem
         # "1652302181137.png"
        lastLoc=findBeast(butarea,"1653449413546.png","ravin");
        lastLoc=lastLoc.getTarget(); 
        if lastLoc!=Location(0,0):
            for k in range(5):
                click(lastLoc);
#                mouseMove(lastLoc);
#                mouseDown(Button.LEFT);
#                Hypnagogia(0.3);
#                mouseUp(Button.LEFT);
                Hypnagogia(1.25);
                locc=LocCenter.offset(0,-ClientRegion.h/15);
#                mouseMove();
                for i in range(3):
                    click(locc);
#                    mouseDown(Button.LEFT);
#                    Hypnagogia(0.3);
#                    mouseUp(Button.LEFT);
                    Hypnagogia(0.25);
            Hypnagogia(2);
            return my_friend_gonext();
   except:
       pass;
   return 77;
#my_friend_gonext();
#print my_friend1();

menudrop=auto_must(Region(1125,94,102,77),inossem);
print menudrop

def my_friend_menu_drop():
   try:
       #would not found first time and die lock next try, contrast with mouseup without sleep?
        lastLoc=menudrop.find(managed("1652299608937.png","my_friend_menu_drop")); 
        #green triangle point down
#        lastLoc= Region(1159,120,29,31).find("1649554885808.png");        
        lastLoc=lastLoc.getTarget(); 
        click(lastLoc); 
        sleep(1.25);
   except:
       pass;
#my_friend_menu_drop();

class missing:
    successtime=t0;
    failtime=t0;
    failcount=0;
    
    def Failed(self):
        self.failcount+=1;
        if self.failtime<=self.successtime:
            self.failtime=now;
    
    def Success(self):
        if self.failtime>=self.successtime:
            self.successtime=now;
    
MissingTries={"my_friend_menu":missing()};
global pick_my_friend_tbd,lastRegion2X4,Region2X4;
Region2X4=Region(0,0,0,0);
lastRegion2X4=t0;
pick_my_friend_tbd="";
    
def try_update_Region2X4():
    global pick_my_friend_tbd,lastRegion2X4,Region2X4;
    if lastRegion2X4>lastClientRegion:
        if Region2X4!=Region(0,0,0,0):
            return Region2X4; 
    now=datetime.datetime.now();
    lastRegion2X4=now;    
    sample="1652931147389.png";
    name="my_friend_tbd";
    locs=ClientRegion.findAll(managed(sample,name)); 
    #"1649621670263.png","1652300097817.png"
    if locs.hasNext():
        picklocs=list(locs);
#        print picklocs
        scores=map(lambda x: x.getScore(),picklocs);#enumerate can be use enumerated only once
        minavg=sum(scores)/len(scores);
        picksample=sample;
    else :
        print "locs sample empty"
        picklocs=[];
        minavg=0.0;
        picksample="";
    for samply in list_managed(sample,name):
        locsy=ClientRegion.findAll(samply); 
        if not locsy.hasNext():
            continue;
        locsy=list(locsy);
        scores=map(lambda x: x.getScore(),locsy);#enumerate can be use enumerated only once
        avg=sum(scores)/len(scores);
        if avg>minavg:
            minavg=avg;
            picklocs=locsy;
            picksample=samply;
    if len(picklocs)==0:
        #nothing can update tbds
        return Region2X4;
    locs=picklocs;
    samply=picksample;
    pick_my_friend_tbd=picksample;
    print minavg,samply,locs;
    lastLoc=Location(0,0);
    minsc=2.0;
    xs=map(lambda x:x.x,locs);
    x1=min(xs);
    x2=max(xs);
    print x1,x2;
    ys=map(lambda x:x.y,locs);
    y1=min(ys);
    y2=max(ys);
    print y1,y2;
    Region2X4=Region(x1,y1,x2-x1,y2-y1);
    return Region2X4;
#try_update_Region2X4();
#print pick_my_friend_tbd

threashold=[[0.97248,0.937],
        [0.930,0.952],
        [0.942,0.961],
            [0.934,0.948]];
global my_friend_active;
my_friend_active=False;
my_friend_menu_lastVisit=0;
#close friend button: L[1220,163]@S(0) R[20,65 1329x661]@S(0) 0.902934537246 0.1482602118
def my_friend_tbd():
    global my_friend_active;
    global my_friend_menu_lastVisit;
    try_update_Region2X4(); 
    if not bool(pick_my_friend_tbd):
        print "pick_my_friend_tbd is null";
        return;
    locs=ClientRegion.findAll(pick_my_friend_tbd); 
    minsc=5.5;
    lastLoc=Location(0,0);
    for loc in locs:
            col=int(round(float(loc.x-Region2X4.x)/Region2X4.w));           
            row=int(round(float(loc.y-Region2X4.y)*3/Region2X4.h));
#            print loc,row,col,loc.getScore();
#            loc=ClientRegion.find(pick_my_friend_tbd);
            locexclScore=0.0;
            try:
                locexcl=Region(loc.x-60,loc.y-40,120,80).find(managed("1653280765013.png","my_friend_tbd.exclude"))
                locexclScore=locexcl.getScore()
            except:
                pass;
                
#            print loc,locexcl
            if loc.getScore()>locexclScore: #threashold[row][col]:
                sc=(1.0-loc.getScore())/(1.0-threashold[row][col]);
                print sc;
                if sc<minsc:
                    minsc=sc;
                    lastLoc=loc.getTarget();
#        print lastLoc;
    if lastLoc==Location(0,0):
        for loc in locs:
                col=int(round(float(loc.x-Region2X4.x)/Region2X4.w));           
                row=int(round(float(loc.y-Region2X4.y)*3/Region2X4.h));
                print loc,row,col,loc.getScore();# log?
        my_friend_active=False;
        return Location(0,0);
    lastLoc=lastLoc.offset(-30,0);
    click(lastLoc);
    my_friend_active=True;
    Hypnagogia(0.5);
    return lastLoc;
#print my_friend_tbd()

#def find_candy(pic,name):
#    ClientRegion.find(managed(pic,name)); 
#find_candy("1652301900036.png","help");

def my_friend_help():
    global my_friend_active;
    try:
        rg={inossem:Region(397,492,241,114),
                gtx1060:Region(383,556,567,452)}[scenario];
        #rg=ClientRegion; #dont want mess up with help all
        lastLoc=findBeast(rg,"1653444593875.png","help");
        #print lastLoc;
        if lastLoc==Location(0,0): 
            my_friend_active=False;
            return 999;
        lastLoc=lastLoc.getTarget(); 
        #the gray color not exluded?
        #"1645891012840.png"inossm
        friend_active=True;
        click(lastLoc); #need 2 clicks?
        mouseMove(lastLoc);
        mouseDown(Button.LEFT);
        Hypnagogia(2);
        mouseUp(Button.LEFT);
        return 0;
    except:
        my_friend_active=False;
        return 999;
#print my_friend_help()


def my_friend_menu():
#   my_friend_menu_drop(); cannot use safely
    for i in (1,2):
        try:
#            region={inossem:Region(1117,376,78,173),
#            gtx1060:Region(1553,344,240,544)}[scenario];
            region=auto_must(Region(1117,376,78,173),inossem);
            lastLoc=region.find(managed("1652299824877.png","my_friend_menu")).getTarget(); 
            MissingTries["my_friend_menu"].Success();
            break;
        except:
            MissingTries["my_friend_menu"].Failed();
            
        lastLoc=autoscale(Location(1176, 128),inossem);
#        print lastLoc
        click(lastLoc);
        Hypnagogia(2.25);
        if i==2:
            Log('Failed friend menu');
            return 999;
    click(lastLoc);
#    mouseMove(lastLoc);
#    mouseDown(Button.LEFT);
#    Hypnagogia(0.3);
#    mouseUp(Button.LEFT);
    Hypnagogia(5);
    my_friend_in();
#    my_friend_tbd();
    return 0;
#my_friend_menu();

global button_help_all;
def update_button_help_all():
    try:         
#        pic=managed("1652302667522.png","help_all");
        pic=managed("1653443300630.png","help_all");
        button_help_all=ClientRegion.find(pic);
    except:
        print "Failed: update_button_help_all";
#update_button_help_all()

preferedimg={};
def findBeast(rg,img,name): #findBest name used
    global preferedimg;
    try:
        loc=rg.find(managed(img,name)); 
        return loc;
    except:
        pass;
    if bool(preferedimg.get(name)):
        try:
            img=preferedimg.get(name);
            loc=rg.find(img); 
            return loc;
        except:
            pass;
    listimg=list_managed(img, name);
    for img in listimg:
        try:
            loc=rg.find(img); 
            preferedimg[name]=img;
            return loc;
        except:
            pass;
    return Location(0,0);
#t=findBeast(ClientRegion, "1653443901464.png","help_all");

def my_friend_in():
    global my_friend_active;
    #lastLoc=Location(0,0);
    kl=my_friend1();
    if kl==0:
         kl=my_friend1();
    if kl==0:
         kl=my_friend1();
#    my_friend_exit();
    for tt in range(1,10):
       notin=(my_friend_tbd()!=Location(0,0));
       if notin :
             if(my_friend_help()==0):
                 notin=False;             
             else:
                  return 0;    
       else:
            try:    
                rg={gtx1060:Region(1256,805,407,272),
                        inossem:Region(918,480,439,288)}[scenario];
                loc=findBeast(rg, "1653443901464.png","help_all"); 
                print loc
                if(loc==Location(0,0)):
                    print "no help_all";
                    my_friend_active=False;
                    return 999;
                print loc
                drag(autoscale(Location(1007, 329),inossem));
                lastLoc=Location(620, 346);
                dropAt(lastLoc);
                Hypnagogia(3);
            except:
                print "no help_all";
                my_friend_active=False;
                return 999;
            notin=(my_friend_tbd()!=Location(0,0));
       if notin :
             if(my_friend_help()==0):
                 notin=False;             
             else:
                  return 0;    
       for h in range(1,8):
           Hypnagogia(22);
           kl=my_friend1();              
           if kl>0:
               break;
       my_friend_exit();
       
    my_friend_active=False;
    my_friend_exit_all();
    return 999;
my_friend_in();
#my_friend_menu();#close popup still in need

def SetRampDest(x,y) :
    global DescX;
    global DescY;
    DescX=x;
    DescY=y;
    Log('Desc [{X},{Y}]'.format(X=x,Y=y));

locss={
        gtx1060:[Location(487, 337),Location(1510, 305),Location(1569, 876),Location(480, 780)],
        inossem:[Location(236, 243),Location(1018, 262),Location(993, 581),Location(223, 566)]
        };
locs=locss[scenario];


def my_ramp():   
    zoo=which_zoo1();
    if(zoo=="unknown"):
        return 999;
    global lastLoc,DescX,DescY,CenterX,CenterY;
    lastLoc=Location(0,0);
    if len(ROI)>0 :
#        ROI=locs;
#        ROI.append(locs[2]);
        dk=[0]*4;
        Log('ROI={R}'.format(R=ROI[0:5])); #OSError too long
        for r in ROI:
            if r.y>LocCenter.y: 
                if r.x>LocCenter.x:
                    k=2;
                else:
                     k=3;
            elif r.x>LocCenter.x:
                 k=1;
            else:
                 k=0;
            dk[k]+=1;
        kmax=0;
        for k in range(1,4):
            if dk[k]>=dk[kmax]:
                   kmax=k;
#        print(kmax);
        k=kmax;
        Log('go direct {K}'.format(K=k));
    elif(CenterX==0 and CenterY==0):
        k=random.getrandbits(1)*3;
    elif (CenterX!=0 or CenterY!=0) and (DescX!=0 or DescY!=0):
        k=0;
        if(DescX>CenterX):
            k=1;
        if(DescY>CenterY):
            k=3-k;  
        if  CenterX-DescX<1000 and CenterX-DescX>-1000 and CenterY-DescY<500 and CenterY-DescY>-500 :
            lastLoc.x=locs[k].x+CenterX-DescX;
            lastLoc.y=locs[k].y+CenterY-DescY;
            Log('Destination Near {L}'.format(L=lastLoc));
            DescX=0;
            DescY=0;
            k=2;#avoid corner restriction
#    elif CenterX/2-CenterY<5100 and CenterX/2+CenterY<1000 and CenterX/2+CenterY>-800 :
#        Log('Top Left k=2');
#        k=2; #top left
    else :
        k=random.getrandbits(2);
       
    if k==0: #top left
        if(CenterX+CenterY<-24):
            Log('Cancle move Top Left');
            return 0;
    if k==1: #top right
        if(CenterX-CenterY>24044):
            Log('Cancle move Top Right');
            return 0;
    if k==2: #bottom right
        if(CenterX+CenterY>27000):
            Log('Cancle move Bottom Right');
            return 0;
    if k==3: #bottom left
        if(CenterX-CenterY<-144):
            Log('Cancle move Bottom Left');
            k=1;

    if lastLoc.x==0 and lastLoc.y==0:
        lastLoc=locs[(k+2)%4];
        lastLoc=Location(lastLoc.x+random.randrange(-10,10)  ,    
                lastLoc.y+random.randrange(-10,10));
#        Log('Drag to {K}/{L}'.format(K=k,L=lastLoc));


    drag(locs[k]);
    dropAt(lastLoc);
    if(CenterX!=0 or CenterY!=0):
        CenterX-=lastLoc.x-locs[k].x;
        CenterY-=lastLoc.y-locs[k].y;
        Log('Ramp {Z}({X},{Y})'.format(Z=zoo,X=CenterX,Y=CenterY));
    Hypnagogia(0.1);
    ScanLandmarks();
    
          
def  SetCenterEstimate(x,y):
    global CenterX;
    global CenterY;    
    CenterX=x;
    CenterY=y;
    Log(('Center[{X},{Y}]').format(X=CenterX,Y=CenterY));
#SetCenterEstimate(0,0)    ;

#print( Region(174,49,1571,978).find());    
Main="Main";
Fir="Fir";
Terrarium="Terrarium";
Kujali="Kujali";

callback_unknown_recovering=[];
need_my_focus_inossem=False;
need_my_splash=True;
need_my_friend1=False;
def unknown_recovering():
    global need_my_focus_inossem;
    global need_my_splash;
    global need_my_friend1;
    need_my_focus_inossem=True; #must run after my_close;
    need_my_splash=True;
    need_my_friend1=True;
    for x in callback_unknown_recovering:
         x();
#unknown_recovering();
#print need_my_focus_inossem;

now=datetime.datetime.now();
lastVisit={Main:t0,Fir:now,Terrarium:now,Kujali:now};
firstVisit={Main:t0,Fir:t0,Terrarium:t0,Kujali:t0};
Blocked={Main:False,Fir:False,Terrarium:False,Kujali:False};
lastCheck={Main:t0,Fir:now,Terrarium:now,Kujali:now};
oldzoo1="unknown";
OldestZoo="Main";
def UpdateOldestZoo():    
    global OldestZoo;
    old="Main";
    for key in lastVisit:
        if key==zoo:
            continue;
        if(lastVisit[key]<lastVisit[old]):
            old=key;
    OldestZoo=old;

def which_zoo():
   global oldzoo,oldzoo1,OldestZoo;
   now=datetime.datetime.now();
   enabledonzoo=True;
   zoo=which_zoo1(); 
   if(oldzoo1!=zoo) :
       if(zoo!="unknown"):
           if(oldzoo!=zoo):
             Log("{O}=>{Z}".format(O=oldzoo,Z=zoo));
             oldzoo=zoo;
             if(oldzoo!="unknown"):
                 #exiting(oldoldzoo);
                 pass;
             firstVisit[zoo]=now;
             if zoo==OldestZoo:
                 UpdateOldestZoo();
       oldzoo1=zoo;
   if(zoo=="unknown"):
            unknown_recovering();
            Log("back to "+oldzoo);
            #type(Key.ESC);              #queue this , for readonly in this function
            return oldzoo;
   lastVisit[zoo]=now;
   return zoo;

zoo=which_zoo(); #4/2
print(zoo);

def my_goto(zoo):
    if(Blocked[zoo]):
        if lastCheck[zoo]+ datetime.timedelta(minutes=720)>now:
            lastVisit[zoo]=now;
            Log("Access Denied: "+zoo);
            return;
        lastCheck[zoo]=now;
    my_close(); # my friend interrupt
    for i in (1,2):
        try:
            lastLoc=auto(Region(1050,467,170,260),inossem).find(managed("1652270187685.png","gotomap"));
#            print lastLoc; #M[1122,597 31x36]@S(0) S:0.95 C:1137,615 [24 msec]
            lastLoc=lastLoc.getTarget();
            click(lastLoc);
#            mouseMove(lastLoc);
#            mouseDown(Button.LEFT);
#            Hypnagogia(0.3);
#            mouseUp(Button.LEFT);
            Hypnagogia(1.25);
            break;
        except:
           pass;
        lastLoc=Location(1176, 128);
        mouseMove(lastLoc);
        mouseDown(Button.LEFT);
        Hypnagogia(0.3);
        mouseUp(Button.LEFT);
        Hypnagogia(1.25);
        if i==2:
            Log('Failed goto menu');
            return 999;
    lastLoc={Main:Location(498, 327),
            Fir:Location(591, 194),
            Terrarium:Location(373, 540),
            Kujali:Location(765, 627)
            }[zoo];
    checkgate=Region(lastLoc.x-50,lastLoc.y-50,100,100);
    try:
        checkgate.find("1651162705271.png");
        Log( "Blocked:"+zoo);
        Blocked[zoo]=True;
        return;
    except:
        if Blocked[zoo]:
            Log( "Reopen:"+zoo);
            Blocked[zoo]=False;
    mouseMove(lastLoc);
    mouseDown(Button.LEFT);
    Hypnagogia(0.3);
    mouseUp(Button.LEFT);
    Hypnagogia(0.5);
    lastLoc=Location(1032, 458);
    mouseMove(lastLoc);
    mouseDown(Button.LEFT);
    Hypnagogia(0.3);
    mouseUp(Button.LEFT);
    Hypnagogia(1);
    click(Location(1135, 146));#inossem
    Hypnagogia(11);
    entering(zoo);    
    Hypnagogia(5);
    zoo=which_zoo();
    print("went "+zoo);
    return 0;
#my_goto(Fir);
#my_goto(Terrarium);
#my_goto(Main);
#my_goto(Kujali);

landmarkss={
        gtx1060:{
            Main:["1640721586941.png","1640719028561.png","1640720333764.png","1644708172971.png","1640720057152.png","1640721817026.png","1640721745982.png","1640741694803.png","1640744943976.png","1641391579681.png","1641394421693.png","1640536842754.png"]
            ,
            Fir:["1641135019722.png","1641135048732.png","1641135072434.png","1640640250064.png"]
            ,
            Terrarium:["1641135019722.png","1641135048732.png","1641135072434.png","1640640250064.png"]
        },
        inossem:{
            Main:["1640721586941.png","1640719028561.png","1640720333764.png","1644708172971.png","1645764608542.png"
                     ,"1640721817026.png","1640721745982.png","1640741694803.png","1640744943976.png","1641391579681.png","1641394421693.png","1640536842754.png"]
            ,
            Fir:["1641135019722.png","1641135048732.png","1641135072434.png","1640640250064.png"]
            ,
            Terrarium:["1641135019722.png","1641135048732.png","1641135072434.png","1640640250064.png"]
            ,Kujali:["1641135019722.png","1641135048732.png","1641135072434.png","1640640250064.png"]
        }}[scenario];
#Region(302,139,1431,864).find(landmarkss[Main][3]);
zoo=Main;
Orig_XsMain  =[0       ,-7     ,2      ,3        ,-90   ,523    ,1988   ,800    ,-500  ,20000                       ,18000     ,102,0,0,0];
Orig_YsMain  =[0       , 0     ,2      ,3       ,-17   ,215    , 827   ,-110   ,30    ,-1500                       ,-2000     ,-200,0,0,0];
Orig_XsFir  =[0       ,27     ,36         ,638,0,0,0,0,0];
Orig_YsFir  =[0       , -20     ,-100     ,418,0,0,0,0,0];
Orig={
        gtx1060:{ Main:{
            "x":[0       ,-7     ,2      ,3        ,590   ,523    ,1988   ,800    ,-500  ,20000                       ,18000     ,102,0,0,0],
            "y":[0       , 0     ,2      ,3       ,17   ,215    , 827   ,-110   ,30    ,-1500                       ,-2000     ,-200,0,0,0]       
            },
       Fir :{
            "x":[0       ,27     ,36         ,638,0,0,0,0,0],
            "y":[0       , -20     ,-100     ,418,0,0,0,0,0] 
            },
       Terrarium :{
            "x":[0       ,27     ,36         ,638,0,0,0,0,0],
            "y":[0       , -20     ,-100     ,418,0,0,0,0,0] 
            }
     },
        inossem:{ Main:{
            "x":[0       ,-7     ,2      ,3        ,590   ,523    ,1988   ,800    ,-500  ,20000                       ,18000     ,102,0,0,0],
            "y":[0       , 0     ,2      ,3       ,17   ,215    , 827   ,-110   ,30    ,-1500                       ,-2000     ,-200,0,0,0]       
            },
       Fir :{
            "x":[0       ,27     ,36         ,638,0,0,0,0,0],
            "y":[0       , -20     ,-100     ,418,0,0,0,0,0] 
            },
         Terrarium:{
            "x":[0       ,27     ,36         ,638,0,0,0,0,0],
            "y":[0       , -20     ,-100     ,418,0,0,0,0,0] 
            },
         Kujali:{
            "x":[0       ,27     ,36         ,638,0,0,0,0,0],
            "y":[0       , -20     ,-100     ,418,0,0,0,0,0] 
            }
        }
        }[scenario];
Orig_Xs=Orig[zoo]["x"];
Orig_Ys=Orig[zoo]["y"];
landmarks=landmarkss[Main];
freqmarks=[0]*len(landmarks);
ScanLandmarksRegions={
        gtx1060:Region(302,139,1431,864),
        inossem:Region(120,185,993,521)
        }[scenario];

olss={};
import json;
class obj(object):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
               setattr(self, a, [obj(x) if isinstance(x, dict) else x for x in b])
            else:
               setattr(self, a, obj(b) if isinstance(b, dict) else b)
    
def loadpics(zoo):
    p=getBundlePath()+"/"+scenario+"/"+zoo;
    try:
        fls=os.listdir(p);
    except:
        Log("Missing "+p);
        return;
    fls=filter(lambda x: (x[:3]=="tmp" and x[-4:]==".png"),fls);
    gls=map(lambda x: {"g":x[3:-4].split("_"),"x":x},fls);
    #print(tuple(gls)); # 33s
    tls=map(lambda y:({"sz":int(y["g"][0]),"x":int(y["g"][1]),"y":int(y["g"][2])
                ,"pic":y["x"]}),gls);
    ols=map(lambda z:obj(z),tls);
    olss[zoo]=ols;

loadpics("Terrarium");
loadpics("Fir");
loadpics("Main");
loadpics("Kujali");

#print (tls[1].sz);
#print(json.dumps(tls[1])); 
#print(json.dumps(tls)); # 33s
#print(ols[1].sz);
def TooManyNoneOverlap(matches,w) :
    for i in range(len(matches)): 
        if i>=len(matches):
              break;
        if i>2: 
            #dup
              break;
        m=matches[i];
        for j in range(i+1,len(matches)): 
          if j>=len(matches):
              break;
          g=matches[j];
          if abs(m.x-g.x)<w and abs(m.y-g.y)<w :
              print(m,g);
              del matches[j];
              j-=1;

import random;
def ScanLandmarks():
    global landmarks,Orig_Xs,Orig_Ys;
    i = 0;
    loc0=Location(0,0);
    found=0;
    while i < len(landmarks):
        try: 
            loc= ScanLandmarksRegions.find(landmarks[i]);
        except:
            i+=1;
            continue;
        freqmarks[i]+=1;
        found=1;
        Log((zoo+" Landmark[{I},{X},{Y},{N}]={L}-maybe-[{X0},{Y0}]").format(X=Orig_Xs[i],Y=Orig_Ys[i]
                    ,I=i,L=loc,N=freqmarks[i]
                    ,X0=CenterX+loc.x-LocCenter.x,Y0=CenterY+loc.y-LocCenter.y));# Do not use > in Log
        if (loc0==Location(0,0) and (Orig_Xs[i]!=0 or Orig_Ys[i]!=0 or i==0)) :
            loc0=loc;
            i0=i;
            SetCenterEstimate(Orig_Xs[i]-loc.x+LocCenter.x,Orig_Ys[i]-loc.y+LocCenter.y);        
        elif (loc0!=Location(0,0)) :            
            Orig_Xs[i]=loc.x-loc0.x+Orig_Xs[i0];            
            Orig_Ys[i]=loc.y-loc0.y+Orig_Ys[i0];           
            Log("L[{X},{Y}], {I} DERIVED FROM {I0}".format(X=Orig_Xs[i],Y=Orig_Ys[i],I=i,I0=i0));            
        elif (Orig_Xs[i]==0 and Orig_Ys[i]==0 ) :
            Orig_Xs[i]=loc.x+CenterX;
            Orig_Ys[i]=loc.y+CenterY;
            Log('L[{X},{Y}], {I} BY GUESS'.format(X=Orig_Xs[i],Y=Orig_Ys[i],I=i));
        i += 1  ;  
    if found==0 :
        Log("Not found any confirmed near[{X},{Y}]".format(X=CenterX,Y=CenterY));
        if(CenterX==0 and CenterY==0) :
           xx=0;
           ols=olss[zoo];
           for x in ols:
               try :
                   matches=ClientRegion.findAllList(scenario+"/"+zoo+"/"+x.pic);
                   TooManyNoneOverlap(matches,x.sz);
                   loc=matches[0].getTarget();
                   Log("Found {P} @ {L}".format(P=x.pic,L=loc));
                   if len(matches)>=2 :
                       Log("But Too Many"); 
                   xx=x;
                   SetCenterEstimate(xx.x-loc.x+LocCenter.x,xx.y-loc.y+LocCenter.y);        
                   break;
               except:
                   pass;        
           if(xx==0):
                Log("Not found any candidate near[{X},{Y}]".format(X=CenterX,Y=CenterY));
        else:
            scenzoo=scenario+"/"+zoo;
            storepath=getBundlePath()+"/"+scenzoo;
            ols=olss[zoo];
            if len(ols)>0 :
                ols.sort(key=lambda x: abs(x.x-CenterX)+abs(x.y-CenterY));
                Log("Nearest [{X},{Y}] {P} ".format(X=ols[0].x,Y=ols[0].y,P=ols[0].pic));
                try:            
                    loc=ClientRegion.find(scenzoo+"/"+ols[0].pic);
                    Log("Found @ {L}".format(L=loc));
                    return;
                except:
                    Log("Not found, try second ...");                
                    for i in range(1,10):                
                        try:
                            loc=ClientRegion.find(scenario+"/"+zoo+"/"+ols[i].pic);                
                            Log("Found {P} @ {L}".format(P=ols[i].pic,L=loc));
                            return;
                        except:
                            pass;
            sc=clickRange.getScreen();
            for w in range(13,61):
                offsetX=random.randrange(-100,100);
                offsetY=random.randrange(-80,80);
                img=sc.capture(LocCenter.x-w+offsetX,LocCenter.y-w+offsetY,2*w,2*w);#.png
                pngName="tmp{W}_{X}_{Y}.png".format(W=w,X=CenterX+offsetX,Y=CenterY+offsetY);
                print(pngName);
                img.save(storepath,pngName);
                matches=clickRange.findAllList(scenzoo+"/"+pngName);
                TooManyNoneOverlap(matches,w);
                if len(matches)<2 :
                    break;
                os.remove(storepath+"/"+pngName);
    #            [error] OSError ( unlink(): an unknown error occurred: C:\Users\Admin\Documents\trump2024.sikuli\gtx1060\tmp13_2664_408.png )
            print(w);
            for m in matches: 
                print(m);
                  

clickRegions={
        gtx1060: Region(304,146,1435,871),
        inossem: Region(120,168,989,517)
        };
clickRange=clickRegions[scenario];



def my_click(img):   
    global lastLoc;
    try:  
        loc=clickRange.find(img);
        lastLoc=loc.getTarget();        
        mouseMove(lastLoc);
        mouseDown(Button.LEFT);
        Hypnagogia(0.3);
        mouseUp(Button.LEFT);
        Hypnagogia(0.25);
        return 0;
    except:
        return 999;

growupRegions={
        gtx1060:Region(537,734,852,301),
        inossem:Region(322,598,280,122) 
        }[scenario];

def my_GrownUp():
    global lastLoc;
    try:  
        loc=growupRegions.find({gtx1060:"growup.png",
                    inossem:"1648566197856.png"}[scenario]);
        lastLoc=loc.getTarget();        
        mouseMove(lastLoc);
        mouseDown(Button.LEFT);
        Hypnagogia(0.3);
        mouseUp(Button.LEFT);
        Hypnagogia(4.3);
        return 0;
    except:
        return 999;
    return r;
#my_GrownUp();

def my_Fir_gtx1060():   
    r=my_click("1640640040396.png")    ;
    if(r==0):
        r=my_click("1640640105756.png")    ;    
        Hypnagogia(3);
    return r;
def my_Fir_inossem():   
    return 999;
my_Fir={gtx1060:my_Fir_gtx1060,inossem:my_Fir_inossem}[scenario];
def my_Terrarium_inossem():   
    r=my_click("1648057110727.png")    ;
    if(r==0):
        r=my_click("1648056732577.png")    ;    
        Hypnagogia(5);
        wheel(LocCenter,Button.WHEEL_DOWN,10);
    return r;
#my_Terrarium_inossem(); tested 3/23/2022
def my_Terrarium_gtx1060():   
    r=my_click("1640640040396.png")    ;
    if(r==0):    
        r=my_click("1640640267632.png")    ;    
        Hypnagogia(5);
        wheel(LocCenter,Button.WHEEL_DOWN,10);
    return r;
my_Terrarium={gtx1060:my_Terrarium_gtx1060,inossem:my_Terrarium_inossem}[scenario];

my_cash_pic={gtx1060:"1640407206306.png",
                inossem:"1645890337103.png"
                }[scenario];

def my_many_cash():   
    global lastLoc;
    locs=list(clickRange.findAll(managed(my_cash_pic,"my_cash")));
    if len(locs)>0:
        for loc in locs:
            lastLoc=loc.getTarget();
            click(lastLoc);
#            mouseMove(lastLoc);
#            mouseDown(Button.LEFT);
#            Hypnagogia(0.1);
#            mouseUp(Button.LEFT);
            Hypnagogia(0.1);
        return 0;
    return 999;
#my_many_cash();

def my_cash():   
    r=my_click(managed(my_cash_pic,"my_cash"))    ;
#    Hypnagogia(1.6);
    return r;
def my_cash_bronze():   
    r=my_click({gtx1060:"1640540150379.png",
                inossem:"1645904477007.png"
                }[scenario])    ;
#    Hypnagogia(1.6);
    return r;

def my_cash1():
    global lastLoc;
    try:  
        loc= Region(304,146,1435,871).find("1640407206306.png");
        lastLoc=loc.getTarget();
        mouseMove(lastLoc);
        mouseDown(Button.LEFT);
        Hypnagogia(0.3);
        mouseUp(Button.LEFT);
        Hypnagogia(0.3);
        return 0;
    except:
        return 999;
       
       #Region(337,143,1273,847)
mmd = Settings.MoveMouseDelay # save default/actual value
Settings.MoveMouseDelay = 1
def my_trash():   
    global lastLoc;
    try:   
        lastLoc=clickRange.find(scenario+'/'+"trash.png").getTarget();
        clickRange.click((scenario+'/'+"trash.png"));

#        mouseMove(lastLoc);
#        mouseDown(Button.LEFT);
        Hypnagogia(0.2);
#        mouseUp(Button.LEFT);
        Hypnagogia(0.3);
        return 0;
    except:
        return 999;
def my_many_trash():   
    global lastLoc;
    locs=list(clickRange.findAll(scenario+'/'+"trash.png"));
    if len(locs)>0:
        for loc in locs:
            lastLoc=loc.getTarget();
            click(lastLoc);
#            mouseMove(lastLoc);
#            mouseDown(Button.LEFT);
#            Hypnagogia(0.1);
#            mouseUp(Button.LEFT);
#            Hypnagogia(0.1);
        return 0;
    return 999;
my_many_trash();

def my_coin():   
    global lastLoc;
    try:   
        loc= {
gtx1060:        Region(383,188,1227,723),
                inossem:clickRange}[scenario].find(
                {gtx1060:"1640236026729.png",
                    inossem:"1645717326846.png"
                    }[scenario]).getTarget();
        lastLoc=loc.offset(0,-9);
        click(lastLoc);
#        mouseMove(lastLoc);
#        mouseDown(Button.LEFT);
#        Hypnagogia(0.3);
#        mouseUp(Button.LEFT);
#        Hypnagogia(1.8);
        return 0;
    except:
        return 999;
#my_coin(); tested 3/23/2022


def my_star():   
    global lastLoc;
    try:   
        lastLoc=clickRange.find(scenario+'/'+ "star.png").getTarget();
        click(lastLoc);
#        mouseMove(lastLoc);
#        mouseDown(Button.LEFT);
#        Hypnagogia(0.6);
#        mouseUp(Button.LEFT);
        Hypnagogia(0.6);
        return 0;
    except:
        return 999;
#my_star();

#  Region(352,167,1185,721);
feedLoc={
            gtx1060:Location(960, 527),
            inossem:LocCenter
            }[scenario];
def my_feed():
    global lastLoc;
    global CenterX;
    global CenterY;    
    try:
        loc1= clickRange .find(scenario+'/'+"feed.png").getTarget();
        click(loc1);
        r=my_feed1(feedLoc);
        if(CenterX!=0 or CenterY!=0):
            CenterX-=lastLoc.x-loc1.x;
            CenterY-=lastLoc.y-loc1.y;
            Log('Feed ({X},{Y})'.format(X=CenterX,Y=CenterY));
        return 0;
    except:
        return 999;
#print my_feed()   

def my_feed1(feedLoc):
    global lastLoc;
    global CenterX;
    global CenterY;    
    loc={
            gtx1060:Location(1390, 464),
            inossem:Location(964, 374)
            }[scenario];
    try:
        loc=ClientRegion.find(managed("1653360099807.png","my_feed1"));
    except:
        pass;
    mouseMove(loc);
    mouseDown(Button.LEFT);
    Hypnagogia(0.4);#hold and relase and hold >=0.34, depend on loading
    #may enter state hard to recover
    mouseUp(Button.LEFT);
    Hypnagogia(0.1);#hold and relase and hold >=0.34, depend on loading/zoo?
    mouseDown(Button.LEFT);
    Hypnagogia(0.1);#hold and relase and hold >=0.34, depend on loading
    drag(loc);
    lastLoc=feedLoc;
    if(zoo=="Terrarium"):
        drag(Location(lastLoc.x,lastLoc.y/2)); #do no devide itself, it actually LocCenter by object reference
    dropAt(lastLoc);
    #this program may stuck, need an absolut exit
#            lastLoc=Location(1073, 404);click(lastLoc); #inossem the close button 
#            auto(Region(1007,329,148,179),inossem).click(managed("1651411946642.png","close feed")); 
    #inossem the close button 
    return 0;
#print my_feed1(???)   

def my_water():
    global lastLoc;
    try:    
        work={ 
        gtx1060:[Region(439,216,1083,712),"water.png"]
                ,
       inossem:[clickRange.grow(-50),inossem+"/"+"water.png"]
                }[scenario];
        loc=work[0].find(work[1]).getTarget();
        drag(loc);
        Hypnagogia(0.1);
#        mouseMove
        drag(loc.offset(100,80));
        Hypnagogia(0.1);
#        mouseMove
        drag(loc.offset(-100,80));
        Hypnagogia(0.1);
        drag(loc.offset(-100,-80));
        Hypnagogia(0.1);
        drag(loc.offset(100,-80));
        Hypnagogia(0.1);
        dropAt(loc);
        lastLoc=loc;    
        return 0;
    except:
        return 999;
#my_water();

mROUTHANLY=0;
lastROUTHANLY=now;
tbdROUTHANLY=now;
def     ROUTHANLY():
    global mROUTHANLY,lastROUTHANLY,tbdROUTHANLY;
    if(lastROUTHANLY<=tbdROUTHANLY):
        lastROUTHANLY=now;
        mROUTHANLY=(clickRange.w+clickRange.h)/10;
    return mROUTHANLY; 
def abs(x):
    if x>0 :
        return x;
    return -x;

import math;
def my_many_water():
    global lastLoc;
    try:    
        work={ 
        gtx1060:[Region(439,216,1083,712),"water.png"]
                ,
       inossem:[clickRange.grow(-20),
                    "1649023518496.png"
#       "1649021770300.png"
                   ]
                }[scenario];
    except:
        return 999;
    locs=list(work[0].findAll(work[1]))+list(work[0].findAll("1649030194070.png")); 
    if len(locs)==0:
        return 999;
    if len(locs)==1:
        click(locs[0]);
        return 0;
#    locs=sorted(locs,key=lambda m:math.atan2(m.x-LocCenter.x,m.y-LocCenter.y));
    locs=sorted(locs,key=lambda m:math.pi*(-2.0)*
            int(math.sqrt((m.x-LocCenter.x)**2+(m.y-LocCenter.y)**2)/3/ROUTHANLY())
            +math.atan2(m.x-LocCenter.x,m.y-LocCenter.y));
    tt=True;
    loc1=Location(0,0);
    for loc in locs:
        if tt :
            drag(loc);
            tt=False;
            loc1=loc;
            continue;
#        print(loc);
        if(abs(loc1.x-loc.x)*3<ROUTHANLY() and abs(loc1.y-loc.y)*3<ROUTHANLY() ):
            continue;
        loc1=loc;
        drag(loc);        
    inRange=clickRange.grow(-100);
    
#    if(loc.x>inRange.x and loc.y>inRange.y and 
#            loc.x<inRange.getBottomRight().x and loc.y<inRange.getBottomRight().y) :
#        drag(loc);
#        drag(loc.offset(100,80));
#        drag(loc.offset(-100,80));
#        drag(loc.offset(-100,-80));
#        drag(loc.offset(100,-80));
    dropAt(loc);
    lastLoc=Location(0,0);    
    return 0;
#my_many_water(); #tested 4/3

woverh=3;
trail=[ 
        [woverh,0,0.05],
        [-woverh-1,0,0.05],
        [-woverh-1,-1,0.05],
        [0,-1,0.05],
        [woverh+1,-1,0.1],
        [woverh+1,1,0.1],
        [0,1,0.1],
        [-woverh-2,1,0.1],
        [-woverh-2,-2,0.1],
        [0,-2,0.1],
        [woverh+2,-2,0.1],
        [woverh+2,+2,0.1],
        [0,+2,0.1],
        [-woverh-3,+2,0.1],
        [-woverh-3,-3,0.1],
        [0,-3,0.1],
        [woverh+3,-3,0.1],
        [woverh+3,+3,0.1],
        [0,+3,0.1],
        [-woverh-4,+3,0.1],
        [-woverh-4,-4,0.1],
        [0,-4,0.1],
        [woverh+4,-4,0.1],
        [woverh+4,+4,0.1],
        [0,+4,0.1],
        [-woverh-5,+4,0.1],
        [-woverh-5,-5,0.1],
        [0,-5,0.1],
        [woverh+5,-5,0.1]
        ];
def my_poo_star():
    for i in range(2):
        try:
           # print auto(Region(356,620,220,101),inossem);           #R[633,870 292x161]@S(0)
#            rg=Region(485,845,318,204);#?gtx
            rg=auto(Region(294,593,231,165),inossem);#inossem
#            print rg;
            if rg.y+rg.h>ClientRegion.y+ClientRegion.h:
                rg.h=ClientRegion.y+ClientRegion.h-rg.y;
#            print rg;            
            #print rg; #R[485,845 318x204]@S(0)
            loc=rg.find(managed("1652277301831.png","my_poo_star"));           
            return True;
        except:
            if i==1:            
                Hypnagogia(1.5);
    return False;
#print (my_poo_star());
poobrush={gtx1060:"1640317826765.png",
                inossem:"1646838706009.png"
                }[scenario];
poorange={gtx1060: Region(219,96,1482,923),
            inossem:ClientRegion
            }[scenario];

def my_poo_find_inossem():
        return clickRange.find("1646838657680.png");

def my_poo_find_gtx1060():
        return {gtx1060: Region(340,186,1294,772),
                inossem:clickRange
                }[scenario].find({gtx1060:"1640315967731.png",
                    inossem:"1646838657680.png"
                    }[scenario])    
my_poo_find={gtx1060:my_poo_find_gtx1060,inossem:my_poo_find_inossem}[scenario];

def my_poo():
    global lastLoc;
    try:    
        loc=my_poo_find();
        loc=loc.getTarget();
        loc0=loc;
    except:
        return 888;
    mouseMove(loc);
    mouseDown(Button.LEFT);
    Hypnagogia(0.3);
    mouseUp(Button.LEFT);
    lastLoc=loc;    
    Hypnagogia(2);
    try:
        loc=poorange.find(poobrush).getTarget();
        print "pooof",CenterX,CenterY;
    except:
        Log("Missingg poo brush!");
        return 999;
    wheel(loc,Button.WHEEL_DOWN,10);
    #mouseDown(Button.LEFT);
    drag(loc);
    Hypnagogia(0.1);
    poogrid=auto(Region
            (0,0,70,60),gtx1060); 
    #            (0,0,80,50)
    print "poogrid=",poogrid;
    for t in trail:
        lastLoc=Location(t[0]*poogrid.w+LocCenter.x,t[1]*poogrid.h+LocCenter.y);
#        mouseMove(lastLoc);    
        drag(lastLoc);
        Hypnagogia(t[2]);
        if not my_poo_star():
            Log("Done poo brush");
#            mouseUp(Button.LEFT);
            dropAt(lastLoc);
            Hypnagogia(1);
            return 0;
#    mouseUp(Button.LEFT);
    Hypnagogia(0.1);
#    mouseDown(Button.LEFT);
    for i in range(1,5):
        for j in range(1,3):
            if not my_poo_star():
                Log("Done poo brush");
                dropAt(lastLoc);
#                Hypnagogia(1);
                return 0;
            try:
                loc= ClientRegion.find(poobrush).getTarget();
                break;
            except:
                Hypnagogia(0.2);
                pass;
        if j>=4 :
            Log("Done poo brush");
            dropAt(lastLoc);
#            Hypnagogia(1);
            return 0;
        cl=ClientRegion.grow(-50);
        lastLoc=Location(random.randrange(cl.x,cl.x+cl.w),
                            random.randrange(cl.y,cl.y+cl.h));
        dropAt(lastLoc);
        Hypnagogia(0.1);
    Log("Failed poo brush {L}".format(L=loc0));
    #mouseUp(Button.LEFT);
    dropAt(lastLoc);
    return 999;
#my_poo();

#print(1==1);
def merge_regions(regions):
    x=min(map(lambda x:x.x,regions));
    y=min(map(lambda x:x.y,regions));
    return Region(x,y,
            max(map(lambda x:x.x+x.w,regions))-x,
            max(map(lambda x:x.y+x.h,regions))-y
            );
#print merge_regions([Region(1501,39,163,253),Region(1640,42,112,124)]);
def my_close_gtx1060():        
    global lastLoc;
    type(Key.ESC);             
    while 1==1:
        try:   
           loc= Region(1286,276,220,174).find("1641265807541.png");
           Log('Close 1');
           break;
        except:
           pass;        
        try:   
           loc= Region(1501,39,163,253).find("1640403388181.png");
           Log('Close 2');
           break;
        except:
           pass;        
        try:   
            loc= Region(1360,58,260,509).find("1640230482499.png");
            Log('Close 3');
            break;
        except:
            pass;
        try:   
            loc= Region(1285,253,211,233).find("1640398758304.png");
            Log('Close 4');
            break;
        except:
            pass;
        try:   
            loc= Region(1475,457,193,144).find("1640537041268.png");
            Log('Close 5');
            break;        
        except:
            pass;
        try:   
            loc= Region(1504,466,167,159).find("1640538477820.png");
            Log('Close 6');
            break;        
        except:
            pass;
        try:   
           loc= Region(1640,42,112,124).find("1640539750376.png");
           Log('Close 7');
           break;
        except:
           pass;        
        try:   
           loc= Region(869,121,105,89).find("1646141916266.png");
           Log('Close superDeal inossem');
           break;
        except:
           pass;        
        return 999;
    
    mouseMove(loc);
    mouseDown(Button.LEFT);
    Hypnagogia(0.3);
    mouseUp(Button.LEFT);
    Hypnagogia(1);        
    lastLoc=loc.getTarget();    
    return 0;

SteamMode=False;
#if zoo is not found
def my_focus_inossem():#also other recovers        
    global SteamMode;
    if QuitGame:
        SteamMode=True;
    if SteamMode:
        print("don't know how to get focus?");
        return;
    global need_my_focus_inossem;
    if need_my_focus_inossem: 
       need_my_focus_inossem=False;
    try:   
       loc= Region(14,0,405,35).find(managed("1652374584338.png","pandaicon"));
       if which_zoo_inossem()=="unknown":
            mouseMove(loc);
            mouseDown(Button.LEFT);
            sleep(0.2);
            mouseUp(Button.LEFT);                    
            type(Key.ESC);             
            sleep(0.2);
            Log('Recover tab');
    except:
       pass;        
    try:
       for i in Range(24):
           loc= auto(Region(398,376,445,313),inossem).find(managed("1652488232002.png","reload"));
           Log('Reloading');
           sleep(3*60);
       click(loc);
       Log('Reload');
       sleep(20);
    except:
       pass;        
#my_focus_inossem();

def my_close_feed():
    try:
        loc=ClientRegion.find(managed("1653359955691.png","my_close_feed"));
        my_feed1(loc.offset(0,ClientRegion.h/4));        
    except:
        pass;
#my_close_feed();
global button_close_friend;
def update_button_close_friend():
#only call this after menu click
    try:         
        button_close_friend=ClientRegion.find(managed("1653162976076.png","button_close_friend"));
        button_close_friend=button_close_friend.getTarget();
        print button_close_friend,ClientRegion,float(button_close_friend.x-ClientRegion.x)/ClientRegion.w,float(button_close_friend.y-ClientRegion.y)/ClientRegion.h;
        #0.902934537246 0.1482602118
        #how to avoid mess up other close button
    except:
        print "Failed: update_button_close_friend";
#update_button_close_friend()

global QuitGame;
QuitGame=False;
def my_close_inossem():        
    global lastLoc;
    global QuitGame;
    try:
        loc=ClientRegion.find("1653352410294.png")
        type(Key.ESC);
        QuitGame=True;
        return 0;
    except:
        pass;
    if not(QuitGame):
        type(Key.ESC);             
    elif random.random()<0.05:
        type(Key.ESC);             
    #hard to close, stuck in feed
    my_close_feed();    
    while 1==1:
        try:   
           loc= Region(850,95,166,130).find(managed("1652377567329.png","superdeal")); #super deal tbd
           Log('Close 0 super deal');
           break;
        except:
           pass;        
        try:   
           loc= Region(918,106,174,124).find("1645849535010.png"); #dialog
           Log('Close 1 dialog');
           break;
        except:
           pass;        
        try:   
           loc= Region(758,195,198,196).find("1645882887382.png");
           Log('Close 2 small dialog');
           break;
        except:
           pass;        
        try:   
            loc= Region(1093,53,203,163).find(managed("1653736131771.png","my_close.dirty"));
            print loc;
            Log('Close 3 dirty ');
            break;
        except:
            pass;
        try:   
            loc= Region(1285,253,211,233).find("1640398758304.png");
            Log('Close 4'); #cover same button for my_friend_exit?
            break;
        except:
            pass;
        try:   
            loc= Region(1082,99,154,84).find("1648564925872.png");
            Log('Close friend scene');
            break;
        except:
            pass;
        try:   
           loc= Region(869,121,105,89).find("1646141916266.png");
           Log('Close superDeal inossem');
           break;
        except:
           pass;        
        return 999;
    click(loc);
#    mouseMove(loc);
#    mouseDown(Button.LEFT);
#    Hypnagogia(0.3);
#    mouseUp(Button.LEFT);
    Hypnagogia(0.5);        
    lastLoc=loc.getTarget();    
    return 0;
#my_close_inossem();

my_close={gtx1060:my_close_gtx1060,inossem:my_close_inossem}[scenario];
#my_close();

def my_ball():    
    global lastLoc;
    try:   
        loc= {gtx1060:Region(383,188,1227,723),
                inossem:clickRange
                }[scenario].find({
                    gtx1060:"1640310968315.png",
                    inossem:"1645925652733.png"
                    }[scenario]);
        mouseMove(loc);
        mouseDown(Button.LEFT);
        Hypnagogia(0.4);
        mouseUp(Button.LEFT);
        Hypnagogia(0.2);
        mouseDown(Button.LEFT);
        Hypnagogia(0.4);
        mouseUp(Button.LEFT);
        Hypnagogia(0.2);
        mouseDown(Button.LEFT);
        Hypnagogia(0.4);
        mouseUp(Button.LEFT);
        Hypnagogia(0.2);
        mouseDown(Button.LEFT);
        Hypnagogia(0.4);
        mouseUp(Button.LEFT);
        Hypnagogia(2.2);
        lastLoc=loc.getTarget();
        return 0;
    except:
        return 999;    

first_try=1;
def my_first_try():
    global first_try;
    if first_try==1:
        first_try=0;
        drag(Location(981, 930));
        dropAt(Location(1047, 210));
        Hypnagogia(0.3);
        drag(Location(901, 519));
        mouseMove(Location(932, 600));
        Hypnagogia(0.3);
        mouseMove(Location(1741, 550));
        Hypnagogia(0.1);
        dropAt(Location(1618, 618));        
#my_first_try();
#ScanLandmarks();

menu={inossem:Region(9,221,86,466),
    gtx1060:Region(178,177,126,806)}[scenario];

def my_born():
  try:
    ClientRegion.click(managed("1652303915096.png","born"));
    sleep(1);
    auto(Region(420,428,337,223),inossem).click(managed("1652304012516.png","Okay"));
    return 0;
  except:
    return 999;
print my_born();

def my_animal_level():
    if(my_click( {
                gtx1060:"1642273227689.png",
                inossem:"1645883000530.png"
           }[scenario]     )==0): 
        lastLoc=Location(947, 562);
        mouseMove(lastLoc);
        mouseDown(Button.LEFT);
        Hypnagogia(0.3);
        mouseUp(Button.LEFT);
        Hypnagogia(0.3);
        lastStatus='Animal Level';
        return 0;
    return 999;
global poppy;
poppy=-1;

def my_zoo():
    global lastVisit,firstVisit,Blocked,lastCheck,lastPoppyVisit,zoo,oldzoo,OldestZoo;
    now=datetime.datetime.now();
    Log("zoo:{T}".format(T=now));
    if ispoppydays(now):
        Log("poppy time");
        if lastPoppyVisit+datetime.timedelta(minutes=31)<now and firstVisit[zoo]+datetime.timedelta(minutes=24)<now:
            if zoo!='Main':
                if my_goto(Main)==0:
                    SetRampDest(-100,20); 
                    #Dest subsbribe zoo, to be poppy
                    return 0;
                Log("failed my_goto(Main) ?");
    wishzoo=OldestZoo;
    stayTime={Main:35,Fir:15,Terrarium:8,Kujali:11};
    t1=firstVisit[zoo]+ datetime.timedelta(minutes=stayTime[zoo]);
    if wishzoo==zoo:
        if t1>now:
            Log("Will change after {T}".format(T=t1));
            return 999;
        else :
            UpdateOldestZoo();
            wishzoo=OldestZoo;
    Log("wishzoo="+wishzoo);
    if firstVisit[zoo]+ datetime.timedelta(minutes=stayTime[zoo])<now :
        print zoo,"->",wishzoo;
        if(my_goto(wishzoo)==0):            
                lastVisit[wishzoo]=now;
                zoo=wishzoo;                
                landmarks=landmarkss[zoo];
                Orig_Xs=Orig[zoo]["x"];
                Orig_Ys=Orig[zoo]["y"];
                return 0;
    return 999;

def ispoppydays(now):
    return (now.month==2 and now.day>=14 and now.day<=14+14 #valentine
        or now.month==4 and now.day>=6 and now.day<=6+14  #easter early?
        or now.month==5 and now.day>=4 and now.day<=4+14 ); #monthers day
            
now = datetime.datetime.now();
#print ispoppydays(now);

try:
    loc= {                
                gtx1060:Region(167,45,137,132), 
                inossem:Region(7,106,77,73) 
                }[scenario].find({ 
                gtx1060:"1644387272438.png", 
                    inossem:"dochead.png" 
                    }[scenario]);
    running=999;
except:
    running=-1;
Log("LocCenter={L}".format(L=LocCenter));
mPoppyLast=0;    
last_fail_poo=now;
lastStatus='init';
t0=datetime.datetime(1,1,1);
my_friend_active=False;
my_friend_menu_lastVisit=now;
lastPoppyVisit=t0;
while 1==1 :    
    now = datetime.datetime.now();
    #print(now.year, now.month, now.day, now.hour, now.minute, now.second)
    if(scenario=='gtx1060'):
        if(running<999) :
            if running!=now.hour:
                if now.hour%2==0 :
                    if(scenario=='gtx1060'):
                        os.system('start steam://rungameid/1352330');
                        Hypnagogia(150);                        
                        my_click("1640459738300.png"); 
                        #to be my_splash
                   # if(scenario=='inossem'):
                else :
                    Hypnagogia(3*60);
                    if( #now.hour>8 and 
                            Mouse.at().x<10 and Mouse.at().y<10) :
                        break;#exit
                    continue;
    running=now.hour;
    Log("running=now.hour");
    i =1;
    NLOOP=500;#1000;
    first_try=1;
    startTime = datetime.datetime.now();   
    if ispoppydays(now) :
        #Monday, February 14 valentine
        #Sunday, April 17 easter
        poppy=0;SetRampDest(100,100);                
    displaceCount=0;    
    lastRun=my_friend;
    while i<NLOOP:
        now = datetime.datetime.now();
        oldz=zoo;
        zoo=which_zoo();
        print(zoo); 
        if zoo=="unknown" :
            zoo=oldz;
            if zoo=="unknown" :
                zoo=Main;
        landmarks=landmarkss[zoo];
        Orig_Xs=Orig[zoo]['x'];
        Orig_Ys=Orig[zoo]['y'];
        
        if(lastLoc!=Location(0,0)): # and now.hour>=8 and now.hour<=22):
            locMouse=Mouse.at();
            dx=lastLoc.x-locMouse.x;
            dy=lastLoc.y-locMouse.y;            
            if( dx*dx+dy*dy>200):
                print('displaced',lastLoc,locMouse,lastStatus);                                
                displaceCount+=1;
                if(displaceCount>=2):
                    #https://sikulix-2014.readthedocs.io/en/latest/interaction.html
                    result=Do.popAsk('Stop?','',8);#,location=Location(30,30));
                    if None == result:
                      print "nothing to do"
                    elif result:
                      print "user said yes";
                      x = input('Exit/idle/nothing):');
                      if x==None :
                          pass;
                      elif x=='' :
                          pass;
                      elif (x[0]=='i'):
                          locMouse=Mouse.at();
                          for y in range(30):
                              Hypnagogia(3*60);
                              locMouse1=Mouse.at();
                              if(locMouse==locMouse1):
                                  Log("Idel detected");                                   
                                  break;
                              locMouse=locMouse1;
                      elif(x>' ' and x[0]!='n') :
                          break;
                    else:
                      print "user said no"
            else:
                displaceCount=0;
        else :
           if((now-startTime).total_seconds()>50*60):
               i=NLOOP;
               break;
        i+=1;
        if(need_my_splash):
            need_my_splash=False;
            if(my_click(managed("1652449514171.png","Splash"))==0):
                lastStatus='Splash';                
                continue;
        mine=[my_animal_level,my_close,my_star,my_GrownUp,my_many_cash,my_many_trash,my_coin,
                my_cash,my_born,my_cash_bronze,my_many_water,my_ball,my_water,my_direct_water
                ,my_direct_ramp,my_feed,my_direct_ramp_right,my_direct_ramp_left
                ,my_focus_inossem,my_zoo];
        did=False;
        for my in mine:
            if my==lastRun:
                #do not repeat? helping out corner stuck
                continue;
            print my;
            if(my()==0):
                did=True;
                lastRun=my;
                lastStatus="{F}".format(F=my)
                break;
        if did:
            continue;
        lastRun="otherdeeds";
#        if need_my_focus_inossem: 
#           need_my_focus_inossem=False;
#           my_focus_inossem();
        if(my_click("1640869435405.png")==0): #over by cash，trash
            lastStatus='Great gtx1060';
            continue;
        if(my_click("1646006271068.png")==0): #over by cash，trash
            lastStatus='Great inossem';
            continue;
        if(my_click("1640623363794.png")==0):
            lastStatus='breed';
            continue;
        if(my_click(managed("1652286241635.png","poppy"))==0):
                #mothers day
               poppy+=1;
               lastPoppyVisited=now;
               orgPoppy=lastLoc.offset(CenterX-LocCenter.x,CenterY-LocCenter.y);
               Log("{T}:Found poppy {L}".format(T=lastPoppyVisited,L=orgPoppy));
               lastStatus='poppy';
               continue;
        if not my_friend_active: 
            if my_friend()==0:
                my_friend_active=True;           
                Log('my_friend_active , last try {T}'.format(T=my_friend_menu_lastVisit));
                lastStatus='friend';           
                continue;
#        print(my_friend_active);
        if my_friend_active :
            Log("my_friend_menu_lastVisit={T}".format(T=my_friend_menu_lastVisit));
            t=my_friend_menu_lastVisit+ datetime.timedelta(minutes=4);
            if(t<now):
                my_friend_menu_lastVisit=now;
                Log('my_friend_menu {T}'.format(T=my_friend_menu_lastVisit));
                my_friend_menu();
                lastStatus='friend menu';                       
                my_friend_active =False;
                continue;
        if(my_click("1640869544082.png")==0):
           lastStatus='check';
           continue;
        if(last_fail_poo+ datetime.timedelta(minutes=3) <now): 
            mypoo=my_poo();
            if(mypoo==999):
                last_fail_poo=now;
                continue;
            elif mypoo!=888:
                continue;

#set destination
##        if(enabledonzoo): 
        my_ramp();
        ROI=[];
    if(i<NLOOP) :
        break;
    os.system('taskkill /IM zoo2.exe');
######################
#stop
#to develop for "no space"



def notyet():
        
    "1641014760839.png"
    
    try:   
            loc= Region(590,899,159,131).find("1640306344923.png");
            mouseMove(loc);
            mouseDown(Button.LEFT);
            Hypnagogia(0.1);
            mouseUp(Button.LEFT);
            loc=Location(1597, 901);
            mouseMove(loc);
            Hypnagogia(0.05);
            #mouseDown(Button.LEFT);
            #Hypnagogia(0.5);#
            #mouseUp(Button.LEFT);
            #Hypnagogia(1.5);
            drag(loc);
            Hypnagogia(0.1);        
            mouseMove(Location(517, 390));
            Hypnagogia(0.1);        
            dropAt(Location(807, 504));
            Hypnagogia(1);        
    except:
           i=999;
            
    
    #Debug.user("hello from JavaScript");
    #Debug.level = 3;
    #Settings.OverwriteImages = 1;
    
    imgPath = getImagePath() # get the list
    print imgPath
    # to loop through
    for p in imgPath:
            print p

poppy=-1;
def poppymenu():   
    if ispoppydays(now):
            if(poppy<0) :
                try:
# "1644682415730.png" #poppy on menu, valentine
                   menu.find(
                           "1651663081444.png"
                           ); #mothers day
                   poppy=0;        
                except:
                   pass;
#"1644338915756.png" #poppy image valentine?
#"1649303197390.png"#easter egg
            PoppyCenterX=22;
            PoppyCenterY=50;        
            if(CenterX<PoppyCenterX+50 and CenterX>PoppyCenterX-50 and CenterY>PoppyCenterY-50 and CenterY<PoppyCenterY+50):
                SetRampDest(0,0);
                Log('All poppy gone');
            mPoppy=int(now.minute/6);
            #Log('Poppy Minuter={m}'.format(m=mPoppy));
            if(mPoppy!=mPoppyLast):
                mPoppyLast=mPoppy;
                SetRampDest(PoppyCenterX,PoppyCenterY);
                Log('Where is poppy?');

poppymenu();


research20220603mom=["1654253115297.png""1654253130553.png""1654253218427.png"];
research20220602gxt1060=["1654216372174.png","1654216443750.png","1654216482447.png","1654216528869.png","1654216900072.png","1654216955197.png","1654216981472.png","1654217008071.png",
        "1654217043760.png""1654217080165.png""1654217110710.png""1654217142276.png""1654217174634.png""1654217210442.png""1654217230861.png""1654217254557.png""1654217287737.png""1654217309163.png""1654217333725.png""1654217351165.png""1654217382882.png"
"1654217427420.png","1654217579782.png","1654217594047.png"       
        ];#jhohose done
research20220602mom=["1654218920852.png""1654219492449.png""1654219625302.png""1654219716427.png""1654219769328.png"];
research20220602trump=["1654220755557.png""1654220987936.png"];

import gc
gc.collect()    


def dump_garbage():
    # force collection
    print "\nGARBAGE:"
    gc.collect()

    print "\nGARBAGE OBJECTS:"
    for x in gc.garbage:
        s = str(x)
        if len(s) > 80: s = s[:80]
        print type(x),"\n  ", s

    if __name__=="__main__":
        import gc
        gc.enable()
        gc.set_debug(gc.DEBUG_LEAK)
    
        # make a leak
        l = []
        l.append(l)
        del l
    
        # show the dirt ;-)
        dump_garbage()


print my_friend()
print my_friend1()
print my_friend_in()
print my_friend_menu()
print my_friend_active()

my.lastRun="";
mine.append(my_friend)
mine_unknown=[my_friend,my_friend1,my_friend_in,my_friend_menu,my_animal_level,my_close,my_star,my_GrownUp,my_many_cash,my_many_trash,my_coin,
        my_cash,my_born,my_cash_bronze,my_many_water,my_ball,my_water,my_direct_water
        ,my_direct_ramp,my_feed,my_direct_ramp_right,my_direct_ramp_left
        ,my_focus,my_zoo,my_friend_active,my_check,my_breed,my_great];

def my_run(mine):
    running=True;
    while running :
        did=False;
        t0=datetime.datetime.now();
        for mi in mine:
            if mi==my.lastRun:
                #do not repeat? helping out corner stuck
                continue;
            if(mi()==0):                            
                print mi;
                did=True;
                my.lastRun=mi;
                my.lastStatus="{F}".format(F=mi)
                break;
        if did:
            continue;
        print datetime.datetime.now()-t0;
        my.lastRun="otherdeeds";
    #        if need_my_focus_inossem: 
    #           need_my_focus_inossem=False;
    #           my_focus_inossem();
        break;
        my_ramp();
        ROI=[];
        
print my_run(mine_unknown)
print mine_unknown
