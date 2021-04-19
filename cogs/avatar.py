import discord
from discord.ext import commands

class avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def gay(self,ctx,member: discord.Member = None):
        member = member or ctx.author
        url = f"https://some-random-api.ml/canvas/gay?avatar={member.avatar_url_as(format='png')}"
        em = discord.Embed(color = ctx.author.color)
        em.set_image(url=url)
        em.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def glass(self,ctx,member: discord.Member = None):
        member = member or ctx.author
        url = f"https://some-random-api.ml/canvas/glass?avatar={member.avatar_url_as(format='png')}"
        em = discord.Embed(color = ctx.author.color)
        em.set_image(url=url)
        em.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def wasted(self,ctx,member: discord.Member = None):
        member = member or ctx.author
        url = f"https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format='png')}"
        em = discord.Embed(color = ctx.author.color)
        em.set_image(url=url)
        em.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def greyscale(self,ctx,member: discord.Member = None):
        """
        Converts an Image to Greyscale
        """
        member = member or ctx.author
        url = f"https://some-random-api.ml/canvas/greyscale?avatar={member.avatar_url_as(format='png')}"
        em = discord.Embed(color = ctx.author.color)
        em.set_image(url=url)
        em.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def invert(self,ctx,member: discord.Member = None):
        member = member or ctx.author
        url = f"https://some-random-api.ml/canvas/invert?avatar={member.avatar_url_as(format='png')}"
        em = discord.Embed(color = ctx.author.color)
        em.set_image(url=url)
        em.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def invertgreyscale(self,ctx,member: discord.Member = None):
        member = member or ctx.author
        url = f"https://some-random-api.ml/canvas/invertgreyscale?avatar={member.avatar_url_as(format='png')}"
        em = discord.Embed(color = ctx.author.color)
        em.set_image(url=url)
        em.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def brightness(self,ctx,member: discord.Member = None):
        member = member or ctx.author
        url = f"https://some-random-api.ml/canvas/brightness?avatar={member.avatar_url_as(format='png')}"
        em = discord.Embed(color = ctx.author.color)
        em.set_image(url=url)
        em.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def threshold(self,ctx,member: discord.Member = None):
        member = member or ctx.author
        url = f"https://some-random-api.ml/canvas/threshold?avatar={member.avatar_url_as(format='png')}"
        em = discord.Embed(color = ctx.author.color)
        em.set_image(url=url)
        em.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(avatar(bot))
    print('avatar file loaded')