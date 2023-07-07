import random,string,time,re,sys,os
from concurrent.futures import ThreadPoolExecutor as tdp
try:
    import requests as r
    from bs4 import BeautifulSoup as bs
except:
    os.system("clear")
logo = ("""                   
    \033[0;31m╔╦╗╦ ╦╔═╗  \033[0;37m╔╦╗╔═╗╔═╗╦╔═  \033[0;34m╔╦╗╔═╗╔╗╔
     \033[0;31m║ ╠═╣║╣   \033[0;37m║║║╠═╣╚═╗╠╩╗  \033[0;34m║║║╠═╣║║║
     \033[0;31m╩ ╩ ╩╚═╝  \033[0;37m╩ ╩╩ ╩╚═╝╩ ╩  \033[0;34m╩ ╩╩ ╩╝╚╝
\x1b[1;90m══════════════════════════════════════════""")
uids=[]
n=0
c=0
os.system('clear')
print(logo)
file=input("\x1b[1;91m[\x1b[1;97m+\x1b[1;91m] \x1b[1;97mCHOSE THE PATH: ")
try:
    open(file,"r").read()
except Exception as e:
  print('\x1b[1;97mNO LOCATION FOUND!')
def s(code):
    ln=15-len(code)
    lim=int("9"*(ln))+1
    for i in range(lim):
        uids.append(code+str(i).zfill(ln))

def gen(code,tt):
    os.system('clear')
    print(logo)
    print('\x1b[1;97mPRESS [1] TO START THE PROCESS')
    nas=int(input("\x1b[1;91m[\x1b[1;97m+\x1b[1;91m] \x1b[1;97mINPUT: "))
    if nas==2:
        s(code)
    else:
        for i in range(tt):
            uids.append(code+''.join(random.choice(string.digits) for _ in range(
        15-len(code)
        )))
        
def geno(code,l,tt):
    for i in range(tt):
        uids.append(code+''.join(random.choice(string.digits) for _ in range(
        l-len(code)
        )))

ugen=['Dalvik/2.1.0 (Linux; U; Android 7.1.1; GIONEE S10C Build/NMF26F)', 'Dalvik/2.1.0 (Linux; U; Android 6.0; R17S Build/MRA58K)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; vivo 1908_19 Build/O11019)', 'Dalvik/2.1.0 (Linux; U; Android 10; SM-G950F Build/QQ3A.200905.001)', 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G600S Build/MMB29M)', 'Dalvik/2.1.0 (Linux; U; Android 5.1; Micromax Q346 Build/LMY47D)', 'Dalvik/2.1.0 (Linux; U; Android 5.0.2; C6902 Build/14.5.A.0.242)', 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; SM-A7108 Build/NMF26X)', 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; SM-C9000 Build/NMF26X)', 'Dalvik/1.6.0 (Linux; U; Android 4.3; SM-G7109 Build/JLS36C)', 'Dalvik/2.1.0 (Linux; U; Android 6.0; Infinix X510 Build/MRA58K)', 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; F-02H Build/V11R051E)', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; HTC_D820pi Build/KOT49H)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; SM-J530S Build/M1AJQ)', 'Dalvik/2.1.0 (Linux; U; Android 5.1; OPPO R9m Build/LMY47I)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; G552KL Build/OPM1.171019.019)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; itel S13 Build/O11019)', 'Dalvik/2.1.0 (Linux; U; Android 7.0; itel P31 Build/NRD90M)', 'Dalvik/1.6.0 (Linux; U; Android 6.1; Tecno V9 Build/KTU84Q)', 'Dalvik/2.1.0 (Linux; U; Android 6.0; 1501-M02 Build/MRA58K)', 'Dalvik/2.1.0 (Linux; U; Android 6.0; P339 Build/MRA58K)', 'Dalvik/1.6.0 (Linux; U; Android 4.4.4; C5502 Build/10.5.1.A.0.283)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; C10 Build/O11019)', 'Dalvik/2.1.0 (Linux; U; Android 8.1; JMM-AL00 Build/HUAWEIJMM-L22)', 'Dalvik/2.1.0 (Linux; U; Android 6.0; Infinix NOTE 3 Build/MRA58K)', 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; LT C1400 Build/N2G47H)', 'Dalvik/1.6.0 (Linux; U; Android 4.1.2; F-05E Build/V11R35A)', 'Dalvik/1.6.0 (Linux; U; Android 7.1; X9 Build/JLS36C)', 'Dalvik/2.1.0 (Linux; U; Android 7.0; S50 Build/NRD90M)', 'Dalvik/2.1.0 (Linux; U; Android 10; L-03K Build/QKQ1.200730.002)', 'Dalvik/2.1.0 (Linux; U; Android 12; Pixel 5 Build/SPB4.210715.014)', 'Dalvik/2.1.0 (Linux; U; Android 9; RG655 Build/PPR1.180610.011)', 'Dalvik/2.1.0 (Linux; U; Android 6.0; Azumi_DOSHI_A55_QL Build/MRA58K)', 'Dalvik/2.1.0 (Linux; U; Android 11; Pixel 5 Build/RQ2A.210505.002)', 'Dalvik/2.1.0 (Linux; U; Android 9; S999 Build/PPR1.180610.011)', 'Dalvik/2.1.0 (Linux; U; Android 11; 6056D Build/RP1A.200720.011)', 'Dalvik/2.1.0 (Linux; U; Android 9.1; SM-A30 Build/LMY47I)', 'Dalvik/2.1.0 (Linux; U; Android 7.0; Moto C Plus Build/NRD90M.07.036)', 'Dalvik/2.1.0 (Linux; U; Android 12; XQ-BC52 Build/61.1.A.0.576)', 'Dalvik/2.1.0 (Linux; U; Android 11; SO-41B Build/60.1.A.2.88)', 'Dalvik/2.1.0 (Linux; U; Android 11; Nokia G10 Build/RP1A.200720.011)', 'Dalvik/2.1.0 (Linux; U; Android 11; motorola edge 20 pro Build/RRA31.Q3-19-32)', 'Dalvik/2.1.0 (Linux; U; Android 10; moto g power Build/QPMS30.80-109-5)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; H1A1000 Build/OPM1.171019.011)', 'Dalvik/2.1.0 (Linux; U; Android 9; BDF-M107 Build/PPR1.180610.011)', 'Dalvik/2.1.0 (Linux; U; Android 9; TX6 PLUS S905X3 Build/PPR1.180610.011)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; CVD1660-WJ Build/O11019)', 'Dalvik/2.1.0 (Linux; U; Android 9; AI PONT Build/PTO1.201213.001)', 'Dalvik/2.1.0 (Linux; U; Android 7.0; PSP7550DUO Build/NRD90M)', 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; moto e5 Build/OPP27.91-176-11)', 'Dalvik/2.1.0 (Linux; U; Android 9; Android TV Build/PTO9.210429.001)', 'Dalvik/2.1.0 (Linux; U; Android 10; H8266 Build/52.1.A.0.618)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; SP19504 Build/O11019)', 'Dalvik/2.1.0 (Linux; U; Android 6.0; Curvy C40i+ Build/MRA58K)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; Swift 2 X Build/OPM5.171019.017)', 'Dalvik/2.1.0 (Linux; U; Android 10; Lenovo TB-X306FA Build/QP1A.190711.020)', 'Dalvik/2.1.0 (Linux; U; Android 7.0; Tablet_DL_2810 Build/NRD90M)', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; M_PPAX510U Build/KOT49H)', 'Dalvik/2.1.0 (Linux; U; Android 11; ZUK Z2121 Build/RQ2A.210505.003)', 'Dalvik/2.1.0 (Linux; U; Android 10; W4 Build/QP1A.190711.020)', 'Dalvik/2.1.0 (Linux; U; Android 9; 801SO Build/52.0.D.5.266)', 'Dalvik/2.1.0 (Linux; U; Android 10; MiTV-MOOQ0 Build/QTG3.200305.006)', 'Dalvik/2.1.0 (Linux; U; Android 6.0; N7 Pro Build/MRA58K)', 'Dalvik/2.1.0 (Linux; U; Android 10; K87CA Build/QKQ1.200517.002)', 'Dalvik/2.1.0 (Linux; U; Android 11; EA1002 Build/RP1A.200720.011)', 'Dalvik/2.1.0 (Linux; U; Android 11; RMX2040 Build/RP1A.200720.011)', 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G975N Build/N2G47H)', 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; PCLM10 Build/N2G47H)', 'Dalvik/2.1.0 (Linux; U; Android 5.1; i4D Build/LMY47D)', 'Dalvik/2.1.0 (Linux; U; Android 11; RMX2163 Build/RP1A.200720.011)', 'Dalvik/2.1.0 (Linux; U; Android 5.0.2; SM-G850S Build/LRX22G)', 'Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 5 Build/RQ2A.210305.006)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; U70C Build/OPM2.171019.012)', 'Dalvik/2.1.0 (Linux; U; Android 11; TECNO KF6 Build/RP1A.200720.011)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; ALO Build/O11019)', 'Dalvik/2.1.0 (Linux; U; Android 6.0; VIE-AL10 Build/HUAWEIVIE-AL10)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; LS032I Build/O11019)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; L503F Plus Build/OPM2.171019.012)', 'Dalvik/2.1.0 (Linux; U; Android 11; RMX2161 Build/RP1A.200720.011)', 'Dalvik/2.1.0 (Linux; U; Android 6.0; Pro_Max11 Build/MRA58K)', 'Dalvik/1.6.0 (Linux; U; Android 8.1; Note6 Build/OOT49H)', 'Dalvik/1.6.0 (Linux; U; Android 4.4.4; HTC One_M8 Eye Build/KTU84P)', 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; F-05J Build/V22R040A)', 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; T700X Build/N4F26M)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; LM-X415L Build/OPM1.171019.026)', 'Dalvik/2.1.0 (Linux; U; Android 10.0; Note20+ Build/LMY47I)', 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; Lenovo K8 Note Build/NMB26.54-87)', 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G900S Build/MMB29M)', 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; C107-9 Build/ZFXCNCT5801803011S)', 'Dalvik/2.1.0 (Linux; U; Android 7.1; Y35 Build/LRX21M)', 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; F-03H Build/V18R045B)', 'Dalvik/1.6.0 (Linux; U; Android 4.4.4; SM-G360V Build/KTU84P)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; C11 Build/O11019)', 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Nexus 5X Build/N2G47Z)', 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A605F Build/R16NW)', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; LG-F200S Build/KOT49I.F200S30k)', 'Dalvik/2.1.0 (Linux; U; Android 5.0.2; F103 Build/LRX21M)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; Infinix X620B Build/OPM1.171019.026)', 'Dalvik/2.1.0 (Linux; U; Android 10; moto g(7) power Build/QPOS30.85-18-3)', 'Dalvik/2.1.0 (Linux; U; Android 9; itel L6501 Build/PPR1.180610.011) XDL', 'Dalvik/2.1.0 (Linux; U; Android 10; motorola one Build/QPKS30.54-22-13-12)', 'Dalvik/2.1.0 (Linux; U; Android 9; H7 Build/PPR1.180610.011)', 'Dalvik/2.1.0 (Linux; U; Android 5.0.2; LG-D722 Build/LRX22G.A1527235094)', 'Dalvik/2.1.0 (Linux; U; Android 9; V4_Viper_PRO Build/P00610)', 'Dalvik/2.1.0 (Linux; U; Android 10; 100011885 Build/QP1A.190711.020)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; INOI 2 Lite 2019 Build/O11019)', 'Dalvik/2.1.0 (Linux; U; Android 9.1; YT9270 Build/O11019)', 'Dalvik/2.1.0 (Linux; U; Android 10; CLT-AL01 Build/HUAWEICLT-AL01)', 'Dalvik/2.1.0 (Linux; U; Android 11; moto g(50) Build/RRFS31.Q1-59-76-2)', 'Dalvik/2.1.0 (Linux; U; Android 10; Note_3 Build/QP1A.190711.020)', 'Dalvik/2.1.0 (Linux; U; Android 10; motorola one fusion Build/QPLS30.62-41-8)', 'Dalvik/2.1.0 (Linux; U; Android 11; GM1917 Build/RQ3A.210805.001.A1)', 'Dalvik/2.1.0 (Linux; U; Android 10; SOG02 Build/58.0.C.11.160)', 'Dalvik/2.1.0 (Linux; U; Android 11; RMX3201 Build/RP1A.200720.011)', 'Dalvik/2.1.0 (Linux; U; Android 10; K4m Build/QP1A.190711.020)', 'Dalvik/2.1.0 (Linux; U; Android 10.0; Q8.q2.0.6330.d4 Build/QQ1D.200105.002)', 'Dalvik/2.1.0 (Linux; U; Android 9; jacuzzi Build/R92-13982.88.0)', 'Dalvik/2.1.0 (Linux; U; Android 9; Samsung Chromebook 3 Build/R92-13982.82.0)', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; HUAWEI MT7-L09 Build/HuaweiMT7-L09)', 'Dalvik/2.1.0 (Linux; U; Android 10; Switch Build/QQ3A.200805.001)', 'Dalvik/2.1.0 (Linux; U; Android 10; POCO F1 MIUI/V12.0.3.0.QEJMIXM) XDL', 'Dalvik/2.1.0 (Linux; U; Android 6.0; F100L Build/MRA58K)', 'Dalvik/2.1.0 (Linux; U; Android 11; M2007J20CI Build/RKQ1.200826.002)', 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J700K Build/LMY48B)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; INOI_3 Build/O11019)', 'Dalvik/2.1.0 (Linux; U; Android 5.1; HUAWEI LYO-L02 Build/HUAWEILYO-L02)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; Venus Z30 Build/VT1150)', 'Dalvik/2.1.0 (Linux; U; Android 7.0; General Mobile 4G Dual Build/NRD90R)', 'Dalvik/2.1.0 (Linux; U; Android 7.0; SM-A710L Build/NRD90M)', 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; ZC553KL Build/MMB29M)', 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; SM-J510K Build/NMF26X)', 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; LGM-V300L Build/OPR1.170623.026)', 'Dalvik/1.6.0 (Linux; U; Android 4.3; HUAWEI P7 mini Build/HuaweiP7Mini)', 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; Lenovo TB-X304X Build/NMF26F)', 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; LG-F740L Build/MXB48T)', 'Dalvik/2.1.0 (Linux; U; Android 7.0; Flare S6 Lite DTV Build/NRD90M)', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; K77 Build/KOT49H)', 'Dalvik/2.1.0 (Linux; U; Android 7.0; SM-A310N0 Build/NRD90M)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; JSN-L22 Build/HONORJSN-L22)', 'Dalvik/2.1.0 (Linux; U; Android 6.0; Vision3 Build/MRA58K)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; LM-X210 Build/OPM1.171019.026)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; D7 Build/O11019)', 'Dalvik/2.1.0 (Linux; U; Android 10; SM-G965F Build/R16NW)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; K200 Build/O11019)', 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; CAM-L32 Build/CAM-L32)', 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-A7000 Build/MMB29M)', 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; moto g(6) play Build/OPPS27.91-140-6)', 'Dalvik/2.1.0 (Linux; U; Android 7.0; GXV3370 Build/NRD90M)', 'Dalvik/2.1.0 (Linux; U; Android 9; Phone 2 Build/P-SMR6-RC001-CKH-201102)', 'Dalvik/2.1.0 (Linux; U; Android 11; A9 Build/RP1A.200720.011)', 'Dalvik/2.1.0 (Linux; U; Android 6.0; iris 870 4G Build/MRA58K)', 'Dalvik/2.1.0 (Linux; U; Android 9; Mediatek MT8173 Chromebook Build/R92-13982.88.0)', 'Dalvik/2.1.0 (Linux; U; Android 11; vivo 2004 Build/RP1A.200720.012)', 'Dalvik/2.1.0 (Linux; U; Android 9; grunt Build/R92-13982.88.0)', 'Dalvik/2.1.0 (Linux; U; Android 6.0; NV6 Build/MRA58K)', 'Dalvik/2.1.0 (Linux; U; Android 9; S9MAX-1 Build/PPR1.180610.011)', 'Dalvik/2.1.0 (Linux; U; Android 10; EML-TL00 Build/HUAWEIEML-TL00)', 'Dalvik/2.1.0 (Linux; U; Android 6.0; s4_pro Build/MRA58K)', 'Dalvik/2.1.0 (Linux; U; Android 6.0; M18 Build/MRA58K)', 'Dalvik/2.1.0 (Linux; U; Android 10; SH-RM12 Build/S6129)', 'Dalvik/2.1.0 (Linux; U; Android 11; Infinix X689C Build/RP1A.200720.011)', 'Dalvik/2.1.0 (Linux; UI; Android 7.0; 5049Z Build/NRD90M', 'Dalvik/2.1.0 (Linux; U; Android 11; SM-A4260 Build/RP1A.200720.012)', 'Dalvik/2.1.0 (Linux; U; Android 6.0; ARES 73 LTE Build/MRA58K)', 'Dalvik/2.1.0 (Linux; U; Android 10; NOH-AN01 Build/HUAWEINOH-AN01)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; moto e5 (XT1920DL) Build/OPP28.44-26)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; NX609J Build/OPM1.171019.011)', 'Dalvik/2.1.0 (Linux; U; Android 9; Q10 Build/PPR1.180610.011)', 'Dalvik/2.1.0 (Linux; U; Android 11; Pixel 5a Build/RD2A.210605.007)', 'Dalvik/2.1.0 (Linux; U; Android 10; PCAM00 Build/QKQ1.190918.001)', 'Dalvik/2.1.0 (Linux; U; Android 10; 4087U Build/QP1A.190711.020)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; A81G Build/O11019)', 'Dalvik/2.1.0 (Linux; U; Android 10; motorola one vision Build/QSAS30.62-28-12-10)', 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; 5199I Build/O00623)', 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; BAC-L23 Build/HUAWEIBAC-L23)', 'Dalvik/2.1.0 (Linux; U; Android 6.0; Spanky 4G Build/MRA58K)', 'Dalvik/2.1.0 (Linux; U; Android 10; AS155 Build/QP1A.190711.020)', 'Dalvik/2.1.0 (Linux; U; Android 11; Nexus 5 Build/RQ3A.210805.001.A1)', 'Dalvik/2.1.0 (Linux; U; Android 11; 5062W Build/RKQ1.201202.002)', 'Dalvik/2.1.0 (Linux; U; Android 11; RMX1992 Build/RKQ1.201112.002)', 'Dalvik/2.1.0 (Linux; U; Android 10; Lenovo TB-X306XA Build/QP1A.190711.020)', 'Dalvik/2.1.0 (Linux; U; Android 11; ONEPLUS A5000 Build/RQ3A.210805.001.A1)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; Pars2 Build/O11019)', 'Dalvik/2.1.0 (Linux; U; Android 6.0; HP Pro 8 Tablet with Voice Build/MRA58K)', 'Dalvik/2.1.0 (Linux; U; Android 7.0; VEN-L22 Build/HONORVEN-L22)', 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; Coolpad T2-00 Build/LMY47V)', 'Dalvik/1.6.0 (Linux; U; Android 4.4.4; SM-G316HU Build/KTU84P)', 'Dalvik/2.1.0 (Linux; U; Android 6.0; Pars Build/MRA58K)', 'Dalvik/1.6.0 (Linux; U; Android 4.4.4; XT1028 Build/KXB21.14-L1.41-1)', 'Dalvik/2.1.0 (Linux; U; Android 5.1; Maad Build/LMY47D)', 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G610L Build/MMB29K)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; Nobby S500 Build/OPM2.171019.012)', 'Dalvik/2.1.0 (Linux; U; Android 5.1; HUAWEI TAG-TL00 Build/HUAWEITAG-TL00)', 'Dalvik/2.1.0 (Linux; U; Android 6.0; Z6 Build/MRA58K)', 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; Coolpad A8 Build/LMY47V)', 'Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G9350 Build/NRD90M)', 'Dalvik/2.1.0 (Linux; U; Android 6.0; LG-F690S Build/MRA58K)', 'Dalvik/1.6.0 (Linux; U; Android 4.4.4; HUAWEI G7-UL20 Build/HuaweiG7-UL20)', 'Dalvik/2.1.0 (Linux; U; Android 5.1; aura 55 Build/LMY47D)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; Z1 Build/O11019)', 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; SNE-LX2 Build/HUAWEISNE-LX2)', 'Dalvik/1.6.0 (Linux; U; Android 4.2.2; HTC Desire 210 dual sim Build/JDQ39)', 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; LG-M150 Build/MXB48T)', 'Dalvik/2.1.0 (Linux; U; Android 7.0; SC-03J Build/NRD90M)', 'Dalvik/2.1.0 (Linux; U; Android 7.0; TECNO i7 Build/NRD90M)', 'Dalvik/1.6.0 (Linux; U; Android 4.2.2; ME-715 Build/JDQ39)', 'Dalvik/2.1.0 (Linux; U; Android 6.0; WOWO Build/MRA58K)', 'Dalvik/2.1.0 (Linux; U; Android 7.1; CHM-TL00H Build/HonorCHM-TL00H)', 'Dalvik/1.6.0 (Linux; U; Android 4.1.2; L-01E Build/JZO54K)', 'Dalvik/2.1.0 (Linux; U; Android 7.0; VIA_A1_1 Build/NRD90M)'] 

def inputs():
    os.system("clear")
    print(logo)
    print('\x1b[1;97mCHOSE THE UID CODE:\x1b[1;97m 1000 10001 10002 10003')
    code=input("\x1b[1;91m[\x1b[1;97m+\x1b[1;91m] \x1b[1;97mINPUT YOUR UID: ")
    tt=int(input("\x1b[1;91m[\x1b[1;97m+\x1b[1;91m] \x1b[1;97mTOTAL LIMIT: "))
    l=0
    if len(code)<4:
        l=int(input("\x1b[1;91m[\x1b[1;97m+\x1b[1;91m] \x1b[1;97mUID LENGHT: "))
    return code,tt,l
 
    
def getname(uid):
    global n,c
    ua=random.choice(ugen)
    hd={'authority':'m.facebook.com',

            'method': 'GET',
            'user-agent':ua

                  
            }
    url="https://m.facebook.com/profile.php?id="+uid
    pi=r.get(url,headers=hd)
    bp=bs(pi.content,"html.parser")
    name=bp.find("title").text.split("|")[0].strip()
    if "\x1b[1;91mSERVER ERROR" not in name and "\x1b[1;91mLOGIN INTO FACEBOOK" not in name:
        n+=1
     
        print(f"\033[1;32m{uid} | {c}")
        open(file,"a").write(uid+" | "+name+"\n")
 
    
    c+=1
    
    print(f'\033[0;32mPROCESSING.. %s ]'%(n),end="\r")

def run():
    with tdp(max_workers=30) as t:
        for uid in uids:
            t.submit(getname,uid)

while True:
    code,tt,l=inputs()
    if len(code)>=4:
        gen(code,tt)
    else:
        geno(code,l,tt)
    
    run()
    print("\033[0;33mDUMP FILE HAS BEEN SAVED TO "+file)
    rr=input("\033[0;33mWANNA DUMP AGAIN? [Y,N]: ")
    if rr in ["Y","y"]:
        code,tt,l=inputs()
        n=0
        c=0
        uids=[]
        gen(code,tt)
        run()
    else:
        break
