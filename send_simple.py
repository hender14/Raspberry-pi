from socket import *

##################
# 送信側プログラム#
##################

# 送信側アドレスの設定
# 送信側IP
#SrcIP = "192.168.43.56"
SrcIP = "192.168.128.130"
# 送信側ポート番号
SrcPort = 8888
# 送信側アドレスをtupleに格納
SrcAddr = (SrcIP,SrcPort)
# バッファサイズ指定
BUFSIZE = 1024

# 受信側アドレスの設定
# 受信側IP
DstIP = "54.248.64.253"
# 受信側ポート番号
DstPort = 8888
# 受信側アドレスをtupleに格納
DstAddr = (DstIP,DstPort)

#クラス定義
class SendData:
  def ComHeader(self):
    version = 1.0
    type = 'car'

  def message(self):
    direction = 'straight'
    speed = 50

# ソケット作成
udpClntSock = socket(AF_INET, SOCK_DGRAM)
# 送信側アドレスでソケットを設定
udpClntSock.bind(SrcAddr)


# 送信データの作成
data = 'demand'
version = '1.0'
# バイナリに変換
data = data.encode('utf-8')
version = version.encode('utf-8')

# 受信側アドレスに送信
udpClntSock.sendto(data, DstAddr)
udpClntSock.sendto(version, DstAddr)
maindata, addr = udpClntSock.recvfrom(BUFSIZE) 

print(maindata.decode(), addr)
udpClntSock.sendto(maindata,DstAddr)

udpClntSock.close()