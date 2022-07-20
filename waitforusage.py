"""Waiting for Text"""

@commands.command(name="ban")
async def ban(self, ctx: Context, member: Member):
    """Ban a member."""

    message = await ctx.send(f"Are you sure you want to ban {member}?")
    check = lambda m: m.author == ctx.author and m.channel == ctx.channel

    try:
        confirm = await self.bot.wait_for("message", check=check, timeout=30)
    except asyncio.TimeoutError:
        await message.edit(content="Ban cancelled, timed out.")
        return

    if confirm.content == "yes":
        await member.ban()
        await message.edit(content=f"{member} has been banned.")
        return

    await message.edit(content="Ban cancelled.")



"""Waiting for Reaction"""

  # Function definition removed for brevity.
    message = await ctx.send(f"Are you sure you want to ban {member}?")
    await message.add_reaction("✅")
    await message.add_reaction("❌")

    check = lambda r, u: u == ctx.author and str(r.emoji) in "✅❌"  # r=reaction, u=user

    try:
        reaction, user = await self.bot.wait_for("reaction_add", check=check, timeout=30)
    except asyncio.TimeoutError:
        await message.edit(content="Ban cancelled, timed out.")
        return

    if str(reaction.emoji) == "✅":
        await member.ban()
        await message.edit(content=f"{member} has been banned.")
        return

    await message.edit(content="Ban cancelled.")