import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from colored import cprint # type: ignore
import os
from pystyle import Anime, Colors, Colorate, Center

senders = {
'qstkennethadams388@gmail.com':'itpz jkrh mtwp escx',
'usppaullewis171@gmail.com':'lpiy xqwi apmc xzmv',
'ftkgeorgeanderson367@gmail.com':'okut ecjk hstl nucy',
'nieedwardbrown533@gmail.com':'wvig utku ovjk appd',
'h56400139@gmail.com':'byrl egno xguy ksvf',
'den.kotelnikov220@gmail.com':'xprw tftm lldy ranp',
'trevorzxasuniga214@gmail.com':'egnr eucw jvxg jatq',
'dellapreston50@gmail.com':'qoit huon rzsd eewo',
'neilfdhioley765@gmail.com':'rgco uwiy qrdc gvqh',
'hhzcharlesbaker201@gmail.com':'mcxq vzgm quxy smhh',
'samuelmnjassey32@gmail.com':'lgct cjiw nufr zxjg',
'allisonikse1922@gmail.com':'tozo xrzu qndn mwuq',
'corysnja1996@gmail.com':'pfjk ocbf augx cgiy',
'maddietrdk1999@gmail.com':'rhqb ssiz csar cvot',
'yaitskaya.alya@mail.ru':'CeiYHA6GNpvuCz584eCp',
'yelena.polikarpova.1987@mail.ru':'70Ktuvrs1iYbvSnbK8hG',
'yeva.zuyeva.85@mail.ru':'EBjgRqq73hue9dGhUA2R',
'zina.yagovenko.69@mail.ru':'QKBmpXnzFZVu9w4ewSrA',
'ilya.yaroslavov.72@mail.ru':'A2gNkb8n54i4T7XdPdH5',
'maryamna.moskvina.62@mail.ru':'dT7ftdX72cMsVemqRRqu',
'zina.zhvikova@mail.ru':'7CwRkjeL3a5viE9we3bt',
'boyarinova.fisa@mail.ru':'NnJfmSBzQ9Eew09xirpY',
'prokhor.sveshnikov.73@mail.ru':'Ybunrxdf95gkzm6A6ipp',
'azhikelyamov.yulian@mail.ru':'r7hanfr0tMqcBE4Edmg0',
'prokhor.siyantsev@mail.ru':'yubs6kvtfpWT4Tram26e',
'yablonev90@mail.ru':'42krThdaYbWCrCbH8UgK',
'mari.dvornikova.86@mail.ru':'qdEzYLWSTz6UEM2E4i0u',
'vika.tobolenko.96@mail.ru':'3WQ2wFTwge9m2C09QsfK',
'koporikov.yura@mail.ru':'nJtyfjqYi91j7tk0udNx',
'zina.podshivalova.92@mail.ru':'u4CL3YxVutmiuTvmTrbu',
'leha.novitskiy.71@mail.ru':'qQZd1gMqkU906Xk2hgJJ',
'rimma.aleksandrovicha.72@mail.ru':'biL4m6h0h4xQrDB3PnPp',
'polina.karaseva.1987@mail.ru':'mxZUqPPTrZHK99jUfPhB',
'prokhor.sablin.82@mail.ru':'vN7FjmmCmAD0JnQsANyc',
'kade.kostya@mail.ru':'U0hdXu7y3c1AVeT1Vpn9',
'yelizaveta.novokshonova.71@mail.ru':'aKPpgaPDuwaKbX1pbcq3',
'pozdovp@mail.ru':'EGDd20c7s82Z0s9LmrXc',
'siyasinovy@mail.ru':'z2ZdsRL04JvBYZrrjrvv',
'nina.gref.73@mail.ru':'sitw1XTxCVgji061iqj7',
'fil.golubkin.80@mail.ru':'PeaLrzjbn408DEeiqmQq',
'venedikt.babinov.71@mail.ru':'tBewA1HQm29c2Zkira96',
'den.verderevskiy.67@mail.ru':'fndp7qr67dpfXBAu0ePH',
'olga.viranovskaya.92@mail.ru':'50QSPrecgk5cMdk1YsBm',
'uyankilovich@mail.ru':'Muw9kX9vAhhKxbZXZ3sh',
'clqdxtqbfj@rambler.ru':'8278384a3L51C',
'qeuvkzwxao@rambler.ru':'72325556pMFol',
'mgiwwgbjqt@rambler.ru':'3180204jCoAdt',
'olwogjcicw@rambler.ru':'3993480P4Gyth',
'qjdmjszsnc@rambler.ru':'6545403StkbOh',
'yqoibpcoki@rambler.ru':'695328653f9Wp',
'vnlhjjkbxr@rambler.ru':'4609313egqV59',
'vpgcdkunar@rambler.ru':'9936120R4LYh3',
'agycsnogqq@rambler.ru':'0234025nWwX5j',
'ctmhzsngse@rambler.ru':'2480571s1sZvW',
'ryztzlttdn@rambler.ru':'9416368kTX5jI',
'hqxybovebw@rambler.ru':'8245145VhX704',
'rejrjswkwb@rambler.ru':'5114881xCYqsB',
'xkbecjvxnx@rambler.ru':'5670524FiFi39',
'xnlqkfvwzx@rambler.ru':'7911186rp8L9P',
'gvzzmqtuzy@rambler.ru':'5133370ZstXEx',
'eijxsbjyfy@rambler.ru':'36196124YQZeI',
'bizdlfuahq@rambler.ru':'8374903tkk2gA',
'dhehumtsef@rambler.ru':'9126453AkhK0Z',
'zsotxpaxvi@rambler.ru':'46227528QryxI',
'ktsgdygeuc@rambler.ru':'1853586bnCyzK',
'uiacgqvgpe@rambler.ru':'65280104FvoJW',
'ynazuhytyd@rambler.ru':'1038469bD3PXc',
'ewmyymarvi@rambler.ru':'5023318Bh3tBg',
'wllhpdisuj@rambler.ru':'24856958LdTsS',
'ldqicaqxqo@rambler.ru':'3878601ZNDUtq',
'qnuumqoreq@rambler.ru':'97575207Is6tx',
'hlqhvdwpvn@rambler.ru':'6886684bPjiyd',
'mjjjxiuadq@rambler.ru':'0606032V81m1F',
'qmasujqfrk@rambler.ru':'277585511anUy',
'mfemvxqdcq@rambler.ru':'8831015UwqwWD',
'jauvxszfam@rambler.ru':'0711044gqzrVR',
'lkmujuagfk@rambler.ru':'08781007DLS8k',
'kcamwmzxjo@rambler.ru':'9812873rVr1MY',
'czkklwifon@rambler.ru':'74278883h9FP8',
'tsjsbqyrfk@rambler.ru':'0150917jIseH2',
'pbetvcnhzh@rambler.ru':'9952234XaKDFu',
'bsahxcpwkw@rambler.ru':'2860163ch8Ido',
'xphyesgbtc@rambler.ru':'6594341ERehhX',
'egmpjoufeq@rambler.ru':'2613441hfDuWr',
'jyaolatwam@rambler.ru':'7668835xdjLbg',
'istooplcmf@rambler.ru':'6592403JR47Wm',
'vxesoednot@rambler.ru':'35885918QZw94',
'oywtklayaz@rambler.ru':'4434448KsCuTf',
'tazxrlpjil@rambler.ru':'8342862p9Wyst',
'aumiycpxid@rambler.ru':'4109383BuuNcN',
'lrrztbfuzy@rambler.ru':'3646406sDO8ay',
'ocggavguxr@rambler.ru':'6406050SL2mZG',
'imprdsrnmd@rambler.ru':'4869746vpxksJ',
'eidyoikavp@rambler.ru':'1243890yXPyix',
'jtbcabsapw@rambler.ru':'566339497yHv3',
'szokdvnzrw@rambler.ru':'5285567I3Bil1',
'jqflrccfjs@rambler.ru':'7239478VeLuf1',
'nhmxjawemh@rambler.ru':'22695409fkCex',
'uoolwvvwdc@rambler.ru':'1073090zX6ebM',
'bdnptczren@rambler.ru':'2684430DcPEuk',
'bfghzdkurg@rambler.ru':'3874335d5hDQy',
'ljlexsfcvo@rambler.ru':'4102671EIquGo',
'byzjhysyyg@rambler.ru':'4637736mzdEcT',
'tlrjbuzcyj@rambler.ru':'2437827AhPaGW',
'denjsbmggh@rambler.ru':'228014585ayVe',
'ekkjrcskzo@rambler.ru':'6609442MFPeDO',
'ptpjocqobw@rambler.ru':'6047270EXk7Hb',
'nekrxmcklm@rambler.ru':'3532718I3vV4C',
'ulgqeqvdqy@rambler.ru':'6764301Nx25yL',
'ezofozvhyn@rambler.ru':'43181265tC6FQ',
'hwklsnkqky@rambler.ru':'2399374mHyEUJ',
'elglaqexoj@rambler.ru':'9803014pMNF9p',
'rgmjfwhhjs@rambler.ru':'3268611cfC3aR',
'vcvwvkntgb@rambler.ru':'6536007UgTXg4',
'phkohtlitv@rambler.ru':'0238010TXt5aN',
'pqqqyejlqi@rambler.ru':'0429804UwSSi2',
'toxevermnd@rambler.ru':'1801000MqDm87',
'dicfdqgxad@rambler.ru':'2062460Tbvjlz',
'sktsnxhcxe@rambler.ru':'35185285Pon91',
'jpljjnrrla@rambler.ru':'0815671xPHjiw',
'rtqpiimiid@rambler.ru':'6534672URa1mI',
'ldygdlpizk@rambler.ru':'6686886YWhL05',
'fqxqadaxfy@rambler.ru':'3195621x5qYdU',
'chybzpsglw@rambler.ru':'8032931YTKllg',
'vkctzanare@rambler.ru':'1157997LGySqk',
'repjncygun@rambler.ru':'3300691BqYJVG',
'khrarivdow@rambler.ru':'7168350Cmqkmj',
'aqbeitoqdl@rambler.ru':'87552792499tS',
'vhauhgmbnc@rambler.ru':'9276444y9YzY1',
'cfoqabqkbi@rambler.ru':'4601718gc2Zji',
'kmqnowhvjp@rambler.ru':'6667003L1jZxc',
'djsdksvzhj@rambler.ru':'7523251yAKPjZ',
'uztbbbfqbp@rambler.ru':'8265517naN9fx',
'ljrbpfuicp@rambler.ru':'39793362TjZIk',
'jzzdyxicjo@rambler.ru':'8117494s6CZVB',
'gjnbtrflkc@rambler.ru':'8623171iqXOD9',
'jfjtwncyeb@rambler.ru':'7066987lMSG2Z',
'rfphqkyyrj@rambler.ru':'8800207M5Nj7Y',
'ilynipkqwx@rambler.ru':'83333032WQo83',
'ifzenleixs@rambler.ru':'69679436xM9U4',
'oevwtysoel@rambler.ru':'6918228UC47Zs',
'hpdkdwqvzx@rambler.ru':'0605431xMVexd',
'ekbkufxdxx@rambler.ru':'1918712uEOQ9t',
'zstxwfwiof@rambler.ru':'4043772UwRp5o',
'rjmrbybhnd@rambler.ru':'5203792lDmxvC',
'eukygnfzno@rambler.ru':'3520959hXs1Zw',
'ljrolbwlad@rambler.ru':'0394475pK0dYa',
'gozpezocmj@rambler.ru':'8282635Gkvuvq',
'asytoiumwt@rambler.ru':'42141199FgP3H',
'fbiooohghv@rambler.ru':'7338453zMbWhb',
'ajwlalfqqu@rambler.ru':'3360915x1XVgt',
'cvegntetwm@rambler.ru':'8091607CSuKMf',
'jnhjnmicbt@rambler.ru':'6375986dokrgG',
'fnaauasmjz@rambler.ru':'4160248ztCRsJ',
'qnwmlvfwct@rambler.ru':'8367630XGXmxW',
'lkycbhjcwp@rambler.ru':'5255980KedZTc',
'bkyojwrkxl@rambler.ru':'1286663uHl4WQ',
'lxddybklck@rambler.ru':'1077242JFSyQN',
'chzhdkoxnp@rambler.ru':'0533445SI0q7c',
'ofjxkwwomf@rambler.ru':'04956317DKrSX',
'jlirgtapbl@rambler.ru':'8728917NdMxgN',
'dgcceghlse@rambler.ru':'2986381aT5V36',
'rkwfhcvlem@rambler.ru':'10022063K5qmY',
'orgjvhbrxw@rambler.ru':'0652659TopL8Z',
'opynskpmzp@rambler.ru':'2881423L4qs6x',
'pbqzrueeko@rambler.ru':'44469262tOGeK',
'raxzhngqti@rambler.ru':'3078265mgWYjl',
'ztnxozwuuj@rambler.ru':'0637919utKekj',
'gtxjzwlgio@rambler.ru':'3737088WWddrY',
'sjbflcwjgn@rambler.ru':'9791667kVGllD',
'znggdpfxzu@rambler.ru':'0209083jdisUI',
'gnvhlocnro@rambler.ru':'4361239Vu3OCl',
'vqeijhgrmo@rambler.ru':'5560137M1oKk2',
'meefvzfwqb@rambler.ru':'9793015vJE0qF',
'sclsjzvugn@rambler.ru':'4631432OQjvWt',
'ybbtiosefy@rambler.ru':'3511505pL04S1',
'agwqdadpkb@rambler.ru':'0930298CUZdLp',
'kudgvibwao@rambler.ru':'5791834nlLQtU',
'qyonxjqbxi@rambler.ru':'9390829m2Edz3',
'jhetdlhlqk@rambler.ru':'5530162MiLHZe',
'bsjvczarsc@rambler.ru':'5747155KvNjcL',
'wlcilpvzqu@rambler.ru':'2757580jLlM9M',
'xxdgcixidw@rambler.ru':'2867562O7zGft',
'wekduwrnkp@rambler.ru':'2646367TlIskI',
'keakcnrorg@rambler.ru':'9223165cV1Jj8',
'nzuspyevwr@rambler.ru':'2212416npkUqe',
'mgjfbgitts@rambler.ru':'7368986roeLXD',
'smfxvrnhmu@rambler.ru':'6947298Kau5qA',
'yvkelubdzf@rambler.ru':'5913332lXWtlC',
'bwywtjxybd@rambler.ru':'2766021wTSkeU',
'dlvyzavolw@rambler.ru':'274983252lHyu',
'oaudcugulf@rambler.ru':'4543030UHFWaV',
'zvqexaokhf@rambler.ru':'1453114PCheCq',
'pjuafpzpoo@rambler.ru':'8474216vNFUG0',
'ckryhpqogh@rambler.ru':'4791674aJHW43',
'vlkqstbhpd@rambler.ru':'3021260kBI3KU',
'jwuupemjpm@rambler.ru':'7769235y719L9',
'bmxuqrzcnk@rambler.ru':'1345552ExHXyu',
'fqrkonqkjc@rambler.ru':'4104158bVEORa',
'gizwbhyrfd@rambler.ru':'3863359lgfpTv',
'onghqwbvnz@rambler.ru':'8249537XWqpPk',
'aeyeyvlnkl@rambler.ru':'6025219f5mGom',
'qcwweqcqbx@rambler.ru':'2503306kHzKPD',
'vefmynztzu@rambler.ru':'1134939bhRpJS',
'qlkhitdctp@rambler.ru':'31621358ZPx5F',
'xhgfgecvrn@rambler.ru':'4116759TRhERi',
'globizrzui@rambler.ru':'9679753mLkmMd',
'vvfcuoibrf@rambler.ru':'13558992CDkJj',
'enccmwktap@rambler.ru':'7631476Lzr9hd',
'njbnyghvdq@rambler.ru':'48585907Qh2NS',
'cobadewaxd@rambler.ru':'6433228NMX7a0',
'zzvsuoiqfx@rambler.ru':'5067380KtnMTb',
'lkdcjpcqxu@rambler.ru':'8319085aRHdoT',
'zcabeofgox@rambler.ru':'0059181TJSaJq',
'rswrifhmtf@rambler.ru':'2987108xzf1Uy',
'gebzgyscic@rambler.ru':'6981082UOD1sL',
'yhncgfwjom@rambler.ru':'7866073mRMAal',
'pvvlmjmiwe@rambler.ru':'2807349CLUZie',
'towqdsigmc@rambler.ru':'48481486UnoRg',
'eyzwvxphxz@rambler.ru':'5532563Bskght',
'aruhbkpsud@rambler.ru':'8022722dNUe59',
'kckwnnvmwf@rambler.ru':'77502899D6ygI',
'emicquwuxf@rambler.ru':'2982514obBgCJ',
'pnefqbonja@rambler.ru':'1443294ZY7BgB',
'wlnecrzvkb@rambler.ru':'2016456ke4QRw',
'lucufydobd@rambler.ru':'4188202gvlmuR',
'obcheovoqy@rambler.ru':'34012721sYlv3',
'fjxwhhlhxp@rambler.ru':'1621680a9CbS0',
'rjggfmhckx@rambler.ru':'4470958ocoPjD',
'oqixhlbhlh@rambler.ru':'4902150aD8Tkr',
'zmlfdygkce@rambler.ru':'4809956HgOdyu',
'zdjqfhdafp@rambler.ru':'9142498RW8Ynh',
'cjoyoxsdby@rambler.ru':'108516737An82',
'hfrcbbwzgb@rambler.ru':'1732107RUVvSu',
'crkbywjfzg@rambler.ru':'9616254qbUhAG',
'luygpfibra@rambler.ru':'9488606qXIvQZ',
'xepjtcrrzo@rambler.ru':'3774977dMOr4c',
'ayrbethwst@rambler.ru':'4658060glYVyA',
'czhjnqqgdd@rambler.ru':'89865789wXqfK',
'oltotetppj@rambler.ru':'0936665mJL9H0',
'eaoeqvygrv@rambler.ru':'5348316HcEpsm',
'dkfvwvkotb@rambler.ru':'3366454MTGiOR',
'wavsfqiarg@rambler.ru':'4220587wVJ8gU',
'gkwlbrhwix@rambler.ru':'6383580cCHutT',
'uachryyzde@rambler.ru':'0643369cWRWhr',
'nuyfldwirg@rambler.ru':'29709163eKxWc',
'fnorovxtvk@rambler.ru':'469173140zLer',
'qrmnfyxdqj@rambler.ru':'7609701E9XfBC',
'ncupywgysj@rambler.ru':'8506439mTgrb6',
'ehhuextqqm@rambler.ru':'4136418EqGa4N',
'utasiosnxd@rambler.ru':'6230428wOiMLm',
'ppizzpzqod@rambler.ru':'6217530deEIGb',
'mgzczmjjpo@rambler.ru':'5974114gf7VLz',
'ezugyxxfkx@rambler.ru':'6920685aZVulS',
'vnuwwwuhuj@rambler.ru':'20889562nRk1x',
'xqkicchcbc@rambler.ru':'4345126XoitUD',
'hykbjrvqsw@rambler.ru':'8281493mLUbNt',
'etyqikxlam@rambler.ru':'1096360Cvg5n7',
'blnpfilkdh@rambler.ru':'6208964Fhgy1O',
'azawxjcfeh@rambler.ru':'8923382Pqo1jI',
'dyumumpgus@rambler.ru':'3454195S5FQ7d',
'ryejfejmef@rambler.ru':'1474062Y49oZE',
'uqyfeqyumv@rambler.ru':'4305431o270vK',
'vardlzqzas@rambler.ru':'8158325VAjymq',
'wvqbwbpofd@rambler.ru':'2037592lvIWZI',
'agsnpvxscg@rambler.ru':'676450330Gmzj',
'ctiwtwpowk@rambler.ru':'7004605qQOK5O',
'vvluscokds@rambler.ru':'2351339uVtaUb',
'gqtipysiyk@rambler.ru':'4672575GMSkQq',
'vwtjzupcul@rambler.ru':'6978060SRfKxQ',
'klvdgsoczb@rambler.ru':'8504791kNehzf',
'lavpussyin@rambler.ru':'1183746FmKlfU',
'xvzoptqyhd@rambler.ru':'7635851M7gCQO',
'yzkgydxjlr@rambler.ru':'3889248nBv9xb',
'tkuscgummb@rambler.ru':'2646861vfBmjy',
'ytbfnnlvuc@rambler.ru':'8680715wXqNoY',
'qrmyueqrpk@rambler.ru':'48163158cQzn3',
'nulburzrsp@rambler.ru':'4628721fbFYDx',
'xpsncakaar@rambler.ru':'8050121QgZtLE',
'rsfyuinlhi@rambler.ru':'7789677doEl7X',
'lruwhkjpmm@rambler.ru':'2407934PCrhbt',
'zqlboekoph@rambler.ru':'4540547BXedBD',
'djrmgdvpxk@rambler.ru':'2516345lt4GhI',
'cdyagajvqt@rambler.ru':'0457036J8b9x1',
'csbmtfyogo@rambler.ru':'8578398RoY5Me',
'mtgjgvchbf@rambler.ru':'6273263XOh0fb',
'hjovrkraea@rambler.ru':'1756354e4T9PL',
'wuasdmqayg@rambler.ru':'8983467Njjbfc',
'dnzaquycrh@rambler.ru':'3047369gLtNHO',
'rdptnhimnz@rambler.ru':'92217639LcTX1',
'yklofyaekj@rambler.ru':'0018913JhfLfv',
'zqfzplzlwp@rambler.ru':'6550676M1gwNy',
'fzcveyejbh@rambler.ru':'9098104PB57ol',
'qcpwhpqape@rambler.ru':'3277585gafS4o',
'xfitvnzvez@rambler.ru':'0023433CgWWiW',
'tiansbolvj@rambler.ru':'0200419d6c8hD',
'ibwukvjyxn@rambler.ru':'6846348Go4rB7',
'tfclkifgjn@rambler.ru':'9973469KBqk2S',
'yscehsgepj@rambler.ru':'0258935Wptd0G',
'webznumpmf@rambler.ru':'4342482ZhTyVk',
'xadehtuxys@rambler.ru':'94129234ZK2kl',
'wsfmuqnmjp@rambler.ru':'7886187uCcru0',
'mhovkuzfnl@rambler.ru':'3632660bLpvSw',
'pppuvtsuxu@rambler.ru':'6227635FqgnGa',
'vvezjeryic@rambler.ru':'7595367ZgjYIn',
'oiukjktkhx@rambler.ru':'35863397YZBFb',
'qswbndmblj@rambler.ru':'3563325a93EZ6',
'ztyfnsdrqa@rambler.ru':'7748929ZbfDrw',
'lrjduagkcj@rambler.ru':'8783147DV4pJe',
'fhrzanukuh@rambler.ru':'169703230lEf6',
'pqnnzwuuku@rambler.ru':'6446752B0qw8H',
'ndctkqjnfc@rambler.ru':'1534939xHfafC',
'tlzuekovcn@rambler.ru':'9668644RKjMla',
'ermdcrjyhu@rambler.ru':'9838788xXiLRC',
'qbfymlhpwj@rambler.ru':'3278597BlWafL',
'uuuzmgapoy@rambler.ru':'2535811Vz3dxV',
'chjolhsihy@rambler.ru':'8253848P8B5cd',
'rrakdmtsdb@rambler.ru':'0459246V4tjHK',
'ngkrbvqvha@rambler.ru':'9835759JQxkal',
'caxeoztjpa@rambler.ru':'1297098SSweKM',
'molnxkchzu@rambler.ru':'3122920NIh3iE',
'murnslgulf@rambler.ru':'1045964Oppb9c',
'qcjyautxca@rambler.ru':'6358075LUbp6R',
'amhlnrxaue@rambler.ru':'3401580IiYPYn',
'wexnexkcct@rambler.ru':'2157766eLIiqP',
'oplwkvkrct@rambler.ru':'7136350vkGkaT',
'pmddwbvmwv@rambler.ru':'3066705M2aCUh',
'aqjcdxeuuh@rambler.ru':'2077271RlOJ0c',
'baiivnfrdy@rambler.ru':'1327519LJwKyi',
'apvskvwhsv@rambler.ru':'2995739T8pCNZ',
'xsejblkgit@rambler.ru':'6224118EhnkyG',
'rxihtsvdxg@rambler.ru':'3045787jhQxfI',
'dgtmxgrdsm@rambler.ru':'0342058YAff0O',
'wuxaurjkuu@rambler.ru':'6231160X8CsYl',
'erimfuxfdl@rambler.ru':'1956070yzlgSl',
'ncklilvfts@rambler.ru':'5077711XhCUzu',
'eerlpvniie@rambler.ru':'6769422kteVgK',
'mcrtyjkbdi@rambler.ru':'5281059WC9HfI',
'izjnzlavcu@rambler.ru':'4201974Gjdy1B',
'tkrywugfgq@rambler.ru':'1037112WpAZzl',
'hpxzczhgwe@rambler.ru':'4522788wYVDJk',
'rtfanictwt@rambler.ru':'9292445IxACdk',
'lhschktxka@rambler.ru':'0731083E0ItX4',
'zfqfwvmnms@rambler.ru':'82390631NIbOF',
'rzaviakxlb@rambler.ru':'2230383uFiVmA',
'rmmueooozx@rambler.ru':'1531525wyFFSm',
'weasmvistt@rambler.ru':'7079364RGZCBs',
'qikszesoqz@rambler.ru':'6739326h2Wy4j',
'gosgrmonmh@rambler.ru':'7425012zw2LXl',
'vuhlehwstc@rambler.ru':'6477750sVXsV3',
'wcbmulbsbk@rambler.ru':'9889803qVwaj6',
'aejerwwnft@rambler.ru':'4598847uygrUg',
'rtrkjygdey@rambler.ru':'4810312JrG4Ti',
'uywyrkhuue@rambler.ru':'6593801fMGH6b',
'flqyimskwk@rambler.ru':'7856809GVZfzT',
'mqjqttpyui@rambler.ru':'3633261lxxEPt',
'asagkqfygx@rambler.ru':'90629300zd5Xm',
'bupfcjoqrc@rambler.ru':'7806644uXzkZy',
'twicbfjgoz@rambler.ru':'0187832xjeOz1',
}
receivers = ['sms@telegram.org, dmca@telegram.org, abuse@telegram.org, sticker@telegram.org, support@telegram.org']

banner = '''

███████╗███╗   ██╗ ██████╗ ███████╗███████╗██████╗ 
██╔════╝████╗  ██║██╔═══██╗██╔════╝██╔════╝██╔══██╗
███████╗██╔██╗ ██║██║   ██║███████╗█████╗  ██████╔╝
╚════██║██║╚██╗██║██║   ██║╚════██║██╔══╝  ██╔══██╗
███████║██║ ╚████║╚██████╔╝███████║███████╗██║  ██║
╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝

            Creator: @spider7_zip
              Special for Marty

╔================================================╗
║ [1] СНОС АККАУНТОВ       [2] СНОС КАНАЛОВ      ║
║                                                ║
║ [3] СНОС БОТОВ           [4] СНОС ЧАТОВ        ║
║                                                ║
║ [5] Check Mail           [6] Create Mail       ║
║       (soon)                   (soon)          ║
║                                                ║
║         Please, dont use for revenge!          ║
║              t.me/spider_rep                   ║                                  
╚================================================╝
'''

color_code = {
    "reset": "\033[0m",  
    "underline": "\033[04m", 
    "green": "\033[32m",     
    "yellow": "\033[93m",    
    "red": "\033[31m",       
    "cyan": "\033[36m",     
    "bold": "\033[01m",        
    "pink": "\033[95m",
    "url_l": "\033[36m",       
    "li_g": "\033[92m",      
    "f_cl": "\033[0m",
    "dark": "\033[90m",     
}

alignment = "{:>50}".format(banner)
banner = Colorate.Horizontal(Colors.blue_to_red, alignment)
print(banner)

def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        if 'gmail.com' in sender_email:
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
        elif 'rambler.ru' in sender_email:
            smtp_server = 'smtp.rambler.ru'
            smtp_port = 587
        elif 'hotmail.com' in sender_email:
            smtp_server = 'smtp.office365.com'
            smtp_port = 587
        elif 'mail.ru' in sender_email:
            smtp_server = 'smtp.mail.ru'
            smtp_port = 587
        else:
            raise ValueError("Unsupported email provider")
        
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        server.quit()
        
        return True
    except Exception as e:
        return False

def main():
    sent_emails = 0
    choice = input(f'{color_code["cyan"]}[root]{color_code["bold"]} Выбор пункта >{color_code["yellow"]} ')

    if choice == '1':
        print("1. ЗА СПАМ, РЕКЛАМУ")
        print("2. ЗА ДОКСUНГ")
        print("3. ЗА ТРОЛЛUНГ(ОСК)")
        print("4. ПР0ДАЖА/РЕКЛАМА НАРК0ТЫ")
        print("5. КУРАТ0РСТВО В НАРК0ШОПЕ")
        print("6. ПРОДАЖА ЦП")
        print("7. ВbIМ0ГАНUЕ UНТUМНЫХ ФОТО У НЕСОВЕРШЕННОЛЕТНUХ")
        print("8. УГНЕТАНUЕ НАЦИИ")
        print("9. УГНЕТАНUЕ РЕЛUГUU")
        print("10. РАСПР0СТР0НЯЕТ РАСЧЛЕНЕНКУ")
        print("11. РАСПР0СТР0НЯЕТ ЖUВОДЕРКУ")
        print("12. РАСПР0СТР0НЯЕТ ПОРНУХУ")
        print("13. СУТЕНЕР(ШЛЮХ ПРОДАЕТ)")
        print("14. ПРUЗЫВ К САМ0ВbIПUЛУ")
        print("15. ПРUЗbIВ К ТЕРР0РУ")
        print("16. УГРОЗbI СВАТА U ТП")
        print("17. УГРОЗbI РАСПРАВbI")
        print("18. СНОС СЕССИЙ")
        print("19. С ВUРТ Н0МЕРОМ")
        print("20. С ПРEМКОЙ")
        print("21. ПР0СТ0 СН0С (НЕ ЭФФЕКТUВЕН)")
        cprint("----------------------------------" , "black")
        comp_choice = input("Выбор пункта > ")
        cprint("----------------------------------" , "black")

        if comp_choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17" ]:
            print("СЛЕДУЙ УКАЗАНUЯМ")
            username = input("USERNAME: ")
            id = input("TG ID: ")
            chat_link = input("CCbIЛКА НА ЧАТ: ")
            violation_link = input("ССbIЛКА НА НАРУШЕНUЕ В ЧАТЕ: ")
            cprint("----------------------------------" , "black")
            cprint("АТАКА НАЧАЛАСb" , "red")
            cprint("----------------------------------" , "black")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка. На вашей платформе я нашел пользователя который отправляет много ненужных сообщений - СПАМ. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю.",
                "2": f"Здравствуйте, уважаемая поддержка, на вашей платформе я нашел пользователя, который распространяет чужие данные без их согласия. его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта.",
                "3": f"Здравствуйте, уважаемая поддержка телеграм. Я нашел пользователя который открыто выражается нецензурной лексикой и спамит в чатах. его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта.",
                "4": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который продает и рекламирует наркотические вещества. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры по отношению к данному пользоателю путем блокировки его аккаунта.",
                "5": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который привлекает людей в сферу нарко-бизнеса. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировни его аккаунта.",
                "6": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который продает порнографические материалы с участием несовешеннолетних. Его юзернейм - {username}, его айди {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его аккаунта.",
                "7": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который вымогает фото интимного характера у несовершенно летних, его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры к данному пользователю путем блокировки его аккаунта.",
                "8": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который угнетает нацию и разжигает конфликты. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры по отношению к данному пользователб=ю путем блокировки его аккаунта.",
                "9": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который угнетает религию и разжигает конфликты. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры по отношению к данному пользоателю путем блокировки его аккаунта.",
                "10": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который распростроняет видео и фото шокирущего контента с убийством людей. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его аккаунта.",
                "11": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который распростроняет видео и фото шокирующего контента с убийством животных. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его аккаунта.",
                "12": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который распростроняет фото и видео порнографического типа. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его аккаунта.",
                "13": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который продает услуги проституции. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его аккаунта.",
                "14": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который отправляет сообщения которые приводят людей к суициду. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примине меры по отношению к данному пользователю путем блокировки его аккаунта.",
                "15": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который отправляет сообщения с призывом к террризму. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его аккаунта.",
                "16": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который угрожает людям распростронением личной информации. Его юзернейи - {username}, его айди {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его аккаунта.",
                "17": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя который угрожает людям расправой. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его аккаунта."
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip(), chat_link=chat_link.strip(),
                                                 violation_link=violation_link.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на аккаунт телеграм', comp_body)
                    cprint(f"ОТПРАВЛЕНО НА {receiver} 0Т {sender_email}", "green")
                    sent_emails += 14888
                    time.sleep(5)

        elif comp_choice in ["18", "21"]:
            print("СЛЕДУЙ УКАЗАНUЯМ")
            username = input("USERNAME: ")
            id = input("TG ID: ")
            cprint("----------------------------------" , "black")
            cprint("АТАКА НАЧАЛАСb" , "red")
            cprint("----------------------------------" , "black")
            comp_texts = {
                "18": f"Здравствуйте, уважаемая поддержка. Я случайно перешел по фишинговой ссылке и утерял доступ к своему аккаунту. Его юзернейм - {username}, его айди - {id}. Пожалуйста удалите аккаунт или обнулите сессии",
                "21": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел пользователя с подозрительной активностью на аккаунте. Его юзернейм - {username}, его айди - {id}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки аккаунта."
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Я утерял свой аккаунт в телеграм', comp_body)
                    cprint(f"ОТПРАВЛЕНО НА {receiver} 0Т {sender_email}", "green")
                    sent_emails += 14888
                    time.sleep(5)

        elif comp_choice in ["19", "20"]:
            print("СЛЕДУЙ УКАЗАНUЯМ")
            username = input("USERNAME: ")
            id = input("TG ID: ")
            cprint("----------------------------------" , "black")
            cprint("АТАКА НАЧАЛАСb" , "red")
            cprint("----------------------------------" , "black")
            comp_texts = {
                "19": f"Добрый день поддержка Telegram!Аккаунт {username} , {id} использует виртуальный номер купленный на сайте по активации номеров. Отношения к номеру он не имеет, номер никак к нему не относиться.Прошу разберитесь с этим. Заранее спасибо!",
                "20": f"Добрый день поддержка Telegram! Аккаунт {username} {id} приобрёл премиум в вашем мессенджере чтобы рассылать спам-сообщения и обходить ограничения Telegram.Прошу проверить данную жалобу и принять меры!"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на пользователя телеграм', comp_body)
                    cprint(f"ОТПРАВЛЕНО НА {receiver} 0Т {sender_email}", "green")
                    sent_emails += 14888
                    time.sleep(5)


    elif choice == "2":
        
        print("1. С ЛUЧНЫМU ДАННЫМU")
        print("2. С ЖUВОДЕРСТВ0М ")
        print("3. С ДЕТСКUМ П0РНО")
        print("4. ДЛЯ КАНАЛ0В ТИПА ПРАЙСОВ")
        print("5. С РАСЧЛЕНЕНК0Й")
        print("6. РУЛЕТКU (КАЗUК)")
        print("7. НАРК0-Ш0П")
        print("8. ПРUЗbIВ К ТЕРРОРУ")
        print("9. ПРUЗbIВ К САМ0ВbIПUЛУ")
        print("10. РАЗЖUГАНUE НЕНАВUCTU")
        print("11. ПРОПОГАНДА НАСUЛUЯ")
        print("12. ПРОДАЖА ДЕТСКUХ UНТUМ0К")
        print("13. УГНЕТЕНUЕ НАЦUU")
        print("14. УГНЕТЕНUЕ РЕЛUГUU")
        print("15. С П0РНУХОЙ")
        cprint("----------------------------------" , "black")
        ch_choice = input("ВbIБUРАЙ: ")
        cprint("----------------------------------" , "black")

        if ch_choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]:
            channel_link = input("ССbIЛКА НА КАНАЛ: ")
            channel_violation = input("ССbIЛКА НА НАРУШЕНUЕ В КАНАЛЕ: ")
            cprint("----------------------------------" , "black")
            cprint("АТАКА НАЧАЛАCb" , "red")
            cprint("----------------------------------" , "black")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал, который распространяет личные данные невинных людей. Ссылка на канал - {channel_link}, ссылки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "2": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который распространяет жестокое обращение с животными. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "3": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который распространяет порнографию с участием несовершеннолетних. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "4": f"Здравствуйте, уважаемый модератор телеграмма. хочу пожаловаться вам на канал,который продает услуги доксинга, сваттинга. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                "5": f"Здравствуйте, уважаемая поддержка Телеграмма. На вашей платформе я нашел канал который распространяет шокирующие кадры убийства людей. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                "6": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который распростроняет рулетки или же казино, которые запрещены на территории РФ статьей 171 УКРФ. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                "5": f"Здравствуйте, уважаемая поддержка Телеграмма. На вашей платформе я нашел канал который распространяет шокирующие кадры убийства людей. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                "7": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который пропогондирует продажу наркотических веществ, которые запрещены на территории РФ статьей 228.1 УКРФ. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                "8": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который призывает людей к террору что запрещено на территории РФ статьей 205.2 УКРФ. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                "9": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который призывает людей к суициду что запрещено на территории РФ статьей 110.1 УКРФ. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                "10": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который разжигает ненависть в сторону определенных людей или же групп лиц. Ссылка на канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                "11": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который пропогандирует насилие что запрещено на территории РФ статьей 282 УКРФ. Ссылка на канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                "12": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который занимается продажей детских интимных фото что запрещено на территории РФ статьей 242.1 УКРФ. Ссылка на канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                "13": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который пропогондирует угнетение нации что запрещено на территории РФ статьей 282 УКРФ. Ссылка на канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                "14": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который пропогондирует угнетение религии что запрещено на территории РФ статьей 148 УКРФ. Ссылка на канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                "15": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который пропогонирует порнографические материалы. Ссыока на канал - {channel_link}, Ссылка на нарушение - {channel_violation}. Просьба заблокировать данный канал."
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[ch_choice]
                    comp_body = comp_text.format(channel_link=channel_link.strip(), channel_violation=channel_violation.strip)
                    send_email(receiver, sender_email, sender_password, 'Жалоба на телеграм канал', comp_body)
                    cprint(f"ОТПРАВЛЕНО НА {receiver} 0Т {sender_email}", "green")
                    sent_emails += 100000
                    time.sleep(5)


    elif choice == "3":
        print("1. ГЛА3 Б0ГА ")
        print("2. ТUПА СUНЕГ0 КUТА")
        print("3. ПР0ДАЖА ЦП")
        print("4. М0ШЕННИЧЕСКUЕ СХЕМЫ")
        print("5. СПАМ, РЕКЛАМА")
        print("6. ШАНТАЖ")
        print("7. UЗВРАЩЕНUЯ(СНАФФ,ЦП U ТП)")
        cprint("----------------------------------" , "black")
        bot_ch = input("ВbIБUРАЙ: ")
        cprint("----------------------------------" , "black")

        if bot_ch in ["1", "2", "3", "4", "5", "6", "7"]:
            bot_user = input("USERNAME BOTA: ")
            cprint("----------------------------------" , "black")
            cprint("АТАКА НАЧАЛАСb" , "red")
            cprint("----------------------------------" , "black")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел бота, который осуществляет поиск по личным данным ваших пользователей. Ссылка на бота - {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота.",
                "2": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел бота который путем заданий приводит людей к суициду что запрещено на территории РФ статьей 110.1 УКРФ. Ссылка на бота {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота.",
                "3": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел бота который продает порнографические материалы с участием лиц не достигших совершеннолетия, что запрещено на территории РФ статьей 242.1 УКРФ. Ссылка на бота {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота.",
                "4": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел бота который занимается мошенническими схемами и обманывает людей на деньги что запрещено на территории РФ статьей 159 УКРФ. Ссылка на бота {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота.",
                "5": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел бота который рассылает навязчивую рекламу и спамит ей в чатах. Ссылка на бота {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота.",
                "6": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел бота который путем шантажа вымогает из людей деньги, личные данные и другие вещи. Ссылка на бота {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота.",
                "7": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел бота который распростроняет видео шокируещего контента по типу детского порно и расчленения людей. Ссылка на бота {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота."
             }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[bot_ch]
                    comp_body = comp_text.format(bot_user=bot_user.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на бота телеграм', comp_body)
                    cprint(f"ОТПРАВЛЕНО НА {receiver} 0Т {sender_email}", "green")
                    sent_emails += 10000
                    time.sleep(5)
        
    elif choice == "4":
        print("1. ПРОСТО СНОС(НЕ ЭФФЕКТUВЕН)")
        print("2. СПАМ/РЕКЛАМА")
        print("3. ЗА АВУ UЛU НАЗВАНUЕ")
        print("4. ПР0П0ГАНДА НАСИЛИЯ U ТП")
        print("5. НАКРУТКА")
        print("6. ОСКU В ЧАТЕ")
        cprint("----------------------------------" , "black")
        bottik = input("ВbIБUРАЙ: ")
        cprint("----------------------------------" , "black")

        if bottik in ["1", "2", "3", "4", "5"]:
            user_chat = input("ССbIЛКА НА ЧАТ: ")
            id_chat = input("TG ID ЧАТА: ")
            cprint("----------------------------------" , "black")
            cprint("АТАКА НАЧАЛАСb" , "red")
            cprint("----------------------------------" , "black")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел группу с подозрительной активностью. Ссылка на группу - {user_chat}, Айди группы - {id_chat}. Пожалуйста примите меры в сторону данной группы и заблокируйте ее.",
                "2": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел группу в которой проходят спам-рассылки. Ссылка на группу - {user_chat}, Айди группы - {id_chat}. Пожалуйста примите меры в сторону этой группы и заблокируйте ее как можно скорее.",
                "3": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел группу в которой стоит вызывающая аватарка и имя, разжигающее конфликты. Ссылка на группу - {user_chat}, Айди группы - {id_chat}. Пожалуйста примите меры в сторону этой группы и заблокируйте ее как можно скорее.",
                "4": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел группу в которой пропогондируется насилие и другие подобные жестокости. Ссылка на группу - {user_chat}, Айди группы - {id_chat}. Пожалуйста примите меры в сторону этой группы и заблокируйте ее как можно скорее",
                "5": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел группу в которой происходит накрутка подписчиков. Ссылка на группу - {user_chat}, Айди группы - {id_chat}. Пожалуйста примите меры в сторону этой группы и заблокируйте ее как можно скорее"
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[bottik]
                    comp_body = comp_text.format(user_chat=user_chat.strip(), id_chat=id_chat.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на группу телеграм', comp_body)
                    cprint(f"ОТПРАВЛЕНО НА {receiver} 0Т {sender_email}", "green")
                    sent_emails += 10000
                    time.sleep(5)     

        elif bottik == "6":
            username_chat = input("ССbIЛКА НА ЧАТ: ")    
            idtg_chata = input("TG ID CHATA: ")   
            ssilka = input("ССbIЛКА НА НАРУШЕНUЕ: ")
            cprint("----------------------------------" , "black")  
            cprint("ATAKA НАЧАЛАСb" , "red")
            cprint("----------------------------------" , "black")
            comp_texts = {
                "6": f"Здравствуйте, уважаемая поддержка телеграмма. Я нашел группу с которой оскорбляют людей и используют ненормативную лексику в их сторону. Ссылка на группу - {username_chat}, Айди группы - {idtg_chata}, Ссылка на нарушение - {ssilka}. Пожалуйста примите меры в сторону этой группы и заблокируйте ее как можно скорее"
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[bottik]
                    comp_body = comp_text.format(username_chat=username_chat.strip(), idtg_chata=idtg_chata.strip(), ssilka=ssilka.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на группу телеграм', comp_body)
                    cprint(f"ОТПРАВЛЕНО НА {receiver} 0Т {sender_email}", "green")
                    sent_emails += 10000
                    time.sleep(5)     

  
if __name__ == "__main__":
    main()
    