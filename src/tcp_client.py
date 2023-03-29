import socket

target_ip = "192.168.237.102" # Vision-navigation-systemが動いているPCのIPアドレス
target_port = 55550 # 55550で固定
buffer_size = 4096  # 受信に十分な程度の2**nサイズ

# 1.ソケットオブジェクトの作成
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_client:
    
    # 2.サーバ(Vision-navigation-system)に接続
    tcp_client.connect((target_ip,target_port))

    # 3. パケットヘッダを作成
    packet_str = b'\xff\x00\x00\x00\xab\xcd\xef\xff'

    while True:
        print('input command', end='-> ')
        command = input() # コマンド用の文字列を入力(OPENなど)
        command = packet_str + command.encode()
        # 4.サーバにデータを送信
        tcp_client.send(command)

        # 5.サーバからのレスポンスを受信
        response = tcp_client.recv(buffer_size)
        print("[*]Received a response : {}".format(response))

