#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import csv
from fractions import Fraction


# In[2]:


def import_data_xsz(filename):
    import csv
    a=[]
    s=[]
    r=[]
    with open(filename) as data:
        data_reader=csv.reader(data)
        for i,column in enumerate(data_reader):
            if i>=8:
                column=list(map(float, column ))
                column=np.array(column)
                column= np.around(column)
                s.append(column[[8,10,21]])   
                a.append(column[[13,27,38]])
                if column[5]==0:
                    column[5]=1
                    r.append(column[[5,8]])
                else:
                    r.append(column[[5,8]])
    return a,s,r

def import_data_sf(filename):
    import csv
    a=[]
    s=[]
    r=[]
    with open(filename) as data:
        data_reader=csv.reader(data)
        for i,column in enumerate(data_reader):
            if i>=8:
                column=list(map(float, column ))
                column=np.array(column)
                column= np.around(column)
                s.append(column[[8,10,20]])   
                a.append(column[[13,26,30]])
                if column[5]==0:
                    column[5]=1
                    r.append(column[[5,8]])
                else:
                    r.append(column[[5,8]])
    return a,s,r

# In[3]:


def import_datas_sf(star_number,end_number,address=r'C:\Users\huang\Desktop\强化学习装载机\DSZ_MANA\20170314_ZL50CN_ZHP_DSZ_MANA_030',address1=r'C:\Users\huang\Desktop\强化学习装载机\DSZ_MANA\20170314_ZL50CN_ZHP_DSZ_MANA_03',):#导入所有Excel数据并储存在列表A,S,R_oil,R_all
    A=[]
    S=[]
    R=[]
    for i in range(star_number,end_number):
        a=[]
        s=[]
        r=[]
        try:
            filename=address+str(i)+'.csv'
            a,s,r=import_data_sf(filename)
        except:
            filename=address1+str(i)+'.csv'
            a,s,r=import_data_sf(filename)
                
        S.append(s)
        A.append(a)
        R.append(r)
    return A,S,R


def import_datas_xsz(star_number,end_number,address=r'C:\Users\huang\Desktop\强化学习装载机\DSZ_MANA\20170314_ZL50CN_ZHP_DSZ_MANA_030',address1=r'C:\Users\huang\Desktop\强化学习装载机\DSZ_MANA\20170314_ZL50CN_ZHP_DSZ_MANA_03',):#导入所有Excel数据并储存在列表A,S,R_oil,R_all
    A=[]
    S=[]
    R=[]
    for i in range(star_number,end_number):
        a=[]
        s=[]
        r=[]
        try:
            filename=address+str(i)+'.csv'
            a,s,r=import_data_xsz(filename)
        except:
            filename=address1+str(i)+'.csv'
            a,s,r=import_data_xsz(filename)
        S.append(s)
        A.append(a)
        R.append(r)
    return A,S,R

def text_save(filename, data):
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')
        s = s.replace("'",'').replace(',','') +'\n'   
        file.write(s)
    file.close()
    print("save files successful")
# In[4]:


def set_dict_keys(*m):
    try:
        m=m[0].tolist()
        M=list(map(str,m))
        return "_".join(M)
    except:
        return str(m)


# In[5]:


def set_dict(target_dict,key,value):
    target_dict[key]=value


# In[6]:


def set_dict_keyname(*m):
    M=[set_dict_keys(i) for i in m]
    dict_name="->".join(M)
    return dict_name    


def set_number_s(S):
    number_s={}
    for state in S:
        for i,state_1 in enumerate(state):
            if i<len(state)-1:
                dict_name=set_dict_keyname(state_1)
                try:
                    set_dict(number_s,dict_name,number_s[dict_name]+1)
                except:
                    set_dict(number_s,dict_name,1)
    return number_s

def set_number_s_s(S,n):
    number_s_s={}
    for state in S:
        for i,state_1 in enumerate(state):
            if i<len(state)-1:
                state_2=state[i+1]
                dict_name=set_dict_keyname(state_1[n],state_2[n])
                try:
                    set_dict(number_s_s,dict_name,number_s_s[dict_name]+1)
                except:
                    set_dict(number_s_s,dict_name,1)
    return number_s_s
# In[7]:


def set_number_s_a(S,A):
    number_s_a={}
    for state,action in zip(S,A):
        for i,(state_1,action_1) in enumerate(zip(state,action)):
            if i<len(state)-1:
                dict_name=set_dict_keyname(state_1,action_1)
                try:
                    set_dict(number_s_a,dict_name,number_s_a[dict_name]+1)
                except:
                    set_dict(number_s_a,dict_name,1)
    return number_s_a


# In[8]:


def set_TPM_s_a_s(S,A,number_s_a):
    TPM={}
    for state,action in zip(S,A):
        for i,(state_1,action_1) in enumerate(zip(state,action)):
            if i<len(state)-1:
                dict_name_2=set_dict_keyname(state_1,action_1)
                dict_name_3=set_dict_keyname(state_1,action_1,state[i+1])
                try:
                    set_dict(TPM,dict_name_3,TPM[dict_name_3]+Fraction(1,number_s_a[dict_name_2]))
                except:
                    set_dict(TPM,dict_name_3,Fraction(1,number_s_a[dict_name_2]))
    return TPM


# In[9]:


def set_number_s_a_s(S,A,s_a_s=1):
    number_s_a={}
    for state,action in zip(S,A):
        for i,(state_1,action_1) in enumerate(zip(state,action)):
            if i<len(state)-1:
                if s_a_s:
                    dict_name=set_dict_keyname(state_1,action_1,state[i+1])
                else:
                    dict_name=set_dict_keyname(state_1,action_1)
                try:
                    set_dict(number_s_a,dict_name,number_s_a[dict_name]+1)
                except:
                    set_dict(number_s_a,dict_name,1)
    return number_s_a


# In[10]:


def get_reward(S,A,R,number_s_a_s):
    Reward={}
    for state,action,reward in zip(S,A,R):
        for i,(state_1,action_1,reward_1) in enumerate(zip(state,action,reward)):
            if i<len(state)-1:
                dict_name=set_dict_keyname(state_1,action_1,state[i+1])
                try:
                    set_dict(Reward,dict_name,Reward[dict_name]+Fraction(reward[i+1],number_s_a_s[dict_name]))
                except:
                    set_dict(Reward,dict_name,Fraction(Fraction(reward[i+1]),number_s_a_s[dict_name]))


# In[11]:


def set_P_s_a_s_r(S,A,R,number_s_a):
    P_s_a_s_r={}
    for state,action,reward in zip(S,A,R):
        for i,(state_1,action_1,reward_1) in enumerate(zip(state,action,reward)):
            if i<len(state)-1: 
                dict_name_2=set_dict_keyname(state_1,action_1)
                dict_name_3=set_dict_keyname(state_1,action_1,state[i+1],reward[i+1])
                try:
                    set_dict(P_s_a_s_r,dict_name_3,P_s_a_s_r[dict_name_3]+Fraction(1,number_s_a[dict_name_2]))
                except:
                    set_dict(P_s_a_s_r,dict_name_3,Fraction(1,number_s_a[dict_name_2]))
    return P_s_a_s_r


# In[5]:


def set_p_state_action_state_reward(P_s_a_s_r):
    p_state_action_state_reward={}
    for key,v in P_s_a_s_r.items():
        keyy=key.split('->')
        name_s_a='->'.join(keyy[0:2])
        name_s_r='->'.join(keyy[2:])
        p={}
        try:
            set_dict(p_state_action_state_reward[name_s_a],name_s_r,v)
        except:
            set_dict(p,name_s_r,v)
            set_dict(p_state_action_state_reward,name_s_a,p)
    return p_state_action_state_reward


# In[6]:


def initialize_Q(number_s_a):
    Q={}
    for key in number_s_a.keys():
        keyy=key.split('->')
        name_s=str(keyy[0])
        name_a=str(keyy[1])
        p={}
        try:
            set_dict(Q[name_s],name_a,0)
        except:
            set_dict(p,name_a,0)
            set_dict(Q,name_s,p)
    return Q


# In[7]:


def epsilon_greedy_police(Q,state,epsilon):
    n=len(Q[state])
    a=max(Q[state],key=Q[state].get)
    action=[key for key in Q[state].keys() if key!=a]
    action.append(a)
    p=[epsilon/n]*n
    p[-1]=1-epsilon+epsilon/n
    return (np.random.choice(action,p=p))


# In[2]:


def step(p_state_action_state_reward,*m):
    key_name='->'.join(m)
    probs=[v for v in p_state_action_state_reward[key_name].values()]
    state_reward=[key for key in p_state_action_state_reward[key_name].keys()]
    next_state_reward=np.random.choice(state_reward,p=probs)
    next_state=next_state_reward.split('->')[0]
    reward=next_state_reward.split('->')[1]
    return next_state,reward


# In[4]:


def update_Q(p_state_action_state_reward,state,Q,alpha,gamma,epsilon):
    for i in range(1000):
        action=epsilon_greedy_police(Q,state,epsilon)
        next_state,reward=step(p_state_action_state_reward,state,action)
        next_value=max(Q[next_state].values())
        Q[state][action]*=1-alpha
        Q[state][action]+=alpha*(float(reward)+gamma*next_value)
        state=next_state
    return Q


# In[ ]:


def generate_one_episode_update_Q(p_state_action_state_reward,\
state,Q,alpha,gamma,epsilon,t=0,t_end=6):
    R=0
    R_fuel=0
    R_weight=0
    while t<=t_end:
        action=epsilon_greedy_police(Q,state,epsilon)
        if t<t_end:
            next_state,reward=step(p_state_action_state_reward,state,action)
            r_fuel=reward.split('_')[0]
            r_fuel=-float(r_fuel)
            r_weight=reward.split('_')[1]
            r_weight=float(r_weight)
            reward=0.1*r_fuel+0.2*r_weight
            next_value=max(Q[next_state].values())
        else:
            next_state,reward=step(p_state_action_state_reward,state,action)
            r_fuel=reward.split('_')[0]
            r_fuel=-float(r_fuel)
            r_weight=reward.split('_')[1]
            r_weight=float(r_weight)
            reward=0.1*r_fuel+0.2*r_weight
            next_value=0
        R+=reward
        R_fuel+=0.1*r_fuel
        R_weight+=0.2*r_weight
        Q[state][action]*=1-alpha
        Q[state][action]+=alpha*(reward+gamma*next_value)
        
        state=next_state
        t+=0.005
    return Q,R,R_fuel,R_weight

def initialize_Q_transfer(Q,number_s_a):
    Q_transfer={}
    for key in number_s_a.keys():
        keyy=key.split('->')
        name_s=str(keyy[0])
        name_a=str(keyy[1])
        p={}
        try:
            set_dict(Q_transfer[name_s],name_a,Q[name_s][name_a])
        except: 
            try:
                set_dict(Q_transfer[name_s],name_a,0)
            except:
                set_dict(p,name_a,0)
                set_dict(Q_transfer,name_s,p)
    return Q_transfer
