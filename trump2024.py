#[error] ImagePath: find: not there: inossem/water.png
import math;

gtx1060="gtx1060";
inossem="inossem";

global cookieItemFulls
cookieItemFulls={};


scenario=inossem;

import datetime;

import inspect

print os.getcwd()
print getBundlePath()
execfile(getBundlePath()+'/trumpy.py')
#import trumpy;

update_scenario();
my.scenario=scenario;
my.esc_close=False
    my.in_cookie=False
my.in_zoo=False
my.last_arena=datetime.datetime.now()- datetime.timedelta(minutes=21)

    


    now=datetime.datetime.now()
                
my.GapProduct=44#22
my.wheel_count=4;
            
cookieItemFulls={};
my.darkLoopMaybe=0;
def my_connectionError():
    if my.lastRun in [my_many_trash,my_many_water]:
        my.darkLoopMaybe=my.darkLoopMaybe+1;
        if my.darkLoopMaybe<9:
            return 888;
    else:
        my.darkLoopMaybe=0;
        return 777;
    try:   
        print 'checking reconnect'
        #find("1682388973929.png")
        #find("1682389019615.png")
        #find)"1682389034244.png")
        #find("1682389062119.png")
        #Region(my.ClientRegion.x+my.ClientRegion.w/4,my.ClientRegion.y+my.ClientRegion.h/2,
        #my.ClientRegion.w/2,my.ClientRegion.h/2).
        click(findAny("reconnect.png","1652488232002.png","1661290954532.png")[0]);sleep(2)
        return 0;
    except:
        return 999;
#print my_connectionError(),my.darkLoopMaybe 

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
    print title
    global cookieItemFulls
    if bool(cookieItemFulls.get(title)):
        return 777;
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
                return 888;
            except:        
                click(loc1);
                sleep(1);
                try:
                    loc2=find("1656888495630.png");
                    click(loc2.getTopRight());
                    cookieItemFulls[title]=True;
                except:                    
                    pass;
            return 0;
    except:
        pass;
    return 999;


cookieItems=[["1666321644716.png",'Wood'],["1658935253872.png",'Suger Cube'],["1655843068695.png",'Flour']#,["1658807426137.png",'Axe']
        ,["1661972624350.png",'Pickaxe']        ,["1663385220033.png",'Donut'],["1655947493149.png",'Birdy Toy']      
            ,["1656277907046.png",'Candy Saw'],["1666320976107.png",'Shovel'],["1655860761062.png",'Milk'],["1655862866954.png",'Basket'],["1655871263617.png",'Flower']
            #,["1656276637754.png",'Jellybean Jam']
        ,["1663160713757.png",'Jellybean Jam x5'],["1661972784003.png",'Sweet Jelly Jam'],["1666321102692.png",'Toffe Jam']#,["1656996995975.png",'Butter']
            ,["1656997272926.png",'Wood'],["1656277184823.png",'Biscuit Planter'],["1663781654636.png",'Shiny Glass'],["1657145423461.png",'Happy Planter']
            ,["1656277384825.png",'Cream'],["1656277517404.png",'Latte'],["1661973370377.png",'Bubbly Boba'],["1656277609357.png",'Pillow'],["1661973487175.png",'Bear Jelly Toy']
            ,["1656860612793.png",'Ring'],["1655947616537.png",'Jelly Stew'],["1661973027719.png",'Jelly Burger'],["1661973122900.png",'Candy Pasta']      
            ,["1656276970547.png",'Hearty Rye'],["1663160270499.png",'Tart Jampie'],["1656860737440.png",'Focaccia'],["1655844115185.png",'JellyBean']      
            ,["1655860711815.png",'Candy Wool'],["1663159291817.png",'Bubbly Boba'],["1663160194097.png",'Lamp']
            ,["1661973592922.png",'Root Beer'],["1661973635640.png",'Spooky Muffin'],["1661973691323.png",'Radiant Shards']              
        ];
#print cookie_wook(cookieItems);
#cookie_produce()
#ci=cookieItems[2]
#cookieiHistory=[];
import os
def Log(str):
    print str
    os.system('echo '+str);

def cookie_wook(cookieItems):
    sel='None';
    now=datetime.datetime.now();
    for ci in cookieItems:
         r=cookie_item (ci[0],ci[1]);
         if r==0: 
             sel=ci[1];
             Log(ci[1]+':$:'+str(datetime.datetime.now()-now));
             break;
         if r==888:
             sel=ci[1];
             Log(ci[1]+':0:'+str(datetime.datetime.now()-now));
             break;
#    cookieiHistory.append(sel);
    return sel;
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

def to_produce():
  for i in range(2):
    try:
        loc=findAny("1655859264104.png","1656038737775.png")
        print loc
        if len(loc)>0:
            click(loc[0])
            sleep(3)
            try:
                click("1664565175064.png")
                sleep(1)
            except:
                pass;
            click(loc[0])
            sleep(5)          
            find("1664565368984.png")
            return 0;    
        break;
    except:
        if i>0:
            return 888;
  return 999;    
#print to_produce()

cookieItemPrior={};
cookieItemHistory=[];

def getCookieItemPrior():
    n=len(cookieItemHistory)
    if n<2:
        return [];
    t=cookieItemPrior.get(cookieItemHistory[n-1])
    if bool(t):
        u=t.get(cookieItemHistory[n-2]);
        if bool(u):
            return filter(lambda x:(x[1]==u), cookieItems);
    return [];
#print getCookieItemPrior()

def cookie_produce():
    global cookieItemFulls;
    to_produce()    
    product()
    for j in range(2624):
        if reset_game()==0:
            Do.popAsk('Reset game','',88)
            reset_job()
            to_produce()    
        try:
            click("1662950256397.png")#Tap to continue
            sleep(1)
        except:
            pass;
        if j%22==0:
            cookieItemFulls={};
        for i in range(31):           
#            print getCookieItemPrior()
            r=cookie_wook(getCookieItemPrior())
            print r #,'<<',cookieItemPrior,'>>',cookieItemHistory;
            if r=='None':
                r=cookie_wook(cookieItems);
#                if r=='None':
#                    if DoEvent():
#                        break;
            click(Location(1012, 529)); #right   
            sleep(1);
            cookieItemHistory.append(r);
            #simple offer last ,predict by 2 history
            n=len(cookieItemHistory)-1
            if n>=3:
                t=cookieItemPrior.get(cookieItemHistory[n-1])
                if not bool(t):
                    t={};
                    cookieItemPrior[cookieItemHistory[n-1]]=t;
                t[cookieItemHistory[n-2]]=cookieItemHistory[n];
            mouseMove(Location(0,0))
            sleep(0.5)         
            locMouse=Mouse.at();
            if not (locMouse.x<10 and locMouse.y<10):
                break;
        if i<31-1:
            break;
        sleep(13) 
#print cookie_produce()        
#poppy was 1306
my.InEvent=False
def DoEvent():
    if my.InEvent:
        return False;
    my.InEvent=True
    now=datetime.datetime.now()
    if not my.off20_tree_of_wishes and my.last_tree_of_wishes+ datetime.timedelta(minutes=9)<now:    
        tree_of_wishes() #20 claim not so work
    elif my.last_arena+ datetime.timedelta(minutes=20)<now:
        fight_arena()
    else:
        my.InEvent=False
        return False
    my.InEvent=False
    return True 
my.InEvent=False;
#print DoEvent()

def run_cookie():        
    for  i in range(2):
        click("1661259211040.png")    
        sleep(1)
        try:
            loc=findAny("1662992312671.png")
            break;
        except:
            pass;
    sleep(30)
    click("1661259332135.png")
    sleep(1)
#run_cookie()    
def tap_to_continue_goods():
    click("1664565175064.png")
    sleep(1)

def train_tap_to_continue():
    click("1661260606547.png")
    sleep(1)
    click("1661262818385.png")
    sleep(1)
    try:
        for i in range(3):
            click("1661260650522.png")
            sleep(1)
    except:
        pass;


def claim_all():
    click("1661260774380.png")
    sleep(2)
    click("1661259332135.png")
    sleep(1)

def kingdom_fairs():
    click("1661260949857.png");
    sleep(1);
    click("1661260990879.png")       
    sleep(1);
    click("1661261045345.png")       
    sleep(40);
    click("1661261443352.png")
    sleep(1)
    loc=find("1661261487014.png")
    click(Location(loc.x+loc.w*0.48,loc.y+loc.h*0.97))
    sleep(1)
    click("1661259332135.png")
    sleep(1)
    click("1661259332135.png")
    sleep(1)

def scroll_left():    
    loc=find("1661262276940.png")
    drag(Location(loc.x+loc.w,loc.y+loc.h/2))
    dropAt(Location(loc.x,loc.y+loc.h/2))
    sleep(1)
    
def play2try(repeater,reseter):
    try:
        return repeater();
    except:
        pass;
    reseter();
    return repeater();

def enter_tower():
    play2try(lambda : (click("1672458170702.png"),sleep(2)),
            lambda : (click("1661262451106.png"),sleep(1))          
            )
            
    
def play_tower():
    play2try(repeat_tower,enter_tower)
#repeat_tower()
            
def repeat_tower():
    for i in range(20):
        wait_appear("1657733279787.png")
        try:
            click("1672455904414.png")
            sleep(20)
        except:
            try:
                click("1672455938084.png");sleep(21)
                click("1672458003403.png");sleep(1)
                click("1672458170702.png");sleep(2)
            except:
                pass;
#                return 999;
        for k in range(5):
           try:
               Region(442,565,1184,515).find("1672456073346.png")
               k1=Region(7,0,786,531).find("1672456125184.png")
               k5=Region(208,0,915,520).find("1672456206786.png")
               loc=Location((k1.x*(4-k)+k5.x*k)/(5-1),k1.y)
               click(loc);sleep(1)
           except:
               break;
        click("1672456569839.png");
        Do.popAsk('done?','tower battle',86);

#play_tower()


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
my.ClientRegion=ClientRegions[scenario];

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
            lc=my.ClientRegion.findAny(wilds[i])[0];
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
            my.ClientRegion.find(managed(wilds[i],"wildtohome"));
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
            my.ClientRegion.find(managed(wilds[i],"wildtohome"));
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

print Screen(0),Screen(1)

def getScreenClientRegion(id):
    try:
        Region(Screen(id).x+Screen(id).w*2/5,Screen(id).y,Screen(id).w*3/5
                ,Screen(id).h/3).findAny("1662427446449.png","1665003899531.png")[0].click()
        sleep(2)
    except:
        pass;

    ds=[
    Region(Screen(id).x,Screen(id).y,313,318).findAny(Pattern("1678365779941.png").similar(0.52),"1682206947789.png","1704694812529.png")[0].getTarget(),
    Region(Screen(id).x+Screen(id).w*4/5,Screen(id).y+Screen(id).h*4/5,Screen(id).w/5
                ,Screen(id).h/5).findAny(Pattern("1678365913557.png").similar(0.53),"1652229805622.png","1704694883103.png")[0].getTarget(),
    Region(Screen(id).x+Screen(id).w*2/5,Screen(id).y,Screen(id).w*3/5
                ,Screen(id).h/3).findAny(Pattern("1652229378603.png").similar(0.52),"1704372181912.png")[0].getTarget()      
            ];
    print 'ds done';

    cs=[
            [Location(43,151),Location(1149,683),Location(982,132),Region(0,100,1184,624)],
            [Location(49,79),Location(1324,677),Location(1140,58),Region(0,24,1366,705)],
            [Location(68,102),Location(1289,663),Location(1118,81),Region(21,50,1311,661)]
    ];
    print 'cs done';
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
    print cr
    return cr;

def update_ClientRegion():
    try:
        my1.ClientRegion=getScreenClientRegion(0);
        print my1.ClientRegion
    except:
        print "Failed: update_ClientRegion";
        my1.ClientRegion=ClientRegions[scenario];
        return my1.ClientRegion
    try:
        my2.ClientRegion=getScreenClientRegion(1);    
        print my2.ClientRegion
    except:
        return my1.ClientRegion
    return None;
update_ClientRegion();
print my.ClientRegion;


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


#LocCenter=my.ClientRegion.getCenter();
#Location(933, 503);//screen select region //can capture! 
def auto(rg,origin): #ClientRegions not my.ClientRegion
#    if(scenario==origin):
#        return rg;
    return auto_must(rg,origin);
    
def auto_must(rg,origin): #ClientRegions not my.ClientRegion
    cro=ClientRegions[origin];
    crs=my.ClientRegion;    #ClientRegions[scenario];    
    return Region(
    (rg.x-cro.x) *crs.w/cro.w+crs.x,
    (rg.y-cro.y) *crs.h/cro.h+crs.y,
    rg.w *crs.w/cro.w,
    rg.h *crs.h/cro.h);
#print auto(ClientRegions[gtx1060],gtx1060);
#print auto(ClientRegions[inossem],inossem);
ROI=[];        
def xwhich_zoo_gtx1060():
    zoo='unknown';
    AdvisorRegion=Region(0,0,481,440);
    try:
        zoc=AdvisorRegion.findAny(Pattern("1648929649914.png").similar(0.74),"1682703766413.png")[0];
        zoo="Kujali";
        return zoo;
    except:
        pass;
    try:
        zoc=AdvisorRegion.findAny(Pattern("1646769583487.png").similar(0.76),Pattern("1646455711214.png").similar(0.69))[0];
        zoo="Main";
        return zoo;
    except:
        pass;
    try:
        zoc=AdvisorRegion.findAny("Aquarium.png","1719349858685.png")[0];
        zoo="Aquarium";
        return zoo;
    except:
        pass;
    try:
        zoc=AdvisorRegion.find(Pattern("1646455590532.png").similar(0.54));
        zoo="Terrarium";
        return zoo;
    except:
        pass;   
    return zoo;
#print which_zoo_gtx1060();
        
def which_zoo1():
    zoo='unknown';
    zoc=None;
    AdvisorRegion=Region(0,0,306,300);
    try:
        zoc=AdvisorRegion.find(Pattern("1646769583487.png").similar(0.76));
        zoo="Main";
        return zoo;
    except:
        pass;
    try:
        zoc=AdvisorRegion.find(Pattern("Aquarium.png").similar(0.56));
        zoo="Aquarium";
        return zoo;
    except:
        pass;   
    try:
        zoc=AdvisorRegion.findAny(Pattern("1652374285038.png").similar(0.79),"fir.png")[0];
        print zoc;
        zoo="Fir";
#            return zoo;
    except:
        pass;
    try:
        zoc3=AdvisorRegion.findAny(Pattern("1648929649914.png").similar(0.74),"1682703766413.png","1648929649914.png")[0];
            zoo="Kujali";
            return zoo;
        zoc=zoc3;
    except:
        pass;
    try:
        zoc=AdvisorRegion.findAny("1646769787903.png",Pattern("1646455590532.png").similar(0.54))[0];
        zoo="Terrarium";
        return zoo;
    except:
        pass;   
    try:
        zoc=AdvisorRegion.findAny("1701004139598.png","1719357599064.png")[0];
        zoo="Oceanside";
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
#print which_zoo1();


oldzoo="unknown";

SetDestFir=0;
SetDestTerrarium=0;
SetDestAquarium=0;
SetDestOceanside=0;

def Hypnagogia(sc):
    if(sc<5):
        sleep(sc);
    else:
        now=datetime.datetime.now();
        print 'sleep ->',now
        togo = now+datetime.timedelta(seconds=sc-5);
        while now<togo:
            locMouse=Mouse.at();
            if locMouse.x<10 and locMouse.y<10:
                return;
            now1=now;
            #ScanLandmarks();
            result=Do.popAsk('66 seconds, No more Wait?',"come back {T}".format(T=togo),66);#,location=Location(30,30));
            if None == result:
              print "nothing to do"
            elif result:
              print "user said ",result;
              break;
            sleep(1)
            now=datetime.datetime.now();
            sk=(now-now1).total_seconds();
            sc-=sk;
            print(sk,"second killed",sc,"remain");            
        Log("Sleep short of {S}".format(S=sc));
        if(sc<0):
            pass;
#            Log("Sleep short of {S}".format(S=sc));
        else:
            if sc<20:
                sleep(sc);
            else:            
                result=Do.popAsk("quit Sleep {N}".format(N=sc),"{T}".format(T=now),sc);#,location=Location(30,30));
            now=datetime.datetime.now();
            print(now);
            
#Hypnagogia(0.1);
#Hypnagogia(4);
#Hypnagogia(40);      

def autoscale(loc,origin): #ClientRegions not my.ClientRegion
    if(scenario==origin):
        if(my.ClientRegion==ClientRegions[origin]):        
            return loc;
    cro=ClientRegions[origin];
    crs=my.ClientRegion;
    return Location(
    (loc.x-cro.x) *crs.w/cro.w+crs.x,
    (loc.y-cro.y) *crs.h/cro.h+crs.y);
def my_friend_1010():
    try:
       findAny(Pattern("1010.png").similar(0.85),Pattern("1682486256321.png").similar(0.86))[0];sleep(2)
#       print '10/10',find(Pattern("1010.png").similar(0.88));#8/10->0.87
       try:
           print '8/10',find(Pattern("1681601403382.png").similar(0.94));
           return 810;
       except:
           pass;
       click(Pattern("treasure_box.png").similar(0.63));sleep(5)
       type(Key.ESC);sleep(1);   
       return my_friend_openbox();
    except:
        return 999;
   
def my_friend_openbox():       
    try:
       click(findAny(Pattern("treasure_box_float.png").similar(0.69),Pattern("1682486456102.png").similar(0.66))[0]);sleep(5);   
       isgtx1060=(gtx1060==my.scenario)
       cards=findAll(["card_question.png","1682486571820.png"][isgtx1060]);
       i=0;
       for card in cards:
           click(card);sleep(2);
           i+=1;
           if (i>=4):
               break;
           click(card.offset(-5,0));sleep(2);
#       click(findAny("RedeemPrize.png","1682486713626.png")[0]);sleep(1);
	   my_redeem_prize();
       return 0;
    except:
        return 999;
#print my_friend_1010();
#print my_friend_openbox();
def my_redeem_prize():
   try:
           click("RedeemPrize.png");sleep(1);
           return 0;
   except:
       pass;
   cards=list(my.ClientRegion.findAll("card_question.png"));
   for card in cards:
      click(card);sleep(2);
      click(card.offset(-5,0));sleep(2);
      try:
           click("RedeemPrize.png");sleep(1);
           return 0;
      except:
          try:
              find("1681860792319.png");return 0;
          except:
           pass;#becare full may click too many cost key?
   return 999;
print my_redeem_prize()

def my_friend_gonext():
    sleep(2);
    if my_friend_1010()==0:
        sleep(1);
    lastLoc=autoscale(Location(513, 585),inossem);
    try: 
       lastLoc=auto(Region(403,538,251,105),inossem).find(managed("1649620530268.png","Yes"));
    except:
        Log("my_friend_gonext missign Yes ");
#            Location(489, 580) # Yes to next friend
    click(lastLoc);sleep(1);
    #sleep(my.TimeLoadZoo*12/22); #nothing to look at yet
    if Do.popAsk('my_friend_gonext..','',my.TimeLoadZoo/4)==False:
        print 'no more friend'
        return 999;
    return 0;
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
def entering_Main_Trump2024():
   for i in range(4):
       if my_breed_from_dialog()==0:
           my_born()
           my_born_success();
           break;
       type(Key.ESC);sleep(1);   
   type(Key.ESC);sleep(1);
   drag(Location(534, 680));dropAt(Location(707, 160));sleep(1)
   for i in range(3):
       r=my_many_cash()
       r=my_many_trash()
       if r==999:
           break;
   r=my_many_cash()
   
   for dg in [[Location(998, 314),Location(232, 482)]
        ,[Location(1062, 218),Location(181, 570)]   
           ,[Location(1062, 218),Location(181, 570)]
           ,[Location(1062, 218),Location(181, 570)]
   ]:
       drag(dg[0]);dropAt(dg[1]);sleep(1)
       for i in range(3):
           r=my_many_cash()
           r=my_many_trash()
           if r==999:
               break;
       r=my_many_cash()
#entering_Main_Trump2024()

def entering_Fir_Trump2024():
   my_breed_from_dialog();
   my_born()
   my_born_success()                    
   type(Key.ESC);
   for i in range(3):
       r=my_many_trash()
       if r==999:
           break;
       r=my_many_cash()
       if r==0:
           break;
       drag(Location(907, 170));dropAt(Location(634, 680));sleep(1)
#entering_Fir_Trump2024()

def entering_Kujali_Trump2024():
   my_breed_from_dialog();
   my_born()
   my_born_success()                    
   type(Key.ESC);
   type(Key.ESC);
   for j in range(3):
       for i in range(3):
           r=my_many_trash()
           if r==999:
               break;
           r=my_many_cash()
           if r==0:
               break;
       drag(Location(907, 170));dropAt(Location(634, 680));sleep(1);
#entering_Kujali_Trump2024()

def entering_Terrarium_Trump2024():
   my_breed_from_dialog();
   my_born()
   my_born_success()                    
   type(Key.ESC);    
   sleep(1);
   LocCenter=my.ClientRegion.getCenter();
   wheel(LocCenter,Button.WHEEL_DOWN,10);
   sleep(2);
   for i in range(3):
       r=my_many_trash()
       if r==999:
           break;
       r=my_many_cash()
   drag(Location(927, 170));dropAt(Location(621, 622));sleep(1)
   for i in range(3):
       r=my_many_cash()
       r=my_many_trash()
       if r==999:
           break;
#entering_Terrarium_Trump2024()
def entering_Aquarium_Trump2024():
   my_breed_from_dialog();
   my_born()
   my_born_success()                    
   type(Key.ESC);    
   sleep(1);
   LocCenter=my.ClientRegion.getCenter();
   wheel(LocCenter,Button.WHEEL_DOWN,10);
   sleep(2);
   for i in range(3):
       r=my_many_trash()
       if r==999:
           break;
       r=my_many_cash()
   drag(Location(927, 170));dropAt(Location(621, 622));sleep(1)
   for i in range(3):
       r=my_many_cash()
       r=my_many_trash()
       if r==999:
           break;
#entering_Aquarium_Trump2024()

def entering_Main_Mom():
   my_breed_from_dialog();
   my_born()
   my_born_success()                    
   type(Key.ESC);
   type(Key.ESC);
   type(Key.ESC);
   drag(Location(534, 680));dropAt(Location(707, 160));sleep(1)
   for i in range(3):
       r=my_many_trash()
       if r==999:
           break;
       r=my_many_cash()
   drag(Location(998, 304));dropAt(Location(232, 482));sleep(1)
   for i in range(3):
       r=my_many_trash()
       if r==999:
           break;
       r=my_many_cash()
   drag(Location(1062, 218));dropAt(Location(181, 570));sleep(1)
   for i in range(3):
       r=my_many_trash()
       if r==999:
           break;
       r=my_many_cash()
   drag(Location(1062, 218));dropAt(Location(181, 570));sleep(1)
   drag(Location(1062, 218));dropAt(Location(181, 570));sleep(1)
   my_many_cash()
#print entering_Main_Mom();


def entering_Fir_Mom():
   my_breed_from_dialog();
   my_born()
   my_born_success()                    
   type(Key.ESC);
   for i in range(3):
       r=my_many_trash()
       if r==999:
           break;
       r=my_many_cash()
       if r==0:
           break;
#entering_Fir_Mom()
def entering_Main_Charlotte():
   my_breed_from_dialog();
   my_born()
   my_born_success()                    
   sleep(1);
   LocCenter=my.ClientRegion.getCenter();
   wheel(LocCenter,Button.WHEEL_DOWN,10);
   for i in range(7):
       d=(my.ClientRegion.w+my.ClientRegion.h)/100;
       loc3=Location(my.ClientRegion.x+my.ClientRegion.w*5/6+random.randint(-d,d),my.ClientRegion.y+my.ClientRegion.h*5/6+random.randint(-d,d))
       loc4=Location(my.ClientRegion.x+my.ClientRegion.w/8+random.randint(-d,d),my.ClientRegion.y+my.ClientRegion.h/6+random.randint(-d,d))
       drag(loc3);dropAt(loc4);sleep(1)    
   loc3=Location(my.ClientRegion.x+my.ClientRegion.w*5/6,my.ClientRegion.y+my.ClientRegion.h*5/6)
   loc4=Location(my.ClientRegion.x+my.ClientRegion.w/8,my.ClientRegion.y+my.ClientRegion.h/6)
   drag(loc3);dropAt(loc4);sleep(1)    
   for i in range(3):
       d=(my.ClientRegion.w+my.ClientRegion.h)/100;
       loc1=Location(my.ClientRegion.x+my.ClientRegion.w*4/6+random.randint(-d,d),my.ClientRegion.y+my.ClientRegion.h/6+random.randint(-d,d))
       loc2=Location(my.ClientRegion.x+my.ClientRegion.w/8+random.randint(-d,d),my.ClientRegion.y+my.ClientRegion.h*5/6+random.randint(-d,d))
       drag(loc1);dropAt(loc2);sleep(1)    
   loc1=Location(my.ClientRegion.x+my.ClientRegion.w*4/6,my.ClientRegion.y+my.ClientRegion.h/6)
   loc2=Location(my.ClientRegion.x+my.ClientRegion.w/8,my.ClientRegion.y+my.ClientRegion.h*5/6)
   drag(loc1);dropAt(loc2);sleep(1)    


def entering_Kujali_Charlotte():
    my_many_cash();
    
    pass;

def entering_Kujali_Mom():
   my_breed_from_dialog();
   my_born()
   my_born_success()                    
   type(Key.ESC);
   for i in range(3):
       r=my_many_cash()
       if r==0:
           break;
       r=my_many_trash()
       if r==999:
           break;
   drag(Location(927, 170));dropAt(Location(621, 622));sleep(1)
   for i in range(3):
       r=my_many_cash()
       if r==0:
           break;
       r=my_many_trash()
       if r==999:
           break;

def entering_Terrarium_Mom():
   my_breed_from_dialog();
   my_born()
   my_born_success()                    
   type(Key.ESC);    
   sleep(1);
   LocCenter=my.ClientRegion.getCenter();
   wheel(LocCenter,Button.WHEEL_DOWN,10);
   sleep(2);
   for i in range(3):
       r=my_many_trash()
       if r==999:
           break;
       r=my_many_cash()
   drag(Location(927, 170));dropAt(Location(621, 622));sleep(1)
   for i in range(3):
       r=my_many_cash()
       r=my_many_trash()
       if r==999:
           break;

def entering(zoo):
    try:
        f=globals()['entering_'+zoo+'_'+getLogin()]
        print f
        f();
        return;
    except:
        pass;
    if zoo==Terrarium:
        sleep(1);
        LocCenter=my.ClientRegion.getCenter();
        wheel(LocCenter,Button.WHEEL_DOWN,10);
        sleep(2);
    elif zoo==Main:
        drag(autoscale(Location(703, 651),inossem));
        dropAt(autoscale(Location(650, 136),inossem));
    
def my_friend_exit():    #exit to tbd
    try:
        rg=my.ClientRegion
        rg=Region(rg.x+rg.w*9/10,rg.y,rg.w/10,rg.h*2/10)
        lastLoc=rg.find(managed("1653518245883.png","my_friend_exit"));
        print lastLoc
        if lastLoc!=Location(0,0):
        #    lastLoc=Location(1169, 133);
            click(lastLoc)
            result=Do.popAsk('faster or','slower TimeLoadZoo',my.TimeLoadZoo*15/22);
            if None == result:
              print "nothing to do"
            elif result:
                my.TimeLoadZoo=my.TimeLoadZoo*7/10;
            else:
                Do.popAsk('wait more',my.TimeLoadZoo*3/10)
                my.TimeLoadZoo=my.TimeLoadZoo*13/10;
            #entering(zoo);
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
        Do.popAsk(inspect.stack()[0][3],'',15);
        entering(zoo);
        return 77;
    except:
        Log("my_friend_exit_all not found");
        pass;
#my_friend_exit_all();

def my_friend():
   try:
        lastLoc=my.ClientRegion.find(managed("1652298276529.png","my_friend")).getTarget(); 
        #was.png for inossem
        return 0;
   except:
       return 999;
#my_friend();

#my.ClientRegion=Region(5,36,1360,694);#for charlotte @ inossem
#scenario='new';
#meshnet="1651443957097.png";
#LocCenter=my.ClientRegion.getCenter();
zoo="Main"
#meshnet=managed("1651687266431.png","meshnet");#was 1645891158890.png for inossem
meshnet=managed("1653449826127.png","meshnet");#was 1645891158890.png for inossem
#print meshnet;
butarea={inossem:Region(291,444,477,310),
        gtx1060:Region(548,859,228,203)}[scenario];

def my_friend_meshnet():
    return findAny(
    	"1677381251161.png",
    	"1653449826127.png",
    	"1665005562955.png")[0]; 

#corco={inossem:Location(1110, 580),gtx1060:Location(1603, 823)}[scenario];
corco=autoscale(Location(1110, 580+20),inossem);
update_ClientRegion()

def my_friend_hare():
    lastLoc=my_friend_meshnet();
    if lastLoc==Location(0,0):
        return 999;
#        print lastLoc             
    reachX=200;
    reachY=126;
    offsetY=40;
    #charlotte:
    if(scenario=="gtx1060"):
        reachX=270;
        reachY=150;
        offsetY=40;
    corco=autoscale(Location(1110, 580+20),inossem);
    try:
        corco=find(Pattern("1677551857161.png").similar(0.37));
    except:
        pass;
    for i in range(26):
        if i>4:
            try:
                ({inossem:Region(515,333,397,343),
                gtx1060:Region(954,641,390,329)}[scenario]).find(
                       managed( "1671483528445.png","gohome"));
                return my_friend_gonext(); 
            except:
                pass;
        if i>8:
            if my_friend_meshnet()==Location(0,0):
                Log("interrupted, try ESC")
                tofail=True
                for k in range(4): 
                    type(Key.ESC);
                    sleep(0.4);
                    tofail=(my_friend_meshnet()==Location(0,0))
                    if not tofail:
                        break;
                if not tofail:
                    continue;
                return 999;
        click(lastLoc);sleep(0.5)                
        ct=0
        offs_rabbit   ={inossem:[[-300,-316+offsetY],[-110,155+offsetY],[220,-220+offsetY]],
                gtx1060:[[-reachX,-reachY+offsetY],[-140,195+offsetY],[270,-295+offsetY]]}[scenario];
        drag(corco);
        locg=my.ClientRegion.getCenter();
        for off in offs_rabbit:            
            drag(locg.offset(off[0],off[1]));
        dropAt(locg);                        
    sleep(0.6);#1.2
    print "Rabbit gone after all attemps";
    r=my_friend_exit();#failed rabit?                    
    type(Key.ESC);
    return 0;
#print my_friend_hare();

#print my_friend1();

#print my_friends();

def my_friend_catch():
    w=50
    LocCenter=my.ClientRegion.getCenter();
    rg=Region(LocCenter.x*3/2-w,LocCenter.y*3/2-w,2*w,2*w);
    rg1=rg.grow(w*2)
    sc=rg.getScreen();                
    lastLoc=my_friend_meshnet();
    if lastLoc==Location(0,0):
        return 999;
#        print lastLoc             
    reachX=200;
    reachY=126;
    offsetY=40;
    #charlotte:
    if(scenario=="gtx1060"):
        reachX=270;
        reachY=150;
        offsetY=40;

        
    for i in range(16):
        if i>4:
            try:
                ({inossem:Region(515,333,397,343),
                gtx1060:Region(954,641,390,329)}[scenario]).find(
                       managed( "1671483528445.png","gohome"));
                return my_friend_gonext(); 
            except:
                pass;
        if i>8:
            if my_friend_meshnet()==Location(0,0):
                dropAt(locg)
                Log("interrupted, try ESC")
                tofail=True
                for k in range(4): 
                    type(Key.ESC);
                    sleep(0.4);
                    tofail=(my_friend_meshnet()==Location(0,0))
                    if not tofail:
                        break;
                if not tofail:
                    continue;
                return 999;
        click(lastLoc);sleep(0.5)                
        img=sc.capture(rg)
        nofound=True;
        now=datetime.datetime.now()
        tt=now;
        for j in range(4):
            click(lastLoc);sleep(0.8)                
            now=datetime.datetime.now()
            try:
                loc1=rg1.find(img);
                print rg.x-loc1.x,rg.y-loc1.y,now
                if nofound:
                    nofound=False
                    tt=now
                    loc0=loc1
                else:
                    break;
            except:
                if nofound:
                    img=sc.capture(rg) 
                pass;
        if nofound:
            print 'moving obj nofound , must be fast rabbit';
            return my_friend_hare();
        dt=(now-tt).total_seconds()
        print dt
        d1=2.1
        locg=LocCenter;
        if dt>0.0:
            locg=LocCenter.offset(int((loc0.x-loc1.x)*d1/dt),int((loc0.y-loc1.y)*d1/dt));
        print 'locg=',locg
        drag(corco);
        drag(locg)
        ct=0
        offs_rabbit   ={inossem:[[-reachX,-reachY+offsetY],[-110,155+offsetY],[220,-220+offsetY]],
                gtx1060:[[-reachX,-reachY+offsetY],[-140,195+offsetY],[270,-295+offsetY]]}[scenario];
        offs_snow_hare={inossem:[[-reachX,-reachY+offsetY],[-110,155+offsetY],[225,-230+offsetY]],
                gtx1060:[[-reachX,-reachY+offsetY],[-140,195+offsetY],[270,-295+offsetY]]}[scenario];
        offs_goat     ={inossem:[[-reachX,-reachY+offsetY],[-100,145+offsetY],[195,-220+offsetY]],
                gtx1060:[[-reachX,-reachY+offsetY],[-140,195+offsetY],[270,-295+offsetY]]}[scenario];
        offs_jagua    ={inossem:[[-reachX,-reachY+offsetY],[-100,145+offsetY],[195,-220+offsetY]],
                gtx1060:[[-reachX,-reachY+offsetY],[-140,195+offsetY],[270,-295+offsetY]]}[scenario];
        offses=[offs_rabbit,offs_snow_hare,offs_goat,offs_jagua]
        id=random.randint(0, 3)
        offs=offses[id];
        print id,':',offs;
        for off in offs:            
            drag(locg.offset(off[0],off[1]));
        dropAt(LocCenter);                        
        sleep(0.5)                
    sleep(0.6);#1.2
    print "Goat/Jaguar gone after all attemps";
    r=my_friend_exit();#failed rabit?                    
    type(Key.ESC);
#print my_friend_catch()
my.friend_active=True;
#print my_friend1();
#print my_friends();

def find_close():
    rg=my.ClientRegion.grow(my.ClientRegion.w/7)
    return rg.findAny(Pattern("1677459673567.png").similar(0.66),"1681431545832.png","Close_top_right.png")[0];

print my.ClientRegion

def my_friend1():
   if not my.friend_active:
       return 999;
   LocCenter=my.ClientRegion.getCenter();
   print LocCenter
   try:
       #my_friend_catch()
       #DO NOT catch
       print my.ClientRegion.findAny(Pattern("catch.png").similar(0.56),Pattern("1682484144561.png").similar(0.62),"1703957091567.png")[0];
#       click(findAny("close.png","1682483897569.png")[0]);sleep(1)
       click(find_close());sleep(1)
       Do.popAsk('my_friend_catch_cancell: too hard ','',my.TimeLoadZoo*3/8);
       r=my_friend_help()
       if r!=0:
            return 999;
   except:
       pass;
   try:
        lastLoc=my.ClientRegion.findAny("1653446315434.png")[0]; 
        #print lastLoc #0.75 grey
        LocCenter=my.ClientRegion.getCenter().offset(my.ClientRegion.w/50,-my.ClientRegion.h/100);
        mouseMove(LocCenter)
        try:        
            rg=Region(my.ClientRegion.x+my.ClientRegion.w*3/4
                    ,my.ClientRegion.y+my.ClientRegion.h*2/4,
                    my.ClientRegion.w*2/5,my.ClientRegion.h/2)
            corco=rg.findAny(Pattern("1677457062553.png").similar(0.69),Pattern("1704685652651.png").similar(0.57),"1704686460714.png")[0];
#            LocCenter=Location((loc.x+4*lastLoc.x)/5,(4*loc.y-2*lastLoc.y)/2);
        except:
            pass;
        for i in range(5):
            click(lastLoc);
            Hypnagogia(my.TimeLoadZoo/50.0);
            loc=corco;
            click(loc)
            sleep(my.TimeLoadZoo/100.0)
            drag(loc);
            Hypnagogia(1);
            dropAt(LocCenter); #for slopy view?
            Hypnagogia(my.TimeLoadZoo/100.0);
        Hypnagogia(2);
        return my_friend_gonext();
   except:
       pass;
   try:        
        lastLoc=my.ClientRegion.findAny("1677381035273.png",Pattern("1653449413546.png").similar(0.54),"Ravin.png")[0];           
        locc=find_close()
        locc=Location((2*locc.x+5*lastLoc.x)/7,(4*locc.y+5*lastLoc.y)/9);
        for k in range(5):
            click(lastLoc);
            Hypnagogia(1.25);
            if k==0:
                try:
                    w=60
                    rg=Region(locc.x-w,locc.y-w,2*w,2*w)
                    locc=rg.find("1672880015647.png").getTarget();
                except:
                    pass;
            for i in range(3):
                click(locc);
                Hypnagogia(0.25);
        return my_friend_gonext();
   except:
       pass;
   LogScreen();
   return 999;
#my_friend_gonext();
#my.friend_active=True;print my_friend1();
    
import logging
def LogScreen():
    sc=Screen()
    img=sc.capture()
    name='{}.{}.png'.format(inspect.stack()[1][3],datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    img.save(getBundlePath(),name);
    Log(name);
    logging.debug('<img src="{}" />'.format(name));
    
def testLogScreen():
    LogScreen();
testLogScreen();

LOG_FILENAME = getBundlePath()+'\example.log'
print LOG_FILENAME 
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
logging.debug('This message should go to the log file')

menudrop=auto_must(Region(1125,94,102,77),inossem);
print menudrop
def my_friend_menu_drop():
   if not my.friend_active:
        return 999;
   try:
        lastLoc=menudrop.findAny("1652299608937.png","my_friend_menu_drop.png")[0]; 
        click(lastLoc); sleep(1.25);
        return 0;
   except:
       pass;
   return 999;
#print my_friend_menu_drop();

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
    t=my.last.get('ClientRegion')
    if t:
     if lastRegion2X4>my.last['ClientRegion']:
        if Region2X4!=Region(0,0,0,0):
            return Region2X4; 
    now=datetime.datetime.now();
    lastRegion2X4=now;    
    sample="1652931147389.png";
    name="my_friend_tbd";
    locs=my.ClientRegion.findAll(managed(sample,name)); 
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
        locsy=my.ClientRegion.findAll(samply); 
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
#close friend button: L[1220,163]@S(0) R[20,65 1329x661]@S(0) 0.902934537246 0.1482602118
my.friend_tbd1=False;
#print my_friend_tbd()
#print my_friend1()
#def find_candy(pic,name):
#    my.ClientRegion.find(managed(pic,name)); 
#find_candy("1652301900036.png","help");




my.tamp_friend_menu=4
def my_friend_menu():
    if not my.friend_active:
        my.tamp_friend_menu=0;
        t=my.last.get('friend_active')            
        now=datetime.datetime.now();
        if now.hour-t.hour<0 or now.hour-t.hour>2:           
            my.friend_active=True;
        elif now.hour==19 and t.hour<19: #daylight saving tbd 20
            my.friend_active=True;
        else:            
            return 999;
    my.tamp_friend_menu=my.tamp_friend_menu+1
    h=(4+datetime.datetime.now().hour)%24; #how about daylight saving?
    if random.random()>h*h/24.01/my.tamp_friend_menu:
       return 888; #next chance
    my_friend_menu_drop(); #cannot use safely
    try:
        lastLoc=find(managed("1652299824877.png","my_friend_menu")); 
        click(lastLoc);sleep(4)
    except:
        return 999;
    return my_friend_help();

idAnyAll={};
def findAnyAll(a):
    key=sum(map(lambda x:hash(x), a))
    if  idAnyAll.get(key) is not None :
        i=idAnyAll.get(key);
        loc_tbd=list(my.ClientRegion.findAll(a[i]));
    else:
        loc_tbd=list(my.ClientRegion.findAny(a));
        if len(loc_tbd)==0:
            if random.random()<0.1:
                del idAnyAll[key];
            return loc_tbd;
        imax=-1;
        nmax=0;
        loc_tbdmax=[];
        print 'xxx'
        for i in range(len(a)):
           print i
           loc_tbd=list(my.ClientRegion.findAll(a[i])); 
           if len(loc_tbd)>nmax:
               nmax=len(loc_tbd);
               imax=i;
               loc_tbdmax=loc_tbd;
        if imax>-1:
            idAnyAll[key]=imax;
            return loc_tbdmax;
    return loc_tbd

def my_friend_helpy():
    #"1717544695161.png"
    isgtx1060=(gtx1060==my.scenario)
    loc_help=False;
    for k in range(2):
        try:
            loc_help=my.ClientRegion.findAny(Pattern("1664845762765.png").similar(0.92),"help2.png")[0];#help
            isHelp=True;
            if loc_help.getScore()<0.93: #gray for 0.85
                try:
                   loc_help_gray=loc_help.grow(100).findAny("1664848752264.png","helpgray.png")[0]; 
                   print loc_help_gray
                   if loc_help_gray.getScore()>loc_help.getScore():
                       isHelp=False;
                except:
                     pass;
            if isHelp:
                click(loc_help);
                Do.popAsk('help...','',my.TimeLoadZoo)               
                return 0;
        except:                               
            pass;
        for ii in range(2):            
           sleep(1);
           try:
               loc_tbd=findAnyAll([Pattern("1681157936645.png").similar(0.66),Pattern("1682484909768.png").similar(0.74),Pattern("1702436558463.png").similar(0.96),Pattern("1704695474006.png").similar(0.94),Pattern("1705519957121.png").similar(0.94)])
               print loc_tbd
 
#               loc_tbd=list(findAll([Pattern("1681157936645.png").similar(0.84),Pattern("1682484909768.png").similar(0.93),Pattern("1702436558463.png").similar(0.97)]))
               AnyWork=False;
               for loc in loc_tbd:
                   try:
                       rg=loc.grow(80);
#                       exs=list(rg.findAny([[Pattern("1681154621992.png").similar(0.89),Pattern("1681239571826.png").similar(0.90)],[Pattern("1682485274966.png").similar(0.95),Pattern("1682485321162.png").similar(0.96)]][isgtx1060]))
                       exs=list(rg.findAny(Pattern("1681154621992.png").similar(0.89),Pattern("1681239571826.png").similar(0.90),Pattern("1682485274966.png").similar(0.95),Pattern("1682485321162.png").similar(0.96),Pattern("1705572783200.png").similar(0.95)))
                       if len(exs)>0:
#                           s1=list(rg.findAny([[Pattern("1681239434782.png").similar(0.89),Pattern("1681239482463.png").similar(0.90)],[Pattern("1682485529411.png").similar(0.92),Pattern("1682485490712.png").similar(0.97)]][isgtx1060]))[0].getScore()
                           sl1=list(rg.findAny(Pattern("1681239434782.png").similar(0.95),Pattern("1681239482463.png").similar(0.95)));
                           if len(sl1)==0:
                               continue;
                           sl=sl1[0].getScore()
                           s2=exs[0].getScore();
                           print s1,' vs ',s2;
                           if s1<s2:
                               continue;
                   except:
                       pass;
                   AnyWork=True;
#                   print loc;mouseMove(loc);sleep(1)
                   click(loc);sleep(1)
                   Do.popAsk('help..##.','',my.TimeLoadZoo/4);#/6
                   return 0;
                   break;
               print AnyWork;
               if AnyWork:
                   break;
               if ii==1:
                   print 'no AnyWork'
                   my.friend_active=False;                    
                   type(Key.ESC);              
                   return 999; 
           except:
               if ii==1:                   
                   print 'no help'                    
                   my.friend_active=False;                    
                   type(Key.ESC);              
                   return 999; 
           sleep(1);
           try:                         
               isgtx1060=(gtx1060==my.scenario)
               click(findAny(Pattern("1664850302990.png").similar(0.68).targetOffset(3,-6),Pattern("1682485603015.png").similar(0.69).targetOffset(17,0))[0]);sleep(2)#2 dots
           except:
               print 'miss dots'                    
               type(Key.ESC);              
               return 999;
    if loc_help:
        print loc_help
        click(loc_help);sleep(1) #cannot merge Do. some strange happen to input
        Do.popAsk('help..in..','',my.TimeLoadZoo/3)               
        return 0;
#my_friend_helpy();
#my.friend_active =True;print my_friends()

def my_friend_help():
    if (my_friend_helpy()!=0):
        return 999;
    Do.popAsk('help friends ','',my.TimeLoadZoo/3)                   
    r=my_friends();
    my.friend_active=False;
    return r
my.friend_active=True
my.friend_togo=3 #40 #minutes
#print my_friend_menu();
#print my_friend_help()
#print my_friend1()
#print my_friends()

def my_friends():    
    togo=datetime.datetime.now()+datetime.timedelta(minutes=my.friend_togo)
    while  datetime.datetime.now()<togo:
       r=my_friend1();
       print r
       if r==999:
           break;
           #return r;
       if r==0:
           err='waiting for next friends...'.format(r);
           Log(err);
           Do.popAsk(err,'',my.TimeLoadZoo/2)
       else:
           err='waiting for failed {} friend '.format(r);
           Log(err);
           Do.popAsk(err,'',my.TimeLoadZoo/6);
    return 77;

global button_help_all;
def update_button_help_all():
    try:         
#        pic=managed("1652302667522.png","help_all");
        pic=managed("1653443300630.png","help_all");
        button_help_all=my.ClientRegion.find(pic);
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
#t=findBeast(my.ClientRegion, "1653443901464.png","help_all");
#print my.idpoppy
my.poppy="1718941701980.png" #"1715211623798.png"

def my_many_poppy():
    rg=my.ClientRegion.grow(-100);#-30 may confuse with menu       
    poppies=["1707347786538.png","1707350753020.png","1707351135101.png"];#rememberance 
#    work=[rg,poppies[my.idpoppy]];
    work=[[rg,"1715211591268.png"],[rg,my.poppy] 
            #Mothers day May 7
#            [rg,"1710997467051.png"]#easter egg 3/21
#                [rg,Pattern("1707371374812.png").similar(0.57)]#Valentine 2/7
#                [rg,"1694086547773.png"]#Autumn prize 6/21
#sunshine            [rg,"1687395907071.png"]#summer prize 6/21
#crown                [rg,Pattern("1683748137350.png").similar(0.59)],[rg,Pattern("1683748152942.png").similar(0.47)],[rg,Pattern("1683748645109.png").similar(0.83)],[rg,"1683748782525.png"]#mother's day 5/10
#leaves                [rg,"1662688883972.png"],[rg,"1662688897467.png"],[rg,"1662688909725.png"]
#pumpkin                ,    [rg,"1666832106820.png"]

               ]
    r0=999;
    for i in range(20):
        r=my_many_work(work);sleep(3);
        if r==999:
            if r0==999:
                tl=t0;
                try:
                    tl=my.last['idpoppy'];
                except:
                    pass;
                if tl+datetime.timedelta(hours=7)<now :    
                    my.idpoppy=random.randrange(0,len(poppies)); 
            return r0;
        my_many_water();sleep(1)
        r0=r;
        sleep(4);   
    return r
#print my_many_poppy()

def my_friend_in():    
    if not my.friend_active:            
        typemaybe_Key_ESC();
        return 999;
    try:
        locgray=find( "1661914433890.png"); 
        print locgray
        if locgray.getScore()>0.97 :
            print "help all is gray!";
            my.friend_active=False
            typemaybe_Key_ESC();
            return 999;
    except:
        pass;
    kl=my_friend1();
    print kl
    while kl==0:
         kl=my_friend1();
#    my_friend_exit();
    for tt in range(1,20):
       notin=(my_friend_tbd()!=0);
       print notin 
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
                print loc,loc.grow(100)
                locgray=loc.grow(100).find( "1661914433890.png"); 
                print locgray 
                if locgray.getScore()>loc.getScore():
                    print 'help all is gray la';
                    my.friend_active=False;
                    typemaybe_Key_ESC();
                    return 999;
                drag(autoscale(Location(1007, 329),inossem));
                lastLoc=Location(620, 346);
                dropAt(lastLoc);
                Hypnagogia(3);
            except:
                print "no help_all";
                my.friend_active=False;
                return 999;
            notin=(my_friend_tbd()!=Location(0,0));
       if notin :
             if(my_friend_help()==0):
                 notin=False;             
             else:
                  return 0;    
       for h in range(1,8):
#           Hypnagogia(22);
           Do.popAsk('more my_friend1','8 times',my.TimeLoadZoo);
           kl=my_friend1();              
           if kl>0:
               break;
       my_friend_exit();
    my.friend_active=False;
    my_friend_exit_all();
    return 999;
my.friend_active=True
#print my_friend_in();
#print my_friend1();
#my_friend_menu();#close popup still in need

def SetRampDest(x,y) :
    global DescX;
    global DescY;
    DescX=x;
    DescY=y;
    Log('Desc [{X},{Y}]'.format(X=x,Y=y));

locss={
        gtx1060:[Location(487, 337),Location(1510, 305),Location(1569, 876),Location(480, 780)],
        inossem:[Location(236, 263),Location(1018, 262),Location(993, 581),Location(223, 566)]
        };
    
my.direct=0

def my_grandpa():
    try:
        click(findAny(Pattern("ramp_helper_head.png").similar(0.53),"1704605432837.png")[0]);sleep(3) #my.TimeLoadZoo/77=1
        click("ramp_helper_news.png");sleep(3);
        if my_breed_from_dialog()==0:
            return 0;
        if my_chest_from_dialog()==0:
            return 0;
        if my_littlehelp_from_dialog()==0:
            return 0;
        type(Key.ESC);sleep(1)
        return 0;
    except:
        return 999;
#print my_grandpa();

def my_littlehelp_from_dialog():
    try:
        click("1704610365099.png");sleep(2)
        click(Pattern("1704610414070.png").targetOffset(-68,-11));sleep(2)
        return my_friend_openbox();        
    except:
        return 999;

def ramp_take_care():
    try:
        click("ramp_take_care.png");sleep(1)
        return 0;
    except:
        return 999;
#ramp_take_care();
my.ramp_reached=0;
def Perturbation():
    type([Key.UP,Key.DOWN,Key.LEFT,Key.DOWN][random.getrandbits(2)]);

def my_ramp():   
    my.ramp_reached=my.ramp_reached+1;
    if scenario!=gtx1060:
        type_Key_ESC()
        type_Key_ESC()
        type_Key_ESC()
        type_Key_ESC()
    else:
        type(Key.ESC);
        type(Key.ESC);
        my_close();
    if random.random()<0.2:
        if my_grandpa()==0:
            return 0;
    if random.random()<0.2:
        if ramp_take_care()==0:
            return 0;
    Perturbation()
    zoo=which_zoo1();
    if(zoo=="unknown"):
        print "ramp unknown not allowed"
        return 999;
    global DescX,DescY,CenterX,CenterY;
    for m in range(10):
        lastLoc=Location(0,0);
        if len(ROI)>0 :
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
            if random.random()>0.2:
                k=my.direct
            else:
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
                continue;
                return 0;
        if k==1: #top right
            if(CenterX-CenterY>24044):
                Log('Cancle move Top Right');
                continue;                
                return 0;
        if k==2: #bottom right
            if(CenterX+CenterY>27000):
                Log('Cancle move Bottom Right');
                continue;
                return 0;
        if k==3: #bottom left
            if(CenterX-CenterY<-144):
                Log('Cancle move Bottom Left');
                k=1;
        break;
    my.direct=k
    locs=locss[my.scenario];
    print my.direct,locs
    if lastLoc.x==0 and lastLoc.y==0:
        print locs,k
        lastLoc=locs[(k+2)%4];
        lastLoc=Location(lastLoc.x+random.randrange(-10,10)  ,    
                lastLoc.y+random.randrange(-10,10));
#        Log('Drag to {K}/{L}'.format(K=k,L=lastLoc));
    loc=locs[k];
#    loc=Mouse.at()
    print 'Drag: ',loc
    ws=[[100,0,0]
            ,[50,0,0],[50,50,0],[50,-50,0],[50,0,50],[50,0,-50]
            ,[20,0,0]
            ,[10,0,0]]
    for w in ws:
        rg=Region(loc.x-w[0]+w[1],loc.y-w[0]+w[2],2*w[0],2*w[0])
#        sc=rg.getScreen();                
        sc=Screen()
        img=sc.capture(rg) #LocCenter.x-w+offsetX,LocCenter.y-w+offsetY,2*w,2*w);#.png
        name='ramp{I}.png'.format(I=w[0])
        img.save(getBundlePath(),name)
        try:        
            lc1=find(img).getTarget()
        except:
            print 'find capture fail: ',name
            continue;
        if lc1==rg.getCenter():
            print w[0],':',lc1
            w.append(img)
        else:
            print w[0],':',lc1,'!=',rg.getCenter()
    mouseMove(loc)
    drag(loc);
#    sleep(0.01)# fail in enclosure 
#    lastLoc=loc.offset(30,30) 
    dropAt(lastLoc);
    print 'Drop >: ',lastLoc
    my.rampcnt+=1;
    Found=False;
    rg=Region(lastLoc.x-200,lastLoc.y-200,400,400)
    for w in ws:
        if len(w)<4:
            continue;
        try:
            img=w[3]
            loc2s=rg.find(img)
            print loc2s
            loc2=loc2s.getTarget()
            print loc2
            if loc.offset(w[1],w[2])==loc2:
                print 'no move'
                return 999;
            Found=True;
            print lastLoc.offset(w[1],w[2]),'=?=',loc2
            img.save(getBundlePath(),'from.png')
            sc.capture(loc2s).save(getBundlePath(),'to.png') 
            break;
        except:
            pass;    
    if not Found:
        my.missing+=1
        print 'missing=',my.missing,'/',my.rampcnt
    CenterX-=lastLoc.x-loc.x;
    CenterY-=lastLoc.y-loc.y;
    Log('Ramp {Z}({X},{Y})'.format(Z=zoo,X=CenterX,Y=CenterY));
    Hypnagogia(0.1);
    return 0;
#print my_ramp()

if False:    
    Log('From {Z}({X},{Y})'.format(Z=zoo,X=CenterX,Y=CenterY));
    print my_ramp()
    print find('ramp100.png')

#findAnyList
#findBest
#findBestList
          
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
Aquarium="Aquarium";
Polar="Polar";
Oceanside="Oceanside";

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
#lastVisit={Main:t0,Fir:now,Terrarium:now,Kujali:now};
firstVisit={Main:t0,Fir:t0,Terrarium:t0,Kujali:t0};
my.Blocked={Main:False,Fir:False,Terrarium:False,Oceanside:False,Aquarium:False,Kujali:False,Polar:False};
#lastCheck={Main:t0,Fir:now,Terrarium:now,Kujali:now};
enteringTime={};#Main:t0,Fir:now,Terrarium:now,Kujali:now};
oldzoo1="unknown";
my.OldestZoo="Main";

nextTime={Main:900,Fir:1500,Terrarium:1400,Kujali:1100,Aquarium:1200,Oceanside:1222,Polar:1234};

def UpdateOldestZoo():    
    old="Main";
    told=my.Visits[old].last+ datetime.timedelta(seconds=nextTime[old])
    for key in [Main,Fir,Terrarium,Kujali,Aquarium,Oceanside]:
        t=my.Visits[key].last+datetime.timedelta(seconds=nextTime[key]);
        if(t<told):
            old=key;
            told=t;
    my.OldestZoo=old;
#UpdateOldestZoo()
#print my.OldestZoo
#to deal with frequency, not sleeping
my.oldzoo1=oldzoo1
my.oldzoo=oldzoo

class AutoGrow:
    newer={}
    me={}
    def __init__(self, d):
        self.newer=d;
    def __getitem__(self, key):
        c=self.me.get(key);
        if c:
            pass;        
        else:
            try:
                c=self.newer();       
            except:
                c=self.newer;
            self.me[key]=c;
        return c;
        
#my.Visits=AutoGrow(Visit);
#print my.Visits

def which_zoo():
   now=datetime.datetime.now();
   enabledonzoo=True;
   zoo=which_zoo1(); 
   if(my.oldzoo1!=zoo) :
       if(zoo!="unknown"):
           if(my.oldzoo!=zoo):
             Log("{O}=>{Z}".format(O=my.oldzoo,Z=zoo));
             my.oldzoo=zoo;
             if(oldzoo!="unknown"):
                 #exiting(oldoldzoo);
                 pass;
             my.Visits[zoo].first=now;
             if zoo==my.OldestZoo:
                 UpdateOldestZoo();
       my.oldzoo1=zoo;
   if(zoo=="unknown"):
            unknown_recovering();
            Log("unknown zoo , back to "+oldzoo);
            #type(Key.ESC);              #queue this , for readonly in this function
            return my.oldzoo;
   my.Visits[zoo].last=now;
   return zoo;

#zoo=which_zoo(); #4/2
#print zoo,Visits[zoo].last;


my.LocDropDown=Location(1176, 128); #menu drop down button
my.LocGotoMap=Location(1712,871)#gtx1060 
my.scenario=scenario
print my.scenario
my.Zoogs={inossem:{Main:Location(498, 327),
        Fir:Location(591, 194),
        Terrarium:Location(373, 540),
        Kujali:Location(765, 627),            
        Oceanside:Location(202, 385),
        Aquarium:Location(214, 618)
        },
        gtx1060:{Main:Location(811, 431),
        Fir:Location(949, 206),
        Terrarium:Location(597, 755),
        Kujali:Location(1224, 887),
        Oceanside:Location(202, 385),
        Aquarium:Location(214, 618),
        Polar:Location(436, 114)
        }
        }[my.scenario];
my.cross_cancel_gotozoo={inossem:Location(1135, 146),
        gtx1060:Location(1848, 118)}[scenario];    
my.Zoops={Main:["1674047529440.png","1716006089332.png"],Fir:["1674049224985.png","1716006099653.png"],Terrarium:["1674049263550.png","1716006109490.png"],Polar:[Pattern("1733028050397.png").similar(0.46)]
        ,Oceanside:["1701004419534.png","1716006040121.png"],Kujali:["1674049288054.png","1716006066106.png"],Aquarium:["1693863721491.png","1716006077447.png"]}
def my_goto(zoo):
    if(my.Blocked[zoo]):
        if lastCheck[zoo]+ datetime.timedelta(minutes=720)>now:
            lastVisit[zoo]=now;
            Log("Access Denied: "+zoo);
            return;
        lastCheck[zoo]=now;
    else:
        my.Blocked[zoo]=False; #for new zoo set default false
    my_close(); # my friend interrupt
    print "my_goto leave ",oldzoo," count=",my_casher(getLogin(),zoo).me;    
    for i in (1,2):
        try:
            #highlightAllOff()
            rg=Region(my.ClientRegion.x+my.ClientRegion.w*5/6,my.ClientRegion.y+my.ClientRegion.h/4,
                    my.ClientRegion.w/4,my.ClientRegion.h*3/4)
            #rg.highlight()
            lastLoc=rg.findAny(Pattern("menu_goto_charlotte.png").similar(0.51),"1652270187685.png")[0] #,"gotomap")); #exclude "1716006308944.png"
            
#            print lastLoc; #M[1122,597 31x36]@S(0) S:0.95 C:1137,615 [24 msec]
            click(lastLoc);
            sleep(2);
            try:
                loc=find(Pattern("menu_drop_down.png").similar(0.65));
                my.cross_cancel_gotozoo=loc;##?
                click(loc);
                sleep(1)
            except:
                pass;
            try:
                click(findAny(Pattern("globalgoto.png").similar(0.56),Pattern("1665485459487.png").similar(0.54))[0]);sleep(1)
            except:
                pass;
            break;
        except:
           pass;
 #       lastLoc=Region(my.ClientRegion.x+my.ClientRegion.w*5/6,0,my.ClientRegion.w*1/6,my.ClientRegion.h*1/6).
        try:
            lastLoc=findAny("1674405637514.png","1676898835462.png")[0]
        except:
            Log('interuped goto menu');
            if (my_close()==0):
                continue;
            return 888;#interuped 
        click(lastLoc);sleep(2.5);
        if i==2:
            Log('Failed goto menu');
            return 999;
    lastLoc=my.Zoogs[zoo];
    try:
        lastLoc=findAny(my.Zoops[zoo])[0];
        my.Zoogs[zoo]=lastLoc;
    except:
        pass;
    checkgate=Region(lastLoc.x-50,lastLoc.y-50,100,100);
    try:
        checkgate.find(Pattern("lock.png").similar(0.62));
        Log( "Blocked:"+zoo);
        my.Blocked[zoo]=True;
        return 999;
    except:
        if my.Blocked[zoo]:
            Log( "Reopen:"+zoo);
            my.Blocked[zoo]=False;
    click(lastLoc);sleep(0.5+my.TimeLoadZoo*0.01);
    lastLoc={inossem:Location(1032, 458),
        gtx1060:Location(1601, 615)
            }[scenario];
    try:
        lastLoc=findAny("1677360226707.png",
        	"SwitchZoo.png",
                "1683604241204.png",
                )[0];
    except:
        pass;
    click(lastLoc);sleep(1);
    lastLoc=my.cross_cancel_gotozoo;
    try:
        lastLoc=findAny(Pattern("cross_cancel_gotozoo.png").similar(0.69),"1677360466689.png","1684380410769.png")[0];        
        my.cross_cancel_gotozoo=lastLoc;
    except:
        pass;
    click(lastLoc);sleep(1);
#    Do.popAsk(zoo,'Zoo ->',38+my.TimeLoadZoo*3)    
    Do.popAsk(zoo,'Zoo ->',my.TimeLoadZoo/7)    
    for i in range(10):
        if zoo==which_zoo1():
            break;
        print my.TimeLoadZoo
        my_GrownUp()
        my_close();
        result=Do.popAsk(zoo,'Zoo -->',my.TimeLoadZoo/6)   
        update_ClientRegion()
        result=Do.popAsk(zoo,'Zoo -=>',my.TimeLoadZoo/6)    
        if None == result:                      
            print "nothing to do"                    
        elif result:                      
            print "user said yes";
            break;
    Do.popAsk(zoo,'Zoo --->',my.TimeLoadZoo/6)    
    entering(zoo);    
    my.zoo=which_zoo();
    print "my_goto arrived ",zoo," count=",my_casher(getLogin(),zoo).me;    
    return 0;
#my_goto(Polar);
#my_goto(Oceanside);
#my_goto(Aquarium);
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
            ,Kujali:["1641135019722.png","1641135048732.png","1641135072434.png","1640640250064.png"]
            ,Aquarium:["1641135019722.png","1641135048732.png","1641135072434.png","1640640250064.png"]
            ,Oceanside:["1641135019722.png","1641135048732.png","1641135072434.png","1640640250064.png"]
        },
        inossem:{
            Main:["1640721586941.png","1640719028561.png","1640720333764.png","1644708172971.png","1645764608542.png"
                     ,"1640721817026.png","1640721745982.png","1640741694803.png","1640744943976.png","1641391579681.png","1641394421693.png","1640536842754.png"]
            ,
            Fir:["1641135019722.png","1641135048732.png","1641135072434.png","1640640250064.png"]
            ,
            Terrarium:["1641135019722.png","1641135048732.png","1641135072434.png","1640640250064.png"]
            ,Kujali:["1641135019722.png","1641135048732.png","1641135072434.png","1640640250064.png"]
            ,Aquarium:["1641135019722.png","1641135048732.png","1641135072434.png","1640640250064.png"]
            ,Oceanside:["1641135019722.png","1641135048732.png","1641135072434.png","1640640250064.png"]
        
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
            },
        Aquarium:{
            "x":[0       ,27     ,36         ,638,0,0,0,0,0],
            "y":[0       , -20     ,-100     ,418,0,0,0,0,0] 
            },
        Oceanside:{
            "x":[0       ,27     ,36         ,638,0,0,0,0,0],
            "y":[0       , -20     ,-100     ,418,0,0,0,0,0] 
            },
         Kujali:{
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
        Aquarium:{
            "x":[0       ,27     ,36         ,638,0,0,0,0,0],
            "y":[0       , -20     ,-100     ,418,0,0,0,0,0] 
            },
        Oceanside:{
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
                   matches=my.ClientRegion.findAllList(scenario+"/"+zoo+"/"+x.pic);
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
                    loc=my.ClientRegion.find(scenzoo+"/"+ols[0].pic);
                    Log("Found @ {L}".format(L=loc));
                    return;
                except:
                    Log("Not found, try second ...");                
                    for i in range(1,10):                
                        try:
                            loc=my.ClientRegion.find(scenario+"/"+zoo+"/"+ols[i].pic);                
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
    ret=999;
    try:  
        for i in range(3):
            loc=growupRegions.find({gtx1060:"growup.png",
                        inossem:Pattern("1648566197856.png").similar(0.64)}[scenario]);
            #print loc
            ret=0;
            click(loc)
            Do.popAsk(inspect.stack()[0][3],'',5);            
    except:
        pass;
    return ret;
#my_GrownUp();

def my_Fir_gtx1060():   
    r=my_click("1640640040396.png")    ;
    if(r==0):
        r=my_click("1640640105756.png")    ;    
        Do.popAsk(inspect.stack()[0][3],'',3);
    return r;
def my_Fir_inossem():   
    return 999;
my_Fir={gtx1060:my_Fir_gtx1060,inossem:my_Fir_inossem}[scenario];
def my_Terrarium_inossem():   
    try:
        r=my_click("1648057110727.png")    ;
        if(r==0):
            r=my_click("1648056732577.png")    ;    
            Do.popAsk(inspect.stack()[0][3],'',5);
            wheel(LocCenter,Button.WHEEL_DOWN,10);
        return r;
    except:
        return 999;
#my_Terrarium_inossem();# tested 3/23/2022

def my_Aquarium_inossem():   
    try:
        r=my_click("1648057110727.png")    ;
        if(r==0):
            Do.popAsk(inspect.stack()[0][3],'',5);
            wheel(LocCenter,Button.WHEEL_DOWN,10);
        return r;
    except:
        return 999;
#my_Aquarium_inossem();

def my_Terrarium_gtx1060():   
    r=my_click("1640640040396.png")    ;
    if(r==0):    
        r=my_click("1640640267632.png")    ;    
        Do.popAsk(inspect.stack()[0][3],'',5);
        wheel(LocCenter,Button.WHEEL_DOWN,10);
    return r;
my_Terrarium={gtx1060:my_Terrarium_gtx1060,inossem:my_Terrarium_inossem}[scenario];

my.my_cash_pic={gtx1060:"1640407206306.png",
                inossem:"1645890337103.png"
                }[scenario];

emptys={"Kujali":{},"Terrarium":{},"Main":{},"Fir":{},"Aquarium":{},"Oceanside":{}};
#from copy import deepcopy
#print emptys.copy(),deepcopy(emptys)

my_cashes={"Trump2024":emptys.copy(),
        "Mom":emptys.copy(),
        "Charlotte":emptys.copy(),
        "unknown":emptys.copy()
        }
class Counter:
    me=0; 
    nextTime=1111;
    def __repr__(self):
        return str(self.me); 
    def count(self):
        self.me+=1;
        return self.me;


#from copy import deepcopy
#print emptys.copy(),deepcopy(emptys)
#my.Polar={'empty':my.emptys[Polar],'nextTime':1111};
def get_default(dic,key,v0):
     n1=dic.get(key);
     if(n1):
         pass;
     else:
         dic[key]=n1=v0;
     return n1;

my_cashes={}

def my_casher(login,zoo):
     if login=='unknown':
         login='Charlotte';
     if zoo=='unknown':
         zoo='Main';
     c1=my_cashes.get(login);
     if(c1):
         pass;
     else:                  
         my_cashes[login]=c1={}
     c=c1.get(zoo)
     if(c):
         pass;
     else:
         c1[zoo]=c={}; 
     if c=={}:
         c=Counter();
         c.nextTime=get_default(nextTime,zoo,1111);
         c1[zoo]=c;
     return c;
#print my_casher("Mom","Polar")
#print my_casher("Mom","Fir")
#print my_casher("Mom","Fir").count()
#print my_casher("Trump2024","Main").count()

my.cnt0=0;
my.cntzoo="";
def my_many_cash():   #cash is full
    rg=my.ClientRegion.grow(-77); #-52 for top#-77 for lefr
    locs=list(rg.findAll(my.my_cash_pic));
    if len(locs)==0:
        pics=["cash_over.png",
				Pattern("cash.png").similar(0.50),Pattern("1715214659740.png").similar(0.69),
				"1645890337103.png", "1674530367809.png"]
        ll=rg.findAny(pics)
        if len(ll)>0:
            c=0;
            #p=my.my_cash_pic;
            for pic in pics:
                lt=list(rg.findAll(pic));
                l=len(lt);            
                if l>c:
                   c=l;
                   p=pic;
                   locs=lt;
            if c>0:
                my.my_cash_pic=p;
#    print locs
    if len(locs)>0:
        zoo=which_zoo();
        if zoo=='unknown':            
            for loc in locs:
                lastLoc=loc.getTarget();
                click(lastLoc);sleep(0.2);
            return 0;
        print getLogin()
        my_cash=my_casher(getLogin(),zoo);    
            if my.cntzoo!=zoo:
                my.cntzoo=zoo;
                my.cnt0=my_cash.me;
            #print zoo,'as of',my.cnt0
            for loc in locs:
                lastLoc=loc.getTarget();
                click(lastLoc);
                cnt=my_cash.count()
                if cnt>my.cnt0+2:
                    nextTime[zoo]=nextTime[zoo]*5/6;
                print zoo,'faster',cnt,nextTime[zoo]
                    my.cnt0=cnt*6;
                sleep(0.2);
        else:
            for loc in locs:
                lastLoc=loc.getTarget();
                click(lastLoc);
                sleep(0.2);
        return 0;
    return 999;
#print my_many_cash(),my.cnt0,my.cntzoo

def my_cash():   

    r=my_click(managed(my_cash_pic,"my_cash"))    ;
    if r==0:
        my_casher(getLogin(),zoo).count();    
    #    Hypnagogia(1.6);
    return r;
def my_cash_bronze():   
    r=my_click({gtx1060:"1640540150379.png",
                inossem:"1645904477007.png"
                }[scenario])    ;
    if r==0:
        my_casher(getLogin(),zoo).count();    
#    Hypnagogia(1.6);
    return r;
my.my_many_bronze_location=Location(0,0) #Location(CenterX,CenterY)
my.waste_time_my_many_bronze=999
def my_many_bronze():   
    now=datetime.datetime.now()
#    cc=Location(CenterX,CenterY)
    if math.sqrt((CenterX-my.my_many_bronze_location.x)**2
            +(CenterY-my.my_many_bronze_location.y)**2)<200 and  (
        my.last['waste_time_my_many_bronze']+datetime.timedelta(minutes=4))>now:
        print now,' skip my_many_bronze saving ',my.waste_time_my_many_bronze
        return 999
    rg=my.ClientRegion.grow(-30);
    work={gtx1060:[[rg,"1640540150379.png"]],
                inossem:[[rg,"1645904477007.png"]]
                }[scenario]
    r=my_many_work(work);
    if r==0:
        my_casher(getLogin(),zoo).count();    
    else:
        my.waste_time_my_many_bronze=datetime.datetime.now()-now;
    return r;
    
#print my_many_bronze()

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
       
mmd = Settings.MoveMouseDelay # save default/actual value
print mmd#0.5
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
#my_trash()

def my_many_trash():
    rg=my.ClientRegion.grow(-50);
    work={
            gtx1060:[[rg,Pattern("1662302599313.png").similar(0.64)]#mess up with Bison rear theigh at somewhere, not easy repeat
                ,[rg,Pattern("trash.png").similar(0.61)],[rg,"1680127775418.png"],[rg,Pattern("1680128974957.png").similar(0.66)]]
            ,   
            inossem:[[rg,"1662302599313.png"],[rg,"1662302599313.png"],[rg,"1662341760704.png"]
               ]
            }[scenario];
    r=my_many_work(work);
    sleep(0.1)
    return r;
#print find(work[1][1])

#print my_many_trash();

def distance(loc1,loc2):
    return math.sqrt((loc1.x-loc2.x)**2+(loc1.y-loc2.y)**2)
#print distance(Location(0,0),Location(3,4))

r1=Region(575,138,461,335);
r2=Region(305,193,618,506)
print r1,r2,r1.getRect().createIntersection(r2.getRect())

def isIntersect(r1,excludes):
    for r2 in excludes:
        rec=r1.grow(0).getRect().createIntersection(r2.grow(0).getRect());
        if rec.width>0:   
            if rec.height>0:    
                return True;
    return False;
            
my.work_count=0
def my_many_work(work):    
    locs=([])
    for w in work:
#        print w[0],w[1]
        try:
            f=list(w[0].findAll(w[1]))
#            print (f)
            locs=list(map(lambda x:x.getTarget(),f))+locs
        except:
            #java.lang.NullPointerException: java.lang.NullPointerException: Cannot invoke "org.sikuli.script.Finder.hasNext()" because "finder" is null
            print 'picture not found :',w[1]
    #+list(work[0].findAll("1649030194070.png")); 
#    br=my.ClientRegion.getBottomRight() #the setup botton, -> excludes
    #locs=filter(lambda z:br.x-z.x>90 or br.y-z.y>80 ,locs) #avoid setting button,step 10
    locs=filter(lambda z:not isIntersect(z,excludes),locs) #avoid setting button,step 10
   #print locs
    if len(locs)==0:
        return 999;
    #anti repeat
    if len(locs)==my.work_count:
        print inspect.stack()[1][3], ' repeated';              
        return 666;
    my.work_count=len(locs)
    my.work0=locs[0]
    if len(locs)==1:
        click(locs[0]);
        return 0;
#    locs=sorted(locs,key=lambda m:math.atan2(m.x-LocCenter.x,m.y-LocCenter.y));
    LocCenter=my.ClientRegion.getCenter();        
    locs=sorted(locs,key=lambda m:math.pi*(-2.0)*
            int(math.sqrt((m.x-LocCenter.x)**2+(m.y-LocCenter.y)**2)/3/ROUTHANLY())
            +math.atan2(m.x-LocCenter.x,m.y-LocCenter.y));
    for i in range(len(locs)-2):
       if distance(locs[i],locs[i+1])>distance(locs[i],locs[i+2]):
               locy=locs[i+2]
               locs[i+2]=locs[i+1]
               locs[i+1]=locy
    if len(locs)==1:
        click(locs[0]);
        return 0;
    tt=True;
#    print 'locs ==',locs;
    for loc in locs:
#        print(loc);
        if tt :
            drag(loc);
            sleep(0.3)
            drag(loc.offset(3,3));
            tt=False;
            loc1=loc;
            continue;
        if abs(loc1.x-loc.x) +abs(loc1.y-loc.y)<0.5*ROUTHANLY():
            continue;
        loc1=loc;
        drag(loc);
#    print(loc);
    dropAt(loc);
    return 0;
#print my_many_water()
#print my_many_trash()



#import argparse        


        
def my_coin():   
    global lastLoc;
    try:   
        loc= {gtx1060: Region(383,188,1227,723),
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


def xmy_star():   
    global lastLoc;
    try:   
#        lastLoc=clickRange.find(scenario+'/'+ "star.png").getTarget();
        lastLoc=clickRange.findAny("star.png","1674533350425.png")[0];
        click(lastLoc);
        Hypnagogia(0.6);
        return 0;
    except:
        return 999;
#now=datetime.datetime.now()    
#print now,my_star(),datetime.datetime.now()-now

def my_many_star():   
#    locs=list(findAll("star.png"));
    locs=findAny("star.png",Pattern("1700810504492.png").similar(0.71));
    if len(locs)>0:
        for loc in locs:
            lastLoc=loc.getTarget();
            click(lastLoc);
            sleep(0.2);
        return 0;
    return 999;
#print my_many_star()

#  Region(352,167,1185,721);
my.CenterX=0
my.CenterY=0
print my2.ClientRegion
def xmy_feedx():
    LocCenter=my.ClientRegion.getCenter();    
    feedLoc=LocCenter
    try:
        loc1= my.ClientRegion.findAny("feed.png",Pattern("1674520785728.png").similar(0.42),"1682555835034.png","1682782992934.png")[0];
        click(loc1);sleep(2)
        r=my_feed1(feedLoc);
        return 0;
    except:
        return 999;

#update_ClientRegion()
#print scenario
bucket=["1653360099807.png","1678452905589.png","1674521889111.png","1678453191130.png",Pattern("1717009406445.png").similar(0.71)];

def my_clear_feed():                
    loc2=my.ClientRegion.getCenter().grow(10)
    for i in range(2):
        try:
            loc1=my.ClientRegion.grow(200).findAny(bucket)[0]
        except:
            try:
             Region(my.ClientRegion.x+my.ClientRegion.w*2/5,my.ClientRegion.y,my.ClientRegion.w*3/5
                ,my.ClientRegion.h/3).findAny(Pattern("1652229378603.png").similar(0.52),"1704372181912.png")[0].getTarget()      
             return 999;
            except:
             pass;
            try:
                loc2=my.ClientRegion.findAny("1703741807202.png")[0];#may be corner
                drag(Location(my.ClientRegion.w+my.ClientRegion.x-1,my.ClientRegion.y+loc2.h))
                dropAt(loc2.offset(0,loc2.h));sleep(3)               
                loc3=Location(my.ClientRegion.w+my.ClientRegion.x-1,my.ClientRegion.y+loc2.h+my.ClientRegion.h/2);
                try:
                    loc3=my.ClientRegion.findAny("1708033313399.png","bucket_corner.png")[0];
                except:
                    pass;
                drag(loc3);
                dropAt(loc2.offset(0,loc2.h));sleep(3)               
                drag(Location(my.ClientRegion.x+1,my.ClientRegion.y+my.ClientRegion.h-loc2.h))
                dropAt(loc2.offset(0,loc2.h));sleep(3)               
                drag(Location(my.ClientRegion.w+my.ClientRegion.x-loc2.w
                            ,my.ClientRegion.y+my.ClientRegion.h-loc2.h))
                dropAt(loc2.offset(0,loc2.h));sleep(3)
            except:
                pass;
            return 999;
        wheel(Screen(),Button.WHEEL_DOWN,10);#error] Mouse.wheel(): Mouse not useable (blocked)
        try:
            loc2=findAny("1703741807202.png")[0]
            break;
        except:
            drag(loc1);sleep(1);
            dropAt(loc1.offset(my.ClientRegion.w/2,my.ClientRegion.h/2));sleep(1);
            pass;
    
    drag(loc1);sleep(1);
    drag(loc2.offset(0,loc2.h));sleep(1);
    dropAt(loc2.offset(0,-loc2.h));sleep(3)
    return 0;
#print my_clear_feed()
    
def OnChange_zoo():
    my.locend=my.ClientRegion.getCenter().offset(my.ClientRegion.w/40,
        [0,-my.ClientRegion.h/10][{Terrarium:1,Aquarium:1,Oceanside:1,Main:0,Fir:0,Kujali:0}
            [my.zoo]])
#    mouseMove(my.locend)
#    my.zoo=which_zoo1()
#    print my.zoo

#print my_feed()     
my.OnChange['zoo']=OnChange_zoo;  

def my_feed():
    try:
        loc1= my.ClientRegion.findAny("feed.png",Pattern("1674520785728.png").similar(0.42),"1682555835034.png","1682782992934.png")[0];
        click(loc1);sleep(4)
    except:
        return 999;
    loc={
            gtx1060:Location(1548, 453),
            inossem:Location(964, 374)
            }[my.scenario]
    loc=loc.offset(my.ClientRegion.x,my.ClientRegion.y);
    try:
        rg=Region(my.ClientRegion.x+my.ClientRegion.w/2,my.ClientRegion.y+my.ClientRegion.h/4,
                my.ClientRegion.w/2,my.ClientRegion.h/2);
        bucket3x=[Pattern("1704975055999.png").similar(0.77).targetOffset(-47,4)];
        loc1=rg.findAny(bucket3x)[0]
        loc=loc1.getTarget();
    except:    
            return 888;
    sleep(0.5)
    drag(loc)
    sleep(0.4);#hold and relase and hold >=0.34, depend on loading
    dropAt(loc.offset(4,4));sleep(2)
    drag(loc)
    #lastLoc=feedLoc;
    lastLoc= my.ClientRegion.getCenter().offset(0,my.ClientRegion.h/8)
    drag(lastLoc.offset(0,my.ClientRegion.h/5));sleep(1)
#    my.zoo=which_zoo()
#    print my.zoo
#    print [0,my.ClientRegion.h/5][{Terrarium:1,Main:0,Fir:0,Kujali:0}[my.zoo]] 
    locend=my.ClientRegion.getCenter().offset(0,[0,-my.ClientRegion.h/20][{Terrarium:1,Aquarium:1,Oceanside:1,Main:0,Fir:0,Kujali:0}[my.zoo]])
    drag(locend);sleep(1)
    try:
        bucket=my.locend.grow(locend.w+locend.h).findAny(bucket)[0]    
    except:
        dropAt(my.locend);
        return 0;
    c1=my.ClientRegion;
    dropAt(Location(random.randrange(c1.x,cl.x+cl.w),random.randrange(c1.y,cl.y+cl.h)))
    my_clear_feed();        
    return 0;
#print my_feed1(my.ClientRegion)   
#wheel(my.ClientRegion,Button.WHEEL_DOWN,10);
my.bucket3x=[Pattern("1704975055999.png").similar(0.77).targetOffset(-47,4),Pattern("1721871980232.png").similar(0.62).targetOffset(-102,7)];
#print my_feed() 

    
def my_water():
    global lastLoc;
    try:    
        work={ 
        gtx1060:[Region(439,216,1083,712),"water.png"]
                ,
       inossem:[clickRange.grow(-50),"water.png"]
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
update_ClientRegion();

def my_many_water():
    rg=my.ClientRegion.grow(-100);
    work={
            gtx1060:[[rg,    Pattern("1649030194070.png").similar(0.53)],[rg,Pattern("water.png").similar(0.61)],[rg,Pattern("1674529539504.png").similar(0.64)],[rg,Pattern("1680128167275.png").similar(0.64)]]
            ,   
            inossem:[[rg,"1649023518496.png"],
            [rg,    "1649030194070.png"],                    
                [rg,"1662301113401.png"]
                ,[rg,"1662301394337.png"]
                ,[rg,"1662301682259.png"]
               ]
            }[my.scenario];
    type(Key.ESC);sleep(0.3)
    type(Key.ESC);sleep(0.3)
    return my_many_work(work);
#print scenario,my_many_water(); #tested 4/3

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
            if rg.y+rg.h>my.ClientRegion.y+my.ClientRegion.h:
                rg.h=my.ClientRegion.y+my.ClientRegion.h-rg.y;
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
        poorange={gtx1060: Region(219,96,1482,923),
            inossem:my.ClientRegion
            }[scenario];        
        loc=poorange.find(poobrush).getTarget();
        print "pooof",my.CenterX,my.CenterY;
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
                loc= my.ClientRegion.find(poobrush).getTarget();
                break;
            except:
                Hypnagogia(0.2);
                pass;
        if j>=4 :
            Log("Done poo brush");
            dropAt(lastLoc);
#            Hypnagogia(1);
            return 0;
        cl=my.ClientRegion.grow(-50);
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


def OnChangeQuitGame():
    if my.QuitGame:
        SteamMode=True;
my.OnChange['QuitGame']=OnChangeQuitGame;
print my.me;
my.QuitGame=False;
my.ramp_reached=0;
#print click(Location(my.ClientRegion.x+my.ClientRegion.w,my.ClientRegion.y+my.ClientRegion.h))
def my_close():        
    r1=999;r0=999;
    for i in range(10):
        try:
            #highlightAllOff()
            rg=Region(my.ClientRegion.x+my.ClientRegion.w*4/6,my.ClientRegion.y,
                    my.ClientRegion.w*3/6,my.ClientRegion.h*3/6);
            #rg.highlight();
            click(rg.findAny(Pattern("1640403388181.png").similar(0.56),"1640230482499.png","1640398758304.png","1640537041268.png","1640538477820.png","1640539750376.png",Pattern("1646141916266.png").similar(0.65),"1704604405809.png"
                        ,Pattern("1707835060805.png").similar(0.65))[0]);sleep(1)
            #to exclude ...
            r1=0;
        except:
            break;
        try:
            type(Key.ESC);sleep(1)
            r1=0;r0=0;
            loc=my.ClientRegion.find(Pattern("quitgame.png").similar(0.45));
            r1=999;r0=999;
            type(Key.ESC);sleep(1)
            break;
        except:
            pass;
    if i>0:         
         return r1;
    if random.random()<0.1:
        try:
            auto(Region(856,819,442,237),gtx1060).click("1684613964081.png");sleep(1)
            return 0;
        except:
            pass;
    return r0;
#print my_close();

my.SteamMode=(scenario=='gtx1060');
#if zoo is not found
def my_focus_inossem():#also other recovers        
    if my.QuitGame:
        my.SteamMode=True;
    if my.SteamMode:
        print("don't know how to get focus?");
        return 777;
    global need_my_focus_inossem;
    if need_my_focus_inossem: 
       need_my_focus_inossem=False;
    try:
       for i in range(24):
           loc= auto(Region(398,376,445,313),inossem).findAny("1652488232002.png","reload.png")[0];
           Log('Reloading');
           Do.popAsk('{}'.format(24-i),'Reloading',3*60);
       click(loc);sleep(1)
       Log('Reload');
       Do.popAsk('Reload','',20);
    except:
       pass;
    try: 
       rg=Region(my.ClientRegion.getScreen())
       rg.h=my.ClientRegion.h/10;
       loc=rg.findAny(Pattern("pandaicon.png").similar(0.64))[0];
    except:
        return 999;
    click(loc);sleep(1)
    for i in range(4):
        type_Key_ESC();sleep(1);
        if my_redeem_prize()==0 or my_great()==0:
            if which_zoo()!="unknown":
                return 0;
        try:
            click(Pattern("1716241840720.png").targetOffset(38,0));sleep(1)        
            try:
                click(Pattern("1716241923686.png").targetOffset(4,8));sleep(1)    
                return 0;
            except:             
                type(Key.F5);
        except:
             pass; 
    LogScreen();            
    Do.popAsk('90 may','Reload except splashing',90);
    for i in range(2):
        if findAny("Splashing.png").isEmpty():
            return 0;
            #exit;
            #break;
        Do.popAsk('Splashing?',i,30);
    #LogScreen();            
    #type(Key.F5); #F5 may be blocked?
    Do.popAsk('Reload F5','',38)
    return 0;

#print my_focus_inossem();

def my_focus_gtx1060():    
    return 999;

my_focus={inossem:my_focus_inossem,gtx1060:my_focus_gtx1060}[scenario];

def my_close_feed():
    try:
        click(findAny(Pattern("1662510570791.png").targetOffset(67,2))[0])
        return 0;
    except:
        pass;
    try:
        loc=my.ClientRegion.find(managed("1653359955691.png","my_close_feed"));
        my_feed1(loc.offset(0,my.ClientRegion.h/4));        
        return 0;    
    except:
        pass;            
    return 999;
#my_close_feed();
global button_close_friend;
def update_button_close_friend():
#only call this after menu click
    try:         
        button_close_friend=my.ClientRegion.find(managed("1653162976076.png","button_close_friend"));
        button_close_friend=button_close_friend.getTarget();
        print button_close_friend,my.ClientRegion,float(button_close_friend.x-my.ClientRegion.x)/my.ClientRegion.w,float(button_close_friend.y-my.ClientRegion.y)/my.ClientRegion.h;
        #0.902934537246 0.1482602118
        #how to avoid mess up other close button
    except:
        print "Failed: update_button_close_friend";
#update_button_close_friend()
#<function my_clean100 at 0x3a> 0:00:03.056000 0:00:03.019000
my.waste_time_my_clean100=999
my.my_clean100_location=Location(0,0) #Location(CenterX,CenterY)
def my_clean100():
    now=datetime.datetime.now()
    if my.last['waste_time_my_clean100']>my.last['ramp_reached']:
        print 'my_clean100_location done before next ramp';
        return 999;
#    cc=Location(CenterX,CenterY)
    if math.sqrt((CenterX-my.my_clean100_location.x)**2
            +(CenterY-my.my_clean100_location.y)**2)<200 and  (
        my.last['waste_time_my_clean100']+datetime.timedelta(minutes=4))>now:
        print now,' skip waste_time_my_clean100 saving ',my.waste_time_my_clean100
        return 999
    try:        
        loc=findAny(Pattern("1665378590572.png").similar(0.86)
               # ,"1681427052382.png"
                )[0]        
        #print loc
        Doit=False;
        bds=loc.grow(270).findAny("1682555390092.png","1682555456211.png"
                #,Pattern("1681427097387.png").similar(0.69)
                );#270 for 3 sec?
        #print len(bds) 
        if len(bds)>0: 
            locs=loc.grow(270).findAny("1665378913352.png","1671561604009.png","1682554868556.png"
                    #,Pattern("1681427097387.png").similar(0.69)
                    );#270 for 3 sec?
  #          print len(locs)
            if len(locs)>0:
                Doit=True;
        else:
            Doit=True;
        if Doit:
            click(Location(loc.x+loc.w,loc.y+loc.h/5));sleep(3)
            my_feed();
            my_ball();
            return 0;
    except:
        pass;
    my.my_clean100_location=Location(my.CenterX,my.CenterY);
    my.waste_time_my_clean100=datetime.datetime.now()-now;
    return 999;
#my.ramp_reached=my.ramp_reached+1;print my_clean100()
def my_clean200():
    my_waste_time(clean200);


my.waste_time_clean200=999
my.clean200_location=Location(0,0) #Location(CenterX,CenterY)
my.ramp_reached=my.ramp_reached+1
#my_clean200()

def my_waste_time(my_clean):
    now=datetime.datetime.now()
    wn='waste_time_'+my_clean.__name__;
    if my.last[wn]>my.last['ramp_reached']:
        print my_clean.__name__,'_location done before next ramp';
        return 999;
#    cc=Location(CenterX,CenterY)
    ml=my_clean.__name__+'_location';
    mm=my.__getattr__(ml);
    if math.sqrt((CenterX-mm.x)**2+(CenterY-mm.y)**2)<200 and  (
        my.last[wn]+datetime.timedelta(minutes=4))>now:
        print now,' skip waste_time_'+my_clean.__name__+' saving ',my.__getattr__(wn)
        return 999;
    if my_clean()==0:
        return 0;
    my.__setattr__(ml,Location(my.CenterX,my.CenterY));
    my.__setattr__(wn,datetime.datetime.now()-now);
    return 999;        


def clean200():    
    try:        
        loc=findAny(Pattern("1683238376754.png").similar(0.81) )[0]        
        #print loc
        Doit=False;
        bds=loc.grow(270).findAny("1682555390092.png");
        #print len(bds) 
        if len(bds)>0: 
            locs=loc.grow(270).findAny("1683238451907.png","1683238460457.png","1683238487850.png")
  #          print len(locs)
            if len(locs)>0:
                Doit=True;
        else:
            Doit=True;
        if Doit:
            click(Location(loc.x+loc.w,loc.y+loc.h/5));sleep(3)
            my_feed();
            my_ball();sleep(1)
            my_many_star();
            return 0;
    except:
        pass;
    return 999;
#x=clean200;print x.__name__
#print clean200()

my.QuitGame=False;
my.waste_time_my_close_inossem=999
def my_close_inossem():        
    now=datetime.datetime.now()
    if my.last['waste_time_my_close_inossem']+datetime.timedelta(minutes=3)>now:
        print now,' skip my_my_close_inossem saving ',my.waste_time_my_close_inossem
        return 999
    global lastLoc;
    try:
        loc=my.ClientRegion.find("1653352410294.png")
        type_Key_ESC();
        my.QuitGame=True;
        return 0;
    except:
        pass;
    if not(my.QuitGame):
        type_Key_ESC();             
    elif random.random()<0.05:
        type_Key_ESC();             
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
        my.waste_time_my_animal_level=datetime.datetime.now()-now
        return 999;
    click(loc);
    Hypnagogia(0.5);        
    lastLoc=loc.getTarget();    
    return 0;
#my_close_inossem();print my.waste_time_my_close_inossem,'ESC count as Waste'

#my_close={gtx1060:my_close_gtx1060,inossem:my_close_inossem}[scenario];
#my_close();

def my_ball():    
    try:   
        loc= {gtx1060:Region(383,188,1227,723),
                inossem:clickRange
                }[scenario].find({
                    gtx1060:"1640310968315.png",
                    inossem:"1645925652733.png"
                    }[scenario]);
        if which_zoo()==Aquarium:
            return 777;
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
        sleep(4);
        return 0;
    except:
        return 999;    
#print which_zoo();
#print my_ball();

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

my.waste_time_my_born=999;
print my.last['waste_time_my_born']
def my_born():
    now=datetime.datetime.now()
    if my.last['waste_time_my_born']+datetime.timedelta(minutes=2)>now:
        print 'my_born skip for a while';
        return 999;
    try:
        click(my.ClientRegion.findAny("1728405511392.png","born.png")[0]);
        sleep(1);
        click(my.ClientRegion)
        try:
            my_born_ok()
        except:
            pass;
        for i in range(8):
            type(Key.ESC);sleep(1)
        my_breed_from_center()        
        return 0;
    except:
        my.waste_time_my_born=datetime.datetime.now()-now;
        return 999;
#now=datetime.datetime.now();print now,my_born(),datetime.datetime.now()-now
#print my.waste_time_my_born,my.last['waste_time_my_born']

def my_born_ok():
  try:    
    auto(Region(420,428,337,223),inossem).click(managed("1652304012516.png","Okay"));
    return 0;
  except:
    return 999;

def my_born_success():
  try:        
    auto(Region(636,211,94,54),inossem).find(managed("1671844970038.png","Born"));
    click(LocCenter);sleep(1)
    my_born_ok()
    return 0;
  except:
    return 999;
#print my_born();


my.waste_time_my_animal_level=999
def my_animal_level():
    now=datetime.datetime.now()
    if my.last['waste_time_my_animal_level']+datetime.timedelta(minutes=31)>now:
        print now,' skip my_animal_level saving ',my.waste_time_my_animal_level
        return 999
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
    my.waste_time_my_animal_level=datetime.datetime.now()-now
    return 999;
#my_animal_level();print my.waste_time_my_animal_level

def ispoppydays(now):
    return (now.month==2 and now.day>=14 and now.day<=14+14 #valentine
        or now.month==4 and now.day>=6 and now.day<=6+14  #easter early?
        or now.month==5 and now.day>=4 and now.day<=4+14 ); #monthers day
            
stayTime={Main:20,Fir:12,Terrarium:8,Aquarium:8,Oceanside:3,Kujali:10};#shall not over minimum wave period
print stayTime
stayTime[Main]=22
stayTime[Oceanside]=1

print t0
class Visit:
    first=t0;
    last=t0;
    stayTime=8;
    nextTime=datetime.datetime.now();
    Orig={"x":[0       ,-7     ,2      ,3        ,590   ,523    ,1988   ,800    ,-500  ,20000                       ,18000     ,102,0,0,0],
          "y":[0       , 0     ,2      ,3       ,17   ,215    , 827   ,-110   ,30    ,-1500                       ,-2000     ,-200,0,0,0]       
        };

my.Visits=AutoGrow(Visit);
#print my.Visits

def my_zoo():
    LocCenter=my.ClientRegion.getCenter();
    global lastCheck,zoo,oldzoo;
    now=datetime.datetime.now();
    Log("zoo:{Z}:{T}".format(Z=zoo,T=now));
    wishzoo=my.OldestZoo;
    zoo=which_zoo1()
    print 'wish ',wishzoo,' from ',zoo
 
    my.Visits[zoo].last=now;
    print my.Visits['Kujali'].last,'!';
    t1=my.Visits[zoo].first+ datetime.timedelta(minutes=my.Visits[zoo].stayTime);
    print t1
    if wishzoo==zoo:
        if t1>now:
            Log("Will change after {T}".format(T=t1));
            return 999;
        else :
            UpdateOldestZoo();
            wishzoo=my.OldestZoo;
    if wishzoo==zoo:
        return 999;
    Log("wishzoo="+wishzoo);
    if my.Visits[zoo].first+ datetime.timedelta(minutes=my.Visits[zoo].stayTime)<now :
        print zoo,"->",wishzoo;
        if(my_goto(wishzoo)==0):            
                my.Visits[wishzoo].last=now;
                zoo=wishzoo;                
                landmarks=landmarkss[zoo];
                Orig_Xs=my.Visits[zoo].Orig["x"];
                Orig_Ys=my.Visits[zoo].Orig["y"];
                return 0;    
    else: 
        print "wishzoo ",wishzoo," unsatified ",my.Visits[wishzoo].last," for staying ",zoo,my.Visits[zoo].first,"+",my.Visits[zoo].stayTime," minites";
    return 999;
#print my_zoo();
#UpdateOldestZoo();
#print my.OldestZoo;

    
my.zoo='Main'
def my_reset4():
        zoo=my.zoo
        now = datetime.datetime.now();
        oldz=zoo;
        zoo=which_zoo();

        print(zoo); 
        if zoo=="unknown" :
            zoo=oldz;
            if zoo=="unknown" :
                zoo=Main;
        else:
            my.zoo=zoo;
        landmarkss[Kujali]=landmarkss[Main]; #something wrong
        Orig[Kujali]=Orig[Main];
        landmarks=landmarkss[zoo];
        Orig_Xs=Orig[zoo]['x'];
        Orig_Ys=Orig[zoo]['y'];
        
        if(lastLoc!=Location(0,0)): # and now.hour>=8 and now.hour<=22):
            locMouse=Mouse.at();
            dx=lastLoc.x-locMouse.x;
            dy=lastLoc.y-locMouse.y;            
            if( dx*dx+dy*dy>200):
                print('displaced',lastLoc,locMouse,my.lastStatus);                                
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
                                  return 0;
                                  #break;
                              locMouse=locMouse1;
                      elif(x>' ' and x[0]!='n') :
                          return 0;
                          #break;
                    else:
                      print "user said no"
            else:
                displaceCount=0;
#        else :
#           if((now-startTime).total_seconds()>50*60):
#               i=NLOOP;
#               return 0;#to close game and back?
               #break;
        #i+=1; count play by loop
#        if(need_my_splash):
#            need_my_splash=False;
import inspect
print inspect.stack()[0][3]
def my_splash():            
    rg=Region(my.ClientRegion.x+my.ClientRegion.w*3/7,my.ClientRegion.y+my.ClientRegion.h*4/10,my.ClientRegion.w/7,my.ClientRegion.h*3/10)
#    rg.highlight()
    for i in range(50):
        try: 
            click(rg.findAny(Pattern("1652449514171.png").similar(0.56),"Splash.png")[0]  );sleep(2) ;#fail sleep 1
            my.lastStatus='Splash';                
            return 0;
        except:        
            if Do.popAsk(inspect.stack()[0][3],'Yes to stop',10):
                return 777;
    return 999;
#my_splash()

my.lastStatus=''

def my_reset5():   
    os.system('taskkill /IM zoo2.exe');
######################
#stop
#to develop for "no space"


def notyet():
        
    #"1641014760839.png"
    
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

#poppymenu();



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



def my_friend1_again():
    r=my_friend1();
    my.friend_active=False;
    return r;

my.lastRun='';
my.runs={}
def my_run(mine,ts,n):
    running=True;
    now=datetime.datetime.now();
    togo=now+ts; 
    for ti in range(n):
        if datetime.datetime.now()>togo:
            break;
        locMouse0=Mouse.at();
        sleep(0.5)         
        locMouse=Mouse.at()
        if (locMouse.x<0 or locMouse.x>=Screen().w or  
                locMouse.y<0 or locMouse.y>=Screen().h):
            result=Do.popAsk('break from running now? ESC to dream','Pause for 30 seconds',30);
            if None == result:
              REM(10*60);
              print "nothing to do after a while"
            elif result:
                break;
            continue;
        x=locMouse.x-locMouse0.x
        y=locMouse.y-locMouse0.y
        if not x*x+y*y<100:
            result=Do.popAsk('break from running now?','Pause for 3 minutes',3*60);
            if None == result:
              print "nothing to do after a while"
            elif result:
                break;
            continue;
        did=False;
        now=datetime.datetime.now();
        now0=now;
        Perturbation()        
        for mi in mine():
            if mi==my.lastRun:
                continue;
            now1=datetime.datetime.now();
            print mi,(now1-now).total_seconds(),(now1-now0).total_seconds();
            now0=now1;
            if(mi()==0):                            
                print mi
                my.runs[mi]=now
                did=True;
                my.lastRun=mi;
                my.lastStatus="{F}".format(F=mi)
                break;
        if did:
            continue;
        print datetime.datetime.now()-now;
        my.lastRun="otherdeeds";
print my.runs;

def typemaybe_Key_ESC():
    if scenario!=gtx1060:    
        type_Key_ESC();
def escape_breed():
    for i in range(10):
        if my_close()!=0:
           if my_born()!=0:
               break;

def my_chest_from_dialog():
    try:
        click(findAny(Pattern("1716289173673.png").targetOffset(36,42))[0]);sleep(1)#exclude 
        click(findAny("1716289235583.png")[0]);sleep(1)#exclude         
    except:
        pass
    return open_cards();
#    return 999;
def my_open_cards():
    rg=Region(my.ClientRegion.x+my.ClientRegion.w/4,my.ClientRegion.y+my.ClientRegion.h/4,
            my.ClientRegion.w/2,my.ClientRegion.h/2)
    try:
        rg.findAny(Pattern("1716583253250.png").similar(0.58),Pattern("1716583343799.png").similar(0.64))[0]
    except:
        return 999;
    open_cards();
#print my_open_cards();

def open_cards():
    click(my.ClientRegion);sleep(3)
    try:
        for i in range(4):
            click(findAny("1716289358771.png")[0]);sleep(1)#exclude         
        click(findAny("1716289428397.png")[0]);sleep(1)
        return 0;
    except:
        pass
    return 999;
#print my_chest_from_dialog();

def my_breed_from_dialog():
    try:
        click(findAny(Pattern("1661736237298.png").similar(0.62),Pattern("1704605890057.png").similar(0.94))[0]);sleep(1)
        my.lastStatus='breed';
        sleep(1)
        typemaybe_Key_ESC();sleep(1)
        typemaybe_Key_ESC();sleep(1)
        typemaybe_Key_ESC();sleep(1)
        escape_breed();
        return 0;
    except:
        pass
    return 999;
#print my_breed_from_dialog()

def my_breed_from_center():
    try:
        click("breed_nipple.png");
        my.lastStatus='breed';
        sleep(1)
        my_breeds()
        return 0;
    except:    
        return 999;
#print my_breed_from_center()

breed_animals=[Pattern("breed_mouse.png").similar(0.46),"breed_panther.png",
        "breed_badger.png","breed_dikdik.png","breed_lybx.png"
        ,"breed_mara.png","breed_pheasant.png"];

def my_breeds():
  for ispg in range(4):
    try:
     click(findAny("my_breed_add.png","1682809597946.png")[0]);sleep(2)
     break;
    except:
        try:
            click("1704873420009.png");sleep(1) 
        except:
            return 999;
        if ispg>2:
            return 888;
  return select_animal();
#my_breeds();

def select_animal():
    cel=Region(451,344,202,203);
    gpx=cel.w    
    gpy=cel.h;    
    for ix in range(1):
        for iy in range(1):            
            Location(cel.x+cel.w*ix+cel.w/2, cel.y+cel.h*iy+cel.h/2).click();sleep(2);
            print choose_two_animals();
            esc_breed()
            
#select_animal();
def esc_breed():
       Region(1468,108,223,180).find("1734380685277.png").click();sleep(1)

def oldmy_breeds():
    for ipg in range(4):
        coks=list(Region(229,253,732,473).findAll(Pattern("1687720628269.png").similar(0.78)))    #+list(findAll(Pattern("1697073349773.png").similar(0.72)))    +list(findAll(Pattern("1697073422435.png").similar(0.71)));
        if len(coks)>0:
            break;
    for k in range(3):
        zp=map(lambda co: [co.x/gpx,co.x%gpx],coks); 
        zp.sort()
        sl=[];
        for i in range(1,len(zp)):
            if zp[i][1]!=zp[i-1][1]:
                 sl+=[(zp[i][0]-zp[i-1][0])/1.0/(zp[i][1]-zp[i-1][1])]
        if(sl==[]):
            break;
        ssl=sum(sl); 
        if ssl==0:
            print 'ssl1=0';
            continue;
        gpx+=int(len(sl)/ssl);
    zpx=zp[0][1]+coks[0].w/2;
    for k in range(3):
        print gpy
        zp=map(lambda co: [co.y/gpy,co.y%gpy],coks); 
        zp.sort()
        sl=[];
        for i in range(1,len(zp)):
            if zp[i][1]!=zp[i-1][1]:
                 sl+=[(zp[i][0]-zp[i-1][0])/1.0/(zp[i][1]-zp[i-1][1])]
        if(sl==[]):
            break;
        ssl=sum(sl); 
        gpy+=int(len(sl)/ssl);
    try:
    zpy=zp[0][1]+coks[0].h/2;
    except: 
        #index out of range: 0
        err='zpy=zp[0][1]+coks[0].h/2;'
        print err,zp, cols
        LogScreen();
        result=Do.popAsk(err,'',38)        
        if None == result:          
            print "nothing to do"
        elif result:          
            print "user said ",result;          
            exit
        return;
    known_parents=[];
#    done=False;
    for k in range(4):
        i=random.randint(2,7);
#    for i in range(2,7):
#        for j in range(2,5):
        j=random.randint(2,5);
        rg=Region(zpx+i*gpx,zpy+j*gpy,gpx,gpy).grow(-20);#.highlight();sleep(1)
        sf='parent{}{}.png'.format(i,j)
        img=Screen().capture(rg);
        img.save(getBundlePath(),sf);
        if len(known_parents)>0:
            if len(rg.findAny(known_parents)):
                rg.findBest(known_parents);
        click(rg);sleep(1)
        if choose_two_animals()==0:            
#                done=True;            
                break;
#        if done:
#            break;    
#select_animal();

def isdoublebread(animal):
    return False;

def choose_two_animals(animal):
    cr=my.ClientRegion;
    ct=my.ClientRegion.getCenter();
    lf=Region(cr.x,cr.y,ct.x-cr.x,cr.h);
    m=bot71(lf);
    print m
    if m<999: 
        sleep(1)
    rf=Region(ct.x,cr.y,cr.x+cr.w-ct.x,cr.h);
    f=bot71(rf);
    if f<999: 
        sleep(1)
    print m, '+',f
    #to choose the change color priority?
    try:
        loc=findAny(Pattern("Chance.png").similar(0.56).targetOffset(47,-1),Pattern("1734382289779.png").similar(0.62))[0];    
    except:
        esc_breed()
        return 999;
    if not(isdoublebread(animal)):
    try:
            rg=loc.grow(loc.h*2)
            rg.findAny(Pattern("1734382544576.png").similar(0.89),Pattern("1682632846440.png").similar(0.82),"20p.png")[0];        #chance more than 30, or =3% 2%? 8%?
            esc_breed()
            return 333;
    except:
        pass;
        try:
            m2=rg.findAny(Pattern("1682632846440.png").similar(0.89),Pattern("1734488253750.png").similar(0.86))[0];        #chance more than 20
            esc_breed()
            return 222;
        except:
            pass;
    if my.StartNow:
        click(findAny(Pattern("StartNow.png").similar(0.63),"1734382393426.png")[0]);sleep(2)
    typemaybe_Key_ESC();
    return 0;

choose_two_animals("1734383062565.png");
#my_breeds()
my.StartNow=True;

def observe_info():
    click("1730805358956.png");sleep(1)
    bf=find("1730805414795.png");click(bf);sleep(1)
    lf=Region(bf.x+bf.w*2,bf.y-bf.h*4/3,bf.w*8,bf.h*5);
    lf.highlight();sleep(0.3)
    #onreturn=
    lf.highlightOff()
    for nm in breed_numbers:
        try:
            te=lf.find(nm[0])
            if te.getScore()>0.83:#0.93 miss
                rg=te.grow(te.w/4)
                try:
                    rg.find(nm[2]) #exclude
                    continue;
                except:
                    pass;

                maxLevel=nm[1];
#                print maxLevel
                rg=Region(te.x-bf.w*2+te.w,te.y,bf.w*2,bf.h*2);
                img=te.getScreen().capture(rg);
                name='tbdan.png'
                img.save(getBundlePath(),name);    
                return nm[1];
        except:
            pass;
            
#print observe_info();


#5 + 5 mess with 5 + 3

#my.my_breed_location=Location(0,0)
my.waste_time_my_breed=999
def my_breed():
    now=datetime.datetime.now()
    t=my.last['waste_time_my_breed'];
    if (    #math.sqrt((CenterX-my.my_breed_location.x)**2
                #+(CenterY-my.my_breed_location.y)**2)<200 and  
                t+datetime.timedelta(minutes=70)>now and                          
                t+datetime.timedelta(minutes=1)<now):
    #        print now,' skip my_breed saving ',my.waste_time_my_breed
            return 999;
    try:    
        click(my.ClientRegion.findAny("1677559485225.png","1727127743964.png")[0]);sleep(1)
        my_close();
    except:    
        pass;        
    try:    
        click(findAny("1677517451920.png","breed_nipple.png","1682809413565.png")[0]);sleep(1)
    except:
#        my.my_breed_location=Location(CenterX,CenterY);    
        if t+datetime.timedelta(minutes=1)<now:        
                my.waste_time_my_breed=datetime.datetime.now()-now;    
        return 999;
    my_breeds();
    type(Key.ESC);sleep(1)    
    return 0;
#now=datetime.datetime.now();print my_breed(),datetime.datetime.now()-now,my.waste_time_my_breed #11.7 / 3
my.waste_time_my_breed=999;

#my_breed();

my.friend_active=False;
my.friend_menu_lastVisit=t0;

def my_friend_wander():
    if my.friend_active :
        return 99;
    try:
        loc=find("1661806315186.png")
        my.friend_active=True;
    except:
        return 999;
    print 11
    t= my.friend_menu_lastVisit + datetime.timedelta(minutes=7);
    print t
    now=datetime.datetime.now()
    print 1
    if(t<now):
        my.friend_menu_lastVisit=now;
        my_friend_menu();
        lastStatus='friend menu';                       
        my.friend_active =False;
    return 0;

#print my_friend_wander()


my.missing=0;
my.rampcnt=0;
my.friend_active =False;
print my.friend_active 

def my_many_water_again():
    return my_many_water();
my.my_lets_go=999;
def my_lets_go():
    if my.last['my_lets_go']>my.last['ramp_reached']:
        print 'my_lets_go done before next ramp';
        return 999;
    now=datetime.datetime.now();
    if my.last['my_lets_go']+datetime.timedelta(minutes=9)>now:
        print '9 minutes try this my_lets_go again';
        return 999;
    
    try:
        click("1664141615204.png")
        sleep(1)
        return 0;
    except:
        my.my_lets_go=datetime.datetime.now()-now;
        return 999;
#print my_lets_go()


def xmy_poppy():
    click("1666832106820.png")
    sleep(1)

my.direct=0
if False:
    my.friend_active =True;
    print my.ClientRegion
    #print my.last['ClientRegion']
#    print my_run(mine_unknown)
#    print my_cashes['Trump2024']['Terrarium'].me

    my.friend_active =True;
    print my_friend1()
       
    print mine_unknown
    print my.lastRun #otherdeeds


    print my_close_feed()
    print my_friend_wander(), my.friend_menu_lastVisit

    my.friend_active =True;
    print my_friend_in()
    my.friend_active =True;
    print my_friend_menu()#fail missing click help, open box too early to stuck
    print my.friend_active()
    print my_many_poppy()
    my_friend_gonext();

if False:#########
    def loc_panda_icon(): 
        try:
           loc= find(managed("1652374584338.png","pandaicon"));
           print loc
           return loc;
        except:
           pass;
    pandaicon=loc_panda_icon()
    if pandaicon:
        print pandaicon;
    else:
        result=Do.popAsk('No panda icon?','please load game',66);
    ###################
    
def feed_cancel():
    loc=find("1662137059133.png")
    print loc
    click(Location(loc.x+loc.w*0.8,loc.y+loc.h*0.8))
#feed_cancel()

breed_numbers=[["1684187930409.png",20]
        ,["1684187950865.png",19]#mess 13
        ,["1677522257885.png",18],["1677522244418.png",17],["1677522276331.png",16]
        ,["1677522123881.png",14]
        ,["1677522105039.png",13],["1662341220893.png",12],[Pattern("1734383153765.png").similar(0.69),12],["1677518282861.png",11],[Pattern("1734384803402.png").similar(0.86),11]#mess 6
        ,["1662341241034.png",10],["1734384832309.png",10],["1704871692613.png",9],[Pattern("1684187259039.png").similar(0.88),9]#mess 8
        ,["1662341241034.png",10]
        ,[Pattern("1704871692613.png").similar(0.91),9,Pattern("3.png").similar(0.83)]#mees 3
        ,["1684187259039.png",9]
        ,[Pattern("1677518318148.png").similar(0.89),8],[Pattern("1734488409836.png").similar(0.95),8] #mess with 6
        ,["1677522158716.png",7]
        ,[Pattern("1677522342750.png").similar(0.81),6,Pattern("1662340932641.png").similar(0.86)]#mess 5 to exclud
        ,["5.png",5]
        ,["1662340932641.png",5],["1734383585597.png",5],["1662340896315.png",4],["1662341143419.png",3],["1662341191084.png",2],["1662341115047.png",1]];
        ,["1662340896315.png",4]
        ,[Pattern("1662341143419.png").similar(0.85),3]
        ,["1662341191084.png",2],["1662341115047.png",1]];
choose_two_animals();

def bot71(lf):
    for nm in breed_numbers:
        try:
            te=lf.find(nm[0])
            if te.getScore()>0.83:#0.93 miss
                rg=Region(te.x-lf.w/3,te.y+te.h/2,lf.w/3+te.w,te.h*3)
                try:
                    rg.findAny("1730803569350.png","1730803584181.png")[0];
                    continue;
                except:
                    pass;
                rg=te.grow(te.w/4)
                try:
                    rg.find(nm[2]) #exclude
                    continue;
                except:
                    pass;
                click(te)
                return nm[1];
        except:
            pass;
    return 999;    



if False: #buy poppy
  for i in range(20):
    click("1663605469873.png");    sleep(1)
    
    click("1663605507758.png");    sleep(1)
    click("1663605541273.png");    sleep(1)
    click("1663605565683.png");    sleep(2)
    drag(find("1663605684923.png"));    sleep(1)    
    #loc=find("1663624499701.png")#Trump2024
    #dropAt(Location(loc.x+loc.w*0.05,loc.y+loc.h*0.9));sleep(1)
    loc=find("1663615211638.png")#Mom
    dropAt(Location(loc.x-loc.w*0.25,loc.y+loc.h*1.2));sleep(1)

    click("1663605898078.png");    sleep(5)
    click("1663605944959.png");    sleep(2)
#    click("1663605991609.png");sleep(1)#trump    
    click("1663615476874.png");    sleep(1)#mom
    click("1663606024074.png");    sleep(1)    
    click("1663606050969.png");    sleep(1)
    click("1663606087763.png");    sleep(1)

if False: #buy halloween poppy
  for i in range(11):
    click("1667214158646.png");    sleep(1)
    
    click("1663605507758.png");    sleep(1)
    drag(find(Pattern("1667214236645.png").targetOffset(33,-16)));    sleep(1)    
    loc=find(Pattern("1667352626974.png").targetOffset(-107,2))
    dropAt(loc);sleep(1)

    click("1663605898078.png");    sleep(5)
    click("1666832106820.png");    sleep(2)
    click("1667329590152.png");    sleep(1)
    click("1663606024074.png");    sleep(1)    
    click("1663606050969.png");    sleep(1)
    click("1663606087763.png");    sleep(1)

if False: #buy chritmas snowflake
  for i in range(50):
    click("1670669613118.png");    sleep(1)
    
    click("1670669685882.png");    sleep(1)#to shop
    click("1670669771737.png");    sleep(1)#arrow down
    
    loc=find(Pattern("1671143931500.png").targetOffset(87,36))
    drag(find("1670669808264.png"));    sleep(1)    
    dropAt(loc);sleep(1)

    click("1670669969525.png");    sleep(5) #check yes
    click("1670670051422.png");    sleep(2)    #poppy - snowflake    
    click("1670671117856.png");    sleep(1) #object in field
    click("1670670246915.png");    sleep(1)    #hand out
    click("1670670333091.png");    sleep(1)#Yes
    click("1670670387139.png");    sleep(1) #sell

def icons():
    dragtop=Location(my.ClientRegion.x+my.ClientRegion.w/20,my.ClientRegion.y+my.ClientRegion.h/4);
    dragbut=Location(my.ClientRegion.x+my.ClientRegion.w/20,my.ClientRegion.y+my.ClientRegion.h*3/4);
    drag(dragtop);
    dropAt(dragbut);
    print findAll("eventLeft.png")

if False: #buy mother's day crown
  for i in range(50):
    click("1684105552130.png");    sleep(1)
    
    click("1670669685882.png");    sleep(1)#to shop
    click("1670669771737.png");    sleep(1)#arrow down
    
    loc=find(Pattern("1684294437375.png").targetOffset(-270,0));
    drag(find(Pattern("1684105606263.png").targetOffset(32,-18)));    sleep(2)    
    dropAt(loc);sleep(2)
    

    click("1670669969525.png");    sleep(5) #check yes
    click("1684105732132.png");    sleep(2)    #poppy - snowflake    
    click(Pattern("1684105764702.png").similar(0.57));    sleep(1) #object in field
    click("1670670246915.png");    sleep(1)    #hand out
    click("1670670333091.png");    sleep(1)#Yes
    click("1670670387139.png");    sleep(1) #sell
    
    

def getLogin2():
    click(find(Pattern("1671656618716.png").targetOffset(34,1)).getTarget().offset(70,0))    
    type("a",Key.CTRL)
    type("javascript:alert(navigator.clipboard.writeText($('div.playerLogin').text()))")
    type(Key.ENTER);sleep(1)
    type(Key.ENTER);
    type(Key.ESC);sleep(1)
    return Env.getClipboard().split(":")[1].strip()
#print getLogin()

def bbs():
    #1p1: highlevesl=water 1>desert 3/2> jungle 3> trpple advance
    find("1671704751248.png")
    pg=1-len(findAny("1671707646707.png"))
    print pg
    brushes=list(findAll(Pattern("1671704874264.png").similar(0.84)))
    print len(brushes)
    for bs in brushes:
        rg=bs.offset(284-318,355-276) #M[319,276 89x84] ->R[284,355 79x31]
        rg.w=79
        rg.h=31
        print rg
        tx=rg.text().strip()
        if(tx[len(tx)-1]=='h'):
            tx=tx+"0m"
        t=tx.split("h")
        s=0
        if len(t)>1:
            h=int(t[0])
            m=int(t[1].split("m")[0])
        else:
            h=0;
            m=t[0].split("m");
            if len(m)>1:
                s=m[1]
                m=int(m[0]);
            else:
                s=m[0];
                m=0;
            s=int(s.split("s")[0]);
        print h,m,s;
        mouseMove(bs)
    
    nipples=list(findAll("1671709919064.png"))
    print len(nipples),nipples[0]
    mouseMove(nipples[0])
    
    for bs in nipples:
        rg=bs.offset(473-516,484-510) #[516,510 24x24] ->R[473,484 72x22]
        rg.w=72
        rg.h=22
        print rg
        tx=rg.text().strip()
        tx=tx.replace('O','0')
        tx=tx.replace('o','0')
        tx=tx.replace(' ','')
        tx=tx.replace('sm','m')
        print tx
        if(tx[len(tx)-1]=='h'):
            tx=tx+"0m"
        t=tx.split("h")
        s=0
        if len(t)>1:
            h=int(t[0])
            m=int(t[1].split("m")[0])
        else:
            h=0;
            m=t[0].split("m");
            if len(m)>1:
                s=m[1]
                m=int(m[0]);
            else:
                s=m[0];
                m=0;
            s=int(s.split("s")[0]);
        print h,m,s;
        mouseMove(bs)
my.login='Charlotte';   
def getLogin():        
    type('0',Key.CTRL);sleep(0.5)
    rg=Region(1074,2,292,295)
    try:
        rg.find(Pattern("1671719739025.png").similar(0.73))
        my.login='Trump2024';
    except:
        try:
            rg.find("1671725002369.png")
            my.login='Mom';
        except:
            pass;
    return my.login;

#print getLogin()

myOptions = OCR.Options()

import java

# get a value
print java.lang.System.getProperty("key-of-property")
print java.lang.System.out
print java.lang.System.in
print java.lang.System.exit
print java.lang.System.getProperty("java.vm.vendor");
java.lang.System.clearProperty("key-of-property")
java.lang.System.setProperty("key-of-property", '12345')
print java.lang.System.getenv("PATH");
print java.lang.System.gc();#None
print java.lang.Thread.activeCount();
java.lang.Thread.dumpStack();
print java.lang.Thread. getDefaultUncaughtExceptionHandler()#None
print java.lang.Thread.holdsLock(my)#False
print java.lang.Thread.interrupted()#False
java.lang.Thread.sleep(1000)
java.lang.Thread.sleep(1234,567)
java.lang.Thread.yield()
print java.lang.Package.getPackages()
#print org.opencv.features2d.
#print org.opencv.osgi.
#print org.opencv.dnn
#org.opencv.utils
#org.opencv.core
#org.opencv.imgproc


x="""
array(java.lang.Package, [package java.awt.datatransfer, package java.security.spec, package java.util.function, package sun.awt.event, package com.sun.imageio.stream, package sun.net.www.protocol.jar, package java.nio.channels.spi, package org.xml.sax, package sun.awt, package sun.reflect.generics.factory, package javax.xml.xpath, package javax.imageio, package sun.java2d.windows, package java.lang.ref, package javax.swing.text.html.parser, package sun.security.ssl, package com.sun.crypto.provider, package jdk.internal.ref, package jdk.internal.foreign.abi, package java.time.zone, package java.util.zip, package java.io, package sun.util.logging.internal, package javax.swing.table, package sun.reflect.annotation, package sun.invoke.empty, package java.lang.foreign, package jdk.internal.jimage.decompressor, package java.nio.charset.spi, package sun.invoke.util, package java.lang.reflect, package com.sun.imageio.plugins.wbmp, package com.sun.java.swing.plaf.windows, package sun.management, package jdk.internal.
icu.text, package sun.swing.text, package java.nio.channels, package sun.io, package sun.nio, package sun.print, package java.lang.module, package jdk.internal.util, package javax.sound.sampled, package sun.text.resources, package java.text.spi, package org.w3c.dom, package sun.java2d.opengl, package sun.util.locale, package javax.net.ssl, package sun.security.action, package jdk.internal.misc, package java.util.prefs, package javax.swing.plaf.synth, package jdk.internal.vm.annotation, package java.nio.file.attribute, package sun.util.resources, package sun.java2d.pipe, package javax.swing.plaf.basic, package javax.accessibility, package sun.net, package java.security.interfaces, package sun.reflect.generics.parser, package javax.imageio.event, package sun.awt.dnd, package java.awt.im, package java.util.concurrent.locks, package javax.crypto, package javax.xml.transform, package javax.imageio.metadata, package jdk.internal.org.objectweb.asm, package com.sun.java.swing, package sun.util.locale.provider, packag
e sun.text.resources.cldr, package sun.datatransfer, package java.awt.image, package java.awt.peer, package sun.net.www.protocol.file, package sun.util.spi, package sun.security.provider, package sun.net.www, package java.util.concurrent.atomic, package javax.security.auth.callback, package com.sun.imageio.plugins.tiff, package java.time.chrono, package sun.awt.geom, package jdk.internal.logger, package sun.util, package sun.java2d.d3d, package java.beans, package sun.java2d.marlin, package java.security.cert, package java.math, package sun.security.util, package java.awt.geom, package java.util.random, package java.applet, package javax.swing.plaf.metal, package sun.net.ext, package jdk.internal.util.random, package java.security, package sun.reflect.generics.scope, package sun.nio.cs, package jdk.internal.icu.impl, package java.util.stream, package jdk.internal.vm.vector, package com.sun.imageio.plugins.common, package javax.crypto.spec, package java.lang.annotation, package sun.awt.shell, package java.time
.temporal, package java.nio, package java.nio.charset, package org.xml.sax.helpers, package com.sun.imageio.plugins.jpeg, package javax.swing.text.html, package jdk.internal.access, package java.awt.desktop, package com.sun.management, package sun.swing, package jdk.internal.event, package java.util, package javax.crypto.interfaces, package java.util.jar, package com.sun.beans.util, package jdk.management.jfr, package jdk.internal.math, package javax.swing.plaf, package javax.security.auth.login, package java.rmi, package java.text, package java.time, package sun.util.resources.cldr, package jdk.internal.jimage, package java.awt.im.spi, package jdk.internal.module, package sun.awt.util, package sun.font, package sun.util.calendar, package sun.reflect.generics.visitor, package javax.swing.border, package sun.text, package jdk.internal.icu.lang, package java.rmi.server, package sun.util.cldr, package sun.reflect.generics.repository, package sun.launcher, package java.util.logging, package com.sun.imageio.plugin
s.gif, package com.sun.imageio.spi, package javax.swing.text, package javax.swing.tree, package com.sun.imageio.plugins.png, package jdk.internal.vm, package java.lang.constant, package jdk.net, package sun.awt.image, package sun.java2d.cmm, package java.nio.file, package java.lang, package javax.management, package java.awt.dnd, package jdk.internal.loader, package java.lang.invoke, package sun.management.spi, package sun.awt.im, package java.awt.font, package sun.nio.ch, package sun.awt.resources, package java.awt, package javax.imageio.stream, package sun.misc, package sun.java2d.pipe.hw, package sun.java2d.loops, package java.util.spi, package java.util.concurrent, package javax.swing.undo, package sun.reflect.generics.tree, package javax.imageio.spi, package java.nio.file.spi, package sun.security.rsa, package jdk.internal.reflect, package sun.security.provider.certpath.ldap, package java.awt.dnd.peer, package sun.awt.datatransfer, package java.awt.print, package sun.reflect.generics.reflectiveObjects, p
ackage com.sun.security.sasl, package java.net.spi, package javax.security.auth, package sun.net.www.protocol.jrt, package java.awt.event, package com.sun.swing.internal.plaf.metal.resources, package sun.security.jca, package sun.awt.windows, package jdk.internal.icu.util, package sun.net.util, package java.lang.management, package jdk.internal.perf, package sun.nio.fs, package jdk.internal.foreign, package com.sun.swing.internal.plaf.basic.resources, package jdk.management.jfr.internal, package sun.util.logging, package javax.security.cert, package com.sun.management.internal, package com.sun.imageio.plugins.bmp, package java.awt.color, package sun.java2d, package java.util.regex, package sun.reflect.misc, package javax.swing, package javax.swing.filechooser, package javax.swing.event, package java.net, package java.sql, package sun.security.ec, package com.sun.security.sasl.gsskerb, package sun.security.jgss, package sun.util.resources.provider, package org.jcp.xml.dsig.internal.dom, package sun.security.sm
artcardio, package sun.util.resources.cldr.provider, package sun.security.mscapi, package javax.script, package sun.security.pkcs11.wrapper, package sun.security.pkcs11, package org.apache.commons.compress.compressors.lz77support, package io.netty.handler.codec.serialization, package io.netty.channel.socket.nio, package jnr.ffi, package org.bouncycastle.jcajce.provider.config, package org.apache.tools.ant.taskdefs.condition, package com.github.jaiimageio.impl.plugins.pcx, package org.bouncycastle.asn1.x9, package jnr.posix.windows, package org.opencv.features2d, package com.github.jaiimageio.impl.plugins.tiff, package org.apache.log4j.helpers, package org.apache.tools.ant.helper, package org.apache.tools.ant.types.selectors, package org.bouncycastle.jcajce.util, package io.netty.handler.ssl, package org.bouncycastle.crypto.util, package org.bouncycastle.cert.ocsp, package org.apache.tools.ant.taskdefs.email, package org.apache.xmlgraphics.image.loader, package org.antlr.runtime.debug, package org.reflections8
.scanners, package org.bouncycastle.util.io.pem, package org.apache.commons.cli, package org.sikuli.guide, package org.apache.commons.io, package org.bouncycastle.i18n, package io.netty.util.internal, package org.apache.commons.collections, package org.python.antlr.ast, package org.python.indexer.ast, package org.bouncycastle.cert, package javassist.bytecode.stackmap, package com.fasterxml.jackson.databind.jsonschema, package com.lowagie.text.xml, package org.bouncycastle.math.field, package jnr.ffi.provider.jffi.platform.x86_64.windows, package org.apache.log4j.or, package org.slf4j.event, package org.apache.xmlgraphics.util.dijkstra, package com.google.common.base, package com.lowagie.text.pdf.draw, package org.reflections8.vfs, package org.bouncycastle.cert.selector.jcajce, package com.ibm.icu.text, package org.python.modules._collections, package org.apache.xmlgraphics.java2d, package org.apache.xmlgraphics.image.loader.cache, package javax.servlet, package com.google.common.cache, package com.fasterxml.j
ackson.databind.ext, package org.apache.tools.ant, package com.jcraft.jsch, package org.slf4j, package org.apache.tools.bzip2, package org.apache.xmlgraphics.java2d.color, package org.python.core.util, package org.bouncycastle.eac.operator.jcajce, package com.fasterxml.jackson.databind.util, package com.sun.jna, package javassist.compiler, package net.sourceforge.lept4j, package py4j.commands, package com.sun.jna.platform.win32.COM, package org.bouncycastle.asn1.icao, package org.bouncycastle.crypto.modes.kgcm, package org.bouncycastle.crypto.digests, package org.apache.tools.ant.taskdefs.optional.jsp, package org.objectweb.asm, package com.google.common.math, package com.ibm.icu.lang, package com.sun.jna.internal, package com.explodingpixels.painter, package org.apache.log4j.pattern, package org.apache.tools.ant.taskdefs.optional.ejb, package io.netty.handler.traffic, package org.apache.commons.compress.utils, package org.apache.tools.ant.types.resources.selectors, package org.antlr.runtime, package org.apac
he.xmlgraphics.xmp.merge, package org.jboss.vfs.util.automount, package org.apache.commons.compress.archivers.tar, package org.apache.commons.compress.archivers, package com.jgoodies.forms.layout, package org.apache.log4j.xml, package org.slf4j.helpers, package io.netty.channel, package com.fasterxml.jackson.databind.deser.impl, package com.fasterxml.jackson.databind, package org.bouncycastle.cert.jcajce, package org.bouncycastle.eac.operator, package org.sikuli.ide, package jnr.x86asm, package jnr.posix.util, package org.python.modules._locale, package com.google.common.primitives, package com.github.jaiimageio.impl.stream, package com.jcraft.jsch.jcraft, package org.bouncycastle.x509, package com.fasterxml.jackson.databind.ser.impl, package org.bouncycastle.est.jcajce, package org.apache.tools.ant.taskdefs.compilers, package org.ghost4j.modifier, package com.fasterxml.jackson.annotation, package org.python.modules.posix, package org.bouncycastle.pqc.math.linearalgebra, package org.bouncycastle.jce.provider,
 package com.lowagie.text.pdf.interfaces, package org.apache.tools.ant.util, package org.apache.commons.io.input, package jxgrabkey, package io.netty.handler.codec, package org.python.modules.itertools, package io.netty.handler.stream, package org.python.core.adapter, package io.netty.channel.socket, package org.apache.tools.ant.taskdefs.optional.native2ascii, package org.bouncycastle.eac.jcajce, package com.google.common.escape, package jnr.ffi.annotations, package javax.annotation.meta, package jnr.ffi.byref, package com.github.jaiimageio.impl.plugins.gif, package org.apache.commons.io.serialization, package com.fasterxml.jackson.core.util, package com.lowagie.text.pdf.codec.wmf, package org.python.modules._io, package com.tigervnc.vncviewer, package com.jcraft.jzlib, package org.objectweb.asm.tree.analysis, package org.stringtemplate.v4, package org.bouncycastle.asn1.x509.qualified, package org.bouncycastle.crypto.tls, package com.sun.jna.platform.win32.COM.tlb.imp, package io.netty.util.concurrent, packag
e jnr.ffi.util, package jline, package org.bouncycastle.asn1.eac, package py4j.reflection, package com.ibm.icu.impl, package org.objectweb.asm.signature, package org.python.modules.sre, package org.apache.commons.compress.archivers.examples, package org.antlr.misc, package org.python.core.packagecache, package org.python.compiler, package org.apache.tools.ant.taskdefs.optional.depend, package jnr.a64asm, package org.sikuli.script.compare, package com.ibm.icu.impl.number, package org.python.modules._threading, package javassist.util.proxy, package org.opencv.osgi, package com.lowagie.text.pdf, package jnr.constants, package org.sikuli.idesupport.syntaxhighlight.style, package org.apache.log4j.spi, package com.lowagie.text, package org.bouncycastle.crypto.ec, package org.bouncycastle.est, package com.ibm.icu.impl.locale, package org.jboss.vfs, package com.tulskiy.keymaster.x11, package com.google.common.util.concurrent, package org.sikuli.script, package jnr.ffi.types, package javassist.bytecode.analysis, packa
ge org.python.antlr.adapter, package org.python.antlr.op, package org.antlr.runtime.misc, package com.google.common.eventbus, package org.apache.xmlgraphics.ps.dsc, package com.google.common.collect, package io.netty.buffer, package com.ziclix.python.sql.pipe.db, package org.bouncycastle.x509.util, package com.github.jaiimageio.impl.common, package org.fusesource.jansi, package org.reflections8.util, package org.jdesktop.layout, package javassist.bytecode.annotation, package io.netty.handler.ipfilter, package org.sikuli.script.support, package com.fasterxml.jackson.databind.ser, package org.apache.tools.ant.dispatch, package com.fasterxml.jackson.databind.cfg, package org.sikuli.hotkey, package org.apache.tools.zip, package com.sun.jna.platform, package com.github.jaiimageio.stream, package org.python.modules.zipimport, package org.bouncycastle.cms, package org.reflections8.serializers, package com.ibm.icu.impl.duration, package jline.internal, package org.bouncycastle.cert.selector, package com.github.jaiima
geio.impl.plugins.raw, package com.google.common.util.concurrent.internal, package com.jgoodies.forms.util, package com.sun.jna.ptr, package org.bouncycastle.pqc.crypto.gmss, package org.python.modules.thread, package org.bouncycastle.tsp.cms, package org.bouncycastle.jce.interfaces, package org.bouncycastle.pqc.jcajce.interfaces, package com.github.jaiimageio.plugins.tiff, package org.python.indexer, package jline.console.completer, package com.sun.jna.platform.win32, package org.sikuli.idesupport.syntaxhighlight.grammar, package javassist.expr, package org.bouncycastle.util.encoders, package com.fasterxml.jackson.core.async, package org.python.modules._jythonlib, package org.python.antlr.base, package io.netty.handler.codec.marshalling, package org.bouncycastle.asn1.x500, package com.kenai.jnr.x86asm, package org.bouncycastle.asn1.x509, package org.bouncycastle.crypto, package com.explodingpixels.widgets.plaf, package org.apache.tools.ant.taskdefs.optional.j2ee, package org.python.modules, package org.antlr
.analysis, package org.apache.xmlgraphics.image.loader.impl, package org.antlr.codegen, package com.tulskiy.keymaster.windows, package org.slf4j.spi, package org.bouncycastle.pqc.crypto.util, package org.apache.commons.exec.launcher, package org.python.core.stringlib, package io.netty.util.internal.shaded.org.jctools.queues.atomic, package org.opencv.dnn, package org.apache.tools.ant.filters, package org.bouncycastle.pkix, package org.bouncycastle.pqc.crypto.xmss, package org.bouncycastle.mime, package org.apache.log4j.config, package org.reflections8.adapters, package org.bouncycastle.cms.jcajce, package org.ghost4j.display, package org.apache.tools.ant.taskdefs.optional.javah, package org.sikuli.basics, package org.apache.tools.ant.taskdefs.optional.depend.constantpool, package com.lowagie.text.pdf.hyphenation, package org.ghost4j, package jnr.posix, package com.fasterxml.jackson.core.filter, package com.sun.jna.platform.unix, package org.bouncycastle.math.ec.endo, package jnr.ffi.provider.jffi, package jnr
.constants.platform.windows, package org.python.modules._functools, package org.apache.commons.compress.archivers.sevenz, package org.apache.tools.tar, package org.python.modules.jffi, package com.kenai.jffi.internal, package io.netty.util.internal.shaded.org.jctools.queues, package org.antlr.tool, package org.apache.commons.compress.archivers.cpio, package com.fasterxml.jackson.databind.jsontype, package py4j, package org.apache.tools.ant.taskdefs.launcher, package org.apache.commons.logging, package javassist.bytecode, package com.kenai.jffi, package org.apache.commons.compress.changes, package org.apache.commons.beanutils.expression, package org.reflections8, package org.bouncycastle.openssl, package org.bouncycastle.crypto.signers, package com.fasterxml.jackson.core.format, package org.python, package io.netty.util.collection, package com.google.common.graph, package com.explodingpixels.widgets, package org.python.modules.time, package org.python.core, package com.fasterxml.jackson.core.type, package org.
objectweb.asm.commons, package org.bouncycastle.crypto.engines, package org.bouncycastle.i18n.filter, package org.apache.tools.ant.util.depend, package org.apache.tools.ant.types.resources, package io.netty.resolver, package org.bouncycastle.util, package org.apache.log4j, package org.jboss.logging, package jline.console, package org.sikuli.util, package com.lowagie.text.xml.simpleparser, package se.vidstige.jadb, package com.fasterxml.jackson.core, package org.apache.xmlgraphics.util, package com.fasterxml.jackson.databind.node, package com.sun.jna.win32, package org.sikuli.idesupport, package io.netty.handler.timeout, package com.ziclix.python.sql.pipe, package javassist.scopedpool, package javassist.compiler.ast, package org.apache.commons.exec, package jnr.ffi.provider, package com.google.common.hash, package org.bouncycastle.math.ec, package org.bouncycastle.crypto.prng.drbg, package org.apache.log4j.lf5, package com.fasterxml.jackson.databind.jsonFormatVisitors, package com.ibm.icu.util, package org.bou
ncycastle.cert.crmf.jcajce, package com.jgoodies.forms.builder, package org.stringtemplate.v4.misc, package jnr.netdb, package org.bouncycastle.crypto.modes.gcm, package org.apache.xmlgraphics.util.i18n, package org.apache.commons.compress.compressors.bzip2, package io.netty.util.internal.logging, package org.apache.tools.ant.taskdefs.optional.jsp.compilers, package io.netty.channel.nio, package org.bouncycastle.operator.bc, package org.python.util, package org.bouncycastle.pkcs, package org.slf4j.impl, package org.python.antlr, package org.sikuli.vnc, package org.sikuli.natives, package org.apache.tools.ant.attribute, package io.netty.channel.pool, package org.sikuli.idesupport.syntaxhighlight.format, package com.ibm.icu.impl.coll, package org.apache.tools.ant.launch, package org.apache.tools.ant.util.regexp, package org.apache.tools.ant.types, package org.sikuli.script.runnerSupport, package org.apache.commons.beanutils, package com.sun.jna.platform.win32.COM.util, package org.opencv.utils, package org.apac
he.xmlgraphics.xmp, package io.netty.util.internal.shaded.org.jctools.util, package com.google.common.reflect, package org.apache.tools.ant.taskdefs.rmic, package org.bouncycastle.jce.exception, package org.apache.commons.io.monitor, package jline.console.history, package org.apache.tools.ant.input, package org.ghost4j.document, package org.bouncycastle.crypto.modes, package org.objectweb.asm.util, package org.opencv.core, package net.sourceforge.tess4j, package com.fasterxml.jackson.core.sym, package com.fasterxml.jackson.databind.introspect, package org.sikuli.script.runners, package org.apache.commons.compress.parallel, package org.bouncycastle.asn1, package com.ziclix.python.sql, package org.python.modules.random, package org.bouncycastle.util.test, package com.tulskiy.keymaster.osx, package com.explodingpixels.macwidgets.plaf, package org.sikuli.idesupport.syntaxhighlight, package jnr.ffi.mapper, package gnu.cajo, package org.python.modules._weakref, package org.apache.commons.compress.archivers.zip, pac
kage jnr.constants.platform, package jnr.ffi.util.ref, package com.tulskiy.keymaster.common, package org.bouncycastle.crypto.paddings, package io.netty.bootstrap, package org.apache.xmlgraphics.image.loader.spi, package org.apache.commons.compress.compressors.deflate64, package org.bouncycastle.cert.crmf, package com.lowagie.text.pdf.parser, package org.apache.tools.ant.taskdefs.optional.extension, package org.antlr.runtime.tree, package org.bouncycastle.asn1.cms, package org.apache.commons.io.file, package com.tigervnc.rdr, package com.ibm.icu.impl.number.formatters, package org.python.core.finalization, package io.netty.channel.group, package org.apache.tools.ant.taskdefs, package org.apache.xmlgraphics.ps, package org.apache.tools.ant.property, package com.github.jaiimageio.impl.plugins.bmp, package org.bouncycastle.pqc.crypto.newhope, package org.apache.tools.ant.taskdefs.optional.sos, package org.bouncycastle.asn1.util, package org.apache.tools.ant.types.selectors.modifiedselector, package org.python.mod
ules._json, package org.apache.commons.io.filefilter, package org.objectweb.asm.tree, package com.explodingpixels.macwidgets, package org.bouncycastle.operator, package org.apache.xmlgraphics.image.writer, package com.tigervnc.network, package com.tigervnc.rfb, package javassist, package org.opencv.imgproc, package jnr.ffi.provider.converters, package com.fasterxml.jackson.databind.deser, package org.bouncycastle.pqc.crypto, package io.netty.util, package org.bouncycastle.jcajce.provider.symmetric.util, package com.ibm.icu.impl.duration.impl, package org.apache.commons.collections.collection, package org.apache.tools.ant.taskdefs.optional.vss, package javassist.tools.web, package org.bouncycastle.asn1.pkcs, package org.apache.commons.compress.compressors, package org.stringtemplate.v4.debug, package org.python.core.buffer, package com.github.jaiimageio.impl.plugins.pnm, package org.python.indexer.types, package org.apache.xmlgraphics.util.io, package org.bouncycastle.jcajce.provider.util, package org.sikuli.a
ndroid, package org.apache.commons.exec.environment, package org.bouncycastle.dvcs, package org.apache.xmlgraphics.image.codec.util, package org.python.core.io, package com.jgoodies.forms.factories, package org.bouncycastle.crypto.prng, package org.python.expose, package org.apache.log4j.rewrite, package org.bouncycastle.cert.dane, package com.github.jaiimageio.impl.plugins.wbmp, package com.google.common.io, package org.apache.commons.collections.iterators])
"""        
my.friend_active =True;

print my.ClientRegion
#print my.last['ClientRegion']
my.esc_close=False
my.TimeLoadZoo=77; #22, based on cpu,space.network?


my.short_term=[];  
my.mustsort=9999;

def externalTimeout():
    pass;
    #percise? multi step approching, Do.pop,sleep?
    #Windows scheduler? record , multi setup squeeze, (cancel?), event triger?,schtasks
    #chance of run loop?, estimate frequency, business pre-post?
    #chance of init, estimate frequency, calendar
    #do not block! 
    
def setTimeout(s,ts):    
    td=datetime.datetime.now()+ts;   
    item={cmd:s,td:td};
    short_term.push(item);
    if mustsort>td:
        mustsort=td;
    if len(item)==1:    
        externalTimeout(td);

def tryTimeout():
    now=datetime.datetime.now();   
    if now>mustsort:              
        sort(short_term,lambda x:x.td);
        #to estimate now and short_term[-1].td, to use long_term?
    i=0;
    short_term=my.short_term;
    for item in  short_term:
       if item.s>now:
           t=short_term.slice(i);
           my.mustsort=t[-1].td;
           my.short_term=t;      
           externalTimeout(t[0].td);
           return;
           break;
       print item.cmd,now
       invoke(item.cmd);
       now=datetime.datetime.now();   
       i+=1;     
    my.short_term=[];      
    my.mustsort=9999;           
    
     

my.esc_close=False    
#print my_run(mine_unknown) 
if False:
    my.friend_active =True;
    my.friend_togo=7 #40 #minutes
    print my_friends()
    print my_friend()
    print my_friend_menu();
    
    my.friend_active =True;
    print my_friend1()
    
    print my_ramp()
    os.system('nbtstat -a 192.168.2.20');
    os.system('net use \\GTX1060\PUBLIC * /USER:HUANGM5')

def my_blue_feeder():
    loc=find("1659095267480.png");
    if loc.getScore()>0.95:                                    
        type(Key.F5);
        Do.popAsk('my_blue_feeder','',3*60);
        my.need_splash=True;

def my_blur():
    try:
        upjers=Region(0,0,246,274).find("1664142336030.png")
        print upjers
        blur=upjers.below(upjers.h).grow(upjers.h).find(Pattern("1664142838204.png").similar(0.76))
        print blur
        score_gate=0.96
        try:
            blur_confused=find(Pattern("1679174063085.png").similar(0.75))
            print blur_confused
            score_gate=blur_confused.getScore()        
        except:
            pass;
        if blur.getScore()>score_gate: #0.8 confused
            click(LocCenter);sleep(1);#my_born 
            if my_GrownUp()==0:
                return 888;
            for i in range(10):
                try:                
                    click("1645882887382.png");sleep(1)
                except:
                    break;
            #my.ClientRegion.click()
            #type(Key.F5); #F5 may be blocked?
            LogScreen();            
            Do.popAsk('blur 1 Reload F5','',38)
            return 0;
    except: 
        pass;
    return 999;
#print my_blur()
#def my_IncreaseMateryLevel():
#    return my_great();
def my_great():
    try:
        Region(my.ClientRegion.x+my.ClientRegion.w/3,
        my.ClientRegion.y+my.ClientRegion.h/2,
        my.ClientRegion.w/3,my.ClientRegion.h/4).click("1681476252642.png");sleep(1)
        return 0;
    except:
        return 999;
#print my_great();

def mine_unknown():
    return [
#my_friend1,#my_friend1_again,my_friend_in,fai

    my_animal_level
#        ,my_friend_menu
    ,my_blur3,my_lets_go,my_clean100,my_clean200
    ,my_close,my_close_feed,my_breed
    ,my_GrownUp,my_connectionError
    ,my_many_cash,my_many_trash,my_coin ,my_many_poppy
    ,my_born,my_many_bronze,my_many_water,my_ball
    ,my_great
    ,my_many_water_again,my_water,my_direct_water,my_friend_menu
    ,my_direct_ramp,my_feed,my_direct_ramp_right,my_direct_ramp_left
    ,my_many_star
    ,my_clear_feed
    ,my_ramp
    ,my_friend_wander,my_open_cards
    ,my_focus,my_zoo,
    #my.friend_active,
    my_breed_from_dialog,
    my_breed_from_center
    ];

print inspect.stack()[0][3]

def my_blur2():
    if my_close()==0:
        return 999;
    try:
        loc=find(Pattern("1679148211092.png").similar(0.66).targetOffset(-38,-3))
        loc.grow(100).find(Pattern("1679099170141.png").similar(0.94))
        click(my.ClientRegion);sleep(1);#my_born 
        if my_close()==0:
            return 999;
        LogScreen();     
        type(Key.F5); #F5 may be blocked?
        Do.popAsk('blur 2 Reload F5','',98)
        return 0;
    except:
        return 999;
#print my_blur2()

if False:
    l=list(findAll("1679098605214.png"));
    l.sort(key=lambda x: x.x);
    click(l[0]);sleep(1);
    type(Key.ESC);
    print l;sleep(1);
    print my_zoo(); ###lead to , growup/born? ->grey out!

def update_scenario():
   my.scenario= scenario;
   
excludes={inossem:[Region(112,635,67,65),Region(961,152,73,67),Region(1107,652,60,60)],
        gtx1060:[Region(1406,97,100,134),Region(331,901,122,116),Region(1646,930,71,91)]
        }[my.scenario];

print 'excludes0 =',excludes;
try:        
    excludes=[find("1681560026685.png").grow(5),find("1681560049431.png").grow(5),find("1681560061965.png").grow(5)];
    print 'excludes1 =',excludes;
except:
    pass;
if False:
    print my_blur2()
    print my_feed()
    update_ClientRegion()
    print my_zoo();
    my_LogScreen()
    
def my_LogScreen():    
    LogScreen()
    
my.friend_togo=20 #40 #minutes

def my_blur3():
    if random.random()>0.1:
        return 999;
    jf=openPaneSample();sleep(3);
    try:
        click(Pattern("1685059837765.png").similar(0.92).targetOffset(-169,0));sleep(1);
        jf.setVisible(False);
        jf.dispose();
        type(Key.F5);sleep(1);
        Do.popAsk('find pic','',3*60);
        my_splash();
        #entering('Main'); this blurs again (at this situation?) miss click on help contest?
        return 0;
    except:
        pass;
    jf.setVisible(False);
    jf.dispose();
    return 999;
#my_blur3();



import java.awt.Toolkit;
import java.awt.Dimension;
import java.awt.Color;
import javax.swing.JComponent;
import javax.swing.JFrame;
import java.awt.BorderLayout;
t=java.awt.Toolkit.getDefaultToolkit();
i=t.getImage("p3.gif");

class DrawPane (javax.swing.JComponent):
    def paintComponent(this,g):
#        javax.swing.JComponent.paintComponent(g);
        g.setColor(java.awt.Color.gray);
        g.fillRect(0,0,100,100);
        pass;

def openPaneSample():
    jf=javax.swing.JFrame();
    jf.setDefaultCloseOperation(1);#EXIT_ON_CLOSE
    jf.add(DrawPane(),java.awt.BorderLayout.CENTER);
    jf.setLocationRelativeTo(None);
    jf.setPreferredSize(java.awt.Dimension(100, 100));
    jf.pack();
    jf.setVisible(True);
    return jf;

if False:
    openPaneSample();sleep(3);
    try:
        click(Pattern("1685059837765.png").similar(0.92).targetOffset(-169,0));sleep(1);
        type(Key.F5);sleep(1);
        Do.popAsk('find pic','',3*60);
        my_splash();
        entering('Main');
    except:
        pass;

if False:
    import SimpleHTTPServer
    import BaseHTTPServer
            
    PORT = 8000
    #print sys.path[0]#D:\Users\Public\Documents\trump2024.charlotte.sikuli
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    #print Handler.__dict__.keys()
#    print Handler.translate_path,Handler.do_HEAD,Handler.send_head,Handler.extensions_map,Handler.guess_type,Handler.server_version
#    print Handler.__module__,Handler.directory,Handler.copyfile,Handler.do_GET,Handler.list_directory,Handler.__doc__
    httpd = BaseHTTPServer.HTTPServer(("", PORT), Handler)
    print("serving at port", PORT)
    
    import threading
    
    def regular_run():
      print("This is my regular run!")
      httpd.serve_forever()
    
    thread_B = threading.Thread(target=regular_run)
    thread_B.start()
    print httpd

#httpd.shutdown();#and need pay a visit
if False: #buy summer sunshine
  for i in range(50):
    click("1687887252106.png");    sleep(1)
    click("1670669685882.png");    sleep(2)#to shop
#    click("1670669771737.png");    sleep(1)#arrow down
    
    loc=find(Pattern("1688523839627.png").similar(0.62).targetOffset(-46,104));
    drag(find("1688518746824.png"));    sleep(2)    
    dropAt(loc);sleep(2)
    
    click("1670669969525.png");    sleep(12) #check yes
    click("1687887411240.png");    sleep(2)    #poppy - snowflake    
    click("1687887438543.png");    sleep(1) #object in field
    click("1670670246915.png");    sleep(1)    #hand out
    click("1670670333091.png");    sleep(2);#Yes
    click("1670670387139.png");    sleep(8); #sell

def my_contest():
    now=datetime.datetime.now()
    if now.hour!=4:
        print now;
        return 999;
    if now.minute>30:
        return 999;
    if my.zoo!='Main':
        print my.zoo;        
        return 999;
    my.ClientRegion.findAny("1716982003122.png","club_eagle.png")[0].click();sleep(1)
    my.ClientRegion.findAny("1716982136322.png")[0].click();sleep(1)
    my.ClientRegion.findAny("1716982189262.png")[0].click();sleep(1)
    my.ClientRegion.findAny(Pattern("1716982929944.png").targetOffset(-18,-76))[0].click();sleep(1)
    my.ClientRegion.findAny(Pattern("1716982970572.png").targetOffset(-15,33))[0].click();sleep(1)
    loc=my.ClientRegion.findAny("1716983033901.png")[0]
    type(Key.ESC);sleep(1)    
    my.ClientRegion.findAny(Pattern("1716982262151.png").targetOffset(3,118))[0].click();sleep(1)
    loc=my.ClientRegion.findAny(Pattern("1716982406386.png").targetOffset(309,-72))[0]
    for i in range(10):
        loc.click();sleep(1)
    if now.hour!=4:
        my_close();
#    my.ClientRegion.findAny("1716982534261.png")[0].click();sleep(1)
    return 0;

print my_contest()

if False:
    for l in range(2):
        click("1691178705630.png");sleep(1)
        click("1691178796904.png");sleep(1);
        mouseMove(Screen().getCenter());sleep(1);
        click("1691178868525.png");sleep(1)
        loc=find(Pattern("1691178895544.png").targetOffset(51,-31));
        for i in range(11):
            click(loc);sleep(0.5)
        click(Pattern("1691178955653.png").targetOffset(-2,47));sleep(1)    
        drag(Location(611, 482));
        dropAt(Location(346, 400));
        loc2=findAny(Pattern("1691179056355.png").similar(0.59).targetOffset(99,-3),"zigborder.png")[0];
        for k in range(12):
            try:    
                loc1=find("1691179104005.png");
            except:
                click("1691179144396.png");sleep(1)
                click("1691179184121.png");sleep(1);
                #mouseMove(my.ClientRegion.getCenter());sleep(1);
                try:
                    click(Pattern("1691179264903.png").targetOffset(-4,15));sleep(1.5);
                    click("1691199881023.png");sleep(1);
                except:
                    pass;
                try:    
                    loc1=find("1691179104005.png");
                except:
                    break;
            drag(loc1);sleep(0.3)   
            drag(Screen());sleep(0.3)    
            rg=Region(425,615,382,114)
            for i in range(50):
                loc=loc2.offset(int(random.random()*500-150),int(random.random()*220-150));
                drag(loc);sleep(0.3)    
                try:
                    rg.find(Pattern("1691179426455.png").similar(0.89));
                except:
                    dropAt(loc);sleep(1)    
                    rg.click(Pattern("1691179482226.png").similar(0.84).targetOffset(-50,0));sleep(2)    
                    break;
                
        for k in range(12):
            click(Location(610, 422));sleep(0.8);
            try:
                Region(507,467,165,159).click("1691180965365.png");sleep(1.5)  
                continue;
            except:
                pass;
            Region(482,426,255,180).click("1691180835535.png");sleep(1)    
            Region(148,284,186,158).click("1691180879171.png");sleep(1.6)   
            try:            
                Region(240,180,266,255).click("1691180914289.png");sleep(0.7)    
            except:
                type(Key.ESC);sleep(1)
                break;
            Region(507,467,165,159).click("1691180965365.png");sleep(1.5)    #can not less ,some time stuck unfold    
            
        drag(Location(286, 320));dropAt(Location(662, 477));  
        click(Pattern("1691181343545.png").similar(0.45));sleep(1)
        click("1691181372306.png");sleep(1)
        click("1691181385811.png");sleep(1)
        click("1691181401862.png");sleep(1)
        loc=find(Pattern("1691181417270.png").targetOffset(81,-66));
        for i in range(12):
            click(loc);sleep(0.5)
        click(Pattern("1691181460652.png").targetOffset(-19,25));sleep(1)
        click("1691181510642.png");sleep(1)
        type(Key.ESC);sleep(1)


if False: #buy christmas snow flakes
  for i in range(50):
    click(Pattern("1702826796966.png").similar(0.43));    sleep(1)
    click(Pattern("1670669685882.png").similar(0.47));    sleep(2)#to shop
    click("1670669771737.png");    sleep(1)#arrow down
    
    loc=findAny(Pattern("1702826868319.png").targetOffset(65,-19),"1702852465710.png",Pattern("1703040702871.png").similar(0.58).targetOffset(96,6))[0];
    drag(find(Pattern("1702826890919.png").similar(0.58)));    sleep(2)    
    dropAt(loc);sleep(2)
    
    click("1670669969525.png");    sleep(12) #check yes
    click(Pattern("1702826948882.png").similar(0.45));    sleep(2)    #poppy - snowflake    
    click(Pattern("1702826663006.png").similar(0.45));    sleep(1) #object in field
    click("1670670246915.png");    sleep(1)    #hand out
    click(findAny("1670670333091.png","1702826720460.png")[0]);    sleep(2);#Yes
    click(Pattern("1670670387139.png").similar(0.67));    sleep(8); #sell

if False: #buy valentine
  for i in range(70):
    click("1707523554389.png");    sleep(1)
    click(Pattern("1670669685882.png").similar(0.47));    sleep(2)#to shop
#    click("1670669771737.png");    sleep(1)#arrow down
    
    loc=findAny(Pattern("1707531926828.png").targetOffset(35,-22),Pattern("1707839258443.png").targetOffset(-25,-25),Pattern("1707839356315.png").targetOffset(75,-9))[0];
    drag(find("1707523613793.png"));    sleep(2)    
    dropAt(loc);sleep(2)
    
    click("1670669969525.png");    sleep(7) #check yes
    click("1707523719629.png");    sleep(2)    #poppy - snowflake    
    click(findAny(Pattern("1707523758791.png").similar(0.55),Pattern("1707532099305.png").similar(0.61))[0]);    sleep(1) #object in field
    click("1670670246915.png");    sleep(1)    #hand out
    click(findAny("1670670333091.png","1702826720460.png")[0]);    sleep(2);#Yes
    click(Pattern("1670670387139.png").similar(0.67));    sleep(8); #sell

def my_spin():
    Region(424,281,454,351).find("1704460952190.png").click();sleep(20)
    type(Key.ESC);
    sleep(1)

drag(my.ClientRegion.findAny(bucket));sleep(1)
dropAt(my.ClientRegion.offset(random.randint(-200, 200),random.randint(-150, 160)));sleep(1)

#rabbit "1707021022220.png"
#7730"1707147386443.png"=>7750, fail...
#print 90000/20*2500=11,250,000


highlightAllOff()
from collections import defaultdict
#class Graph:


#polar bear 18% "1711754523344.png"

#"1715035567925.png" what is crypto...?
#Mother's day

def read_menu():
    
    rg=Region(my.ClientRegion.x,my.ClientRegion.y+my.ClientRegion.h/9,my.ClientRegion.w/6,my.ClientRegion.h/6)
    topLeftMenu=findAny(Pattern("1715211979534.png").similar(0.54),"1715212202381.png")[0];

    rg=Region(my.ClientRegion.x,my.ClientRegion.y+my.ClientRegion.h*5/6,my.ClientRegion.w/6,my.ClientRegion.h/6)
    butLeftMenu=rg.findAny(Pattern("1715212022118.png").similar(0.60),"1715212255610.png")[0];
#    top ones no arc?
    rg=Region(my.ClientRegion.x,my.ClientRegion.y+my.ClientRegion.h*4/6,my.ClientRegion.w/6,my.ClientRegion.h*2/6)
    cicletop=rg.findAny(Pattern("1715212627647.png").targetOffset(-2,30))[0];
#    drag(cicletop);dropAt(Location(cicletop.x,(topLeftMenu.y*5+butLeftMenu.y*1)/6));sleep(1)
    
    rg=Region(my.ClientRegion.x,topLeftMenu.y,my.ClientRegion.w/6,my.ClientRegion.h*1/6)
    cicletop=rg.findAny(Pattern("1715212627647.png").targetOffset(-2,30))[0];
    drag(cicletop);dropAt(Location(cicletop.x,(topLeftMenu.y*1+butLeftMenu.y*5)/6));sleep(1)
    

import threading;

from threading import Thread, Lock

behaves=list()
def dobehaves():
    locker = Lock()
    while True:
        l0=len(behaves)
        if l0>3: 
            bh=behaves.pop();
        else:
            with locker:            
                if l0>0:
                    bh=behaves.pop();
                else:
                    return;
        bh["target"](bh["args"]);
     
def addBehave(target,args):
    bh={"target":target,"args":args}
    locker = Lock()
    l0=len(behaves);
    if l0>3: 
        behaves.append(bh);
    else:
        with locker:            
            behaves.append(bh);
        if l0==0:
            t2=threading.Thread(target=dobehaves)
            t2.start()

def abortBehave():
    locker = Lock()
    with locker:            
        behaves=list()
def clicks(x):
    for y in x:
        click(y);sleep(1)
#clicks(locs)
if False:
    for k in range(2):
        locs=list(my.ClientRegion.findAll("1717202058362.png"));print len(locs)
        addBehave(clicks,locs);
        locs=list(my.ClientRegion.findAll("1717205864243.png"));print len(locs)
        addBehave(clicks,locs);
        locs=list(my.ClientRegion.findAll("1717205961144.png"));print len(locs)
        addBehave(clicks,locs);
        locs=list(my.ClientRegion.findAll("1717206549560.png"));print len(locs)
        addBehave(clicks,locs);
        rg=Region(my.ClientRegion.x+my.ClientRegion.w/3,my.ClientRegion.y+my.ClientRegion.h/4,my.ClientRegion.w/3,my.ClientRegion.h/4)
        try:
            rg.find(Pattern("1717206897958.png").similar(0.67))
            abortBehave();
            click(Location(my.ClientRegion.x+my.ClientRegion.w/4,my.ClientRegion.y+my.ClientRegion.h/4));sleep(0.4)
        except:
            pass;
        sleep(3)
        sleep(10)

if False:
    t1 = threading.Thread(target=clicks,args=(locs,))
    t1.start()
    #t2.start()
    t1.join()
    #t2.join()

my.idpoppy=0
my.Blocked={Main:False,Fir:False,Terrarium:False,Oceanside:False,Aquarium:False,Kujali:False};
print stayTime
stayTime[Main]=22
stayTime[Oceanside]=1
my.friend_active =True;print my_friends()
print my_run(mine_unknown,datetime.timedelta(hours=49),55555)
#print my.friend_active #7730->
print my.ClientRegion
#MISSING "1710628275582.png"
print my_clear_feed()
#print my_zoo();
#print my_many_star()
#top 1 "1718192057868.png"
#894 init
if False: #buy easter egg
  for i in range(70):
    click(findAny("1711253199163.png","1719108402847.png","1726084177266.png","1730237918061.png","1734387245291.png","1719355134173.png","1726085425097.png","1730238568696.png")[0]);    sleep(1)
    click(findAny(Pattern("1670669685882.png").similar(0.47),"1719108468733.png")[0]);    sleep(2)#to shop
#    click(findAny("1670669771737.png","1719108506525.png")[0]);    sleep(1)#arrow down
    
    loc=findAny(Pattern("1707839356315.png",).targetOffset(75,-9)
            ,Pattern("1726084514688.png").similar(0.60).targetOffset(-185,-49),Pattern("1730237999723.png").similar(0.69).targetOffset(89,-77),Pattern("1734387299906.png").similar(0.66).targetOffset(-171,207)
            ,"1711253241702.png"
            ,Pattern("1719355216503.png").similar(0.42).targetOffset(93,30)
            ,Pattern("1719606372507.png").similar(0.51).targetOffset(75,37)
            ,Pattern("1726085568390.png").similar(0.63).targetOffset(-9,-29),Pattern("1726346535166.png").similar(0.63).targetOffset(57,-110),Pattern("1727258356362.png").similar(0.67)
            ,Pattern("1730238634348.png").similar(0.68).targetOffset(61,87))[0];
    drag(findAny("1711253259826.png","1719108566225.png","1726084270086.png","1730237979236.png",Pattern("1734387352138.png").targetOffset(0,-77)
    ,findAny("1719355240773.png","1726085644677.png","1730238682162.png")[0]);    sleep(2)    
    dropAt(loc);sleep(2)
    
    click(findAny("1670669969525.png","1719108961803.png")[0]);    sleep(7) #check yes
    click(findAny("1711253305562.png","1719108625026.png","1726084364607.png","1730238078340.png","1734387433423.png")[0]);    sleep(2)    #poppy - snowflake    
    click(findAny(Pattern("1719108646459.png").similar(0.61),Pattern("1726084385926.png").similar(0.54),Pattern("1730238101525.png").similar(0.66).targetOffset(16,-12),Pattern("1734387486665.png").similar(0.64))[0]);    sleep(2) #object in field
    click(findAny("1670670246915.png",Pattern("1719108676400.png").similar(0.55))[0]);    sleep(1)    #hand out
    click(findAny("1670670333091.png","1702826720460.png","1719108707927.png")[0]);    sleep(2);#Yes
    click(findAny(Pattern("1670670387139.png").similar(0.67),"1719108739794.png")[0]);    sleep(6); #sell
#fail from numpy import random    
def ob0():
    rg=Region(Screen().x,Screen().y+Screen().h-30,Screen().w,30);
    taskicon=rg.find("1733027409639.png");#"1733020213238.png"
    
obs=[ob0];

def REM(lt):
    tot=datetime.datetime.now()+lt;
    now=datetime.datetime.now();
    while now<tot:
        now1=now;
        obs[0]();
        now=datetime.datetime.now();
        tt=now1-now;
        obs.push([f,tt]);
    
if False:
    def changed(event):
            print "something changed in ", event.region
            for ch in event.changes:
                    ch.highlight() # highlight all changes
            sleep(1)
            for ch in event.changes:
                    ch.highlight() # turn off the highlights
    r=selectRegion("select a region to observe")
        # any change in r larger than 50 pixels would trigger the changed function
    r.onChange(10, changed)
    r.observe(True)
    sleep(30) 
    
#    r.stopObserver()

    rg=selectRegion("select a region to observe")
    sc=rg.getScreen()
    #rg=sc.getCenter().grow(20)
#    print rg
    for i in range(300): 
        r=math.sqrt(-math.log(random.random()))*(sc.w+sc.h)/30
        th=random.random()*3.1415927/2.0
        w=int(math.cos(th)*r)
    #    h=random.randint(0, sc.h)
        h=int(math.sin(th)*r)
    #    print w,h
    #    print random.poisson(lam=1.0, size=None)
        rg=Region(random.randint(0, sc.w-w)+sc.x,random.randint(0, sc.h-h)+sc.y,w,h)
        img=sc.capture(rg)
        sleep(0.5)
        rgc=rg.getCenter()
        try:
            loc=rg.grow(rg.w*4).find(img)
            lcc=loc.getCenter()
            if rgc.x!=lcc.x:
                Region(rgc.x,rgc.y,lcc.x-rgc.x,lcc.y-rgc.y).highlight(0.1)
        except:        
            rg.highlight(0.1);

#The upper incomplete function: 
#Γ(s,x)= EXP(GAMMALN(s))*(1-GAMMA.DIST(x,s,1,TRUE))
#fail from sympy import erfinv

#highlands to remove "1726943480151.png" level 52
goal=["1727483952239.png", "1727484044529.png"]

breedorder=["1727737763548.png" #tbd , new specicy, (level<3 included), requres level 2, <4% not involved, not odd
       , "1727737904915.png" #new specicy, requres level 3? , rest
      ,"1727738013308.png" # 20%, level 4 ,must (brown) avoid(6), requres level 2?, 
     , "1727738069224.png" #level 8, requres level 2?, rest
        ,"1727738442458.png" #level 3, 24%, requres level 3 , rest
        ,"1727738577830.png" #level 1?, 16%, requres level 3
        ,"1727738683024.png" #level 10, 10% , requres level 2
         #level 4  , 5% , was fail same level tbd
      ];

print len(locals())

for obj in locals() :
    print sys.getsizeof(obj),obj
#import tracemalloc

print dir(setBottomRight)
print dir(Orig_XsFir)
print dir(JRegion.BOTTOM.conjugate)
print dir(my_GrownUp.func_code.co_varnames.count)
print (my_poo_find_gtx1060.func_name)
print (my_poo_find_gtx1060.func_dict)


#  File "C:\Users\Public\Documents\trump2024.charlotte.sikuli\trump2024.py", line 3995, in select_animal
#    zpx=zp[0][1]+coks[0].w/2;

#polar bear 18% "1711754523344.png"

#"1715035567925.png" what is crypto...?
#protect diamond , was 172 on 7/14, now 72 7/16 for trump2024
#white zwbra "1726377776556.png"
breedorder=["1727753999631.png"#level 5,requires 1, 
        ]
#tbd "1730632316575.png"
def observ():
    pass;