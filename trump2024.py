#manage holidays
#to allow merge tool
#to allow multiple scenario
#keep configable from sikuli /ok /revisit 1 month 3/28
#2D facets to 3D finding stories
#freq visit route
import math;

gtx1060="gtx1060";
inossem="inossem";
scenario=inossem;

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

ClientRegions={
        gtx1060:Region(161,40,1598,998),
        inossem:Region(1,100,1200,625)
        };
ClientRegion=ClientRegions[scenario];
LocCenter=ClientRegion.getCenter();
#Location(933, 503);//screen select region //can capture! 
def auto(rg,origin):
    if(scenario==origin):
        return rg;
    cro=ClientRegions[origin];
    crs=ClientRegions[scenario];    
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
    try:
        zoc=Region(48,126,29,43).find("1646769583487.png");
        zoo="Main";
        return zoo;
    except:
        pass;
    try:
        zoc=Region(2,99,97,87).find("1650649103774.png");
        zoo="Fir";
        return zoo;
    except:
        pass;
    try:
        zoc=Region(48,126,29,43).find("1648929649914.png");
        zoo="Kujali";
        return zoo;
    except:
        pass;
    try:
        zoc=Region(44,94,54,71).find("1646769787903.png");
        zoo="Terrarium";
        return zoo;
    except:
        pass;   
    try:
        zoc=Region(8,104,108,73).find("1649521451422.png");
        Log("in somebody houese, hope you can close");
        return zoo;
    except:
        pass;   
    return zoo;
#zoo=which_zoo_inossem();
which_zoo={gtx1060:which_zoo_gtx1060,inossem:which_zoo_inossem}[scenario];
zoo=which_zoo(); #4/2
print(zoo);

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

def my_friend_gonext():
    global lastLoc;
    Hypnagogia(2);
    lastLoc=Location(564, 487);    
    try: 
       lastLoc=auto(Region(396,401,279,150),inossem).find(managed("1651154628086.png","1010"));
       print lastLoc; #score 0.79 faile
       if lastLoc.score>0.84:
    #       click(Location(702, 483));
           lastLoc=lastLoc.offset(140,0);
           click(lastLoc);
           Hypnagogia(2);    
           click(LocCenter);
           Hypnagogia(3);
    #       print LocCenter;#L[601,412]@S(0)
           click(Location(304, 514));
           click(Location(511, 459));
           click(Location(698, 454));
           click(Location(881, 475));
           Hypnagogia(2);    
           lastLoc=Location(746, 592); #Redeem
           click(lastLoc);
           Hypnagogia(1);    
    except:
        Hypnagogia(1);
    lastLoc=Location(513, 585);
    try: 
       lastLoc=auto(Region(403,538,251,105),inossem).find(managed("1649620530268.png","Yes"));
    except:
        Log("my_friend_gonext missign Yes ");
#            Location(489, 580) # Yes to next friend
    click(lastLoc);
    Hypnagogia(8.25);
#my_friend_gonext();

import shutil;
def managed(img, nametag):
    scenzoo=scenario+"/"+zoo;
    storepath=getBundlePath()+"\\"+scenzoo;
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

def my_friend_exit():    
    try:
        lastLoc=auto(Region(1026,116,155,166),inossem).find(managed("1649762735950.png","my_friend_exit"));
        #    lastLoc=Location(1169, 133);
        mouseMove(lastLoc);
        mouseDown(Button.LEFT);
        Hypnagogia(0.3);
       
        mouseUp(Button.LEFT);
        Hypnagogia(8.25);
    except:
        #Log("my_friend_exit not found");
        pass;
#my_friend_exit();

def my_friend_exit_all():
    try:    
        lastLoc=Region(1047,163,84,77).find("1648086212284.png");
        #    lastLoc=Location(1087, 191);
        mouseMove(lastLoc);
        mouseDown(Button.LEFT);
        Hypnagogia(0.3);
        mouseUp(Button.LEFT);
        Hypnagogia(8.25);
        return 77;
    except:
        Log("my_friend_exit_all not found");
        pass;
#my_friend_exit_all();

def my_friend():
   try:
        lastLoc=ClientRegion.find("1645890484137.png").getTarget(); 
        return 0;
   except:
       return 999;
   
def my_friend1(): 
   #lastLoc=Location(0,0);
   try:
        lastLoc=auto(Region(374,628,98,84),inossem).find(managed("1645891158890.png","meshnet")).getTarget(); 
        for i in range(10):
            mouseMove(lastLoc);
            mouseDown(Button.LEFT);
            mouseUp(Button.LEFT);
            loc=Location(1110, 580);
            drag(loc);
            drag(LocCenter.offset(-20,-20));
            drag(LocCenter.offset(20,-20));
            dropAt(LocCenter.offset(-20,20));
        Hypnagogia(1.2);
        try:
            lastLoc=auto(Region(374,628,98,84),inossem).find(managed("1645891158890.png","meshnet")).getTarget(); 
            return my_friend_exit();#failed rabit?
        except:
           return my_friend_gonext(); 
   except:
       pass;
   try:
        lastLoc=Region(374,628,98,84).find("1645891351088.png").getTarget(); 
        for i in range(5):
            mouseMove(lastLoc);
            Hypnagogia(0.2);
            mouseDown(Button.LEFT);
            Hypnagogia(0.2);
            mouseUp(Button.LEFT);
            Hypnagogia(0.8);
            loc=Location(1110, 580);
            mouseMove(loc);
            Hypnagogia(0.4);
            drag(loc);
            Hypnagogia(0.5);
            dropAt(LocCenter);
            Hypnagogia(0.2);
        Hypnagogia(3.2);
        return my_friend_gonext();
   except:
       pass;
   try:
        lastLoc=Region(374,628,98,84).find("1645893212213.png").getTarget(); 
        for k in range(5):
            mouseMove(lastLoc);
            mouseDown(Button.LEFT);
            Hypnagogia(0.3);
            mouseUp(Button.LEFT);
            Hypnagogia(1.25);
            mouseMove(LocCenter);
            for i in range(3):
                mouseDown(Button.LEFT);
                Hypnagogia(0.3);
                mouseUp(Button.LEFT);
                Hypnagogia(0.25);
        Hypnagogia(3.2);
        return my_friend_gonext();
   except:
       pass;
   return 77;
#my_friend_gonext();
print(my_friend1());

menudrop=auto(Region(1125,94,102,77),inossem);

def my_friend_menu_drop():
   try:
       #would not found first time and die lock next try, contrast with mouseup without sleep?
#        lastLoc=menudrop.find("1645890659925.png").getTarget(); 
        lastLoc= Region(1159,120,29,31).find("1649554885808.png");        
        lastLoc=lastLoc.getTarget(); 
        mouseMove(lastLoc);
        sleep(0.02);
        mouseDown(Button.LEFT);
        sleep(0.02);
        mouseUp(Button.LEFT);
        sleep(1.25);
        #Hypnagogia(1.25);
   except:
       pass;
#my_friend_menu_drop();
import datetime;
t0=datetime.datetime(1,1,1);
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

my_friend_active=False;
my_friend_menu_lastVisit=0;

def my_friend_tbd():
    global my_friend_active;
    global my_friend_menu_lastVisit;
    try:
    #            lastLoc=Region(718,238,325,392).find("1648085114160.png").getTarget().offset(-20,0);  
    #mess with red/gray heart when no gray
    #            lastLoc=Region(718,238,325,392).find("1649620992351.png"); 
        lastLoc=auto(Region(718,238,325,392),inossem).find("1649621670263.png"); 
        print lastLoc.getScore();
        if lastLoc.getScore()>0.97248: #0.97 for mess , 1 for match ,0.978, 0.972483694553 corner           
            lastLoc=lastLoc.getTarget().offset(-30,0);
            mouseMove(lastLoc);
            mouseDown(Button.LEFT);
            Hypnagogia(0.3);
            mouseUp(Button.LEFT);
            Hypnagogia(0.5);
            my_friend_active=True;
            return lastLoc;
    except:
        pass; 
    return Location(0,0);
def my_friend_help():
    global my_friend_active;
    try:
        lastLoc=Region(397,492,241,114).find("1645891012840.png").getTarget(); 
        friend_active=True;        
        mouseMove(lastLoc);
        mouseDown(Button.LEFT);
        Hypnagogia(0.3);
        mouseUp(Button.LEFT);
        return 0;
    except:
        my_friend_active=False;
        return 999;

def my_friend_menu():
#   my_friend_menu_drop(); cannot use safely
    for i in (1,2):
        try:
            region=auto(Region(1117,376,78,173),inossem);
            #print region;#R[1117,376 78x173]@S(0)
            lastLoc=region.find("1645890909817.png").getTarget(); 
            MissingTries["my_friend_menu"].Success();
            break;
        except:
            MissingTries["my_friend_menu"].Failed();
            
        lastLoc=Location(1176, 128);
        click(lastLoc);
#        mouseMove(lastLoc);
#        mouseDown(Button.LEFT);
#        Hypnagogia(0.3);
#        mouseUp(Button.LEFT);
        Hypnagogia(2.25);
        if i==2:
            Log('Failed friend menu');
            return 999;
    mouseMove(lastLoc);
    mouseDown(Button.LEFT);
    Hypnagogia(0.3);
    mouseUp(Button.LEFT);
    Hypnagogia(3.25);
    my_friend_in();
#    my_friend_tbd();
    return 0;
#my_friend_menu();


def my_friend_in():
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
                Region(930,629,168,76).find("1648081939889.png"); 
                drag(Location(1007, 329));
                lastLoc=Location(620, 346);
                dropAt(lastLoc);
                Hypnagogia(2.3);
            except:
                my_friend_active=False;
                return 999;
            notin=(my_friend_tbd()!=Location(0,0));
       if notin :
             if(my_friend_help()==0):
                 notin=False;             
             else:
                  return 0;    
       Hypnagogia(13);
       for h in range(1,8):
           kl=my_friend1();              
           if kl>0:
               break;
       my_friend_exit();
       
    my_friend_active=False;
    my_friend_exit_all();
    return 999;
#my_friend_in();
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
    global lastLoc;
    global CenterX;
    global CenterY;
    lastLoc=Location(0,0);
    if len(ROI)>0 :
#        ROI=locs;
#        ROI.append(locs[2]);
        dk=[0]*4;
        Log('ROI={R}'.format(R=ROI));
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
        Log('Ramp ({X},{Y})'.format(X=CenterX,Y=CenterY));
    Hypnagogia(0.1);
    ScanLandmarks();
    
def Log(str):
    os.system('echo '+str);
            
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

now=datetime.datetime.now();
lastVisit={Main:t0,Fir:now,Terrarium:now,Kujali:now};
Blocked={Main:False,Fir:False,Terrarium:False,Kujali:False};
lastCheck={Main:t0,Fir:now,Terrarium:now,Kujali:now};

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
            lastLoc=auto(Region(1050,467,170,260),inossem).find(managed("1649547381869.png","gotomap"));
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
    Hypnagogia(12);
    if zoo==Terrarium:
        Hypnagogia(3);
        wheel(LocCenter,Button.WHEEL_DOWN,10);
    zoo=which_zoo();
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
            mouseMove(lastLoc);
            mouseDown(Button.LEFT);
            Hypnagogia(0.1);
            mouseUp(Button.LEFT);
            Hypnagogia(0.1);
        return 0;
    return 999;
my_many_cash();

def my_cash():   
    r=my_click(managed(my_cash_pic,"my_cash"))    ;
    Hypnagogia(1.6);
    return r;
def my_cash_bronze():   
    r=my_click({gtx1060:"1640540150379.png",
                inossem:"1645904477007.png"
                }[scenario])    ;
    Hypnagogia(1.6);
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
            mouseMove(lastLoc);
            mouseDown(Button.LEFT);
            Hypnagogia(0.1);
            mouseUp(Button.LEFT);
            Hypnagogia(0.1);
        return 0;
    return 999;
#my_many_trash();

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
        mouseMove(lastLoc);
        mouseDown(Button.LEFT);
        Hypnagogia(0.3);
        mouseUp(Button.LEFT);
        Hypnagogia(1.8);
        return 0;
    except:
        return 999;
#my_coin(); tested 3/23/2022


def my_star():   
    global lastLoc;
    try:   
        lastLoc=clickRange.find(scenario+'/'+ "star.png").getTarget();
        mouseMove(lastLoc);
        mouseDown(Button.LEFT);
        Hypnagogia(0.6);
        mouseUp(Button.LEFT);
        Hypnagogia(0.6);
        return 0;
    except:
        return 999;
#my_star();

#  Region(352,167,1185,721);
def my_feed():
    global lastLoc;
    global CenterX;
    global CenterY;    
    try:
            loc1= clickRange .find(scenario+'/'+"feed.png").getTarget();
            mouseMove(loc1);
            mouseDown(Button.LEFT);
            Hypnagogia(0.3);
            mouseUp(Button.LEFT);
            loc={
                    gtx1060:Location(1390, 464),
                    inossem:Location(964, 374)
                    }[scenario];
            mouseMove(loc);
            Hypnagogia(0.4);
            mouseDown(Button.LEFT);
            Hypnagogia(0.5);
            mouseUp(Button.LEFT);
            Hypnagogia(1.5);
            drag(loc);
            Hypnagogia(1);
            lastLoc={
                    gtx1060:Location(960, 527),
                    inossem:LocCenter
                    }[scenario];
            if(zoo=="Terrarium"):
                lastLoc=Location(lastLoc.x,lastLoc.y/2); #do no devide itself, it actually LocCenter by object reference
            dropAt(lastLoc);
            if(CenterX!=0 or CenterY!=0):
                CenterX-=lastLoc.x-loc1.x;
                CenterY-=lastLoc.y-loc1.y;
                Log('Feed ({X},{Y})'.format(X=CenterX,Y=CenterY));
            Hypnagogia(1);
            return 0;
    except:
            return 999;
#my_feed();

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
#    locs=sorted(locs,key=lambda m:math.atan2(m.x-LocCenter.x,m.y-LocCenter.y));
    locs=sorted(locs,key=lambda m:math.pi*-2.0*int(math.sqrt((m.x-LocCenter.x)**2+(m.y-LocCenter.y)**2)/20.0)
            +math.atan2(m.x-LocCenter.x,m.y-LocCenter.y));
    tt=True;
    for loc in locs:
        if tt :
            mouseMove(loc);
            tt=False;
        print(loc);
        drag(loc);
    loc.getTarget();
    drag(loc);
    Hypnagogia(0.1);
    drag(loc.offset(100,80));
    Hypnagogia(0.1);
    drag(loc.offset(-100,80));
    Hypnagogia(0.1);
    drag(loc.offset(-100,-80));
    Hypnagogia(0.1);
    drag(loc.offset(100,-80));
    Hypnagogia(0.1);
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
    try:
        Region(356,620,220,101).find("1646838860480.png");
        return True;
    except:
        Hypnagogia(2);
    try:
        Region(356,620,220,101).find("1646838860480.png");
        return True;
    except:
        return False;
#print (my_poo_star());
def my_poo():
    global lastLoc;
    try:    
        loc={gtx1060: Region(340,186,1294,772),
                inossem:clickRange
                }[scenario].find({gtx1060:"1640315967731.png",
                    inossem:"1646838657680.png"
                    }[scenario]).getTarget();
        loc0=loc;
    except:
        return 888;
    mouseMove(loc);
    mouseDown(Button.LEFT);
    Hypnagogia(0.3);
    mouseUp(Button.LEFT);
    lastLoc=loc;    
    Hypnagogia(2);
    poobrush={gtx1060:"1640317826765.png",
                    inossem:"1646838706009.png"
                    }[scenario];
    poorange={gtx1060: Region(219,96,1482,923),
                inossem:ClientRegion
                }[scenario];
    try:
        loc=poorange.find(poobrush).getTarget();
    except:
        Log("Missingg poo brush!");
        return 999;
    wheel(loc,Button.WHEEL_DOWN,10);
    #mouseMove(loc);
    mouseDown(Button.LEFT);
    Hypnagogia(0.1);
    poogrid=auto(Region
            (0,0,70,60),gtx1060); 
    #            (0,0,80,50)
#    print(poogrid);
    for t in trail:
        lastLoc=Location(t[0]*poogrid.w+LocCenter.x,t[1]*poogrid.h+LocCenter.y);
        mouseMove(lastLoc);    
        Hypnagogia(t[2]);
        if not my_poo_star():
            Log("Done poo brush");
            mouseUp(Button.LEFT);
            Hypnagogia(1);
            return 0;
#    mouseUp(Button.LEFT);
    Hypnagogia(0.1);
#    mouseDown(Button.LEFT);
    for i in range(1,5):
        for j in range(1,3):
            if not my_poo_star():
                Log("Done poo brush");
                mouseUp(Button.LEFT);
                Hypnagogia(1);
                return 0;
            try:
                loc= ClientRegion.find(poobrush).getTarget();
                break;
            except:
                Hypnagogia(0.2);
                pass;
        if j>=4 :
            Log("Done poo brush");
            mouseUp(Button.LEFT);
            Hypnagogia(1);
            return 0;
        cl=ClientRegion.grow(-50);
        lastLoc=Location(random.randrange(cl.x,cl.x+cl.w),
                            random.randrange(cl.y,cl.y+cl.h));
        mouseMove(lastLoc);                
        Hypnagogia(0.1);
    Log("Failed poo brush {L}".format(L=loc0));
    mouseUp(Button.LEFT);
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

#if zoo is not found
def my_focus_inossem():        
        try:   
           loc= Region(14,0,405,35).find("1649353378650.png");
           if which_zoo_inossem()=="unknown":
                mouseMove(loc);
                mouseDown(Button.LEFT);
                sleep(0.2);
                mouseUp(Button.LEFT);
                sleep(0.2);
                Log('Recover tab');
        except:
           pass;        
#my_focus_inossem();

def my_close_inossem():        
    global lastLoc;
    
    my_friend_exit();
    while 1==1:
        try:   
           loc= Region(850,95,166,130).find("1649449467461.png"); #super deal tbd
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
            loc= Region(1093,53,203,163).find(managed("1649767973217.png","my_close.dirty"));
            print loc;
            Log('Close 3 dirty ');
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
            loc= Region(1082,99,154,84).find("1648564925872.png");
            Log('Close friend scene');
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
ScanLandmarks();

def ispoppydays(now):
    return (now.month==2 and now.day>=14 and now.day<=14+14 
        or now.month==4 and now.day>=6 and now.day<=6+14 ); #easter early?
            
now = datetime.datetime.now()
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
    need_my_focus_inossem=False;
    need_my_splash=True;
    need_my_friend1=False;
    while i<NLOOP:
        oldzoo=zoo;
        enabledonzoo=True;
        zoo=which_zoo();
        if(zoo=="unknown"):
            need_my_focus_inossem=True; #must run after my_close;
            need_my_splash=True;
            need_my_friend1=True;
        now = datetime.datetime.now();
        if(zoo=='unknown') :
           zoo=oldzoo;
           Log("back to "+zoo);
            #enabledonzoo=False;
        elif(zoo!=oldzoo):
            lastVisit[oldzoo]=now;
            Log(zoo);
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
                      x = input('Exit(no):');
                      if(x>' ' and x[0]!='n') :
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
            if(my_click("1649437078845.png")==0):
                lastStatus='Splash';                
                continue;
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
            continue;
        if(my_close()==0) : #>star
           lastStatus='close';
           continue;
        if need_my_focus_inossem: 
           need_my_focus_inossem=False;
           my_focus_inossem();
#my_first_try();
        if(my_star()==0) :
           lastStatus='star';
           ROI.append(lastLoc);
           continue;
        if(my_GrownUp()==0) : #>coin
           lastStatus='Growup';
           continue;
        if(my_click("1640869435405.png")==0): #over by cash，trash
            lastStatus='Great gtx1060';
            continue;
        if(my_click("1646006271068.png")==0): #over by cash，trash
            lastStatus='Great inossem';
            continue;
        if(my_many_trash()==0) :
           lastStatus='trash';
           ROI.append(lastLoc);
           continue;
        if(my_many_cash()==0) :
            lastStatus='many cash';
            ROI.append(lastLoc);
            continue;
        if(my_cash_bronze()==0) :
            lastStatus='cash bronze';
            ROI.append(lastLoc);
            continue;
        if(my_cash()==0) :
            lastStatus='cash';
            ROI.append(lastLoc);
            continue;
        if(my_coin()==0) :
            lastStatus='coin';
            ROI.append(lastLoc);
            continue;
        if(my_click("1640623363794.png")==0):
            lastStatus='breed';
            continue;
        if ispoppydays(now):
            if(poppy<0) :
                try:
                   Region(178,177,126,806).find("1644682415730.png"); 
                   poppy=0;        
                except:
                   pass;
            if(my_click(
                       # "1644338915756.png" #poppy image?
                        "1649303197390.png"
                        )==0):
               poppy+=1;
               SetRampDest(0,0);
               lastStatus='poppy';
               continue;
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
        if not my_friend_active: 
            if my_friend()==0:
                my_friend_active=True;           
                Log('my_friend_active , last try {T}'.format(T=my_friend_menu_lastVisit));
                lastStatus='friend';           
                continue;
#        print(my_friend_active);
        if my_friend_active :
            t=my_friend_menu_lastVisit+ datetime.timedelta(minutes=5);
            if(t<now):
                my_friend_menu_lastVisit=now;
                Log('my_friend_menu {T}'.format(T=my_friend_menu_lastVisit));
                my_friend_menu();
                lastStatus='friend menu';                       
                my_friend_active =False;
                continue;
        if(my_ball()==0):
           lastStatus='ball';
           ROI.append(lastLoc);
           continue;
        if(my_many_water()==0):
           lastStatus='water many';
           ROI.append(lastLoc);
           continue;
        if(my_water()==0):
           lastStatus='water';
           ROI.append(lastLoc);
           continue;
        if(my_feed()==0) :
           lastStatus='feed2';
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
        if not ispoppydays(now) and zoo=='Main' and i>160*NLOOP/400 :#80
            if SetDestFir:
                SetDestFir=1; # do not set again even failed ramping
                SetRampDest(100,20); #'Garage'
        if(zoo==Terrarium and lastVisit[Main]+ datetime.timedelta(minutes=10)<now):
            if my_goto(Main)==0:
                SetRampDest(-100,20); #Dest subsbribe zoo, to be puppy sometime
                continue;
        if(zoo==Main and lastVisit[Fir]+ datetime.timedelta(minutes=20)<now):
            if(my_Fir()==0):            
                    lastVisit[Main]=now;
                    zoo=Fir;                
                    landmarks=landmarkss[zoo];
                    Orig_Xs=Orig_XsFir;
                    Orig_Ys=Orig_YsFir;                
                    SetRampDest(0,0);
                    continue;
        if(zoo==Main or zoo==Fir) and lastVisit[Terrarium]+ datetime.timedelta(minutes=20)<now:
            if my_goto(Terrarium)==0:
                SetRampDest(0,0); 
                continue;
        if(zoo==Main or zoo==Fir) and lastVisit[Terrarium]+ datetime.timedelta(minutes=20)<now:
            if(my_Terrarium()==0):            
                lastVisit[zoo]=now;
                zoo=Terrarium; #cannot handle feed by accident
                landmarks=landmarkss[zoo];
                SetRampDest(0,0);
                continue;
#        if(enabledonzoo): 
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
