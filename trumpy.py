import datetime;
class MakeSense:
    me={};
    OnChange={};
    inuse=[False];
    last={}
    asof={}
    def __getattr__(self,attr):
        if attr=='__str__':
            return self.me.__str__;
        t=self.me.get(attr);
        if t is not None:        
            return t;
        print "init ",attr;
        t=globals()['update_'+attr]();                
#        t=locals()['update_'+attr]();                
        if self.inuse[0]:
            if t is None:
                print 'fail init ,please run update_'+attr;
            return t;
        self.inuse[0]=True;
        t=__getattr__(self,attr);
        self.inuse[0]=False;
        return t;
    def __setattr__(self,attr,value):
        self.asof[attr]=datetime.datetime.now();
        if  self.me.get(attr) is not None :
            if self.me[attr]==value:
                return;
        print "change ",attr;
        self.me[attr]=value;
        self.last[attr]=datetime.datetime.now();
        if  self.OnChange.get(attr) is not None :
            self.OnChange[attr]();

global my;

try:
    my
    print("sure, it was defined.")
except NameError:
    print("well, it WASN'T defined after all!")
    my1=MakeSense();        
    my2=MakeSense();        
    my=my1
print my
import random;



def check():
    click("1666014112674.png");sleep(6)        
    try:
        click("1666014167890.png");sleep(6)
    except:        
        pass;
    try:    
        click("1666014276124.png");sleep(12)    
    except:        
        pass;
    try:    
        for i in range(3):
            click("1666014395459.png");sleep(12)    
    except:    
        pass;
    escape();
#check()    
def escape():                    
    try:
        click("1665268267062.png");sleep(6)
    except:
        pass;
    try:
        tap_to_continue_goods()
    except:
        pass;
    type(Key.ESC);
    sleep(1)
    try:       
       find("1662174618471.png");       
       type(Key.ESC);       
       sleep(1);    
    except:        
       pass;           

def product_no0(loc):
    try:
        loc1=loc;loc1.getTarget().grow(loc1.w/2).find(Pattern("1671723345580.png").similar(0.79))
    except:
        click(loc);sleep(4)            

def storage_full():
    try:    
        click(Pattern("1683081066475.png").targetOffset(-8,153));sleep(1);    
        return 0;
    except:
        return 999;
#storage_full()    

def close():
    click("1682979919831.png");sleep(1)
def tap_to_continue():    
    click(Pattern("1682980099873.png").similar(0.37));sleep(2)
def claim():    
    click(Pattern("1682980012154.png").similar(0.38));sleep(2)

if False:      
    try:    
        fight_arena()
    except:    
        pass;
    sleep(100)

    try:    
        try_again()
    except:    
        pass;
    fight_again();
    product()
    play_tower()
    guild_again()    
    try:    
        battle();
        type(Key.ESC);
        
        my.GapProduct=44#22
        my.in_cookie=False
        my.wheel_count=2;        
        my.next_tree_of_wishes=datetime.datetime.now()
        product()
    except:    
        pass;
    my.in_cookie=False
    my.next_tree_of_wishes=datetime.datetime.now()
    product(); 
    my.off20_tree_of_wishes=False       
    my.last_tree_of_wishes=datetime.datetime(1,1,1)                   
    try:
       for i in range(7):
           click("1682979985214.png");sleep(2);
           Train=False;
           for loc in findAll("1682987361833.png"):
               Train=True;
               click(loc);sleep(1);
           for loc in findAll(Pattern("1682987822625.png").similar(0.87)):
               Train=True;               
               click(loc);sleep(1);                          
           if Train:
               close();
               continue;
           tap_to_continue(); 
           try:
               claim();                  
               if(storage_full()==0):                      
                   type(Key.ESC);
                   print tree_of_wishes();
                   break;
                   #donot try again
               continue;
           except:
               pass;
           try:
               click("1683081529461.png");sleep(2);
           except:
               pass;
           try:               
               close()
           except:
               pass;
    except:
        pass;
    switch_to_zoo() #fail tbd
    os.system('taskkill /IM dnplayer.exe ');
    os.system('taskkill /IM LdBoxHeadless.exe');    
    os.system('taskkill /IM LdBoxSVC.exe');#may fail?
    play_zoo(60*60)
    
def product():       
    scrollDown=False;
    for i in range(2000):    
        if reset_game()==0:
            #Do.popAsk('Reset game','',344)
            yield_from_cookie(344)
            reset_job()
        try:    
            click("1666015424014.png");sleep(7)                                
            wheel(Screen(),Button.WHEEL_DOWN,my.wheel_count);    
            sleep(4)
        except:
            pass
        NoGood=True
        for j in range(5):
            try:            
                click("1666650332481.png");sleep(4)      
                NoGood=False
                break;
            except:
                pass;
            result=Do.popAsk('Expecting .., recheck now?','',8)
            print result
            if None == result:
              continue;
            if result: #True 
              continue;            
            print 'No means quit'
            return;
        if NoGood:
            continue;
        try:
            click("1666015516934.png");sleep(4)  
            if storage_full()==0:
                return 0;
        except:
            sleep(10);
            continue;
        print my.next_tree_of_wishes;
        now=datetime.datetime.now();
        my.nextLong=min(filter(lambda x:x>now,[now+ datetime.timedelta(minutes=11)
                        ,my.next_tree_of_wishes
                    #,my.last_arena+ datetime.timedelta(minutes=20)
                    ]) );
#        print my.nextLong
        print random.random()
        if random.random()<0.2:
            scrollDown=False;
        if my.nextLong>now:
            for loc in findAll(Pattern("1666708671613.png").similar(0.84).targetOffset(34,22)):
                scrollDown=True;
                try:
                    loc1=loc;loc1.getTarget().grow(loc1.w/2).find(Pattern("1671723345580-1.png").similar(0.79))
                except:
                    click(loc);sleep(4)                  
            for prd in [Pattern("1666650266263.png").similar(0.87).targetOffset(3,13),Pattern("1666708825075.png").similar(0.87).targetOffset(36,26),Pattern("1666907457700.png").similar(0.80).targetOffset(26,23)]:
                
                for loc in findAll(prd):
                    product_no0(loc);
            for loc in findAll(Pattern("1671723225640.png").similar(0.69).targetOffset(30,23)):
                scrollDown=False;
                try:
                    loc1=loc;
                    rg=loc1.getTarget().grow(loc1.w/2);
                    rg.find(Pattern("1671723345580-1.png").similar(0.79));                            
                    try:
                        rg.click(Pattern("1682989866956.png").similar(0.78));sleep(4);
                    except:
                        pass;
                except:
                    click(loc);sleep(4)                  
            sleep(1);            
            if scrollDown:                   
                wheel(Location(593, 541),Button.WHEEL_DOWN,my.wheel_count);
            else:                   
                wheel(Location(608, 501),Button.WHEEL_UP,my.wheel_count);
            sec=my.GapProduct 
            yield_from_cookie(sec)
        else:
            for loc in findAll(Pattern("1667749740366.png").similar(0.81).targetOffset(26,18)):
                click(loc);sleep(4)                  
            for loc in findAll(Pattern("1667749803947.png").similar(0.77).targetOffset(28,17)):
                click(loc);sleep(4)                  
            for loc in findAll(Pattern("1667749836132.png").similar(0.75).targetOffset(27,18)):
                click(loc);sleep(4)                  
            for loc in findAll(Pattern("1666907457700.png").similar(0.80).targetOffset(26,23)):
                click(loc);sleep(4)                  
            escape()
            cookie_long()
            escape()
    return 999;            
#product()
#print my.nextLong

def cookie_long():        
    if tree_of_wishes()==0: #to deal with 2
        return;
#    if battle()==0:#to deal with from groud
#        return;
#    if fight_arena()==0:
#        return;
    #
def cookie_lab():
    try:
        Region(my.ClientRegion.x+my.ClientRegion.w/3,my.ClientRegion.y,my.ClientRegion.w/3,my.ClientRegion.h/5).find("1665268137317.png")
        click("1665268267062-1.png")
        sleep(1)
    except:
        pass;
#cookie_lab();

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
                Do.popAsk('my_friend','20',20);
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

def update_scenario():
    if socket.gethostname()=='Inossem':
        my.scenario=inossem;
    else:
        my.scenario=gtx1060;

def my_blue_feeder():
    loc=find("1659095267480.png");
    if loc.getScore()>0.95:                                    
        type(Key.F5);
        Do.popAsk('my_blue_feeder','',3*60);
        my.need_splash=True;
                
def skipAds():
    click("1659010237092.png")
    click(Location(2684, 360));
    click(Location(2455, 286));



# explore, best set production in advance
def fight_again():
    click("1657733279787.png")#Tap to continue
    sleep(5)
    try_again()
    
def try_again():    
    for i in range(34):
        try:
        
            click("1657733139896.png")#try again ?click cannt try catch?
        except:
            break;
#        yieldy(3*60)
#        sleep(50)
        yield_from_cookie(120)
#        def wait_appear("1657733279787.png")#,40,2,5,10)
        for j in range(40):
            try:
                loc=find("1657733279787.png");
                print loc
                sleep(3);
                click(loc);
                print j;                
                sleep(4);
                break;
            except:
                pass;
            sleep(20);
#fight_again()
def guild_again():    
    for i in range(4):
        q= Region(657,26,666,266).findAny(Pattern("1672969594841.png").similar(0.80).targetOffset(49,-1))
#        print q
        if not q.isEmpty():
            loc=q[0].getTarget()
            rg=loc.grow(40)
            if not rg.findAny(Pattern("1673536924486.png").similar(0.83)).isEmpty():
                break;
        try:
            click("1672518275730.png");sleep(2);
            click("1672518315284.png");sleep(2);
        except:
            break;
        yield_from_cookie(50)
        
        wait_appear("1657733279787.png")
        click("1672518450419.png");sleep(12);
#guild_again()

def wait_appear(pic):
    for j in range(40):
        try:
            loc=find(pic);
            print loc
            sleep(3);
            click(loc);
            print j;                
            sleep(4);
            break;
        except:
            pass;
        sleep(20);

my.off20_tree_of_wishes=False
my.last_tree_of_wishes=datetime.datetime(1,1,1)
def tree_of_wishes(): #20 claim not so work
  now=datetime.datetime.now()
  if   my.off20_tree_of_wishes :
       t=my.last_tree_of_wishes
       if t.day==now.day:
           if t.hour<12 and now.hour>12:
               my.off20_tree_of_wishes=False;
           else:           
               return 999;
       elif t.day+1==now.day:
           if t.hour<12 or now.hour>12:
               my.off20_tree_of_wishes=False;
           else:           
               return 999;
       else:        
           my.off20_tree_of_wishes=False;
  my.next_tree_of_wishes=my.last_tree_of_wishes+datetime.timedelta(minutes=10)         
  if my.next_tree_of_wishes>now:
      return 999;
  my.last_tree_of_wishes=now
  try:
      click("1665487412832.png");sleep(2)
  except:
      try:
          click("1666115410365.png");sleep(2)                    
          click("1666115435888.png");sleep(3)
      except:
          pass;
  for j in range(8):
    try:
        find("1665499924337.png")
        my.off20_tree_of_wishes=True
        t=now
        t=datetime.datetime(t.year,t.month,int(t.hour>11)+t.day,11,0,0)
        print 'next_tree_of_wishes=',t
        my.next_tree_of_wishes=t
        escape()
        return;
    except:
        pass;
    try:
        click("1665495127582.png");sleep(1)#20 claim not so work
        click("1665495161240.png");sleep(1)
        tap_to_continue_goods();        
    except:
        pass;
    for k in range(3):
        for loc in findAny(Pattern("1666115771368.png").targetOffset(-80,41),Pattern("1665417386400.png").similar(0.97) ,Pattern("1665456226837.png").similar(0.95)):
            click(loc);sleep(2)
    refresh=False
    for i in range(4):
        try:
#            loc=find(Pattern("1665417524046.png").similar(0.84))
#            locs=findAny(Pattern("1665456110469.png").similar(0.86),"1667789140875.png");
            loc=findAny(Pattern("1665417524046.png").similar(0.84),Pattern("1665456110469.png").similar(0.86),"1667789140875.png")[0];

            loc=loc.grow(200); #tbd
            click(Region(loc.x,0, loc.w,loc.y).find("1665417758173.png"));sleep(3)    
            refresh=True
        except:
            pass;
    if refresh:
        continue;
    try:
        click("1665417122943.png");sleep(1)
    except:
        escape()
        break;
    sleep(4)

#tree_of_wishes()

def reset_job():
   for i in range(30):
       try:
           loc=findAny("1663094523954.png","1661259236739.png")    #Touch to Start
           click(loc)
           break;
       except:                           
           result=Do.popAsk('Waiting for Touch to Start','',18);                    
           if None == result:                      
               print 'nothing to do'
   Do.popAsk('Connecting ?','',60);                
   type(Key.ESC);
   sleep(1)
   try:       
       find("1662174618471-1.png");       
       type(Key.ESC);       
       sleep(1);    
   except:        
       pass;           
#reset_job()

def battle():
    if reset_game()==0:
        Do.popAsk('Reset game','',222)#155 not enough, no click connecting?
        reset_job()            
    try:
        click("1657737194879.png")    
        sleep(1)
        click("1665460736450.png")
        sleep(1)
        click(findAny("1665840012043.png","1665460781886.png"))
        sleep(1)
        click("1665460832094.png")
        sleep(1)
    except:
        pass;
    click("1661631507950.png")
    sleep(4*60)
    fight_again();
#    reset_jobs(); #??
#battle()


def type_Key_ESC():
    if scenario==gtx1060:
        print 'ignore Key.ESC for' #stack ?
        if random.random()<0.1:
            if my_close()==0:
                Log('found missing ESC ') #stack
            else:
                type( Key.ESC);sleep(0.07) #0.04-0.06
                if my.esc_close:
                    try:
                        my.esc_close=my.esc_close.grow(30).find("1674402319815.png");
                        click(my.esc_close);sleep(0.5)
                    except:
                        my.esc_close=False
                else:
                    try:
                        my.esc_close=find("1674402319815.png")
                        click(my.esc_close);sleep(0.5)
                    except:
                        pass;
    else:
        type( Key.ESC);sleep(0.07)
#type_Key_ESC()

def play_zoo(ts):    
    #many cancel tbd
    if scenario==gtx1060:
    	my_close();
    else:
        type( Key.ESC);
        type( Key.ESC);
        type( Key.ESC);
    sleep(1)
    try:
        find("1654141832902.png")    ;sleep(1)
        type_Key_ESC();
    except:
        pass;
    sleep(1) ;
    print my_run(mine_unknown,datetime.timedelta(seconds=ts),55555);
#play_zoo(60*60);


if False:      
    play_zoo(40)     
    my.in_cookie=False
    yield_from_cookie(100)
    fight_again();
    print cookie_produce()        
    battle();
    click('kindom')
    sleep(30)
    my.next_tree_of_wishes=now
    my.in_cookie=False
    product()      
    
def switch_to_zoo():
    try:
        loc=find("1662678940466.png")
        print loc
    except:
        print 'no zoo window'
        return 999;
    try:
        loc2=find("1662679089252.png")
        print loc2
        click(loc)
        sleep(1)
    except:
        pass;
    return 0;
#print switch_to_zoo()
def switch_to_cookie():
    try:
        loc=find("1662679322546.png")
        print loc
    except:
        print 'no cookie window'
        return 999;
    try:
        loc2=find("1662679089252.png")
        print loc2
    except:
        click(loc)
        sleep(1)
    return 0;
#print switch_to_cookie()


def yield_from_cookie(ts):
    if my.in_cookie:
        Do.popAsk('yield_from_cookie in_cookie all ready',ts)
        return 999;
    my.in_cookie=True
    t0=datetime.datetime.now()
    if switch_to_zoo()==0:
        play_zoo(ts)
        switch_to_cookie()
    dt=(datetime.datetime.now()-t0).total_seconds()
    dt=int(ts-dt)
    if dt>0:
        Do.popAsk('switch_to_zoo glitch, wait {T}'.format(T=dt),dt)
    my.in_cookie=False
    return 0;
#yield_from_cookie(30)


def yield_from_zoo(ts):
    if my.in_zoo:
        return 999;
    my.in_zoo=True
    switch_to_cookie()
    play_cookie(ts)
    switch_to_zoo()
    my.in_zoo=False

    

def reset_game():
   try:
       click(findAny("1678928540541.png","1674282754719.png")[0]);#2nd Aniv
       return 0;
   except:
       return 999;


def reset_job():
   loc=Location(946, 843)
   for i in range(5):
       try:
           locs=findAny("1663094523954.png","1661259236739.png")    #Touch to Start
           if len(locs)>0:
               loc=locs[0];
               break;
       except:
           pass;
       result=Do.popAsk('Waiting for Touch to Start','',4);                    
   click(loc)#did but not effect?
   result=Do.popAsk('Waiting for Touch twice','',28);                    
   click(loc)#did but not effect?
   yield_from_cookie(220)            
#   Do.popAsk('Connecting ?','',220);                
   escape()
       
#reset_job()

def is_in_map():
   try:
       my.play=find("1662081077750.png")#play 
       return True;
   except:
       return False;
#print is_in_map()
    
def reset_cookie():    
    for i in range(20):              
       try:       
           find("1662174618471-1.png");       
           type(Key.ESC);       
           sleep(1);                     
           continue;
       except:             
           pass;                   
       if is_in_map():
           break;        
       type(Key.ESC);               
       sleep(10)

def play_cookie(ts):
    reset_cookie()
    print cookie_produce()        
    battle();
       
#print play_cookie(10)

def castle():
    for i in range(2):
        if i>0:
            if play_cookie()!=0:
                return 999;
        try:
            click("1662082005228.png")
            sleep(1)
            return 0;
        except:
            pass;
       
#tbd  castle()    
import datetime;

def fight_arena():
    now=datetime.datetime.now()
    if my.last_arena+ datetime.timedelta(minutes=20)>now:
        print 'you fighted no less than 20 miuntes ago. no more'
        return
    my.last_arena=now
    if reset_game()==0:
        Do.popAsk('Reset game','',88)
        reset_job()
    try:
        click("1657737194879.png")    
        sleep(2)
        drag(Location(Screen().w*3/4,Screen().h/2))
        sleep(1)
        dropAt(Location(Screen().w*1/4,Screen().h/2))
        sleep(1)
        click(findAny("1665521594524.png","1666131077554.png"))
        sleep(4)
        click("1666131127702.png");                sleep(4)
    except:
        pass;
    for i in range(4):
        locs=findAny("1665580520017.png","1666147048549.png","1666147059666.png","1666147078124.png")
#        locs=findAny("1665580520017.png")
        for loc in locs:
            print loc
            if loc.getScore()>0.92:
                locw=25 #middle 
                rg=Region(loc.x,loc.y-21/4,locw*14/6,loc.h+10)
                try:
                    n1=rg.find("1665582787351.png")
                    if n1.getScore()>0.92:
                        continue;
                    #print 'n1',n1 
                except:    
                    pass;
                #print loc
                rg=Region(loc.x+locw*11/6,loc.y-5,locw*6/6,loc.h+10)
                nums=list(rg.findAny("1665580662651.png","1665581238874.png","1665582624250.png","1665583843047.png"))
                print nums
                nums=filter(lambda x:x.getScore()>0.83,nums) 
                #print nums #0.82?
                if len(nums)<=0:
                    continue;
                click(nums[0])
                
                rg=Region(loc.x+100,loc.y-80,500,200)
                #print rg
                try:
                    loc=rg.find("1665521756283.png")
                    print loc
                    click(loc);sleep(1)
                    click("1661631507950.png");
                    Do.popAsk('Battle! ... ','',2*60)
                    click(Location(1048, 875));sleep(1)
                    click("1665582060405.png");sleep(12)
                    break;
                except:
                    pass;
        if i==2:
            try:
                click("1666131800112.png")
                sleep(1)
                i=0;
                continue;
            except:
                break;
        for k in range(3):
            wheel(Screen(),Button.WHEEL_DOWN,2);    
            sleep(2)
    escape()            
#my.last_arena=datetime.datetime(1,1,1);fight_arena() 
            
        
    
def enter_fight_bounty():
    try:
        play();
    except:
        pass;
    try:
        scroll_left()
    except:
        pass;
    loc=find("1666132272557.png");
    print loc
    sleep(1);
    try:
        loc1=loc.find("1662081285348.png");
        if loc1.getScore()>0.9: #0.8mess
            print '0 bounties left',loc1
            my.bounties=0;
            return 888;
    except:
        pass;
    click(loc)
    sleep(3);
    my.bounties=3;##?
    click("1661096053061.png");
    sleep(1);
    try:
        click("1661096094711.png");#Lv.12 Enemy Defeated
        sleep(1);
    except:
        pass;
    try:
        click("1661096094711.png");#Lv.11 Enemy Defeated
        sleep(1);
    except:
        pass;
    click("1661096121527.png");
    sleep(1);
    click("1661096152110.png");


def fight_bounty():
    play2try(repeat_fight_bounty,enter_fight_bounty)
    
def repeat_fight_bounty():
    for i in range(2):
        sleep(5); #to allow switch yield
        for j in range(17):
            try:
                click("1657733279787.png")#Tap to continue
                sleep(2)     
                break;
            except:
                sleep(10);
        try:
            click("1661096647328.png")
            sleep(2)
        except:
            break;
    click("1665120070567.png")            
    Do.popAsk('Loading ... done?','',142)
    type(Key.ESC);sleep(0.4)
    return 0;
    
#print fight_bounty()
