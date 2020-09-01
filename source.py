# Tool by NguyenHoa
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)]
# Embedded file name: tool.py
import requests
from time import sleep
import random, concurrent.futures
print('=============================================================')
print('''
             - NguyenHoa#6595 TOOL CÀY XU TRAODOISUB.COM -

    /\_____/\     ███╗   ██╗ ██████╗ ██╗   ██╗██╗   ██╗███████╗███╗   ██╗██╗  ██╗ ██████╗  █████╗
   /  o   o  \    ████╗  ██║██╔════╝ ██║   ██║╚██╗ ██╔╝██╔════╝████╗  ██║██║  ██║██╔═══██╗██╔══██╗
  ( ==  ^  == )   ██╔██╗ ██║██║  ███╗██║   ██║ ╚████╔╝ █████╗  ██╔██╗ ██║███████║██║   ██║███████║
   )         (    ██║╚██╗██║██║   ██║██║   ██║  ╚██╔╝  ██╔══╝  ██║╚██╗██║██╔══██║██║   ██║██╔══██║
   )         (    ██║ ╚████║╚██████╔╝╚██████╔╝   ██║   ███████╗██║ ╚████║██║  ██║╚██████╔╝██║  ██║
   )         (    ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝
  (           )   ========================================================
(__(__)___(__)__) ===== Version: [ Private ]''')
print('TOOL CÀY XU TRAODOISUB.COM CÓ THỂ TẢI TẠI Github.com/SMLxuneo')
print('Versoin: 3.0')
print('Copyright © 2020 By NguyenHoa')
print('=============================================================')
print('======[CẤU HÌNH]======')
like = str(input('> Chế độ Like (on/off):'))
if like == '':
    like = 'on'
else:
    page = str(input('> Chế độ Page (on/off):'))
    if page == '':
        page = 'on'
    else:
        sub = str(input('> Chế độ Sub (on/off):'))
        if sub == '':
            sub = 'on'
        else:
            cmt = str(input('> Chế độ comment (on/off):'))
            if cmt == '':
                cmt = 'on'
            else:
                vonglap = input('> Số vòng lập (vòng, mặc đinh(100)):')
                if vonglap == '':
                    vonglap = 100
                else:
                    vonglap = int(vonglap)
                delayvong = input('> Thời gian nghỉ khi hết 1 vòng (giây, mặc đinh(100 giây)):')
                if delayvong == '':
                    delayvong = 100
                else:
                    delayvong = int(delayvong)
            delaynv = input('> Thời gian nghỉ giữa các nhiệm vụ (giây, min 10 giây, mặc đinh(15 giây)):')
            if delaynv == '':
                delaynv = 15
            else:
                delaynv = int(delaynv)
        listnv = []
        list_acc = []
        if like == 'on':
            listnv.append('like')
        if page == 'on':
            listnv.append('page')
        if sub == 'on':
            listnv.append('sub')
        if cmt == 'on':
            listnv.append('cmt')
        acc_tds = open('acc_tds.txt', 'r', encoding='utf-8').readlines()
        i = 1
        for x in acc_tds:
            data = x.replace('\n', '').split('|')
            data.append(i)
            list_acc.append(data)
            i += 1

        def thread(method, data, maxtab=20):
            with concurrent.futures.ThreadPoolExecutor(max_workers=maxtab) as (executor):
                (executor.map)(method, *zip(*data))


        def cmt(user, idfb, access_token, cookies):
            global xu
            dem = 0
            response = requests.get('https://traodoisub.com/scr/api_job.php?chucnang=cmt', cookies=cookies)
            try:
                data = response.json()
                so_nv = len(data)
                print(f"{user} -> {idfb} đã tìm thấy {so_nv} nhiệm vụ!")
            except:
                print('Sever đang gặp sự cố sẽ chạy lại sau 30s')
                sleep(30)
                cmt(user, idfb, access_token, cookies)
            else:
                if so_nv > 0:
                    for xxx in data:
                        uid = xxx['id']
                        msg = xxx['nd']
                        if dem < 15:
                            data = {'access_token':access_token, 
                             'message':msg}
                            r = requests.post(f"https://graph.facebook.com/{uid}/comments", data=data)
                            sleep(1)
                            data = {'id': uid}
                            if 'id' in r.json():
                                nhantien = requests.post('https://traodoisub.com/scr/nhantiencmt.php', cookies=cookies, data=data)
                                if nhantien.text == '2':
                                    xu += 800
                                    print(f"{user} -> {idfb} comment thành công id {uid}: +800 xu => {xu}")
                            elif r.json()['error']['code'] == 368:
                                print('Đã bị block chuyển ID khác')
                                break
                            else:
                                print(f"{user} -> {idfb} comment thất bại id {uid}")
                                requests.post('https://traodoisub.com/scr/nhantiencmt.php', cookies=cookies, data=data)
                            dem += 1
                            sleep(delaynv)
                        else:
                            print(f"{user} -> {idfb} hoàn thành! Chuyển sang ID khác!")
                            break

                else:
                    print(f"{user} -> {idfb} hết nhiệm vụ comment! Chuyển sang ID khác")


        def follow(user, idfb, access_token, cookies):
            global xu
            dem = 0
            response = requests.get('https://traodoisub.com/scr/api_job.php?chucnang=follow', cookies=cookies)
            try:
                data = response.json()
                so_nv = len(data)
                print(f"{user} -> {idfb} đã tìm thấy {so_nv} nhiệm vụ!")
            except:
                print('Sever đang gặp sự cố sẽ chạy lại sau 30s')
                sleep(30)
                follow(user, idfb, access_token, cookies)
            else:
                if so_nv > 0:
                    for uid in data:
                        if dem < 15:
                            data = {'access_token': access_token}
                            r = requests.post(f"https://graph.facebook.com/{uid}/subscribers", data=data)
                            sleep(1)
                            data = {'id': uid}
                            if r.text == 'true':
                                nhantien = requests.post('https://traodoisub.com/scr/nhantiensub.php', cookies=cookies, data=data)
                                if nhantien.text == '2':
                                    xu += 600
                                    print(f"{user} -> {idfb} follow thành công id {uid}: +600 xu => {xu}")
                            else:
                                try:
                                    if r.json()['error']['code'] == 368:
                                        print(f"{user} -> {idfb} đã bị block chuyển ID khác")
                                        break
                                except:
                                    print(f"{user} -> {idfb} follow thất bại id {uid}")
                                    requests.post('https://traodoisub.com/scr/nhantiensub.php', cookies=cookies, data=data)

                            dem += 1
                            sleep(delaynv)
                        else:
                            print(f"{user} -> {idfb} hoàn thành! Chuyển sang ID khác!")
                            break

                else:
                    print(f"{user} -> {idfb} hết nhiệm vụ sub! Chuyển sang ID khác")


        def like(user, idfb, access_token, cookies):
            global xu
            dem = 0
            response = requests.get('https://traodoisub.com/scr/api_job.php?chucnang=like', cookies=cookies)
            try:
                data = response.json()
                so_nv = len(data)
                print(f"{user} -> {idfb} đã tìm thấy {so_nv} nhiệm vụ!")
            except:
                print('Sever đang gặp sự cố sẽ chạy lại sau 30s')
                sleep(30)
                like(user, idfb, access_token, cookies)
            else:
                if so_nv > 0:
                    for uid in data:
                        if dem < 15:
                            data = {'access_token': access_token}
                            r = requests.post(f"https://graph.facebook.com/{uid}/likes", data=data)
                            sleep(1)
                            data = {'id': uid}
                            if r.text == 'true':
                                nhantien = requests.post('https://traodoisub.com/scr/nhantienlike.php', cookies=cookies, data=data)
                                if nhantien.text == '2':
                                    xu += 300
                                    print(f"{user} -> {idfb} like thành công id {uid}: +300 xu => {xu}")
                            else:
                                try:
                                    if r.json()['error']['code'] == 368:
                                        print('Đã bị block chuyển ID khác')
                                        break
                                except:
                                    print(f"{user} -> {idfb} follow thất bại id {uid}")
                                    requests.post('https://traodoisub.com/scr/nhantienlike.php', cookies=cookies, data=data)

                            dem += 1
                            sleep(delaynv)
                        else:
                            print(f"{user} -> {idfb} hoàn thành! Chuyển sang ID khác!")
                            break

                else:
                    print(f"{user} -> {idfb} hết nhiệm vụ like! Chuyển sang ID khác")


        def page(user, idfb, access_token, cookies):
            global xu
            dem = 0
            response = requests.get('https://traodoisub.com/scr/api_job.php?chucnang=likepage', cookies=cookies)
            try:
                data = response.json()
                so_nv = len(data)
                print(f"{user} -> {idfb} đã tìm thấy {so_nv} nhiệm vụ!")
            except:
                print('Sever đang gặp sự cố sẽ chạy lại sau 30s')
                sleep(30)
                page(user, idfb, access_token, cookies)
            else:
                if so_nv > 0:
                    for uid in data:
                        if dem < 15:
                            headersfb = {'authority':'mbasic.facebook.com',  'cache-control':'max-age=0', 
                             'upgrade-insecure-requests':'1', 
                             'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36', 
                             'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
                             'sec-fetch-site':'none', 
                             'sec-fetch-mode':'navigate', 
                             'sec-fetch-user':'?1', 
                             'sec-fetch-dest':'document', 
                             'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5', 
                             'cookie':cookie_fbs}
                            response = requests.get(f"https://mbasic.facebook.com/{uid}/about", headers=headersfb, timeout=10)
                            check_login = response.text.find('https://mbasic.facebook.com/login.php')
                            if check_login > 0:
                                print(f"{user} -> {idfb} cookie die!")
                                break
                            else:
                                try:
                                    url = response.text.split('style="width:25%"><a href="')[1].split('" class="')[0].replace('amp;', '')
                                except:
                                    url = ''

                                data = {'id': uid}
                                requests.get(f"https://mbasic.facebook.com{url}", headers=headersfb, timeout=15)
                                nhantien = requests.post('https://traodoisub.com/scr/nhantienpage.php', cookies=cookies, data=data)
                                if nhantien.text == '2':
                                    xu += 600
                                    print(f"{user} -> {idfb} like thành công page {uid}: +600 xu => {xu}")
                                else:
                                    print(f"{user} -> {idfb} like thất bại page {uid}")
                                dem += 1
                                sleep(delaynv)
                        else:
                            print('Chuyển sang ID khác!')
                            break

                else:
                    print(f"{user} -> {idfb} hết nhiệm page,chuyển nick")


        def datnick(user, uid, cookies, access_token):
            setad = requests.post('https://traodoisub.com/scr/datnick.php', cookies=cookies, data={'iddat[]': uid})
            if setad.text == '1':
                mod = random.choice(listnv)
                if mod == 'like':
                    like(user, uid, access_token, cookies)
                elif mod == 'page':
                    page(user, uid, access_token, cookies)
                elif mod == 'cmt':
                    cmt(user, uid, access_token, cookies)
                else:
                    follow(user, uid, access_token, cookies)
            else:
                print(f"{user} -> Cấu hình thất bại ID {uid}, chuyển nick!")


        def get_token(user, cookie_fb, cookies):
            global cookie_fbs
            cookie_fbs = cookie_fb.replace('\n', '')
            headers = {'authority':'m.facebook.com', 
             'cache-control':'max-age=0', 
             'upgrade-insecure-requests':'1', 
             'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36', 
             'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
             'sec-fetch-site':'none', 
             'sec-fetch-mode':'navigate', 
             'sec-fetch-user':'?1', 
             'sec-fetch-dest':'document', 
             'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5', 
             'cookie':cookie_fbs}
            response = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed', headers=headers)
            try:
                access_token = response.text.split('accessToken\\":\\"')[1].split('\\",\\"useLocalFilePreview')[0]
            except:
                print(f"{user} -> Lỗi!, chuyển nick!")
                list_x.remove(cookie_fb)
            else:
                data = {'access_token': access_token}
                r = requests.get('https://graph.facebook.com/me/', params=data)
                if 'id' in r.json():
                    uid = r.json()['id']
                    datnick(user, uid, cookies, access_token)
                else:
                    print('Lỗi không xác định!, chuyển nick')


        def login(user, pwd, stt):
            global list_x
            global xu
            name = f"list_fb_{stt}.txt"
            list_x = open(name, 'r', encoding='utf-8').readlines()
            data = {'username':user, 
             'password':pwd}
            print(f"Đang đăng nhập traodoisub user {user}")
            session = requests.session()
            login = session.post('https://traodoisub.com/scr/login.php', data=data)
            if login.status_code == 200:
                if 'success' in login.json():
                    __cfduid = session.cookies['__cfduid']
                    PHPSESSID = session.cookies['PHPSESSID']
                    cookies = {'__cfduid':__cfduid, 
                     'PHPSESSID':PHPSESSID}
                    check_live = requests.post('https://traodoisub.com/', cookies=cookies)
                    if len(check_live.text.split('<strong id="soduchinh">')) == 2:
                        xu = int(check_live.text.split('<strong id="soduchinh">')[1].split('</strong> xu</span>')[0])
                        print(f"Đăng nhập thành công user: {user} - xu hiện tại: {xu} xu")
                        print(f"{user} -> Đang setup!")
                        for x in range(1, vonglap + 1):
                            for fb in list_x:
                                get_token(user, fb, cookies)

                            sleep(delayvong)

                else:
                    print(f"Đăng nhập thất bại user: {user}")
            else:
                print('Web đang gặp sự cố, vui lòng đợi 1 phút tool tự chạy lại!')
                sleep(60)
                login(user, pwd, stt)


        if delaynv < 10:
            print('Thời gian nghỉ nhỏ nhất là 10 giây để tránh die clone, vui lòng cài lại!')
            sleep(3)
        else:
            if len(listnv) == 0:
                print('Chưa chon bất kì nhiệm vụ nào')
                sleep(3)
            else:
                thread(login, list_acc)