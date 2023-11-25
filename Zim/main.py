import typing
import discord
from discord import app_commands

token = "OTAwNDgyNTgwODI5MzA2OTQx.GwzLhl.LucBcMvw_kHlhIkHUFSx2ua1v9E-jh64mKBVrQ"

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
guild_object = discord.Object(id=1137432547652022403)

@client.event
async def on_ready():
    print(f"Bot is ready. Client ID: {client.user.id}")
    await tree.sync(guild=guild_object) # none 



@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='member')
    if role is not None:
        await member.add_roles(role)
        print(f'Assigned role to {member.name} ({member.id})')

    welcome_message = "سلام! خوش آمدید به چنل دیسکورد ما. ما بسیار خوشحالیم که شما را در جمع خود می‌بینیم. " \
                      "برای ادامه فعالیت در چنل، لطفاً به دقت قوانین زیر را مطالعه کرده و رعایت نمایید:\n\n" \
                      "قوانین چنل:https://discord.com/channels/1137432547652022403/1163853940807434372\n\n" \
                      "لطفاً به این قوانین رعایت کامل بفرمایید تا محیط مطلوبی برای همه اعضا ایجاد شود. " \
                      "در صورت داشتن سوال یا ابهام، شما می‌توانید از چنل تیکت استفاده کنید و با باز کردن یک تیکت در " \
                      "اینجاhttps://discord.com/channels/1137432547652022403/1165633218553335818 تمامی سوالات و ابهامات خود را مطرح کنید.\n\n" \
                      "با تشکر از شما و امیدواریم که اقامت خوبی در چنل ما داشته باشید."
    await member.send(welcome_message)

@tree.command(name="send", description="Chating", guild=guild_object)
async def announce(interaction, message: str, reply: typing.Optional[str]):
    if interaction.user:
        await interaction.response.send_message("sending...", ephemeral=True)
        message_replaced = message.replace("++", "\n")
        try:
            message_reply = await interaction.channel.fetch_message(reply)
            await message_reply.reply(message_replaced)
        except:
            await interaction.channel.send(message_replaced)

@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 1163856487521726475:
        if payload.emoji.name == 'Yes':
            guild = await client.fetch_guild(payload.guild_id)
            user = await guild.fetch_member(payload.user_id)
            role = discord.utils.get(guild.roles, name='Verify')
            if user and role:
                await user.add_roles(role)
                Verify_message = "سلام! شما با موفقیت در کانال ما وریفای شدید."\
                                 "امیدواریم از خدمات ما لذت ببرید و تجربه‌ی مثال‌زدنی‌ای را در اینجا داشته باشید.\n"\
                                 "خدمت‌رسانی به شما در اینجا از اهمیت ویژه‌ای برخوردار است و اگر هر گونه سوال یا نیاز به راهنمایی دارید،شما می‌توانید از چنل تیکت ما استفاده کنید.\n"\
                                 "با باز کردن یک تیکت در اینجاhttps://discord.com/channels/1137432547652022403/1165633218553335818، تمامی سوالات و ابهامات خود را مطرح کنید تا تیم پشتیبانی ما بتواند به شما بهترین پاسخ را ارائه دهد.\n" \
                                 "ما در خدمت شما هستیم تا تجربه‌ی بهتری را برای شما فراهم کنیم.\n"\
                                 "با تشکر از انتخاب شما!\n"\
                                 
                await user.send(Verify_message)                

@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == 1163856487521726475:
        if payload.emoji.name == 'Yes':
            guild = client.get_guild(payload.guild_id)  
            user = guild.get_member(payload.user_id)  
            role = discord.utils.get(guild.roles, name='Verify')  
            if user and role:
                if role in user.roles:
                    await user.remove_roles(role)
                    UnVerify_message = " رول وریفای از شما گرفته شد و از برخی خدمات ما محروم شده‌اید.برای دریافت رول و فعال شدن خدمات بر روی ریکشنhttps://discord.com/channels/1137432547652022403/1163853940807434372/1163856487521726475 کلیک کرده .\n\n"\
                                       "اگر سوالی دارید یا به کمکی نیاز دارید با باز کردن یک تیکت در https://discord.com/channels/1137432547652022403/1165633218553335818 با تیم پشتیبانی ما تماس بگیرید."\

                    await user.send(UnVerify_message)

client.run(token)
