import os
import json
import random
import asyncio
from aiohttp import web
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# الإعدادات الأساسية
TOKEN =8972861822:AAEb0aCiSl-jQ2ZMqmoHgceXha4yJmVsQC4# ضع توكن البوت هنا
ADMIN_DEFAULT_USER = admin
ADMIN_DEFAULT_PASS = 123456

DB_FILE = database.json

def init_db()
    if not os.path.exists(DB_FILE)
        default_data = {
            status active,
            admin_auth {
                username ADMIN_DEFAULT_USER,
                password ADMIN_DEFAULT_PASS
            },
            stats {
                total_users 0,
                subscribers 1250,
                boy_prompts_count 0,
                girl_prompts_count 0
            },
            prompts {
                boys [
                    🚀 بروميت ولاد 1 Cinematic cyber punk street portrait, 8k, highly detailed,
                    🔥 بروميت ولاد 2 Epic dark fantasy warrior in heavy armor, dramatic lighting
                ],
                girls [
                    ✨ بروميت بنات 1 Elegant pastel aesthetic cozy room, soft warm lighting, 4k,
                    💖 بروميت بنات 2 Cute aesthetic minimalist fashion portrait, cinematic glow
                ]
            },
            settings {
                welcome_msg أهلاً بك في البوت الاحترافي لتوليد البروميتات الجاهزة! 🌟nاختر القسم المناسب لك أدناه,
                help_msg 📖 دليل الاستخدامn- قسم الأولاد أرسل رقماً عشوائياً مباشراً وسيرسل لك البوت بروميت عشوائي خاص بالشباب.n- قسم البنات أرسل الرقم متبوعاً برمز شباك (#) مثل (5#) وسيرسل لك البوت بروميت خاص للبنات.
            }
        }
        with open(DB_FILE, w, encoding=utf-8) as f
            json.dump(default_data, f, ensure_ascii=False, indent=4)

init_db()

def load_db()
    with open(DB_FILE, r, encoding=utf-8) as f
        return json.load(f)

def save_db(data)
    with open(DB_FILE, w, encoding=utf-8) as f
        json.dump(data, f, ensure_ascii=False, indent=4)

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_main_keyboard()
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=👨 قسم الشباب, callback_data=section_boys),
            InlineKeyboardButton(text=👩 قسم البنات, callback_data=section_girls)
        ],
        [
            InlineKeyboardButton(text=📖 شرح الاستخدام, callback_data=show_help)
        ]
    ])
    return keyboard

@dp.message(Command(start))
async def cmd_start(message types.Message)
    db = load_db()
    if db[status] != active
        await message.answer(🛠️ البوت في حالة صيانة حالياً، يرجى المحاولة لاحقاً.)
        return
    
    db[stats][total_users] += 1
    save_db(db)

    await message.answer(db[settings][welcome_msg], reply_markup=get_main_keyboard())

@dp.callback_query(F.data == show_help)
async def process_help(callback types.CallbackQuery)
    db = load_db()
    await callback.message.answer(db[settings][help_msg])
    await callback.answer()

@dp.callback_query(F.data == section_boys)
async def process_boys_section(callback types.CallbackQuery)
    await callback.message.answer(👨 قسم الشبابnأرسل الآن أي رقم عشوائي (مثلاً 7، 42، 100) وسأرسل لك بروميت عشوائي جاهز فوراً!)
    await callback.answer()

@dp.callback_query(F.data == section_girls)
async def process_girls_section(callback types.CallbackQuery)
    await callback.message.answer(👩 قسم البناتnأرسل الآن رقماً يتبعه رمز شباك `#` (مثلاً `7#` أو `15#`) وسأرسل لك بروميت مخصص للبنات!)
    await callback.answer()

@dp.message()
async def handle_user_input(message types.Message)
    db = load_db()
    if db[status] != active
        return

    text = message.text.strip()
    
    if text.endswith(#)
        prompts = db[prompts][girls]
        if not prompts
            await message.answer(⚠️ عذراً، لا توجد بروميتات بنات متاحة حالياً.)
            return
        selected_prompt = random.choice(prompts)
        await message.answer(f✨ بروميت بنات عشوائيnn`{selected_prompt}`, parse_mode=Markdown)
    
    elif text.isdigit()
        prompts = db[prompts][boys]
        if not prompts
            await message.answer(⚠️ عذراً، لا توجد بروميتات شباب متاحة حالياً.)
            return
        selected_prompt = random.choice(prompts)
        await message.answer(f🔥 بروميت شباب عشوائيnn`{selected_prompt}`, parse_mode=Markdown)
    else
        await message.answer(❓ يرجى اتباع التعليماتn- للشباب أرسل رقماً فقط.n- للبنات أرسل رقماً متبوعاً بـ # (مثال 5#)nأو اضغط start للعودة للقائمة الرئيسية.)


# ----------------- لوحة التحكم (Responsive + PWA Web App) -----------------
HTML_DASHBOARD = 
!DOCTYPE html
html lang=ar dir=rtl
head
    meta charset=UTF-8
    meta name=viewport content=width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no
    titleلوحة التحكم الإداريةtitle
    link rel=manifest href=manifest.json
    meta name=theme-color content=#0f172a
    meta name=apple-mobile-web-app-capable content=yes
    meta name=apple-mobile-web-app-status-bar-style content=black-translucent
    meta name=apple-mobile-web-app-title content=إدارة البوت
    style
        root {
            --bg-color #0f172a;
            --card-bg #1e293b;
            --accent #38bdf8;
            --accent-hover #0284c7;
            --text-main #f8fafc;
            --text-muted #94a3b8;
            --danger #ef4444;
            --success #22c55e;
        }
        body {
            font-family 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color var(--bg-color);
            color var(--text-main);
            margin 0;
            padding 15px;
            -webkit-tap-highlight-color transparent;
        }
        .container {
            max-width 1100px;
            margin 0 auto;
        }
        .header {
            display flex;
            flex-direction row;
            justify-content space-between;
            align-items center;
            background var(--card-bg);
            padding 15px 20px;
            border-radius 12px;
            box-shadow 0 4px 20px rgba(0,0,0,0.4);
            margin-bottom 20px;
            gap 10px;
        }
        .header h1 { margin 0; font-size 20px; color var(--accent); }
        .btn {
            background var(--accent);
            color white;
            border none;
            padding 10px 16px;
            border-radius 8px;
            cursor pointer;
            font-weight bold;
            transition 0.3s;
            text-decoration none;
            font-size 14px;
            text-align center;
            display inline-block;
        }
        .btnhover { background var(--accent-hover); }
        .btn-danger { background var(--danger); }
        .btn-dangerhover { background #dc2626; }
        
        .grid {
            display grid;
            grid-template-columns repeat(auto-fit, minmax(220px, 1fr));
            gap 15px;
            margin-bottom 20px;
        }
        .card {
            background var(--card-bg);
            padding 15px 20px;
            border-radius 12px;
            box-shadow 0 4px 15px rgba(0,0,0,0.3);
        }
        .card h3 { margin-top 0; color var(--text-muted); font-size 13px; }
        .card .value { font-size 24px; font-weight bold; color var(--accent); }
        
        .section-box {
            background var(--card-bg);
            padding 20px;
            border-radius 12px;
            margin-bottom 15px;
            box-shadow 0 4px 15px rgba(0,0,0,0.3);
        }
        .section-box h2 { border-bottom 2px solid #334155; padding-bottom 8px; margin-top 0; font-size 16px; color var(--accent); }
        
        input, select, textarea {
            width 100%;
            padding 12px;
            margin 8px 0 12px 0;
            background #0f172a;
            border 1px solid #334155;
            color white;
            border-radius 8px;
            box-sizing border-box;
            font-size 16px;
        }
        ul { padding-right 0; list-style none; margin 0; }
        li { margin-bottom 8px; display flex; justify-content space-between; align-items center; background #0f172a; padding 10px; border-radius 8px; font-size 14px; gap 10px; word-break break-all; }

        @media (max-width 768px) {
            body { padding 10px; }
            .header { flex-direction column; align-items flex-start; text-align right; }
            .header .btn { width 100%; margin-top 10px; }
        }
    style
head
body
    div class=container
        div class=header
            div
                h1🌟 لوحة التحكم الإداريةh1
                p style=margin 3px 0 0 0; color var(--text-muted); font-size 13px;إدارة البوت بكفاءة وسرعة من أي جهاز.p
            div
            a href=logout class=btn btn-dangerتسجيل خروج (تبديل مستخدم)a
        div

        div class=grid
            div class=card
                h3إجمالي المستخدمينh3
                div class=value{{ total_users }}div
            div
            div class=card
                h3عدد الاشتراكات النشطةh3
                div class=value{{ subscribers }}div
            div
            div class=card
                h3حالة البوتh3
                div class=value style=color {{ 'var(--success)' if status == 'active' else 'var(--danger)' }}; font-size 20px;
                    {{ 'يعمل بنجاح' if status == 'active' else 'في الصيانة' }}
                div
            div
        div

        div class=section-box
            h2⚙️ التحكم في حالة البوت والاشتراكاتh2
            form action=update_settings method=POST
                labelحالة البوتlabel
                select name=status
                    option value=active {{ 'selected' if status == 'active' else '' }}يعمل بشكل طبيعي (Active)option
                    option value=maintenance {{ 'selected' if status == 'maintenance' else '' }}وضع الصيانة (Maintenance)option
                select

                labelعدد الاشتراكاتlabel
                input type=number name=subscribers value={{ subscribers }}
                button type=submit class=btnحفظ التعديلاتbutton
            form
        div

        div class=section-box
            h2➕ إضافة بروميت جديدh2
            form action=add_prompt method=POST
                labelاختر القسمlabel
                select name=section
                    option value=boysقسم الشبابoption
                    option value=girlsقسم البناتoption
                select

                labelنص البروميتlabel
                textarea name=prompt_text rows=3 placeholder=أدخل نص البروميت الاحترافي هنا... requiredtextarea
                button type=submit class=btnإضافة البروميت للبوتbutton
            form
        div

        div class=section-box
            h2🔐 إدارة حساب الأدمن (يوزرنيم وباسورد)h2
            form action=update_auth method=POST
                labelاسم المستخدم الجديدlabel
                input type=text name=new_user value={{ admin_user }} required

                labelكلمة المرور الجديدةlabel
                input type=password name=new_pass value={{ admin_pass }} required
                button type=submit class=btnتحديث بيانات الدخولbutton
            form
        div

        div class=section-box
            h2📋 البروميتات الحاليةh2
            h3 style=color var(--accent);شبابh3
            ul
                {% for p in boys_prompts %}
                lispan{{ p }}span a href=delete_promptsection=boys&index={{ loop.index0 }} class=btn btn-danger style=padding 4px 10px; font-size 12px;حذفali
                {% endfor %}
            ul
            h3 style=color var(--accent); margin-top 15px;بناتh3
            ul
                {% for p in girls_prompts %}
                lispan{{ p }}span a href=delete_promptsection=girls&index={{ loop.index0 }} class=btn btn-danger style=padding 4px 10px; font-size 12px;حذفali
                {% endfor %}
            ul
        div
    div
body
html


HTML_LOGIN = 
!DOCTYPE html
html lang=ar dir=rtl
head
    meta charset=UTF-8
    meta name=viewport content=width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no
    titleتسجيل الدخول - لوحة التحكمtitle
    style
        body { background #0f172a; color white; font-family Tahoma; display flex; justify-content center; align-items center; height 100vh; margin 0; padding 15px; box-sizing border-box; }
        .login-card { background #1e293b; padding 30px; border-radius 15px; box-shadow 0 4px 25px rgba(0,0,0,0.5); width 100%; max-width 350px; text-align center; }
        input { width 100%; padding 12px; margin 10px 0; background #0f172a; border 1px solid #334155; color white; border-radius 8px; box-sizing border-box; font-size 16px; }
        button { background #38bdf8; color white; border none; padding 12px; width 100%; border-radius 8px; font-weight bold; cursor pointer; margin-top 10px; font-size 16px; }
        buttonhover { background #0284c7; }
        .error { color #ef4444; margin-bottom 10px; font-size 14px; }
    style
head
body
    div class=login-card
        h2🔒 تسجيل دخول الأدمنh2
        {% if error %}div class=error{{ error }}div{% endif %}
        form method=POST
            input type=text name=username placeholder=اسم المستخدم required
            input type=password name=password placeholder=كلمة المرور required
            button type=submitدخول للوحةbutton
        form
    div
body
html


MANIFEST_JSON = 
{
  name لوحة إدارة البوت,
  short_name إدارة البوت,
  start_url ,
  display standalone,
  background_color #0f172a,
  theme_color #0f172a,
  icons [
    {
      src httpscdn-icons-png.flaticon.com51220992099192.png,
      sizes 512x512,
      type imagepng
    }
  ]
}


active_sessions = set()

async def handle_manifest(request)
    return web.Response(text=MANIFEST_JSON, content_type='applicationjson')

async def handle_login(request)
    error = 
    if request.method == 'POST'
        data = await request.post()
        username = data.get('username')
        password = data.get('password')
        
        db = load_db()
        if username == db[admin_auth][username] and password == db[admin_auth][password]
            session_id = authenticated_admin_session
            active_sessions.add(session_id)
            raise web.HTTPFound('dashboard')
        else
            error = اسم المستخدم أو كلمة المرور غير صحيحة!
    
    html = HTML_LOGIN.replace({% if error %}div class=error{{ error }}div{% endif %}, f'div class=error{error}div' if error else )
    return web.Response(text=html, content_type='texthtml')

async def handle_dashboard(request)
    if authenticated_admin_session not in active_sessions
        raise web.HTTPFound('')
    
    db = load_db()
    html = HTML_DASHBOARD
    html = html.replace({{ total_users }}, str(db[stats][total_users]))
    html = html.replace({{ subscribers }}, str(db[stats][subscribers]))
    html = html.replace({{ status }}, db[status])
    html = html.replace({{ admin_user }}, db[admin_auth][username])
    html = html.replace({{ admin_pass }}, db[admin_auth][password])
    
    boys_li = .join([f'lispan{p}span a href=delete_promptsection=boys&index={i} style=background#ef4444;colorwhite;padding5px 12px;border-radius6px;text-decorationnone;font-size12px;white-spacenowrap;حذفali' for i, p in enumerate(db[prompts][boys])])
    girls_li = .join([f'lispan{p}span a href=delete_promptsection=girls&index={i} style=background#ef4444;colorwhite;padding5px 12px;border-radius6px;text-decorationnone;font-size12px;white-spacenowrap;حذفali' for i, p in enumerate(db[prompts][girls])])
    
    html = html.replace({% for p in boys_prompts %}n                lispan{{ p }}span a href=delete_promptsection=boys&text={{ loop.index0 }} class=btn btn-danger style=padding 4px 10px; font-size 12px;حذفalin                {% endfor %}, boys_li)
    html = html.replace({% for p in girls_prompts %}n                lispan{{ p }}span a href=delete_promptsection=girls&text={{ loop.index0 }} class=btn btn-danger style=padding 4px 10px; font-size 12px;حذفalin                {% endfor %}, girls_li)
    
    return web.Response(text=html, content_type='texthtml')

async def handle_logout(request)
    if authenticated_admin_session in active_sessions
        active_sessions.remove(authenticated_admin_session)
    raise web.HTTPFound('')

async def handle_update_settings(request)
    data = await request.post()
    db = load_db()
    db[status] = data.get(status)
    db[stats][subscribers] = int(data.get(subscribers, 0))
    save_db(db)
    raise web.HTTPFound('dashboard')

async def handle_add_prompt(request)
    data = await request.post()
    section = data.get(section)
    prompt_text = data.get(prompt_text)
    
    db = load_db()
    if section in db[prompts]
        db[prompts][section].append(prompt_text)
        save_db(db)
    raise web.HTTPFound('dashboard')

async def handle_delete_prompt(request)
    query = request.query
    section = query.get(section)
    index = int(query.get(index))
    
    db = load_db()
    if section in db[prompts] and len(db[prompts][section])  index
        db[prompts][section].pop(index)
        save_db(db)
    raise web.HTTPFound('dashboard')

async def handle_update_auth(request)
    data = await request.post()
    db = load_db()
    db[admin_auth][username] = data.get(new_user)
    db[admin_auth][password] = data.get(new_pass)
    save_db(db)
    raise web.HTTPFound('dashboard')

async def main()
    app = web.Application()
    app.router.add_get('', handle_login)
    app.router.add_post('', handle_login)
    app.router.add_get('manifest.json', handle_manifest)
    app.router.add_get('dashboard', handle_dashboard)
    app.router.add_get('logout', handle_logout)
    app.router.post('update_settings')(handle_update_settings)
    app.router.post('add_prompt')(handle_add_prompt)
    app.router.add_get('delete_prompt', handle_delete_prompt)
    app.router.post('update_auth')(handle_update_auth)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    await site.start()
    print(🌐 Web Dashboard running on httplocalhost8080)

    await dp.start_polling(bot)

if __name__ == '__main__'
    asyncio.run(main())
