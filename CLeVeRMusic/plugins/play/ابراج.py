import asyncio

import config

from pyrogram import Client, filters

from CLeVeRMusic import app

from config import OWNER_ID

from CLeVeRMusic.misc import SUDOERS

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup

from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)

from CLeVeRMusic import (Apple, Resso, Spotify, Telegram, YouTube, app)





@app.on_message(filters.command(["ابراج ✯","الابراج","ابراج"], ""))

async def abrag(c: Client, m: Message):

    global mid

    mid = m.id

    keyboard = InlineKeyboardMarkup(inline_keyboard=[



        [InlineKeyboardButton("الجدي", callback_data="elgadee " + str(m.from_user.id))] +

        [InlineKeyboardButton("الدلو", callback_data="eldaloo " + str(m.from_user.id))],

        [InlineKeyboardButton("الحوت", callback_data="elhout " + str(m.from_user.id))] +

        [InlineKeyboardButton("الحمل", callback_data="elhamal " + str(m.from_user.id))],

        [InlineKeyboardButton("الثور", callback_data="elthawr " + str(m.from_user.id))] +

        [InlineKeyboardButton("الجوزاء", callback_data="elgawzaa " + str(m.from_user.id))],

        [InlineKeyboardButton("السرطان", callback_data="elsaratan " + str(m.from_user.id))] +

        [InlineKeyboardButton("الأسد", callback_data="elaasad " + str(m.from_user.id))],

        [InlineKeyboardButton("العذراء", callback_data="elazraaa " + str(m.from_user.id))] +

        [InlineKeyboardButton("الميزان", callback_data="elmezaan " + str(m.from_user.id))],

        [InlineKeyboardButton("العقرب", callback_data="elaqrab " + str(m.from_user.id))] +

        [InlineKeyboardButton("القوس", callback_data="elqoos " + str(m.from_user.id))],

         [InlineKeyboardButton("𝗚𝗿𝗢𝘂𝗣", url=f"https://t.me/Tm_CLeVeR")],

         [InlineKeyboardButton("𝗧𝗲𝗠 𝗝𝗮𝗖𝗞", url=f"https://t.me/SOURCE_CLeVeR")],

        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],



    ])

    await m.reply_text("• مرحبآ بك عزيزي × قسم ( ابراج ) آنقر علي الازرار لآختيار برجك 🤸‍♂️", reply_markup=keyboard)





@app.on_callback_query(filters.regex("^elgadee (\\d+)$"))

async def elgadee(c: Client, m: CallbackQuery):

    a = m.data.split(" ")

    if m.from_user.id != int(a[1]):

        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)

        return

    await m.message.delete()

    abrag_text = """•︙برج الجدي

•︙من تاريخ 2023-4-1

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙عاطفياً :  حاول ترطيب الأجواء مع الشريك، بعد ثورة الغضب التي انتابتك في الأيام الماضية 

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙صحياً :  لا تنجرّ وراء محاولات استدراجك إلى أن تثور وتغضب لتعريض وضعك الصحي للخطر

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙مهنياً :  يدعوك هذا اليوم المليء بالسلبيات إلى عدم التورط في قضايا أكبر منك، وخصوصاً أن رياح التغيير بدأت تعصف باتجاهك"""

    await m.message.reply_text(abrag_text, reply_to_message_id=mid)





@app.on_callback_query(filters.regex("^eldaloo (\\d+)$"))

async def eldaloo(c: Client, m: CallbackQuery):

    a = m.data.split(" ")

    if m.from_user.id != int(a[1]):

        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)

        return

    await m.message.delete()

    abrag_text = """•︙برج الدلو

•︙من تاريخ 2023-4-1

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙عاطفياً :  لا تتسرّع في الموافقة على قرار مهم قبل أن تدرس الوضع من جميع جوانبه، لأن الندم قد لا يفيدك لاحقاً 

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙صحياً :  لكي تحافظ على صحتك السليمة، ما عليك سوى ممارسة الرياضة ثلاث مرات على الأقل في الأسبوع

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙مهنياً :  هذا اليوم يفرض عليك أن تنظر إلى الأمور بطريقة أخرى، وأن تتعلّم كيف تحوّل الخسارة إلى ربح"""

    await m.message.reply_text(abrag_text, reply_to_message_id=mid)





@app.on_callback_query(filters.regex("^elhout (\\d+)$"))

async def elhout(c: Client, m: CallbackQuery):

    a = m.data.split(" ")

    if m.from_user.id != int(a[1]):

        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)

        return

    await m.message.delete()

    abrag_text = """•︙برج الحوت

•︙من تاريخ 2023-4-1

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙عاطفياً :  صداقة قديمة تعود إلى الواجهة عن طريق المصادفة، لكنّ الشريك يشعر بالقلق، فسارع إلى توضيح الأمور 

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙صحياً :  لا تستسلم للإحباط بسبب وضعك الصحّي المتردي نوعاً ما، بل كن متسلّحاً بالتفاؤل

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙مهنياً :  يرّوج بعض الزملاء الإشاعات عن وضعك، لكنّك تبقى صلباً وتحديداً في المركز المهم الذي أسنده إليك أرباب العمل"""

    await m.message.reply_text(abrag_text, reply_to_message_id=mid)





@app.on_callback_query(filters.regex("^elhamal (\\d+)$"))

async def elhamal(c: Client, m: CallbackQuery):

    a = m.data.split(" ")

    if m.from_user.id != int(a[1]):

        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)

        return

    await m.message.delete()

    abrag_text = """•︙برج الحمل

•︙من تاريخ 2023-4-1

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙عاطفياً :  يحتاج الشريك اليوم إلى عاطفتك واهتمامك أكثر من أي وقت مضى، فاستمع إليه وأمن له ما يتمنّاه 

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙صحياً :  القيام ببعض التمارين الخفيفة صباحاً تساعد على تليين العضلات وخصوصاً عضلات العنق الكتفين

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙مهنياً :  قد يطرأ اليوم ما يهدد ببعض المشاريع على الصعيد المهني ويكون المناخ ضاغطاً جداً وملبداً بغيوم المشاكل"""

    await m.message.reply_text(abrag_text, reply_to_message_id=mid)





@app.on_callback_query(filters.regex("^elthawr (\\d+)$"))

async def elthawr(c: Client, m: CallbackQuery):

    a = m.data.split(" ")

    if m.from_user.id != int(a[1]):

        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)

        return

    await m.message.delete()

    abrag_text = """•︙برج الثور

•︙من تاريخ 2023-4-1

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙عاطفياً :  يطلب منك الشريك أن تعطيه جواباً حاسماً بشأن طبيعة العلاقة بينكما، من دون أن يغفل عن أمور تهمكما 

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙صحياً :  ترتاح من تعب أرهقك جداً وأبقاك في حالة صحية متذبذبة ومضطربة بعض الشيء

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙مهنياً :  حاول ألاّ توظف طاقتك في مشاريع صغيرة لا خطط واضحة لها، وانتظر حتى تعرض عليك المشاريع الكبيرة"""

    await m.message.reply_text(abrag_text, reply_to_message_id=mid)





@app.on_callback_query(filters.regex("^elgawzaa (\\d+)$"))

async def elgawzaa(c: Client, m: CallbackQuery):

    a = m.data.split(" ")

    if m.from_user.id != int(a[1]):

        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)

        return

    await m.message.delete()

    abrag_text = """•︙برج الجوزاء

•︙من تاريخ 2023-4-1

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙عاطفياً :  مهمة إقناع الشريك بالسير معك حتى النهاية ليست صعبة، وتجاربه السابقة معك مشجعة جداً 

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙صحياً :  أنت المسؤول عما آل إليه وضعك الصحي، لأنك لم تلتزم إرشادات الطبيب ولم تطبقها

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙مهنياً :  يطرأ اليوم ما يبشر بيوم دقيق من التجارب المرة، لكن النجاح يكون حليفك في نهاية المطاف"""

    await m.message.reply_text(abrag_text, reply_to_message_id=mid)





@app.on_callback_query(filters.regex("^elsaratan (\\d+)$"))

async def elsaratan(c: Client, m: CallbackQuery):

    a = m.data.split(" ")

    if m.from_user.id != int(a[1]):

        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)

        return

    await m.message.delete()

    abrag_text = """•︙برج السرطان

•︙من تاريخ 2023-4-1

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙عاطفياً :  تمنحك مساندة الحبيب لك في هذه المرحلة الاندفاع والتفاؤل في الحياة والتفكير في الخطوات المقبلة بثقة كبيرة جداً 

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙صحياً :  انتبه لصحتك وانظر إلى الخيارات المتاحة أمامك للمحافظة عليها معافاة

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙مهنياً :  يحمل إليك هذا اليوم كلمات الإطراء والمديح والتهنئة، فيسطع نجمك وتبدأ بمشروع جديد"""

    await m.message.reply_text(abrag_text, reply_to_message_id=mid)





@app.on_callback_query(filters.regex("^elaasad (\\d+)$"))

async def elaasad(c: Client, m: CallbackQuery):

    a = m.data.split(" ")

    if m.from_user.id != int(a[1]):

        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)

        return

    await m.message.delete()

    abrag_text = """•︙برج الاسد

•︙من تاريخ 2023-4-1

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙عاطفياً :  لا تحمّل الشريك مسؤولية الأخطاء القديمة، وحاول أن تتخطى ذلك برحابة صدر وبساطة 

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙صحياً :  التدخين والإفراط في شرب الكحول والسهر سرعان ما تظهر نتائجهما على صحتك

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙مهنياً :  قد يجعلك هذا اليوم تتردّد في تسلم مهمة مع أنك تمتلك القدرة على ذلك وتحقيق النجاح المطلو"""

    await m.message.reply_text(abrag_text, reply_to_message_id=mid)





@app.on_callback_query(filters.regex("^elazraaa (\\d+)$"))

async def elazraaa(c: Client, m: CallbackQuery):

    a = m.data.split(" ")

    if m.from_user.id != int(a[1]):

        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)

        return

    await m.message.delete()

    abrag_text = """•︙برج العذراء

•︙من تاريخ 2023-4-1

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙عاطفياً :  تشعر بقوة العاطفة وتزداد رغبتك في التقرّب من الشريك الذي تكنّ له الحب الكبير 

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙صحياً :  إذا أحسست أن وضعك الصحي يتحسّن، فهذا جراء تطبيق إرشادات أصحاب الاختصاص في مجال التغذية

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙مهنياً :  يولّد هذا اليوم كلاماً غير مقنع أو لا يتمتّع بمصداقية، فتحاول معرفة الأسباب الكامنة وراء كل ما يحصل وتنجح في ذلك"""

    await m.message.reply_text(abrag_text, reply_to_message_id=mid)





@app.on_callback_query(filters.regex("^elmezaan (\\d+)$"))

async def elmezaan(c: Client, m: CallbackQuery):

    a = m.data.split(" ")

    if m.from_user.id != int(a[1]):

        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)

        return

    await m.message.delete()

    abrag_text = """•︙برج الميزان

•︙من تاريخ 2023-4-1

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙عاطفياً :  تمرّ بظرف صعب اليوم وأنت بأمسّ الحاجة إلى مساندة الشريك لتجاوز ما تواجهه بأقل ضرر ممكن 

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙صحياً :  تنضم إلى إحدى الفرق أو المجموعات الرياضية وتواظب على المشاركة في جميع أنشطتها فتستفيد صحياً

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙مهنياً :  يجعلك هذا اليوم تشغل نفسك بأمور صغيرة لن تنفعك بشيء، بل بالعكس قد تضيّع لك وقتك، وأنت بحاجة ماسة إلى كل ثاني"""

    await m.message.reply_text(abrag_text, reply_to_message_id=mid)





@app.on_callback_query(filters.regex("^elaqrab (\\d+)$"))

async def elaqrab(c: Client, m: CallbackQuery):

    a = m.data.split(" ")

    if m.from_user.id != int(a[1]):

        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)

        return

    await m.message.delete()

    abrag_text = """•︙برج العقرب

•︙من تاريخ 2023-4-1

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙عاطفياً :  كثرة التأجيل في حسم الأمور المصيرية تهدد علاقتك بالشريك، وتدفعها إلى المزيد من التأزم 

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙صحياً :  قد تشعر بضيق في النفس وباضطراب مفاجئ في الرئتين بسبب إدمانك التدخين

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙مهنياً :  قد يعرقل طارئ هذا اليوم تقدمك في مجالك المهني، لكنك قادر على تخطي المصاعب مهما تكن شدد"""

    await m.message.reply_text(abrag_text, reply_to_message_id=mid)





@app.on_callback_query(filters.regex("^elqoos (\\d+)$"))

async def elqoos(c: Client, m: CallbackQuery):

    a = m.data.split(" ")

    if m.from_user.id != int(a[1]):

        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)

        return

    await m.message.delete()

    abrag_text = """•︙برج القوس

•︙من تاريخ 2023-4-1

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙عاطفياً :  كن طويل البال مع الشريك وامنحه مزيداً من الوقت، فهو ساعدك كثيراً ويستحق منك بعض التضحية 

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙صحياً :  تجنّب قدر الإمكان الأماكن الرطبة ولا سيما أنك تعاني الربو وضيقاً في التنفس

┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉

•︙مهنياً :  قد يفقدك هذا اليوم الظروف المشجعة على التحرّك والاستثمار وتوظيف الأموال وتحقيق الأرباح"""

    await m.message.reply_text(abrag_text, reply_to_message_id=mid)
