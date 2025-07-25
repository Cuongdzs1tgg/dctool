from curl_cffi import requests
import re, json,time,sys
from colorama import Fore
import fake_useragent,random
class THREADS:
    def gettt(self, COOKIES):
        self.headers = {
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.threads.com',
            'priority': 'u=1, i',
            'referer': 'https://www.threads.com/@meoxeo?hl=vi',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
            'sec-ch-ua-full-version-list': '"Chromium";v="134.0.6998.196", "Not:A-Brand";v="24.0.0.0", "Google Chrome";v="134.0.6998.196"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"Nexus 5"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"6.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36',
            'x-asbd-id': '359341',
            'x-bloks-version-id': 'cf39c6377e026a1760665d37cfc1b31a93ae150e5d202da0aa6d36af9f0749fd',
            'x-csrftoken': COOKIES.split("csrftoken=")[1].split(";")[0],
            'x-fb-friendly-name': 'BarcelonaNotificationBadgeContextQueryDirectQuery',
            'x-fb-lsd': 'G0sAXWRqgfALvLibOPeyho',
            'x-ig-app-id': '238260118697367',
            'x-root-field-name': 'xdt_text_app_notification_badge',
            'cookie':COOKIES,
        }

    def laythongtin(self):
        response = requests.get("https://www.threads.com/", headers=self.headers)
        A = response.text
        av1 = re.findall('actorID.*?,', A)
        if not av1:
            raise Exception("❌ Không tìm thấy userID trong mã nguồn trang Threads.")
        self.av = av1[0].split(':')[1].split(',')[0].split('"')[1]
        jazoest = re.findall('__a=1&__user=0&__comet_req=29&jazoest.*?"', A)
        if not jazoest:
            raise Exception("❌ Không tìm thấy jazoest trong mã nguồn.")
        self.jazoest = jazoest[0].split('jazoest=')[1].split('"')[0]
        dtsg1 = re.findall('DTSGInitialData".*?"}', A)
        if not dtsg1:
            raise Exception("❌ Không tìm thấy fb_dtsg trong mã nguồn.")
        self.dtsg = dtsg1[0].split(':"')[1].split('}')[0].split('"')[0]
        return self.av, self.dtsg
    def getusername(self):
        real = requests.get("https://www.threads.com/",headers=self.headers).text
        oki =re.findall('username.*?,',real)
        username = oki[0].split(':')[1].split('"')[1]
        print(f"{Fore.YELLOW}Bạn Đang Chạy Tài Khoản THREADS : {username}")
    def follow(self, av, dtsg, ID_JOB):
        data = {
            'av': self.av,
            'fb_dtsg': self.dtsg,
            'jazoest': self.jazoest,
            'lsd': 'G0sAXWRqgfALvLibOPeyho',
            '__spin_r': '1022496133',
            '__spin_b': 'trunk',
            '__spin_t': '1746266308',
            '__crn': 'comet.threads.BarcelonaProfileThreadsColumnRoute',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'useBarcelonaFollowMutationFollowMutation',
            'variables': json.dumps({
                "target_user_id": ID_JOB,
                "media_id_attribution": None,
                "container_module": "ig_text_feed_profile"
            }),
            'server_timestamps': 'true',
            'doc_id': '9843083475741978',
        }

        response = requests.post('https://www.threads.com/graphql/query',headers=self.headers,data=data).json()
        try:
            if response.get('data') and response['data'].get('data') and \
            response['data']['data'].get('user') and \
            response['data']['data']['user'].get('friendship_status') and \
            response['data']['data']['user']['friendship_status'].get('following') == True:
                return True
            else:
                sys.exit()
        except Exception:
            sys.exit()
# cookie='ig_did=FFFDD1E6-9FDF-48B3-9B65-FD57B5BC29C0; csrftoken=bWfEnuxjL9chEQJTygYovU8Sdr6kIu8y; mid=aBX21QALAAFlQkV6TEvkBtAyB83O; ds_user_id=63217191721; ps_l=1; ps_n=1; sessionid=63217191721%3AhbntQA0QuslVaD%3A9%3AAYf5vdyZojSDsZL8kL7tCPGpxi2TG_L20mZknNojIe8; dpr=1.25; useragent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzNy4wLjAuMCBTYWZhcmkvNTM3LjM2; _uafec=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F137.0.0.0%20Safari%2F537.36; '
# A=THREADS()
# A.gettt(cookie)
# av,dtsg=A.laythongtin()
# A.follow(av,dtsg,"66516162781")
class TIM:
    def __init__(self,cookieTHR):
        self.headersTHR = {
                        'accept': '*/*',
                        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                        'content-type': 'application/x-www-form-urlencoded',
                        'cookie': cookieTHR,
                        'origin': 'https://www.threads.net',
                        'priority': 'u=1, i',
                        'referer': 'https://www.threads.net/@dreyt041',
                        'sec-ch-prefers-color-scheme': 'dark',
                        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                        'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.182", "Google Chrome";v="126.0.6478.182"',
                        'sec-ch-ua-mobile': '?1',
                        'sec-ch-ua-model': '"Pixel 5"',
                        'sec-ch-ua-platform': '"Android"',
                        'sec-ch-ua-platform-version': '"13"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36',
                        'x-asbd-id': '129477',
                        'x-csrftoken': cookieTHR.split('csrftoken=')[1].split(';')[0],
                        'x-fb-friendly-name': 'useBarcelonaFollowMutationFollowMutation',
                        'x-fb-lsd': '6Z5u6bYBj-kOXPD0nbgSGu',
                        'x-ig-app-id': '238260118697367',
                    }
    def tim(self,url):
        check = requests.get(url,headers=self.headersTHR).text
        try:
            fb_dtsg = check.split('"f":"')[1].split('",')[0]
            post_id = check.split('"props":{"post_id":"')[1].split('",')[0]
            # print(post_id)
            av= re.findall('"actorID":.*?,',check)
            avok=av[0].split(':')[1].split('"')[1]
            data = {
    'av': avok,
    '__user': '0',
    '__a': '1',
    '__req': 'g',
    '__hs': '20281.HYP:barcelona_web_pkg.2.1...0',
    'dpr': '3',
    '__ccg': 'EXCELLENT',
    '__rev': '1024692921',
    '__s': '3927pw:54vcnt:yp2zmb',
    '__hsi': '7526131220211906551',
    '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0qa0FE2awgo9oO0n24oaEd82lwv89k2C1Fwc60D85m1mzXwae4UaEW0Loco5G0zK5o4q0HU1IEGdwtU2ewbS1LwTwKG0hq1Iwqo9EpwUwiQ1mwLwHxW17y9UjgbVE-19w9y1swnrwu8',
    '__csr': 'ggq4qOFsOFR4fOLeGmx2gPnqsAGiFwzLWxOezoy8xxau8xauQfCURB-1mU01sKA0o62G1LG545Z03Ghwx2VQ0Ioc4kWyl2w2d5haxh1sn40bO0NpUgg1ho2ZF2qDCgcE0iWw8ZyE2pw4WAwlo3Rx20N81441sw-wdgb2H41sm1Dw9wU2ug3Kw4CwcK8U3Oxe0BUfo6mp7N2xh1vg8Xxy5WxlBP121E7Bg15Ux0KwSw3283dw6UhUB2U02iFhonwEg',
    '__hsdp': 'gctSB7C0h5FNUgcor2mhT50RbSWhgUxHkifE6r8ge8gl5iGskb61l0FgY5kigNEC2cbAswS6WsYUjq18bhmbwihFU9E4a8yoB2o9E2uxG0E8LqxK1VwtUlQ4oa8rw9Kt09m5EeCdw_xB0',
    '__hblp': '1qU1847oV12264Ex0Dwq43WaxW3OE4K3i4Hy8-13Ud9onxi2uEeE4a8yopwxwNw4EzWw4zQ5qy8ogq-9wkHxaU9QawyxSchodqxe2y6Vofu6k',
    '__comet_req': '29',
    'fb_dtsg': fb_dtsg,
    'jazoest': '26308',
    'lsd': 'qRyXh9N15g-T3ugTxiYo_h',
    '__spin_r': '1024692921',
    '__spin_b': 'trunk',
    '__spin_t': '1752313976',
    '__crn': 'comet.threads.BarcelonaPostColumnRoute',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'useBarcelonaLikeMutationLikeMutation',
    'variables': '{"mediaID":"'+post_id+'"}',
    'server_timestamps': 'true',
    'doc_id': '10095211437184657',
}
            try:
                response = requests.post('https://www.threads.com/api/graphql', headers=self.headersTHR, data=data).text
                # print(response)
                if '"has_liked":true' in response:
                    return True
                else:
                    return False
            except Exception as e:
                sys.exit()
                return True
        except Exception as e:
            print(f"Lỗi{e}")
            return False
        data = {
    'av': avok,
    '__user': '0',
    '__a': '1',
    '__req': 'g',
    '__hs': '20281.HYP:barcelona_web_pkg.2.1...0',
    'dpr': '3',
    '__ccg': 'EXCELLENT',
    '__rev': '1024692921',
    '__s': '3927pw:54vcnt:yp2zmb',
    '__hsi': '7526131220211906551',
    '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0qa0FE2awgo9oO0n24oaEd82lwv89k2C1Fwc60D85m1mzXwae4UaEW0Loco5G0zK5o4q0HU1IEGdwtU2ewbS1LwTwKG0hq1Iwqo9EpwUwiQ1mwLwHxW17y9UjgbVE-19w9y1swnrwu8',
    '__csr': 'ggq4qOFsOFR4fOLeGmx2gPnqsAGiFwzLWxOezoy8xxau8xauQfCURB-1mU01sKA0o62G1LG545Z03Ghwx2VQ0Ioc4kWyl2w2d5haxh1sn40bO0NpUgg1ho2ZF2qDCgcE0iWw8ZyE2pw4WAwlo3Rx20N81441sw-wdgb2H41sm1Dw9wU2ug3Kw4CwcK8U3Oxe0BUfo6mp7N2xh1vg8Xxy5WxlBP121E7Bg15Ux0KwSw3283dw6UhUB2U02iFhonwEg',
    '__hsdp': 'gctSB7C0h5FNUgcor2mhT50RbSWhgUxHkifE6r8ge8gl5iGskb61l0FgY5kigNEC2cbAswS6WsYUjq18bhmbwihFU9E4a8yoB2o9E2uxG0E8LqxK1VwtUlQ4oa8rw9Kt09m5EeCdw_xB0',
    '__hblp': '1qU1847oV12264Ex0Dwq43WaxW3OE4K3i4Hy8-13Ud9onxi2uEeE4a8yopwxwNw4EzWw4zQ5qy8ogq-9wkHxaU9QawyxSchodqxe2y6Vofu6k',
    '__comet_req': '29',
    'fb_dtsg': fb_dtsg,
    'jazoest': '26308',
    'lsd': 'qRyXh9N15g-T3ugTxiYo_h',
    '__spin_r': '1024692921',
    '__spin_b': 'trunk',
    '__spin_t': '1752313976',
    '__crn': 'comet.threads.BarcelonaPostColumnRoute',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'useBarcelonaLikeMutationLikeMutation',
    'variables': '{"mediaID":"'+post_id+'"}',
    'server_timestamps': 'true',
    'doc_id': '10095211437184657',
}
        try:
            response = requests.post('https://www.threads.com/api/graphql', headers=self.headersTHR, data=data).text
            print(response)
            if '"is_final":true' in response:
                return True
            else:
                return False
        except Exception as e:
            sys.exit()
# TIM('ig_did=103A5C1B-3FF9-4167-BCA4-BB7FD24BF8C9; mid=aBMRaQALAAHyRrwmHI7ib0DGqGa9; ps_l=1; ps_n=1; csrftoken=9p2ftHw2elyUUhZW88RHmAMmZb64feho; ds_user_id=68648164571; sessionid=68648164571%3AoWDEkMChzsytSe%3A12%3AAYe_GHNN2cPpzBOqwQbHQRYrSjLZwLzWX23obq-EWg; dpr=2.0000000298023224; rur="EAG\05468648164571\0541784912572:01fece10f31531a19ba8ea16b1a597c356d91ff1aa3414a47c7a13cb5aeca0cecf7f4834"; useragent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzNy4wLjAuMCBTYWZhcmkvNTM3LjM2; _uafec=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F137.0.0.0%20Safari%2F537.36; ').tim("https://www.threads.com/@linhhueleee/post/DMf37EgRunpdddd")