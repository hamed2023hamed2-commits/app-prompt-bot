require('dotenv').config();
const { Telegraf } = require('telegraf');

const bot = new Telegraf(process.env.BOT_TOKEN);

bot.start((ctx) => {
  const userName = ctx.from.first_name || 'صديقي';
  ctx.reply(`👋 أهلاً بك يا ${userName}!\nأنا بوت البرومبتات السريع (مستضاف على Render 🚀).\nابعتلي رقم البرومبت مباشرة أو استخدم الأزرار.`);
});

bot.on('text', (ctx) => {
  const text = ctx.message.text.trim();
  if (/^\d+$/.test(text)) {
    ctx.reply(`🎯 أنت طلبت البرومبت رقم: ${text}\n(جاري جلب البيانات من القناة والشيت...)`);
  } else {
    ctx.reply('🔹 استخدم الأوامر أو ابعت رقم البرومبت مباشرة.');
  }
});

const PORT = process.env.PORT || 3000;
const RENDER_URL = process.env.RENDER_EXTERNAL_URL;

if (RENDER_URL) {
  bot.telegram.setWebhook(`${RENDER_URL}/bot${process.env.BOT_TOKEN}`);
  bot.startWebhook(`/bot${process.env.BOT_TOKEN}`, null, PORT);
  console.log(`Bot running via Webhook on port ${PORT}`);
} else {
  bot.launch();
  console.log('Bot running via Polling (Local)...');
}

process.once('SIGINT', () => bot.stop('SIGINT'));
process.once('SIGTERM', () => bot.stop('SIGTERM'));
