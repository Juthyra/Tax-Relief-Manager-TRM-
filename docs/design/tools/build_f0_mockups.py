"""Builds the F0 mockup pages (English and Bahasa Malaysia) for phase 1, release R1.
Usage: python3 docs/design/tools/build_f0_mockups.py
Writes docs/design/phase-1_R1/F0_User_Profile/mockups/en/*.html and .../ms/*.html.
Test data only (the test family Aisyah). The Bahasa Malaysia text is a draft for a native speaker to review."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "phase-1_R1", "F0_User_Profile", "mockups")

ICON = {
 "home": '<path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/>',
 "calc": '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 12h2M12 12h2M8 16h2M12 16h2"/>',
 "list": '<path d="M8 6h12M8 12h12M8 18h12M4 6h.01M4 12h.01M4 18h.01"/>',
 "wallet": '<path d="M4 7h15a1 1 0 011 1v11a1 1 0 01-1 1H5a2 2 0 01-2-2V6a2 2 0 012-2h12"/><path d="M16 14h2"/>',
 "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>',
 "edit": '<path d="M4 20h4L19 9l-4-4L4 16v4z"/>',
 "lock": '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 018 0v3"/>',
 "chev": '<path d="M9 6l6 6-6 6"/>',
 "plus": '<path d="M12 5v14M5 12h14"/>',
 "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2 20c0-3.5 3-5.5 7-5.5s7 2 7 5.5"/><path d="M16 5a3.5 3.5 0 010 7M19 20c0-2.5-1.5-4-3.5-4.8"/>',
 "rules": '<path d="M6 3h9l4 4v14H6z"/><path d="M9 12h7M9 16h7M9 8h3"/>',
}
def ic(n, s=20): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[n]}</svg>'

T = {
"en": {
 "lang": "en", "nav": ["Dashboard", "Calculator", "Reliefs", "Spending", "Profile"], "yaw": "YA", "yafull": "Year of Assessment",
 "status": "Works offline · Synced 2 min ago", "draft": "Draft", "active": "Active", "filed": "Filed",
 "incomplete": "Incomplete", "complete": "Complete", "edit": "Edit", "notans": "Not answered", "yes": "Yes", "no": "No", "required": "Required",
 "profile": "Profile", "back": "Back", "next": "Next", "cancel": "Cancel", "save": "Save",
 "pf_title": "Profile for YA 2027", "pf_count": "8 of 9 answered, 88%",
 "pf_hint": "Reliefs, the calculator, spending and the dashboard stay locked for YA 2027 until every question is answered.",
 "next_q": "Answer the next question",
 "pf_copied": "<b>Copied from YA 2026.</b> Check each answer and confirm your dependants.",
 "about": "About you", "deps": "Dependants", "home": "First home",
 "q_res": "Tax residency", "a_res": "Resident", "q_mar": "Marital status", "a_mar": "Married",
 "q_sp": "Spouse has income", "q_spd": "Spouse is disabled", "q_spf": "Spouse has income from outside Malaysia above RM 4,000",
 "q_dis": "You are disabled", "q_pub": "Public servant on the pension scheme",
 "q_home": "First-home loan",
 "dep1": "Child · 7 years at 31/12/2027", "dep2": "Child · 4 years at 31/12/2027",
 "dep_conf": "Dependants list: not confirmed yet", "add_dep": "Add dependant", "dep_ok": "Dependants list confirmed",
 "pf_title26": "Profile for YA 2026", "pf_count26": "9 of 9 answered, 100%", "dep1_26": "Child · 6 years at 31/12/2026", "dep2_26": "Child · 3 years at 31/12/2026", "editing": "Editing",
 "l_hist": "Tax-year history", "l_chg": "Change history", "l_cmp": "Compare years",
 "r01": "R01 Individual", "r02": "R02 Disabled individual", "r03": "R03 Spouse or alimony", "r04": "R04 Disabled spouse", "r14": "R14 Employee EPF", "r20": "R20 Child under 18", "r06": "R06 First-home loan interest", "rebate": "Spouse rebate",
 # guided
 "g_title": "Set up your profile", "g_step": "Step 3 of 7",
 "g_steps": ["Account", "Residency", "Marital status", "Disability and pension", "Dependants", "First home", "Review"],
 "g_q": "What is your marital status?", "g_help": "Decides the spouse relief, the alimony relief and the spouse rebate",
 "g_opts": ["Single", "Married", "Divorced", "Widowed"],
 "g_hint": "Choose an answer to continue. Your answers are saved when you tap Next, so you can leave and come back.",
 # gate
 "gate_t": "Complete your profile for YA 2027", "gate_b": "The calculator is locked for this year until your profile is complete.",
 "gate_todo": "Still to answer", "gate_item": "Dependants: confirm your list (Nur, Adam)",
 "gate_note": "You can still open Profile, Tax-year history and Settings.",
 # dependant form
 "df_t": "Add dependant", "df_for": "For YA 2027",
 "f_nick": "Nickname", "f_nick_h": "A nickname is enough. Do not enter an identity number.",
 "f_type": "Type", "child": "Child", "parent": "Parent",
 "f_dob": "Date of birth (DD/MM/YYYY)", "f_dob_e": "Enter a date that is not in the future.",
 "f_age": "Age at 31/12/2027 is shown after a valid date.",
 "f_dis": "Is this person disabled?", "f_unm": "Is this child unmarried?", "f_edu": "Education level",
 "edu": ["Choose one", "Not in education", "School", "Pre-university", "Diploma or above (Malaysia)", "Degree or above (overseas)", "Other"],
 "f_sh": "Is this child's relief shared 50/50 with someone who is not your spouse living with you, for example a former spouse?",
 "f_inc": "Does this child have own income above the child relief?",
 # dialog
 "d_t": "Also apply this change to later years?", "d_change": "Changed in YA 2026: You are disabled, No → Yes",
 "d_y27": "YA 2027 · Draft", "d_note": "A later year that is filed is shown greyed as “Filed, not changed”.",
 "d_apply": "Apply", "d_cancel": "Cancel", "d_cancel_h": "Cancel keeps the change for YA 2026 only.",
 # history
 "h_title": "Tax-year history", "cols": ["Year", "Rules", "Stage", "Result", "Saved calculations", "Profile"],
 "announced": "Announced", "gazetted": "Gazetted", "confirmed": "Confirmed",
 "s_prog": "In progress", "s_calc": "Calculated", "s_filed": "Filed",
 "final": "Final", "estimate": "Estimate", "taxp": "Tax payable", "relief": "Total relief", "months": "Based on the months entered so far",
 "none": "None", "saved2": "2 saved, latest 10/11/2026", "saved1": "1 saved, 20/04/2026",
 "p_draft": "Draft · 88%", "p_act": "Active · complete", "dash": "—", "open_y": "Open this year",
 # admin
 "a_nav": ["Users", "Rules", "Account"], "a_title": "Support", "a_banner": "You are editing Aisyah's profile for YA 2026",
 "a_years": "Tax years", "a_noshow": "Support does not see the stage, the result or the saved calculations.",
 "a_name": "Name", "a_lang": "Language", "a_langv": "English", "a_user": "Aisyah (test user)",
 "a_note": "Support cannot change the email or the password. Changes apply to this year only.",
 "a_view": "View only", "a_dismiss": "Support changes are shown to the owner at the next open.",
},
"ms": {
 "lang": "ms", "nav": ["Papan pemuka", "Kalkulator", "Pelepasan", "Perbelanjaan", "Profil"], "yaw": "TT", "yafull": "Tahun Taksiran",
 "status": "Boleh digunakan tanpa talian · Disegerak 2 minit lalu", "draft": "Draf", "active": "Aktif", "filed": "Difailkan",
 "incomplete": "Belum lengkap", "complete": "Lengkap", "edit": "Ubah", "notans": "Belum dijawab", "yes": "Ya", "no": "Tidak", "required": "Wajib dijawab",
 "profile": "Profil", "back": "Kembali", "next": "Seterusnya", "cancel": "Batal", "save": "Simpan",
 "pf_title": "Profil untuk TT 2027", "pf_count": "8 daripada 9 dijawab, 88%",
 "pf_hint": "Pelepasan, kalkulator, perbelanjaan dan papan pemuka dikunci untuk TT 2027 sehingga semua soalan dijawab.",
 "next_q": "Jawab soalan seterusnya",
 "pf_copied": "<b>Disalin daripada TT 2026.</b> Semak setiap jawapan dan sahkan tanggungan anda.",
 "about": "Tentang anda", "deps": "Tanggungan", "home": "Rumah pertama",
 "q_res": "Status pemastautin cukai", "a_res": "Pemastautin", "q_mar": "Status perkahwinan", "a_mar": "Berkahwin",
 "q_sp": "Pasangan ada pendapatan", "q_spd": "Pasangan orang kurang upaya (OKU)", "q_spf": "Pasangan ada pendapatan dari luar Malaysia melebihi RM 4,000",
 "q_dis": "Anda orang kurang upaya (OKU)", "q_pub": "Penjawat awam dalam skim pencen",
 "q_home": "Pinjaman rumah pertama",
 "dep1": "Anak · 7 tahun pada 31/12/2027", "dep2": "Anak · 4 tahun pada 31/12/2027",
 "dep_conf": "Senarai tanggungan: belum disahkan", "add_dep": "Tambah tanggungan", "dep_ok": "Senarai tanggungan telah disahkan",
 "pf_title26": "Profil untuk TT 2026", "pf_count26": "9 daripada 9 dijawab, 100%", "dep1_26": "Anak · 6 tahun pada 31/12/2026", "dep2_26": "Anak · 3 tahun pada 31/12/2026", "editing": "Sedang diubah",
 "l_hist": "Sejarah tahun cukai", "l_chg": "Sejarah perubahan", "l_cmp": "Banding tahun",
 "r01": "R01 Individu", "r02": "R02 Individu kurang upaya", "r03": "R03 Pasangan atau alimoni", "r04": "R04 Pasangan kurang upaya", "r14": "R14 KWSP pekerja", "r20": "R20 Anak bawah 18 tahun", "r06": "R06 Faedah pinjaman rumah pertama", "rebate": "Rebat pasangan",
 "g_title": "Sediakan profil anda", "g_step": "Langkah 3 daripada 7",
 "g_steps": ["Akaun", "Kediaman cukai", "Status perkahwinan", "Kecacatan dan pencen", "Tanggungan", "Rumah pertama", "Semak"],
 "g_q": "Apakah status perkahwinan anda?", "g_help": "Menentukan pelepasan pasangan, pelepasan alimoni dan rebat pasangan",
 "g_opts": ["Bujang", "Berkahwin", "Bercerai", "Balu atau duda"],
 "g_hint": "Pilih satu jawapan untuk meneruskan. Jawapan anda disimpan apabila anda menekan Seterusnya, jadi anda boleh keluar dan kembali kemudian.",
 "gate_t": "Lengkapkan profil anda untuk TT 2027", "gate_b": "Kalkulator dikunci untuk tahun ini sehingga profil anda lengkap.",
 "gate_todo": "Masih perlu dijawab", "gate_item": "Tanggungan: sahkan senarai anda (Nur, Adam)",
 "gate_note": "Anda masih boleh membuka Profil, Sejarah tahun cukai dan Tetapan.",
 "df_t": "Tambah tanggungan", "df_for": "Untuk TT 2027",
 "f_nick": "Nama panggilan", "f_nick_h": "Nama panggilan sudah memadai. Jangan masukkan nombor kad pengenalan.",
 "f_type": "Jenis", "child": "Anak", "parent": "Ibu bapa",
 "f_dob": "Tarikh lahir (HH/BB/TTTT)", "f_dob_e": "Masukkan tarikh yang tidak melebihi hari ini.",
 "f_age": "Umur pada 31/12/2027 dipaparkan selepas tarikh yang sah.",
 "f_dis": "Adakah individu ini OKU?", "f_unm": "Adakah anak ini belum berkahwin?", "f_edu": "Tahap pendidikan",
 "edu": ["Pilih satu", "Tidak belajar", "Sekolah", "Pra-universiti", "Diploma ke atas (Malaysia)", "Ijazah ke atas (luar negara)", "Lain-lain"],
 "f_sh": "Adakah pelepasan anak ini dikongsi 50/50 dengan seseorang yang bukan pasangan yang tinggal bersama anda, contohnya bekas pasangan?",
 "f_inc": "Adakah anak ini ada pendapatan sendiri melebihi pelepasan anak?",
 "d_t": "Terapkan perubahan ini pada tahun-tahun seterusnya juga?", "d_change": "Diubah dalam TT 2026: Anda OKU, Tidak → Ya",
 "d_y27": "TT 2027 · Draf", "d_note": "Tahun seterusnya yang telah difailkan dipaparkan kelabu sebagai “Difailkan, tidak diubah”.",
 "d_apply": "Terapkan", "d_cancel": "Batal", "d_cancel_h": "Batal mengekalkan perubahan untuk TT 2026 sahaja.",
 "h_title": "Sejarah tahun cukai", "cols": ["Tahun", "Peraturan", "Peringkat", "Keputusan", "Pengiraan disimpan", "Profil"],
 "announced": "Diumumkan", "gazetted": "Diwartakan", "confirmed": "Disahkan",
 "s_prog": "Sedang berjalan", "s_calc": "Telah dikira", "s_filed": "Difailkan",
 "final": "Muktamad", "estimate": "Anggaran", "taxp": "Cukai kena dibayar", "relief": "Jumlah pelepasan", "months": "Berdasarkan bulan yang telah dimasukkan setakat ini",
 "none": "Tiada", "saved2": "2 disimpan, terkini 10/11/2026", "saved1": "1 disimpan, 20/04/2026",
 "p_draft": "Draf · 88%", "p_act": "Aktif · lengkap", "dash": "—", "open_y": "Buka tahun ini",
 "a_nav": ["Pengguna", "Peraturan", "Akaun"], "a_title": "Sokongan", "a_banner": "Anda sedang mengubah profil Aisyah untuk TT 2026",
 "a_years": "Tahun cukai", "a_noshow": "Sokongan tidak melihat peringkat, keputusan atau pengiraan yang disimpan.",
 "a_name": "Nama", "a_lang": "Bahasa", "a_langv": "Bahasa Malaysia", "a_user": "Aisyah (pengguna ujian)",
 "a_note": "Sokongan tidak boleh mengubah e-mel atau kata laluan. Perubahan hanya untuk tahun ini.",
 "a_view": "Lihat sahaja", "a_dismiss": "Perubahan oleh sokongan dipaparkan kepada pemilik pada bukaan seterusnya.",
}}

FONTS = "https://fonts.googleapis.com/css2?family=Lexend:wght@400;600;700&family=Source+Sans+3:wght@400;600;700&display=swap"

def shell(t, title, active, content, admin=False, fixed=False, flow=False, banner="", overlay="", ya_select=True, ya="2027", badge=None):
    nav = [("home", t["nav"][0]), ("calc", t["nav"][1]), ("list", t["nav"][2]), ("wallet", t["nav"][3]), ("user", t["nav"][4])]
    if admin: nav = [("users", t["a_nav"][0]), ("rules", t["a_nav"][1]), ("user", t["a_nav"][2])]
    items = lambda cls="": "".join(f'<a href="#" class="{"on" if i == active else ""}" {"aria-current=page" if i == active else ""}>{ic(n)}<span>{l}</span></a>' for i, (n, l) in enumerate(nav))
    tag = f'<span class="tag-admin">Admin</span>' if admin else ""
    bdg = '<span class="badge">' + badge + '</span>' if badge else ""
    yasel = f'<label class="ya"><span class="sr">{t["yafull"]}</span><select><option>{t["yaw"]} {ya}</option></select>{bdg}</label>' if ya_select else ""
    bar = f'<header class="appbar"><div class="brand"><span class="logo">TRM</span><span class="title">{title}</span>{tag}</div>{yasel}</header>'
    tabs = "" if flow else f'<nav class="tabbar" aria-label="Main">{items()}</nav>'
    rail = "" if flow else f'<aside class="rail" aria-label="Main"><span class="logo">TRM</span>{items()}</aside>'
    return f'''<!doctype html>
<html lang="{t["lang"]}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>TRM · {title} · F0 mockup (test data only)</title>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="../../../../tokens/tokens.css">
<link rel="stylesheet" href="../../../../components.css">
</head><body>
<div class="app{" fixedview" if fixed else ""}">{rail}<div class="col">{bar}{banner}<div class="status" role="status"><span class="dot"></span>{t["status"]}</div>
<main>{content}</main>{tabs}</div>{overlay}</div>
</body></html>'''

def row(t, q, a, chips, open_=False):
    ans = f'<span class="ans open">{t["notans"]}</span>' if open_ else f'<span class="ans">{a}</span>'
    ch = "".join(f'<span class="chip">{c}</span>' for c in chips)
    return f'<li class="row"><div class="rowmain"><span class="q">{q}</span>{ans}<div class="chips">{ch}</div></div><button class="edit" aria-label="{t["edit"]}: {q}">{ic("edit",18)}</button></li>'

def profile_content(t, y="2027"):
    done = y == "2026"
    rows = "".join([
        row(t, t["q_res"], t["a_res"], [t["r01"]]),
        row(t, t["q_mar"], t["a_mar"], [t["r03"], t["rebate"]]),
        row(t, t["q_sp"], t["no"], [t["r03"], t["rebate"]]),
        row(t, t["q_spd"], t["no"], [t["r04"]]),
        row(t, t["q_spf"], t["no"], [t["r03"]]),
        row(t, t["q_dis"], t["yes"] if done else t["no"], [t["r02"]]),
        row(t, t["q_pub"], t["no"], [t["r14"]]),
    ])
    ttl, cnt, pct = (t["pf_title26"], t["pf_count26"], 100) if done else (t["pf_title"], t["pf_count"], 88)
    pill = f'<span class="pill complete">{t["complete"]}</span>' if done else f'<span class="pill incomplete">{t["incomplete"]}</span>'
    cta = "" if done else f'<p class="hint">{t["pf_hint"]}</p><button class="btn btn-primary btn-block">{t["next_q"]}</button>'
    note = "" if done else f'<div class="notice" role="note">{t["pf_copied"]}</div>'
    side = f'''<section class="card" aria-labelledby="c1"><div class="ctop"><h2 id="c1">{ttl}</h2>{pill}</div>
<p class="count">{cnt}</p><div class="bar" role="progressbar" aria-valuenow="{pct}" aria-valuemin="0" aria-valuemax="100" aria-label="{cnt}"><span style="width:{pct}%"></span></div>
{cta}</section>{note}
<nav class="links" aria-label="{t["profile"]}"><a href="#">{t["l_hist"]} {ic("chev",16)}</a><a href="#">{t["l_chg"]} {ic("chev",16)}</a><a href="#">{t["l_cmp"]} {ic("chev",16)}</a></nav>'''
    main = f'''<h3 class="sec">{t["about"]}</h3><ul class="group">{rows}</ul>
<h3 class="sec">{t["deps"]}</h3><ul class="group">
<li class="dep"><div><b>Nur</b><small>{t["dep1_26"] if done else t["dep1"]}</small></div><span class="chip">{t["r20"]}</span></li>
<li class="dep"><div><b>Adam</b><small>{t["dep2_26"] if done else t["dep2"]}</small></div><span class="chip">{t["r20"]}</span></li></ul>
<button class="btn btn-secondary btn-block mt">{ic("plus",18)} {t["add_dep"]}</button>
<p class="line{"" if done else " warn"}">{t["dep_ok"] if done else t["dep_conf"]}</p>
<h3 class="sec">{t["home"]}</h3><ul class="group">{row(t, t["q_home"], t["no"], [t["r06"]])}</ul>'''
    return f'<div class="cols"><div class="side">{side}</div><div>{main}</div></div>'

def badge_title(t, label, badge): return label

def p01(t):
    steps = t["g_steps"]
    seg = "".join(f'<span class="{"done" if i < 2 else "now" if i == 2 else ""}"></span>' for i in range(7))
    lst = "".join(f'<li class="{"done" if i < 2 else "now" if i == 2 else ""}"><span class="n">{i+1}</span>{s}</li>' for i, s in enumerate(steps))
    opts = "".join(f'<label><input type="radio" name="mar"><span>{o}</span></label>' for o in t["g_opts"])
    c = f'''<div class="guided"><ol class="steplist" aria-label="{t["g_title"]}">{lst}</ol><div>
<div class="stepper" role="progressbar" aria-valuenow="3" aria-valuemin="1" aria-valuemax="7" aria-label="{t["g_step"]}">{seg}</div>
<div class="stepmeta"><span>{t["g_step"]}</span><span>{steps[2]}</span></div>
<div class="card" style="margin-top:14px"><fieldset class="field" style="border:0;padding:0;margin:0"><legend style="font-family:var(--font-head);font-size:20px;font-weight:600;margin-bottom:6px">{t["g_q"]}</legend>
<p class="help">{t["g_help"]}</p><div class="chips" style="margin:0 0 14px"><span class="chip">{t["r03"]}</span><span class="chip">{t["r04"]}</span><span class="chip">{t["rebate"]}</span></div>
<div class="choice">{opts}</div></fieldset></div>
<p class="hint">{t["g_hint"]}</p>
<div class="btn-row"><button class="btn btn-secondary">{t["back"]}</button><button class="btn btn-primary" disabled>{t["next"]}</button></div></div></div>'''
    return shell(t, t["g_title"], 4, c, flow=True, ya_select=False)

def p02(t):
    c = f'''<div class="gatebox"><span class="lock">{ic("lock",28)}</span><h1 style="font-size:22px">{t["gate_t"]}</h1>
<p class="hint" style="font-size:16px">{t["gate_b"]}</p>
<p class="count">{t["pf_count"]}</p><div class="bar" role="progressbar" aria-valuenow="88" aria-valuemin="0" aria-valuemax="100" aria-label="{t["pf_count"]}"><span style="width:88%"></span></div>
<h3 class="sec">{t["gate_todo"]}</h3><ul class="todo"><li><span class="mark" aria-hidden="true">!</span><span>{t["gate_item"]}</span></li></ul>
<button class="btn btn-primary btn-block">{t["next_q"]}</button><p class="hint mt">{t["gate_note"]}</p></div>'''
    return shell(t, t["nav"][1], 1, c)

def seg(t, name): return f'<div class="seg"><label><input type="radio" name="{name}"><span>{t["yes"]}</span></label><label><input type="radio" name="{name}"><span>{t["no"]}</span></label></div>'
def p04(t):
    edu = "".join(f"<option>{o}</option>" for o in t["edu"])
    c = f'''<h2 style="font-size:20px">{t["df_t"]}</h2><p class="hint" style="margin-top:2px">{t["df_for"]} · {t["required"]}</p>
<form class="card" onsubmit="return false"><div class="formgrid">
<div class="field"><label for="nick">{t["f_nick"]}</label><p class="help" id="nickh">{t["f_nick_h"]}</p><input id="nick" class="input" value="Adam" aria-describedby="nickh"></div>
<div class="field"><fieldset><legend>{t["f_type"]}</legend><div class="seg"><label><input type="radio" name="type" checked><span>{t["child"]}</span></label><label><input type="radio" name="type"><span>{t["parent"]}</span></label></div></fieldset></div>
<div class="field"><label for="dob">{t["f_dob"]}</label><input id="dob" class="input err" value="05/02/2027" aria-invalid="true" aria-describedby="dobe"><div class="error" id="dobe">{t["f_dob_e"]}</div><div class="age">{t["f_age"]}</div></div>
<div class="field"><fieldset><legend>{t["f_dis"]}</legend>{seg(t, "dis")}</fieldset></div>
<div class="field"><fieldset><legend>{t["f_unm"]}</legend>{seg(t, "unm")}</fieldset></div>
<div class="field"><label for="edu">{t["f_edu"]}</label><select id="edu" class="input">{edu}</select></div>
<div class="field"><fieldset><legend>{t["f_sh"]}</legend>{seg(t, "sh")}</fieldset></div>
<div class="field"><fieldset><legend>{t["f_inc"]}</legend>{seg(t, "inc")}</fieldset></div>
</div><div class="btn-row"><button class="btn btn-secondary" type="button">{t["cancel"]}</button><button class="btn btn-primary" type="submit">{t["save"]}</button></div></form>'''
    return shell(t, t["profile"], 4, c)

def p05(t):
    under = profile_content(t, "2026")
    ov = f'''<div class="overlay" role="dialog" aria-modal="true" aria-labelledby="dt"><div class="sheet"><h2 id="dt">{t["d_t"]}</h2>
<div class="change">{t["d_change"]}</div>
<label class="tick"><input type="checkbox" checked><span>{t["d_y27"]}</span></label>
<p class="hint" style="margin:6px 0 0">{t["d_note"]}</p>
<div class="btn-row"><button class="btn btn-secondary">{t["d_cancel"]}</button><button class="btn btn-primary">{t["d_apply"]}</button></div>
<p class="hint" style="margin:10px 0 0">{t["d_cancel_h"]}</p></div></div>'''
    return shell(t, t["profile"], 4, under, fixed=True, overlay=ov, ya="2026", badge=t["active"])

def p06(t):
    data = [
     ("2027", t["announced"], t["s_prog"], f'<span class="sub">{t["dash"]}</span>', t["none"], t["p_draft"], None),
     ("2026", t["gazetted"], t["s_calc"], f'<span class="tagline">{t["estimate"]}</span><span class="sub">{t["taxp"]} RM 1,449.00 · {t["relief"]} RM 22,850.00</span><span class="sub">{t["months"]}</span>', t["saved2"], t["p_act"], None),
     ("2025", t["confirmed"], t["s_filed"], f'<span class="tagline final">{t["final"]}</span><span class="sub">{t["taxp"]} RM 1,209.00 · {t["relief"]} RM 20,850.00</span>', t["saved1"], t["p_act"], None)]
    cards = "".join(f'''<li class="yacard"><header><h3>{t["yaw"]} {y}</h3><span class="tagline">{st}</span></header>
<dl class="kv"><dt>{t["cols"][1]}</dt><dd>{ru}</dd><dt>{t["cols"][3]}</dt><dd>{res}</dd><dt>{t["cols"][4]}</dt><dd>{sv}</dd><dt>{t["cols"][5]}</dt><dd>{pr}</dd></dl>
<a class="more" href="#">{t["open_y"]} {ic("chev",16)}</a></li>''' for y, ru, st, res, sv, pr, _ in data)
    trs = "".join(f'<tr><td><b>{t["yaw"]} {y}</b></td><td>{ru}</td><td><span class="tagline">{st}</span></td><td>{res}</td><td>{sv}</td><td>{pr}</td></tr>' for y, ru, st, res, sv, pr, _ in data)
    ths = "".join(f"<th scope=\"col\">{c}</th>" for c in t["cols"])
    c = f'<h2 style="font-size:20px;margin-bottom:12px">{t["h_title"]}</h2><ul class="yacards">{cards}</ul><table class="ytable"><thead><tr>{ths}</tr></thead><tbody>{trs}</tbody></table>'
    return shell(t, t["profile"], 4, c)

def p07(t):
    yrs = [("2027", t["announced"], t["draft"], "88%", False), ("2026", t["gazetted"], t["active"], "100%", False), ("2025", t["confirmed"], t["active"], "100%", True)]
    def arow(y, ru, pr, pc, f):
        sel = ' style="border-left:4px solid var(--color-accent)"' if y == "2026" else ""
        ed = " · <b>" + t["editing"] + "</b>" if y == "2026" else ""
        lk = '<div class="chips"><span class="lockflag">' + ic("lock", 12) + " " + t["filed"] + "</span></div>" if f else ""
        lab = t["a_view"] if f else t["edit"]
        return ('<li class="row"' + sel + '><div class="rowmain"><span class="q">' + t["yaw"] + " " + y + ed + '</span><span class="ans">' + ru + " · " + pr + " · " + pc + "</span>" + lk +
                '</div><button class="edit" aria-label="' + lab + ": " + y + '">' + ic("chev", 18) + "</button></li>")
    cards = "".join(arow(*y) for y in yrs)
    form = f'''<div class="card"><div class="field"><label for="n">{t["a_name"]}</label><input id="n" class="input" value="Aisyah"></div>
<div class="field"><label for="l">{t["a_lang"]}</label><select id="l" class="input"><option>{t["a_langv"]}</option></select></div></div>
<ul class="group mt">{row(t, t["q_mar"], t["a_mar"], [t["r03"]])}{row(t, t["q_dis"], t["no"], [t["r02"]])}</ul>
<p class="notice mt">{t["a_note"]}</p><div class="btn-row"><button class="btn btn-primary">{t["save"]}</button></div>'''
    c = f'<h3 class="sec" style="margin-top:0">{t["a_user"]}</h3><div class="cols"><div class="side"><h3 class="sec">{t["a_years"]}</h3><ul class="group">{cards}</ul><p class="hint">{t["a_noshow"]}</p></div><div>{form}<p class="hint">{t["a_dismiss"]}</p></div></div>'
    banner = f'<div class="banner" role="status">{ic("edit",18)}<span>{t["a_banner"]}</span></div>'
    return shell(t, t["a_title"], 0, c, admin=True, banner=banner, ya_select=False)

SCREENS = [("01_guided_creation", p01), ("02_gate_screen", p02), ("03_profile_screen", lambda t: shell(t, t["profile"], 4, profile_content(t), badge=t["draft"])),
           ("04_dependant_form", p04), ("05_apply_to_later_years", p05), ("06_tax_year_history", p06), ("07_admin_support_mode", p07)]
for lang, t in T.items():
    d = os.path.join(OUT, lang); os.makedirs(d, exist_ok=True)
    for name, fn in SCREENS:
        open(os.path.join(d, name + ".html"), "w", encoding="utf-8").write(fn(t))
print("built", len(SCREENS) * len(T), "pages")
