from utils import import_data_sf,import_datas_sf,import_data_xsz,import_datas_xsz,set_dict_keys,set_dict,set_dict_keyname,set_number_s_a,set_TPM_s_a_s,step,update_Q,initialize_Q_transfer
import numpy as np
from tqdm import tqdm
from utils import set_number_s_a_s,get_reward,set_P_s_a_s_r,set_p_state_action_state_reward,epsilon_greedy_police,initialize_Q,generate_one_episode_update_Q
A,S,R=import_datas_xsz(1,53,address=r'C:\Users\Administrator\Desktop\XSZ_MANA3\20170306_ZL50CN_ZHP_XSZ_MANA_02_out0',address1=r'C:\Users\Administrator\Desktop\XSZ_MANA3\20170306_ZL50CN_ZHP_XSZ_MANA_02_out')
number_s_a=set_number_s_a(S,A)
TPM=set_TPM_s_a_s(S,A,number_s_a)
number_s_a_s=set_number_s_a_s(S,A,s_a_s=1)
number_s_a=set_number_s_a_s(S,A,s_a_s=0)
P_s_a_s_r=set_P_s_a_s_r(S,A,R,number_s_a)
p_state_action_state_reward=set_p_state_action_state_reward(P_s_a_s_r)
Q=initialize_Q(number_s_a)


RRR=[]
reward_fuel_x=[]
reward_weight_x=[]
init_state=[]
for i in tqdm(range(2000)):
    try:
        state=np.random.choice(init_state)
        Q,r,fuel,weight=generate_one_episode_update_Q(p_state_action_state_reward,state,Q,alpha=0.15,gamma=0.9,epsilon=0.1,t=0,t_end=3.7)
        RRR.append(r)
        reward_fuel_x.append(fuel)
        reward_weight_x.append(weight)
    except:
        state=np.random.choice(init_state)
        Q,r,fuel,weight=generate_one_episode_update_Q(p_state_action_state_reward,state,Q,alpha=0.15,gamma=0.9,epsilon=0.1,t=0,t_end=3.7)
        RRR.append(r)
        reward_fuel_x.append(fuel)
        reward_weight_x.append(weight)
	
	
import matplotlib.pyplot as plt
plt.plot(np.around(RRR,1))
plt.show() 
plt.plot(np.around(reward_weight_x,1))
plt.show() 
plt.plot(np.around(reward_fuel_x,1))
plt.show()
