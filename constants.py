from database import DataBase
from datetime import datetime
from bittrex_utils import *
import logging as log
log.basicConfig(filename='errors.log',level=log.ERROR)

DB = DataBase(host="104.236.177.161",    # your host, usually localhost
                     user="kurush",         # your username
                     passwd="=2@fcM6LT6Vg=Exe",  # your password
                     db="crypto")        # name of the data base


currency_names = {"BTC":"Bitcoin","LTC":"Litecoin","DOGE":"Dogecoin","VTC":"Vertcoin","PPC":"Peercoin","FTC":"Feathercoin","RDD":"ReddCoin","NXT":"NXT","DASH":"Dash","POT":"PotCoin","BLK":"BlackCoin","EMC2":"Einsteinium","XMY":"Myriad","AUR":"AuroraCoin","UTC":"UltraCoin","MZC":"MazaCoin","EFL":"ElectronicGulden","GLD":"GoldCoin","FAIR":"FairCoin","SLR":"SolarCoin","PTC":"PesetaCoin ","GRS":"Groestlcoin","NLG":"Gulden","RBY":"RubyCoin","XWC":"WhiteCoin","MONA":"MonaCoin","BITS":"BitStarCoin","OC":"OrangeCoin","THC":"HempCoin","ENRG":"EnergyCoin","SFR":"SaffronCoin","ERC":"EuropeCoin","NAUT":"NautilusCoin","VRC":"VeriCoin","CURE":"CureCoin","BLC":"BlakeCoin","XC":"XCurrency","XDQ":"Dirac","XBB":"Boolberry","HYPER":"Hyper","CCN":"CannaCoin","XMR":"Monero","CLOAK":"CloakCoin","BSD":"BitSend","CRYPT":"CryptCoin","START":"StartCoin","KORE":"KoreCoin","XDN":"DigitalNote","TRK":"TruckCoin","TRUST":"TrustPlus","NAV":"NAVCoin","XST":"StealthCoin","APEX":"ApexCoin","BTCD":"BitcoinDark","VIA":"ViaCoin","TRI":"Triangles","UNO":"Unobtanium","PINK":"PinkCoin","IOC":"I/OCoin","MAX":"MaxCoin","LXC":"LibrexCoin","BOB":"DobbsCoin","CANN":"CannabisCoin","FC2":"FuelCoin","SSD":"SonicCoin","J":"JoinCoin","SYS":"SysCoin","NEOS":"NeosCoin","DGB":"Digibyte","ROOT":"RootCoin","BTS":"BitShares","BURST":"BURST","TIT":"TitCoin","BSTY":"GlobalBoost-Y","PXI":"Prime-XI","DGC":"DigitalCoin","SLG":"Sterlingcoin","STV":"SativaCoin","EXCL":"ExclusiveCoin","SWIFT":"Bitswift","NET":"NetCoin","GHC":"GamerholicCoin","DOPE":"DopeCoin","BLOCK":"BlockNet","ABY":"ArtByte","VIOR":"ViorCoin","BYC":"Bytecent","UFO":"UFOCoin","XMG":"Magi","XQN":"Quotient","BLITZ":"Blitzcash","VPN":"VPNCoin","BAY":"BitBay","DTC":"DayTraderCoin","AM":"AeroME","METAL":"MetalCoin","SPR":"SpreadCoin","VTR":"vTorrent","XPY":"Paycoin","XRP":"Ripple","GAME":"GameCredits","GP":"GoldPieces","NXS":"Nexus","COVAL":"Circuits of Value","FSC2":"FriendshipCoin2","SOON":"SoonCoin","HZ":"Horizon","XCP":"Counterparty","BITB":"BitBean","XTC":"TileCoin","XVG":"Verge","GEO":"GeoCoin","FLDC":"FoldingCoin","GEMZ":"Gemz","GRC":"GridCoin","XCO":"X-Coin","MTR":"MasterTraderCoin","FLO":"Florin","U":"UCoin","NBT":"Nubits","XEM":"NewEconomyMovement","MUE":"MonetaryUnit","XVC":"Vcash","8BIT":"8bit","CLAM":"CLAMs","XSEED":"BitSeeds","NTRN":"Neutron","SLING":"Sling","DMD":"Diamond","GAM":"Gambit","UNIT":"UniversalCurrency","GRT":"Grantcoin","VIRAL":"Viral","SPHR":"Sphere","ARB":"ArbitCoin","OK":"OkCash","ADC":"AudioCoin","SNRG":"Synergy","PKB":"ParkByte","TES":"TeslaCoin","CPC":"CapriCoin","AEON":"Aeon","BITZ":"Bitz","ETH":"Ethereum","GCR":"GlobalCurrencyReserve","TX":"TransferCoin","BCY":"BitCrystals","PRIME":"PrimeChain","EXP":"Expanse","NEU":"NeuCoin","SWING":"SwingCoin","INFX":"InfluxCoin","OMNI":"OmniCoin","USDT":"Tether","AMP":"SynereoAmp","AGRS":"IDNI Agoras","XLM":"Lumen","SPRTS":"Sprouts","YBC":"YBCoin","BTA":"Bata","MEC":"MegaCoin","BITCNY":"BitCNY","AMS":"AmsterdamCoin","SCRT":"SecretCoin","SCOT":"ScotCoin","CLUB":"ClubCoin","VOX":"Voxels","MND":"MindCoin","EMC":"EmerCoin","FCT":"Factom","MAID":"MaidSafeCoin","FRK":"Franko","EGC":"EverGreenCoin","SLS":"SaluS","ORB":"OrbitCoin","STEPS":"Steps","RADS":"Radium","DCR":"Decred","SAFEX":"SafeExchangeCoin","PIVX":"Pivx","WARP":"WarpCoin","CRBIT":"CreditBit","MEME":"Memetic","STEEM":"STEEM","2GIVE":"2GIVE","LSK":"Lisk","KR":"Krypton","PDC":"Project Decorum","DGD":"Digix DAO","BRK":"Breakout","WAVES":"Waves","RISE":"Rise","LBC":"LBRY Credits","SBD":"SteemDollars","BRX":"Breakout Stake","DRACO":"DT Token","ETC":"Ethereum Classic","UNIQ":"Uniqredit","STRAT":"Stratis","UNB":"UnbreakableCoin","SYNX":"Syndicate","TRIG":"TRIG Token","EBST":"eBoost","VRM":"Verium","XAUR":"Xaurum","SEQ":"Sequence","SNGLS":"SingularDTV","REP":"Augur","SHIFT":"Shift","ARDR":"Ardor","XZC":"ZCoin","NEO":"Neo","ZEC":"ZCash","ZCL":"Zclassic","IOP":"Internet Of People","DAR":"Darcrus","GOLOS":"Golos","GBG":"Gbg","UBQ":"Ubiq","HKG":"HackerGold","KMD":"Komodo","SIB":"Siberian Chervonets","ION":"Ion","LMC":"Lomocoin","QWARK":"Qwark","CRW":"Crown","SWT":"Swarm City Token","TIME":"Chronobank Time","MLN":"Melon","TKS":"Tokes","ARK":"Ark","DYN":"Dynamic","MUSIC":"Musicoin","DTB":"Databits","INCNT":"Incent","GBYTE":"Byteball","GNT":"Golem","NXC":"Nexium","EDG":"Edgeless","LGD":"Legends","TRST":"Trustcoin","WINGS":"Wings DAO","RLC":"iEx.ec","GNO":"Gnosis","GUP":"Guppy","LUN":"Lunyr","APX":"Apx","TKN":"TokenCard","HMQ":"Humaniq","ANT":"Aragon","ZEN":"ZenCash","SC":"Siacoin","BAT":"Basic Attention Token","1ST":"Firstblood","QRL":"Quantum Resistant Ledger","CRB":"CreditBit","TROLL":"Bittrex Test Currency","PTOY":"Patientory","MYST":"Mysterium","CFI":"Cofound.it","BNT":"Bancor","NMR":"Numeraire","SNT":"Status Network Token","DCT":"DECENT","XEL":"Elastic","MCO":"Monaco","ADT":"adToken","FUN":"FunFair","PAY":"TenX Pay Token","MTL":"METAL","STORJ":"STORJ","ADX":"AdEx","OMG":"OmiseGO","CVC":"Civic","PART":"Particl","QTUM":"Qtum","BCC":"Bitcoin Cash","DNT":"district0x"}
tx_fees = {"Bitcoin" : 0.001,"Litecoin" : 0.002,"Dogecoin" : 2.0,"Vertcoin" : 0.02,"Peercoin" : 0.02,"Feathercoin" : 0.2,"ReddCoin" : 2.0,"NXT" : 2.0,"Dash" : 0.002,"PotCoin" : 0.002,"BlackCoin" : 0.02,"Einsteinium" : 0.2,"Myriad" : 0.2,"AuroraCoin" : 0.002,"UltraCoin" : 0.02,"MazaCoin" : 0.2,"ElectronicGulden" : 0.2,"GoldCoin" : 0.0002,"FairCoin" : 0.02,"SolarCoin" : 0.2,"PesetaCoin " : 0.002,"Groestlcoin" : 0.2,"Gulden" : 0.2,"RubyCoin" : 0.02,"WhiteCoin" : 0.2,"MonaCoin" : 0.2,"BitStarCoin" : 0.002,"OrangeCoin" : 0.2,"HempCoin" : 0.2,"EnergyCoin" : 0.2,"SaffronCoin" : 0.2,"EuropeCoin" : 0.2,"NautilusCoin" : 2.0,"VeriCoin" : 0.0002,"CureCoin" : 0.0002,"BlakeCoin" : 0.2,"XCurrency" : 2e-05,"Dirac" : 0.02,"Boolberry" : 0.0002,"Hyper" : 0.02,"CannaCoin" : 0.02,"Monero" : 0.04,"CloakCoin" : 0.02,"BitSend" : 0.002,"CryptCoin" : 0.02,"StartCoin" : 0.02,"KoreCoin" : 0.02,"DigitalNote" : 0.01,"TruckCoin" : 0.02,"TrustPlus" : 0.02,"NAVCoin" : 0.2,"StealthCoin" : 0.02,"ApexCoin" : 0.02,"BitcoinDark" : 0.02,"ViaCoin" : 0.2,"Triangles" : 0.0002,"Unobtanium" : 0.0002,"PinkCoin" : 0.2,"I/OCoin" : 0.2,"MaxCoin" : 0.2,"LibrexCoin" : 0.02,"DobbsCoin" : 0.02,"CannabisCoin" : 0.2,"FuelCoin" : 0.02,"SonicCoin" : 0.02,"JoinCoin" : 0.02,"SysCoin" : 0.0002,"NeosCoin" : 0.02,"Digibyte" : 0.2,"RootCoin" : 0.2,"BitShares" : 5.0,"BURST" : 2.0,"TitCoin" : 0.2,"GlobalBoost-Y" : 0.2,"Prime-XI" : 0.2,"DigitalCoin" : 0.2,"Sterlingcoin" : 0.2,"SativaCoin" : 0.2,"ExclusiveCoin" : 0.2,"Bitswift" : 2.0,"NetCoin" : 0.2,"GamerholicCoin" : 0.2,"DopeCoin" : 0.002,"BlockNet" : 0.2,"ArtByte" : 0.2,"ViorCoin" : 0.2,"Bytecent" : 0.02,"UFOCoin" : 0.2,"Magi" : 0.0002,"Quotient" : 0.02,"Blitzcash" : 0.02,"VPNCoin" : 0.2,"BitBay" : 0.2,"DayTraderCoin" : 0.2,"AeroME" : 0.2,"MetalCoin" : 20.0,"SpreadCoin" : 0.2,"vTorrent" : 0.02,"Paycoin" : 0.002,"Ripple" : 0.02,"GameCredits" : 0.2,"GoldPieces" : 0.2,"Nexus" : 0.2,"Circuits of Value" : 200.0,"FriendshipCoin2" : 0.2,"SoonCoin" : 0.2,"Horizon" : 2.0,"Counterparty" : 0.2,"BitBean" : 0.2,"TileCoin" : 100.0,"Verge" : 0.2,"GeoCoin" : 0.002,"FoldingCoin" : 150.0,"Gemz" : 5.0,"GridCoin" : 0.2,"X-Coin" : 0.02,"MasterTraderCoin" : 0.2,"Florin" : 0.2,"UCoin" : 0.2,"Nubits" : 0.02,"NewEconomyMovement" : 15.0,"MonetaryUnit" : 0.02,"Vcash" : 0.002,"8bit" : 0.002,"CLAMs" : 0.2,"BitSeeds" : 0.002,"Neutron" : 0.02,"Sling" : 0.002,"Diamond" : 0.002,"Gambit" : 0.02,"UniversalCurrency" : 2.0,"Grantcoin" : 2.0,"Viral" : 0.002,"Sphere" : 0.002,"ArbitCoin" : 0.02,"OkCash" : 0.2,"AudioCoin" : 2.0,"Synergy" : 0.002,"ParkByte" : 0.02,"TeslaCoin" : 0.2,"CapriCoin" : 0.2,"Aeon" : 0.1,"Bitz" : 0.02,"Ethereum" : 0.005,"GlobalCurrencyReserve" : 0.02,"TransferCoin" : 0.02,"BitCrystals" : 5.0,"PrimeChain" : 0.02,"Expanse" : 0.01,"NeuCoin" : 0.02,"SwingCoin" : 0.1,"InfluxCoin" : 0.1,"OmniCoin" : 0.1,"Tether" : 5.0,"SynereoAmp" : 0.1,"IDNI Agoras" : 0.1,"Lumen" : 0.01,"Sprouts" : 1.0,"YBCoin" : 1.0,"Bata" : 1.0,"MegaCoin" : 1.0,"BitCNY" : 1.5,"AmsterdamCoin" : 1.0,"SecretCoin" : 1.0,"ScotCoin" : 5.0,"ClubCoin" : 0.02,"Voxels" : 0.1,"MindCoin" : 1.0,"EmerCoin" : 0.02,"Factom" : 0.1,"MaidSafeCoin" : 1.0,"Franko" : 0.002,"EverGreenCoin" : 0.2,"SaluS" : 0.002,"OrbitCoin" : 0.2,"Steps" : 0.2,"Radium" : 0.2,"Decred" : 0.03,"SafeExchangeCoin" : 1.0,"Pivx" : 0.02,"WarpCoin" : 0.02,"CreditBit" : 1.0,"Memetic" : 0.02,"STEEM" : 0.01,"2GIVE" : 0.01,"Lisk" : 0.1,"Krypton" : 0.01,"Project Decorum" : 1.0,"Digix DAO" : 0.01,"Breakout" : 0.02,"Waves" : 0.001,"Rise" : 0.1,"LBRY Credits" : 0.02,"SteemDollars" : 0.01,"Breakout Stake" : 0.02,"DT Token" : 2.0,"Ethereum Classic" : 0.01,"Uniqredit" : 0.1,"Stratis" : 0.2,"UnbreakableCoin" : 0.2,"Syndicate" : 0.2,"TRIG Token" : 50.0,"eBoost" : 0.1,"Verium" : 0.4,"Xaurum" : 0.1,"Sequence" : 0.2,"SingularDTV" : 1.0,"Augur" : 0.1,"Shift" : 0.01,"Ardor" : 2.0,"ZCoin" : 0.02,"Neo" : 0.025,"ZCash" : 0.0002,"Zclassic" : 0.002,"Internet Of People" : 0.2,"Darcrus" : 1.0,"Golos" : 0.01,"Gbg" : 0.01,"Ubiq" : 0.01,"HackerGold" : 0.1,"Komodo" : 0.002,"Siberian Chervonets" : 0.2,"Ion" : 0.2,"Lomocoin" : 0.2,"Qwark" : 0.1,"Crown" : 0.02,"Swarm City Token" : 0.1,"Chronobank Time" : 0.1,"Melon" : 0.003,"Tokes" : 0.1,"Ark" : 0.1,"Dynamic" : 0.02,"Musicoin" : 0.01,"Databits" : 5.0,"Incent" : 0.1,"Byteball" : 0.002,"Golem" : 0.01,"Nexium" : 0.01,"Edgeless" : 1.0,"Legends" : 0.01,"Trustcoin" : 0.01,"Wings DAO" : 0.01,"iEx.ec" : 0.01,"Gnosis" : 0.005,"Guppy" : 0.01,"Lunyr" : 0.01,"Apx" : 0.1,"TokenCard" : 0.01,"Humaniq" : 0.01,"Aragon" : 0.01,"ZenCash" : 0.002,"Siacoin" : 0.1,"Basic Attention Token" : 0.01,"Firstblood" : 0.01,"Quantum Resistant Ledger" : 0.01,"CreditBit" : 0.01,"Bittrex Test Currency" : 0.001,"Patientory" : 0.01,"Mysterium" : 0.01,"Cofound.it" : 0.01,"Bancor" : 0.01,"Numeraire" : 0.01,"Status Network Token" : 0.01,"DECENT" : 0.1,"Elastic" : 0.2,"Monaco" : 0.01,"adToken" : 0.01,"FunFair" : 0.01,"TenX Pay Token" : 0.01,"METAL" : 0.01,"STORJ" : 0.01,"AdEx" : 0.01,"OmiseGO" : 0.01,"Civic" : 0.01,"Particl" : 0.1,"Qtum" : 0.01,"Bitcoin Cash" : 0.001,"district0x" : 0.01}
top_100 = ["Bitcoin","Ethereum","Bitcoin Cash","Ripple","Litecoin","IOTA","NEM","Dash","NEO","Ethereum Classic","Monero","BitConnect","OmiseGo","Qtum","Stratis","Zcash","Waves","EOS","TenX","BitShares","Tether","Lisk","Steem","Iconomi","Binance Coin","Augur","network","Veritaseum","MaidSafeCoin","bcn","Factom","Stellar Lumens","Siacoin","Dogecoin","basic","gno","Byteball","0x","Status","Ark","Metal","Civic","Populous","DigixDAO","Decred","MCAP","Ardor","Komodo","GameCredits","Monaco","Bytom","DigiByte","district0x","Nxt","Bancor","FunFair","PIVX","Lykke","MobileGo","Aragon","ICO","SingularDTV","Pillar","Storj","Nexus","BitcoinDark","Gas","Stox","Bitquence","cofound.it","Ubiq","DECENT","Metaverse ETP","SysCoin","AdEx","Asch","FirstBlood","Particl","iExec RLC","Wings","Blocknet","LEOcoin","Melon","Numeraire","Emercoin","Counterparty","Peercoin","Round","Elastic","Rialto","TokenCard","Gulden","NoLimitCoin","Etheroll","OpenAnx","adToken","vSlice","I/O Coin","TaaS","XEM","New Economy Movement"]

ROUNDING_VALUE = 12

MESSAGE = "message"
RESULT = "result"
SUCCESS = "success"