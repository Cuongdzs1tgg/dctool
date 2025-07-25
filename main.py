from curl_cffi import requests
import time,os,sys
from time import strftime
from colorama import Fore,ansi,init,Style
import random,json
from lamJob import THREADS,TIM
def man_hinh():
    os.system("cls" if os.name == "nt" else "clear")
    banner = f"""

                                                                                            

    \033[1;3m██████╗  ██████╗    ████████╗ ██████╗  ██████╗ ██╗     
    \033[1;3m██╔══██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
    \033[1;34m██║  ██║██║            ██║   ██║   ██║██║   ██║██║     
    \033[1;34m██║  ██║██║            ██║   ██║   ██║██║   ██║██║     
    \033[1;36m██████╔╝╚██████╗       ██║   ╚██████╔╝╚██████╔╝███████╗
    \033[1;36m╚═════╝  ╚═════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                        
    \033[1;31m────────────────────────────────────────────────────────────
    \033[0;32mADMIN : Nguyễn Đăng Cương
    \033[0;32mMới Tập làm Tool Có lỗi Anh Em Bỏ Qua Nhé !
    """
    for char in banner:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)  # Điều chỉnh tốc độ in từng ký tự
    print("\n")
    # Khởi tạo Colorama
    init(autoreset=True)
TOKEN_GLOBAL = None 
colors = [Fore.GREEN, Fore.BLUE,Fore.CYAN, Fore.MAGENTA,Fore.BLACK,Fore.LIGHTMAGENTA_EX,Fore.LIGHTBLUE_EX,Fore.LIGHTCYAN_EX,Fore.LIGHTYELLOW_EX]
color = random.choice(colors)
class API:
    def lay_token():
        global TOKEN_GLOBAL
        filename = 'Authorization.txt'

        # Nếu token đã tồn tại trong bộ nhớ
        if TOKEN_GLOBAL:
            return TOKEN_GLOBAL

        # Nếu file tồn tại → đọc token từ file
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                TOKEN_GLOBAL = file.read().strip()
                print("✅ Authorization đã được tải từ file.")
                return TOKEN_GLOBAL

        # Nếu không có file → yêu cầu nhập mới
        TOKEN_GLOBAL = input("🔐 Nhập Authorization của bạn: ").strip()
        with open(filename, 'w') as file:
            file.write(TOKEN_GLOBAL)
            print("💾 Authorization mới đã được lưu vào file.")
        return TOKEN_GLOBAL
    def xoa_token():
        filename = 'Authorization.txt'
        if os.path.exists(filename):
            os.remove(filename)
            print("🗑️ Đã xóa Authorization khỏi file.")
        else:
            print("⚠️ Không tìm thấy file Authorization.")
    def lay_cookie():
        cookie_file = 'cookie.txt'

        if os.path.exists(cookie_file):  # Nếu file cookie tồn tại
            while True:
                print(f"Bạn có muốn sử dụng cookie cũ không?")
                choice = input(f"(Y/N): ").strip().lower()
                if choice == 'y' or choice =='':
                    with open(cookie_file, 'r') as file:
                        cookie = file.read().strip()
                        print(f"Sử dụng cookie cũ.")
                    return cookie
                elif choice == 'n':
                    os.remove(cookie_file)
                    print(f"Cookie cũ đã bị xóa. Vui lòng nhập cookie mới.")
                    break  # Thoát vòng lặp để nhập cookie mới
                else:
                    print(f"Lựa chọn không hợp lệ, vui lòng nhập 'Y' hoặc 'N'.")

        # Nếu không có cookie cũ hoặc chọn nhập mới
        cookie = input("Nhập COOKIE của bạn: ").strip()
        with open(cookie_file, 'w') as file:
            file.write(cookie)
            print(f"Cookie mới đã được lưu vào file.")
        return cookie
    def __init__(self,authorization):
        self.demjob=0
        self.tongxu=0
        self.headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3,ru;q=0.2,ko;q=0.1',
            'authorization': authorization,
            'content-type': 'application/json;charset=utf-8',
            'dnt': '1',
            'origin': 'https://app.golike.net',
            'priority': 'u=1, i',
            'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            't': 'VFZSak1FNXFRVE5QVkVWNVQxRTlQUT09',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36',
        }
    def getthongtin_acc(self):
        pban = requests.Session(impersonate="chrome110")
        response = pban.get('https://gateway.golike.net/api/users/me', headers=self.headers).json()
        if "status" in response:
            data = response['data']
            tentk = data['username']
            tien = data['coin']
            print(f"Tên Tài Khoản: {tentk} | Tiền : {tien}")
        else:
            print("ERROR")
    def get_info(self):
        response = requests.get('https://gateway.golike.net/api/threads-account', headers=self.headers,impersonate= 'chrome110').json()
        acc_list = response.get('data', [])
        for index, acc in enumerate(acc_list, start=1):
            self.ten_ins = acc['threads_username']
            id_acc = acc['id']
            self.user_id=acc['user_id']
            print(f"{index}. Tên acc: {self.ten_ins}, ID: {id_acc}")
    def get_nv(self,id_acc):
        params = {'account_id':id_acc,}

        response = requests.get('https://gateway.golike.net/api/advertising/publishers/threads/jobs', params=params, headers=self.headers,impersonate="chrome110").json()
        # print(response)
        if response.get("status") == 200 and response.get("data"):
            data = response['data']
            id_job = data['id']
            self.link_job = data['link']
            self.kieu_job = data['type']
            obj_id = data['object_id']
            object_data_str = data.get("object_data", "{}")
            # Lấy giá trị message trong lock nếu có
            lock_info = response.get("lock", {})
            lock_message = lock_info.get("message")
            try:
                object_data = json.loads(object_data_str)
                self.pk_id = object_data.get("pk", obj_id)  # fallback nếu pk không có
            except json.JSONDecodeError:
                self.pk_id =obj_id
            # print(f"[JOB] ID: {id_job}, LINK: {self.link_job}, TYPE: {self.kieu_job}, OBJECT ID: {obj_id}, PK_ID: {self.pk_id}, NDCMT: {lock_message}")
            return id_job, obj_id, self.link_job, self.kieu_job, self.pk_id, lock_message
        elif response.get("status") == 400:
            print(f"\r{Fore.LIGHTYELLOW_EX}{response.get('message')}", end='')
            sys.stdout.flush()
            # print(" " * 80, end='\r')
            
        else:
            print("\rKhông lấy được dữ liệu job.", end='')
            print(" " * 80, end='\r')
        return None
    def skip_job(self,id_acc,id_job,obj_job):
        json_data = {
            'account_id': id_acc,
            'ads_id': id_job,
            'object_id': obj_job,
        }
        try:
            response = requests.post('https://gateway.golike.net/api/advertising/publishers/threads/skip-jobs',impersonate='chrome110', headers=self.headers,json=json_data).json()
        except:
            return self.skip_job(id_acc,id_job,obj_job)
        # print(message)
    def succes(self,id_acc,id_job):
        json_data = {
    'account_id': id_acc,
    'ads_id': id_job,
}
        response = requests.post('https://gateway.golike.net/api/advertising/publishers/threads/complete-jobs',headers=self.headers,json=json_data,impersonate="chrome110").json()
        # print(response)
        if response.get("status") == 200:
            data = response['data']
            tien = data['prices']
            link = data['link']
            self.demjob += 1
            self.tongxu+=tien
            print(f"{Fore.MAGENTA}[{self.demjob}] [{self.kieu_job.upper()}] "
                  f"{Fore.LIGHTCYAN_EX}[{strftime('%H:%M:%S')}] "
                  f"{Fore.YELLOW}[{link}] "
                  f"{Fore.CYAN}[+{tien} -> {self.tongxu} xu]{Style.RESET_ALL}"
                  )
    def countdown_lamjob(seconds):
        for i in range(seconds, 0, -1):
            print(f"{Fore.LIGHTMAGENTA_EX}Delay Làm Job: {i}s", end='\r', flush=True)
            time.sleep(1)
        print(" " * 80, end='\r')  # Đảm bảo xóa hoàn toàn
    def countdown_getjob(seconds):
        for i in range(seconds, 0, -1):
            print(f"{Fore.LIGHTMAGENTA_EX}Delay Get Job: {i}s", end='\r', flush=True)
            time.sleep(1)
        print(" " * 80, end='\r')  # Xóa dòng "Delay: Xs" sau khi đếm xong
def main():
    while True:  # 👉 Làm mới màn hình (chỉ dùng cho Windows)
        man_hinh()
        print("\n MENU:")
        print("1. Đăng nhập golike")
        print("2. Làm Job Threads")
        print("3. Xóa Authorization")
        print("0. Thoát")

        choice = input("👉 Nhập lựa chọn của bạn (0-3): ")

        if choice == "1":
            token = API.lay_token()
            api = API(token)
            api.getthongtin_acc()

        elif choice == "2":
            token = API.lay_token()
            api = API(token)
            api.get_info()
            id_acc = input("👉 Nhập ID acc bạn muốn dùng: ").strip()
            cookie = API.lay_cookie()
            delay_lamnv = int(input("\033[1;35mNhập thời gian delay làm job: \033[0m").strip())
            delay_getjob = int(input("\033[1;35mNhập thời gian delay get job: \033[0m").strip())
            man_hinh()
            A = THREADS()
            A.gettt(cookie)
            B= TIM(cookie)
            A.getusername()
            while True:
                API.countdown_getjob(delay_getjob)
                try:
                    job_data = api.get_nv(id_acc)
                except:
                    continue
                if job_data:
                    id_job, obj_job, link_job,kieu_job, pk_id,lock_message = job_data
                    try:
                        if kieu_job == 'follow':
                            API.countdown_lamjob(delay_lamnv)
                            A.gettt(cookie)
                            av, dtsg = A.laythongtin()
                            A.follow(av,dtsg,pk_id)
                            time.sleep(5)
                            api.succes(id_acc,id_job)
                        elif kieu_job == "like":
                            API.countdown_lamjob(delay_lamnv)
                            url=link_job
                            try:
                                antim = B.tim(url)
                            except :
                                api.skip_job(id_acc,id_job,obj_job)
                            time.sleep(5)
                            api.succes(id_acc,id_job)
                        else:
                            api.skip_job(id_acc,id_job,obj_job)
                    except:
                        api.skip_job(id_acc,id_job,obj_job)

        elif choice == "3":
            API.xoa_token()

        elif choice == "0":
            print("👋 Tạm biệt!")
            break

        else:
            print("❌ Lựa chọn không hợp lệ, vui lòng thử lại.")

main()






# A= API('Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9nYXRld2F5LmdvbGlrZS5uZXRcL2FwaVwvbG9naW4iLCJpYXQiOjE3NDYwNzkxMjEsImV4cCI6MTc3NzYxNTEyMSwibmJmIjoxNzQ2MDc5MTIxLCJqdGkiOiJCV1R6TDlseGZLV0trZGV3Iiwic3ViIjo5ODc0MTgsInBydiI6ImI5MTI3OTk3OGYxMWFhN2JjNTY3MDQ4N2ZmZjAxZTIyODI1M2ZlNDgifQ.Z_PO5bnBAfYT_zhh2I4FUExsABTi5lQVFDtnP91VWP4')
# A.get_info()
# B = input("acc chay : ")
# A.get_nv(B)
# A.skip_job('246','74243','DJL6iRHBdl7')
# A.succes('17189','66911')
