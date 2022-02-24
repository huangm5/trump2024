#keep configable from sikuli
#to allow merge tool
#to allow multiple scenario
gtx1060="gtx1060";
inossem="inossem";
scenario=gtx1060;
#2D facets to 3D finding stories
#valuntine
#freq visit route

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
        gtx1060:Region(161,40,1598,998)
        };
ClientRegion=ClientRegions[scenario];
LocCenter=ClientRegion.getCenter();#Location(933, 503);//screen select region //can capture!

def SetRampDest(x,y) :
    global DescX;
    global DescY;
    DescX=x;
    DescY=y;
    Log('Desc [{X},{Y}]'.format(X=x,Y=y));

locss={
        gtx1060:[Location(487, 337),Location(1510, 305),Location(1569, 876),Location(480, 780)]
        };
locs=locss[scenario];

def my_ramp():   
    global lastLoc;
    global CenterX;
    global CenterY;
    lastLoc=Location(0,0);
    if(CenterX==0 and CenterY==0):
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
    elif CenterX/2-CenterY<5100 and CenterX/2+CenterY<1000 and CenterX/2+CenterY>-800 :
        Log('Top Left k=2');
        k=2; #top left
        #k=1; #from left botom
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
        lastLoc=Location(lastLoc.x+random.randrange(-10,10)  ,    lastLoc.y+random.randrange(-10,10));
#        Log('Drag to {K}/{L}'.format(K=k,L=lastLoc));


    drag(locs[k]);
    dropAt(lastLoc);
    if(CenterX!=0 or CenterY!=0):
        CenterX-=lastLoc.x-locs[k].x;
        CenterY-=lastLoc.y-locs[k].y;
        Log('Ramp ({X},{Y})'.format(X=CenterX,Y=CenterY));
    sleep(0.1);
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
landmarkss={
        Main:["1640721586941.png","1640719028561.png","1640720333764.png","1644708172971.png","1640720057152.png","1640721817026.png","1640721745982.png","1640741694803.png","1640744943976.png","1641391579681.png","1641394421693.png","1640536842754.png"]
        ,
        Fir:["1641135019722.png","1641135048732.png","1641135072434.png","1640640250064.png"]
        };
#Region(302,139,1431,864).find(landmarkss[Main][3]);
Orig_XsMain  =[0       ,-7     ,2      ,3        ,590   ,523    ,1988   ,800    ,-500  ,20000                       ,18000     ,102,0,0,0];
Orig_YsMain  =[0       , 0     ,2      ,3       ,17   ,215    , 827   ,-110   ,30    ,-1500                       ,-2000     ,-200,0,0,0];
Orig_XsFir  =[0       ,27     ,36         ,638,0,0,0,0,0];
Orig_YsFir  =[0       , -20     ,-100     ,418,0,0,0,0,0];
Orig={ Main:{
            "x":[0       ,-7     ,2      ,3        ,590   ,523    ,1988   ,800    ,-500  ,20000                       ,18000     ,102,0,0,0],
            "y":[0       , 0     ,2      ,3       ,17   ,215    , 827   ,-110   ,30    ,-1500                       ,-2000     ,-200,0,0,0]       
            },
       Fir :{
            "x":[0       ,27     ,36         ,638,0,0,0,0,0],
            "y":[0       , -20     ,-100     ,418,0,0,0,0,0] 
            }
     };
landmarks=landmarkss[Main];
freqmarks=[0]*len(landmarksMain);
def ScanLandmarks():
    global landmarks,Orig_Xs,Orig_Ys;
    i = 0;
    loc0=Location(0,0);
    while i < len(landmarks):
        try: 
            loc= Region(302,139,1431,864).find(landmarks[i]);
        except:
            i+=1;
            continue;
        freqmarks[i]+=1;
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
        
ScanLandmarks();


def my_click(img):   
    global lastLoc;
    try:  
        loc= Region(304,146,1435,871).find(img);
        lastLoc=loc.getTarget();        
        mouseMove(lastLoc);
        mouseDown(Button.LEFT);
        sleep(0.3);
        mouseUp(Button.LEFT);
        sleep(0.25);
        return 0;
    except:
        return 999;
def my_GrownUp():
    global lastLoc;
    try:  
        loc= Region(537,734,852,301).find("1640642196950.png");
        lastLoc=loc.getTarget();        
        mouseMove(lastLoc);
        mouseDown(Button.LEFT);
        sleep(0.3);
        mouseUp(Button.LEFT);
        sleep(4.3);
        return 0;
    except:
        return 999;
    return r;
def my_Fir():   
    r=my_click("1640640040396.png")    ;
    if(r==0):
        r=my_click("1640640105756.png")    ;    
        sleep(3);
    return r;
def my_Terrarium():   
    r=my_click(landmarksFir[3])    ;
    r=my_click("1640640267632.png")    ;    
    sleep(3);
    return r;

import random;
def my_cash():   
    r=my_click("1640407206306.png")    ;
    sleep(1.6);
    return r;
def my_cash_bronze():   
    r=my_click("1640540150379.png")    ;
    sleep(1.6);
    return r;

def my_cash1():
    global lastLoc;
    try:  
        loc= Region(304,146,1435,871).find("1640407206306.png");
        lastLoc=loc.getTarget();
        mouseMove(lastLoc);
        mouseDown(Button.LEFT);
        sleep(0.3);
        mouseUp(Button.LEFT);
        sleep(0.3);
        return 0;
    except:
        return 999;
     
def my_trash():   
    global lastLoc;
    try:   
        lastLoc= Region(337,143,1273,847).find("1640533677248.png").getTarget();
        mouseMove(lastLoc);
        mouseDown(Button.LEFT);
        sleep(0.2);
        mouseUp(Button.LEFT);
        sleep(0.3);
        return 0;
    except:
        return 999;

def my_coin():   
    global lastLoc;
    try:   
        loc= Region(383,188,1227,723).find("1640236026729.png").getTarget();
        lastLoc=loc.offset(0,-9);
        mouseMove(lastLoc);
        mouseDown(Button.LEFT);
        sleep(0.3);
        mouseUp(Button.LEFT);
        sleep(1.8);
        return 0;
    except:
        return 999;
    

def my_star():   
    global lastLoc;
    try:   
        lastLoc= Region(322,144,1328,796).find("1640230937076.png").getTarget();
        mouseMove(lastLoc);
        mouseDown(Button.LEFT);
        sleep(0.6);
        mouseUp(Button.LEFT);
        sleep(0.6);
        return 0;
    except:
        return 999;

def my_feed():
    global lastLoc;
    global CenterX;
    global CenterY;    
    try:
            loc1= Region(352,167,1185,721).find("1640139660539.png").getTarget();
            mouseMove(loc1);
            mouseDown(Button.LEFT);
            sleep(0.3);
            mouseUp(Button.LEFT);
            loc=Location(1390, 464);
            mouseMove(loc);
            sleep(0.4);
            mouseDown(Button.LEFT);
            sleep(0.5);#
            mouseUp(Button.LEFT);
            sleep(1.5);
            drag(loc);
            sleep(1);
            lastLoc=Location(960, 527);#
            dropAt(lastLoc);
            if(CenterX!=0 or CenterY!=0):
                CenterX-=lastLoc.x-loc1.x;
                CenterY-=lastLoc.y-loc1.y;
                Log('Feed ({X},{Y})'.format(X=CenterX,Y=CenterY));
            sleep(1);
            return 0;
    except:
            return 999;

def my_water():
    global lastLoc;
    try:    
        loc= Region(352,167,1185,721).find("1640125687306.png").getTarget();
        drag(loc);
        sleep(0.1);
        mouseMove(loc.offset(100,80));
        sleep(0.1);
        mouseMove(loc.offset(-100,80));
        sleep(0.1);
        mouseMove(loc.offset(-100,-80));
        sleep(0.1);
        mouseMove(loc.offset(100,-80));
        sleep(0.1);
        dropAt(loc);
        lastLoc=loc;    
        return 0;
    except:
        return 999;

def my_poo():
    global lastLoc;
    try:    
        loc= Region(340,186,1294,772).find("1640315967731.png").getTarget();
        mouseMove(loc);
        mouseDown(Button.LEFT);
        sleep(0.3);
        mouseUp(Button.LEFT);
        sleep(2);
        lastLoc=loc;    
    except:
        return 999;
    
    Region(601,907,150,112).find("1640316099386.png");        
    loc= Region(219,96,1482,923).find("1640317826765.png").getTarget();
    mouseMove(loc);
    lastLoc=loc;    
    
    fruits = ["1640316288074.png", "1640317465662.png","1640317490156.png","1640317623212.png","1640317634822.png"]
    loc2=Location(0,0);
    for x in fruits:
        try:   
             loc2= Region(317,108,1345,828).find(x).getTarget();
             print(x);
             break;
        except:
            pass;
    if (loc2==Location(0,0)) :
       return 999;
    mouseDown(Button.LEFT);
    sleep(0.3);
    mouseMove(loc2);    
    sleep(0.3);
    mouseUp(Button.LEFT);
    sleep(1);
    lastLoc=loc2;    
    return 0;

def merge_regions(regions):
    x=min(map(lambda x:x.x,regions));
    y=min(map(lambda x:x.y,regions));
    return Region(x,y,
            max(map(lambda x:x.x+x.w,regions))-x,
            max(map(lambda x:x.y+x.h,regions))-y
            );
#print merge_regions([Region(1501,39,163,253),Region(1640,42,112,124)]);
def my_close():        
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
        return 999;
    
    mouseMove(loc);
    mouseDown(Button.LEFT);
    sleep(0.3);
    mouseUp(Button.LEFT);
    sleep(1);        
    lastLoc=loc.getTarget();    
    return 0;
#my_close();

def my_ball():    
    global lastLoc;
    try:   
        loc= Region(383,188,1227,723).find("1640310968315.png");
        mouseMove(loc);
        mouseDown(Button.LEFT);
        sleep(0.4);
        mouseUp(Button.LEFT);
        sleep(0.2);
        mouseDown(Button.LEFT);
        sleep(0.4);
        mouseUp(Button.LEFT);
        sleep(0.2);
        mouseDown(Button.LEFT);
        sleep(0.4);
        mouseUp(Button.LEFT);
        sleep(0.2);
        mouseDown(Button.LEFT);
        sleep(0.4);
        mouseUp(Button.LEFT);
        sleep(0.2);
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
        sleep(0.3);
        drag(Location(901, 519));
        mouseMove(Location(932, 600));
        sleep(0.3);
        mouseMove(Location(1741, 550));
        sleep(0.1);
        dropAt(Location(1618, 618));        
#my_first_try();

import datetime
now = datetime.datetime.now()

try:
    loc= Region(167,45,137,132).find("1644387272438.png");
    running=999;
except:
    running=-1;
mPoppyLast=0;    
lastStatus='init';
while 1==1 :
    zoo='Main';        
    landmarks=landmarksMain;
    Orig_Xs=Orig_XsMain;
    Orig_Ys=Orig_YsMain;
    
    now = datetime.datetime.now();
    #print(now.year, now.month, now.day, now.hour, now.minute, now.second)
    if(running<999) :
        if(now.hour%2==0 and running!=now.hour) :
            os.system('start steam://rungameid/1352330');
            sleep(150);
            
            my_click("1640459738300.png");
        else :
            sleep(3*60);
            if(now.hour>8 and Mouse.at().x<10 and Mouse.at().y<10) :
                break;#exit
            continue;
    running=now.hour;
    i =1;
    NLOOP=500;#1000;
    first_try=1;
    startTime = datetime.datetime.now();   
    poppy=0;SetRampDest(100,100);                
    displaceCount=0;    
    while i<NLOOP:
        now = datetime.datetime.now();
        if(lastLoc!=Location(0,0) and now.hour>=8 and now.hour<=22):
            locMouse=Mouse.at();
            dx=lastLoc.x-locMouse.x;
            dy=lastLoc.y-locMouse.y;            
            if( dx*dx+dy*dy>200):
                print('displaced',lastLoc,locMouse,lastStatus);                                
                displaceCount+=1;
                if(displaceCount>=2):
                    x = input('Exit(no):');
                    if(x>' ' and x[0]!='n') :
                        print(x);
                        break;
            else:
                displaceCount=0;
        else :
           if((now-startTime).total_seconds()>50*60):
               i=NLOOP;
               break;
        i+=1;
        if(my_click("1642273227689.png")==0): 
            lastLoc=Location(947, 562);
            mouseMove(lastLoc);
            mouseDown(Button.LEFT);
            sleep(0.3);
            mouseUp(Button.LEFT);
            sleep(0.3);
            lastStatus='Animal Level';
            continue;
        if(my_close()==0) : #>star
           lastStatus='close';
           continue;
        my_first_try();
        if(my_star()==0) :
           lastStatus='star';
           continue;
        if(my_GrownUp()==0) : #>coin
           lastStatus='Growup';
           continue;
        if(my_click("1640869435405.png")==0): #over by cash，trash
            lastStatus='Great';
            continue;
        if(my_trash()==0) :
           lastStatus='trash';
           continue;
        if(my_cash_bronze()==0) :
            lastStatus='cash bronze';
            continue;
        if(my_cash()==0) :
            lastStatus='cash';
            continue;
        if(my_coin()==0) :
            lastStatus='coin';
            continue;
        if(my_click("1640623363794.png")==0):
            lastStatus='breed';
            continue;
        if(poppy<0) :
            try:
               Region(178,177,126,806).find("1644682415730.png"); 
               poppy=0;        
            except:
               pass;
        if(my_click("1644338915756.png")==0):
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
        if(my_ball()==0):
           lastStatus='ball';
           continue;
        if(my_water()==0):
           lastStatus='water';
           continue;
        if(my_feed()==0) :
           lastStatus='feed2';
           continue;
        if(my_click("1640869544082.png")==0):
           lastStatus='check';
           continue;
        if(zoo=='MainXXX' and i>160*NLOOP/400) :#80
            SetRampDest(100,20); #'Garage'
            if(poppy>0):
                if(my_Fir()==0):            
                    zoo='Fir';
                    landmarks=landmarksFir;
                    Orig_Xs=Orig_XsFir;
                    Orig_Ys=Orig_YsFir;                
                    SetRampDest(0,0);
                    continue;
        if(zoo=='FirXZZ' and i>250*NLOOP/400) :
            SetRampDest(Orig_XsFir[3],Orig_YsFir[3]); #station
            if(my_Terrarium()==0):            
                zoo='Terrarium'; #cannot handle feed by accident
                SetRampDest(0,0);
                continue;
            
        my_ramp();
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
            sleep(0.1);
            mouseUp(Button.LEFT);
            loc=Location(1597, 901);
            mouseMove(loc);
            sleep(0.05);
            #mouseDown(Button.LEFT);
            #sleep(0.5);#
            #mouseUp(Button.LEFT);
            #sleep(1.5);
            drag(loc);
            sleep(0.1);        
            mouseMove(Location(517, 390));
            sleep(0.1);        
            dropAt(Location(807, 504));
            sleep(1);        
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
