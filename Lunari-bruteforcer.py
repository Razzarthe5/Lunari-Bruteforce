import tkinter as tk #line:1
from tkinter import filedialog ,messagebox #line:2
import threading #line:3
import time #line:4
import ctypes #line:5
import os #line:6
user32 =ctypes .WinDLL ('user32',use_last_error =True )#line:9
VK_RETURN =0x0D #line:10
SPEEDS ={'Slow':1.0 ,'Medium':0.3 ,'Fast':0.05 }#line:17
LOGO =r'''
╦  ┬ ┬┌┐┌┌─┐┬─┐┬       ╔╗ ╦═╗╦ ╦╔╦╗╔═╗╔═╗╔═╗╦═╗╔═╗╔═╗
║  │ ││││├─┤├┬┘│  ───  ╠╩╗╠╦╝║ ║ ║ ║╣ ╠╣ ║ ║╠╦╝║  ║╣ 
╩═╝└─┘┘└┘┴ ┴┴└─┴       ╚═╝╩╚═╚═╝ ╩ ╚═╝╚  ╚═╝╩╚═╚═╝╚═╝
'''#line:24
class PasswordBruteforcer :#line:26
    def __init__ (O00O0O0OO0O00O000 ,OOOO0OOO0O0OOOO00 ):#line:27
        O00O0O0OO0O00O000 .root =OOOO0OOO0O0OOOO00 #line:28
        O00O0O0OO0O00O000 .root .title ('Lunari 1.0.0')#line:29
        O00O0O0OO0O00O000 .root .attributes ('-topmost',True )#line:30
        O00O0O0OO0O00O000 .root .geometry ('600x400')#line:31
        O00O0O0OO0O00O000 .root .resizable (False ,False )#line:32
        O00O0O0OO0O00O000 .wordlists =[]#line:33
        O00O0O0OO0O00O000 .passwords =[]#line:34
        O00O0O0OO0O00O000 .running =False #line:35
        O00O0O0OO0O00O000 .speed =tk .StringVar (value ='Medium')#line:36
        O00O0O0OO0O00O000 .current_password =tk .StringVar (value ='')#line:37
        O00O0O0OO0O00O000 .status =tk .StringVar (value ='Stopped')#line:38
        O00O0O0OO0O00O000 .thread =None #line:39
        O00O0O0OO0O00O000 .countdown_thread =None #line:40
        O00O0O0OO0O00O000 .countdown_cancel =False #line:41
        O00O0O0OO0O00O000 .stop_window =None #line:42
        O00O0O0OO0O00O000 .password_list_window =None #line:43
        O00O0O0OO0O00O000 .password_listbox =None #line:44
        O00O0O0OO0O00O000 .setup_ui ()#line:45
        O00O0O0OO0O00O000 .root .bind_all ('<Return>',lambda OO00000O0OOOOOOO0 :O00O0O0OO0O00O000 .root .destroy ())#line:46
        O00O0O0OO0O00O000 .root .focus_force ()#line:47
    def setup_ui (OOOOO00OOOO0OOO00 ):#line:49
        OOOOO00OOOO0OOO00 .root .configure (bg ='black')#line:50
        OOOOO0OOOOOOOO0O0 =tk .Frame (OOOOO00OOOO0OOO00 .root ,bg ='black')#line:51
        OOOOO0OOOOOOOO0O0 .pack (padx =20 ,pady =20 )#line:52
        OO00OOO0OO000O0OO =tk .Label (OOOOO0OOOOOOOO0O0 ,text =LOGO ,fg ='white',bg ='black',font =('Courier New',10 ,'bold'),justify ='center')#line:55
        OO00OOO0OO000O0OO .grid (row =0 ,column =0 ,columnspan =5 ,pady =(0 ,8 ),sticky ='ew')#line:56
        OOOOOO0OO0O0O0O0O =tk .Label (OOOOO0OOOOOOOO0O0 ,text ='By Razzarthe5',fg ='white',bg ='black',font =('Courier New',10 ),justify ='center')#line:57
        OOOOOO0OO0O0O0O0O .grid (row =1 ,column =0 ,columnspan =5 ,pady =(0 ,18 ),sticky ='ew')#line:58
        tk .Button (OOOOO0OOOOOOOO0O0 ,text ='Add Wordlist(s)',command =OOOOO00OOOO0OOO00 .add_wordlists ,bg ='#222',fg ='white',activebackground ='#333',activeforeground ='white').grid (row =2 ,column =0 ,sticky ='ew',pady =(0 ,0 ))#line:60
        tk .Label (OOOOO0OOOOOOOO0O0 ,text ='Speed:',bg ='black',fg ='white').grid (row =2 ,column =1 ,padx =(10 ,0 ))#line:61
        for OOO000OO0O0O0O0OO ,O00OO0OO0OOOOOOOO in enumerate (SPEEDS .keys ()):#line:62
            tk .Radiobutton (OOOOO0OOOOOOOO0O0 ,text =O00OO0OO0OOOOOOOO ,variable =OOOOO00OOOO0OOO00 .speed ,value =O00OO0OO0OOOOOOOO ,bg ='black',fg ='white',selectcolor ='#222',activebackground ='black',activeforeground ='white').grid (row =2 ,column =2 +OOO000OO0O0O0O0OO ,padx =(0 ,8 ))#line:63
        OOOOO00OOOO0OOO00 .wordlist_info =tk .Label (OOOOO0OOOOOOOO0O0 ,text ='No wordlist selected.',bg ='black',fg ='white',font =('Courier New',10 ))#line:66
        OOOOO00OOOO0OOO00 .wordlist_info .grid (row =3 ,column =0 ,columnspan =5 ,sticky ='w',pady =(18 ,8 ))#line:67
        OOOOO00OOOO0OOO00 .password_label =tk .Label (OOOOO0OOOOOOOO0O0 ,textvariable =OOOOO00OOOO0OOO00 .current_password ,fg ='#00ffff',bg ='black',font =('Courier New',14 ,'bold'),width =30 ,anchor ='center')#line:70
        OOOOO00OOOO0OOO00 .password_label .grid (row =4 ,column =0 ,columnspan =5 ,pady =(0 ,0 ))#line:71
        tk .Label (OOOOO0OOOOOOOO0O0 ,text ='Status:',bg ='black',fg ='white').grid (row =5 ,column =0 ,sticky ='e',pady =(10 ,0 ))#line:74
        OOOOO00OOOO0OOO00 .status_label =tk .Label (OOOOO0OOOOOOOO0O0 ,textvariable =OOOOO00OOOO0OOO00 .status ,fg ='#00ff00',bg ='black',font =('Courier New',10 ,'bold'))#line:75
        OOOOO00OOOO0OOO00 .status_label .grid (row =5 ,column =1 ,sticky ='w',pady =(10 ,0 ))#line:76
        OOOOO00OOOO0OOO00 .start_button =tk .Button (OOOOO0OOOOOOOO0O0 ,text ='Start',command =OOOOO00OOOO0OOO00 .start_countdown ,bg ='#222',fg ='white',activebackground ='#333',activeforeground ='white',width =12 )#line:79
        OOOOO00OOOO0OOO00 .start_button .grid (row =6 ,column =0 ,columnspan =2 ,pady =(18 ,0 ))#line:80
        tk .Label (OOOOO0OOOOOOOO0O0 ,text ='A floating password list/stop window will appear after countdown.',bg ='black',fg ='#888').grid (row =7 ,column =0 ,columnspan =5 ,pady =(18 ,0 ),sticky ='ew')#line:81
    def add_wordlists (OOOOO0OO0000O0OO0 ):#line:83
        OO0OOO000O00OO0OO =filedialog .askopenfilenames (title ='Select Wordlist(s)',filetypes =[('Text Files','*.txt'),('All Files','*.*')])#line:84
        for OO0O0000OO00OO0O0 in OO0OOO000O00OO0OO :#line:85
            if OO0O0000OO00OO0O0 not in OOOOO0OO0000O0OO0 .wordlists :#line:86
                OOOOO0OO0000O0OO0 .wordlists .append (OO0O0000OO00OO0O0 )#line:87
        OOOOO0OO0000O0OO0 .update_wordlist_info ()#line:88
        OOOOO0OO0000O0OO0 .load_passwords ()#line:89
    def update_wordlist_info (O000OO0O0OOO0OOOO ):#line:91
        if not O000OO0O0OOO0OOOO .wordlists :#line:92
            O000OO0O0OOO0OOOO .wordlist_info .config (text ='No wordlist selected.')#line:93
        else :#line:94
            O0O0OOO0O0OO00OOO =', '.join ([os .path .basename (O0O00O0O000OOOO00 )for O0O00O0O000OOOO00 in O000OO0O0OOO0OOOO .wordlists ])#line:95
            O000OO0O0OOO0OOOO .wordlist_info .config (text =f'Selected: {O0O0OOO0O0OO00OOO} | Passwords: {len(O000OO0O0OOO0OOOO.passwords)}')#line:96
    def load_passwords (OO00000000O000O00 ):#line:98
        OO00000000O000O00 .passwords =[]#line:99
        for O0OO000OO000OOO00 in OO00000000O000O00 .wordlists :#line:100
            try :#line:101
                with open (O0OO000OO000OOO00 ,'r',encoding ='utf-8',errors ='ignore')as OO0OOO0O0OO0OOO0O :#line:102
                    OO00000000O000O00 .passwords .extend ([OOOO0O00000OOOO0O .strip ()for OOOO0O00000OOOO0O in OO0OOO0O0OO0OOO0O if OOOO0O00000OOOO0O .strip ()])#line:103
            except Exception as OO000O00O00O0OO00 :#line:104
                messagebox .showwarning ('Wordlist Error',f'Could not read {O0OO000OO000OOO00}: {OO000O00O00O0OO00}')#line:105
        OO00000000O000O00 .update_wordlist_info ()#line:106
        if not OO00000000O000O00 .passwords :#line:107
            OO00000000O000O00 .status .set ('No passwords loaded')#line:108
        else :#line:109
            OO00000000O000O00 .status .set ('Ready')#line:110
    def start_countdown (OOO000OOO000000OO ):#line:112
        if OOO000OOO000000OO .running or OOO000OOO000000OO .countdown_thread :#line:113
            return #line:114
        if not OOO000OOO000000OO .passwords :#line:115
            messagebox .showerror ('No Wordlist','No passwords loaded. Please add at least one wordlist.')#line:116
            return #line:117
        OOO000OOO000000OO .countdown_cancel =False #line:118
        OOO000OOO000000OO .start_button .config (state ='disabled')#line:119
        OOO000OOO000000OO .countdown_thread =threading .Thread (target =OOO000OOO000000OO ._countdown_and_start ,daemon =True )#line:120
        OOO000OOO000000OO .countdown_thread .start ()#line:121
    def _countdown_and_start (O0OO00O000OO0OO0O ):#line:123
        for OOOOO0O00OO00O000 in range (5 ,0 ,-1 ):#line:124
            if O0OO00O000OO0OO0O .countdown_cancel :#line:125
                O0OO00O000OO0OO0O ._reset_start_button ()#line:126
                return #line:127
            O0OO00O000OO0OO0O .start_button .config (text =f'Starting in {OOOOO0O00OO00O000}...')#line:128
            time .sleep (1 )#line:129
        O0OO00O000OO0OO0O .start_button .config (text ='Start')#line:130
        O0OO00O000OO0OO0O .countdown_thread =None #line:131
        O0OO00O000OO0OO0O .root .after (0 ,O0OO00O000OO0OO0O ._minimize_and_start )#line:132
    def _minimize_and_start (O000OOOOO00OOO000 ):#line:134
        O000OOOOO00OOO000 .root .iconify ()#line:135
        O000OOOOO00OOO000 ._show_password_list_window ()#line:136
        O000OOOOO00OOO000 .start_bruteforce ()#line:137
    def _show_password_list_window (O0O0O00OOOOOO0000 ):#line:139
        if O0O0O00OOOOOO0000 .password_list_window is not None :#line:140
            return #line:141
        O0O0O00OOOOOO0000 .password_list_window =tk .Toplevel ()#line:142
        O0O0O00OOOOOO0000 .password_list_window .title ('Bruteforce Progress')#line:143
        O0O0O00OOOOOO0000 .password_list_window .geometry ('350x400+100+100')#line:144
        O0O0O00OOOOOO0000 .password_list_window .attributes ('-topmost',True )#line:145
        O0O0O00OOOOOO0000 .password_list_window .configure (bg ='black')#line:146
        tk .Label (O0O0O00OOOOOO0000 .password_list_window ,text ='Bruteforce Running',fg ='white',bg ='black',font =('Courier New',10 )).pack (pady =(16 ,0 ))#line:147
        O0O0O00OOOOOO0000 .password_listbox =tk .Listbox (O0O0O00OOOOOO0000 .password_list_window ,width =40 ,height =15 ,bg ='#111',fg ='white',font =('Courier New',10 ),selectbackground ='#00ffff',selectforeground ='black')#line:148
        O0O0O00OOOOOO0000 .password_listbox .pack (pady =(10 ,10 ))#line:149
        for O00O0OOOO0OOO0000 in O0O0O00OOOOOO0000 .passwords :#line:150
            O0O0O00OOOOOO0000 .password_listbox .insert (tk .END ,O00O0OOOO0OOO0000 )#line:151
        O0O0O00OOOOOO0000 .password_listbox .selection_clear (0 ,tk .END )#line:152
        O0OOOOO0O000OO0O0 =tk .Button (O0O0O00OOOOOO0000 .password_list_window ,text ='STOP',command =O0O0O00OOOOOO0000 .stop_bruteforce ,bg ='#a00',fg ='white',font =('Courier New',12 ,'bold'),width =10 )#line:153
        O0OOOOO0O000OO0O0 .pack (pady =(10 ,16 ))#line:154
        O0O0O00OOOOOO0000 .password_list_window .protocol ('WM_DELETE_WINDOW',O0O0O00OOOOOO0000 .stop_bruteforce )#line:155
    def _close_password_list_window (OO0O000000O00O000 ):#line:157
        if OO0O000000O00O000 .password_list_window is not None :#line:158
            OO0O000000O00O000 .password_list_window .destroy ()#line:159
            OO0O000000O00O000 .password_list_window =None #line:160
            OO0O000000O00O000 .password_listbox =None #line:161
    def _reset_start_button (O0O0O000OO0OO0OO0 ):#line:163
        O0O0O000OO0OO0OO0 .start_button .config (text ='Start',state ='normal')#line:164
        O0O0O000OO0OO0OO0 .countdown_thread =None #line:165
    def start_bruteforce (O0O0OOO00O0O0OO0O ):#line:167
        if O0O0OOO00O0O0OO0O .running :#line:168
            return #line:169
        O0O0OOO00O0O0OO0O .running =True #line:170
        O0O0OOO00O0O0OO0O .status .set ('Running')#line:171
        O0O0OOO00O0O0OO0O .thread =threading .Thread (target =O0O0OOO00O0O0OO0O .bruteforce_loop ,daemon =True )#line:172
        O0O0OOO00O0O0OO0O .thread .start ()#line:173
    def stop_bruteforce (O00O0O0OO0OOO000O ,OO000OO0OOO00O0OO =None ):#line:175
        O00O0O0OO0OOO000O .countdown_cancel =True #line:176
        O00O0O0OO0OOO000O .running =False #line:177
        O00O0O0OO0OOO000O .status .set ('Stopped')#line:178
        O00O0O0OO0OOO000O ._reset_start_button ()#line:179
        O00O0O0OO0OOO000O ._close_password_list_window ()#line:180
        O00O0O0OO0OOO000O .root .deiconify ()#line:181
        O00O0O0OO0OOO000O .root .lift ()#line:182
        O00O0O0OO0OOO000O ._flash_status_label ()#line:183
    def _flash_status_label (OOOOO0000OO000OO0 ):#line:185
        O0OO0O00OOO00O000 =OOOOO0000OO000OO0 .status_label .cget ('fg')#line:186
        OOOOO0000OO000OO0 .status_label .config (fg ='red')#line:187
        OOOOO0000OO000OO0 .root .after (300 ,lambda :OOOOO0000OO000OO0 .status_label .config (fg =O0OO0O00OOO00O000 ))#line:188
    def bruteforce_loop (O0O0O000OO0O000O0 ):#line:190
        for O0000OOOOO0OOOOO0 ,O0000OO0O0000O0O0 in enumerate (O0O0O000OO0O000O0 .passwords ):#line:191
            if not O0O0O000OO0O000O0 .running :#line:192
                break #line:193
            O0O0O000OO0O000O0 .current_password .set (O0000OO0O0000O0O0 )#line:194
            O0O0O000OO0O000O0 ._highlight_password_in_list (O0000OOOOO0OOOOO0 )#line:195
            O0O0O000OO0O000O0 .type_password (O0000OO0O0000O0O0 )#line:196
            OO000000000O0OO00 =SPEEDS [O0O0O000OO0O000O0 .speed .get ()]#line:197
            for _O0O0O0O0OOOO0000O in range (int (OO000000000O0OO00 *20 )):#line:198
                if not O0O0O000OO0O000O0 .running :#line:199
                    break #line:200
                time .sleep (0.05 )#line:201
        O0O0O000OO0O000O0 .running =False #line:202
        O0O0O000OO0O000O0 .status .set ('Stopped')#line:203
        O0O0O000OO0O000O0 .current_password .set ('')#line:204
        O0O0O000OO0O000O0 ._reset_start_button ()#line:205
        O0O0O000OO0O000O0 ._close_password_list_window ()#line:206
        O0O0O000OO0O000O0 .root .deiconify ()#line:207
        O0O0O000OO0O000O0 .root .lift ()#line:208
    def _highlight_password_in_list (O0OO0O00OO000OO0O ,OO0OOOOOOOOO0OO0O ):#line:210
        if O0OO0O00OO000OO0O .password_listbox is not None :#line:211
            O0OO0O00OO000OO0O .password_listbox .selection_clear (0 ,tk .END )#line:212
            O0OO0O00OO000OO0O .password_listbox .selection_set (OO0OOOOOOOOO0OO0O )#line:213
            O0OO0O00OO000OO0O .password_listbox .see (OO0OOOOOOOOO0OO0O )#line:214
    def type_password (OO00OOO000000O0OO ,O0OOOOO0O0O0000O0 ):#line:216
        for O0OOO0O00000000OO in O0OOOOO0O0O0000O0 :#line:217
            if not OO00OOO000000O0OO .running :#line:218
                break #line:219
            OO00OOO000000O0OO .send_key (O0OOO0O00000000OO )#line:220
            time .sleep (0.02 )#line:221
        if OO00OOO000000O0OO .running :#line:222
            OO00OOO000000O0OO .send_key ('\r')#line:223
    def send_key (OO00OOOOOO0000000 ,O0OO000O00O0OOOO0 ):#line:225
        O0OO000OO0O00OOO0 =OO00OOOOOO0000000 .char_to_vk (O0OO000O00O0OOOO0 )#line:226
        if O0OO000OO0O00OOO0 :#line:227
            OO00OOOOOO0000000 .key_down (O0OO000OO0O00OOO0 )#line:228
            OO00OOOOOO0000000 .key_up (O0OO000OO0O00OOO0 )#line:229
    def char_to_vk (OO000O000O0OO00OO ,O0O0O00OO00OOOOOO ):#line:231
        if O0O0O00OO00OOOOOO =='\r':#line:232
            return VK_RETURN #line:233
        if 'A'<=O0O0O00OO00OOOOOO <='Z':#line:234
            return ord (O0O0O00OO00OOOOOO )#line:235
        if 'a'<=O0O0O00OO00OOOOOO <='z':#line:236
            return ord (O0O0O00OO00OOOOOO .upper ())#line:237
        if '0'<=O0O0O00OO00OOOOOO <='9':#line:238
            return ord (O0O0O00OO00OOOOOO )#line:239
        return None #line:240
    def key_down (O000OO0O0OO00000O ,OOO00O0OO00O000O0 ):#line:242
        user32 .keybd_event (OOO00O0OO00O000O0 ,0 ,0 ,0 )#line:243
    def key_up (OOOOO0O0000000O00 ,O0O00000O0OOO0OOO ):#line:245
        user32 .keybd_event (O0O00000O0OOO0OOO ,0 ,2 ,0 )#line:246
if __name__ =='__main__':#line:248
    root =tk .Tk ()#line:249
    app =PasswordBruteforcer (root )#line:250
    root .mainloop ()