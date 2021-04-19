import discord
from discord.ext import commands
import os 
from discord.ext.commands import has_permissions, MissingPermissions

class Moderation(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.has_permissions(kick_members = True)
    @commands.command(name="kick",aliases=['k'])
    async def kick(self , ctx ,user:discord.Member,*,reason=None):
        if reason == None:
            reason = "No reason given"
        await user.kick(reason = reason)
        await user.send(f"Hey You have been kicked from **{user.guild.name}** for the reason `{reason}`")
        em = discord.Embed(title=f"Kicked",description = f"user: {user.mention} has been kicked :raised_back_of_hand:")
        em.add_field(name="Reason" , value = reason)
        em.set_author(name = ctx.author.display_name,icon_url=ctx.author.avatar_url)
        await ctx.send(embed = em)
        
            
    @commands.has_permissions(ban_members = True)
    @commands.command(name = "ban",aliases = ['b'])
    async def ban(self, ctx , user: discord.Member,*,reason = None):
        if reason == None:
            reason = "No reason given"
        await user.ban(reason = reason)
        await user.send(f"Hey You have been banned from **{user.guild.name}** for the reason `{reason}`")
        em = discord.Embed(
            title=f"Banned", description=f"user: {user.mention} has been banned :hammer:")
        em.add_field(name = "Reason",value = reason)
        em.set_author(name = ctx.author.display_name,icon_url=ctx.author.avatar_url)
        await ctx.send(embed = em)
    
    @commands.is_owner()
    @commands.command(name = "mass kick",aliases = ['mk','masskick'])
    async def mass_kick(self,ctx,user:discord.Member = [],*,reason = None):
        if reason == None:
            reason = "Indefinite"
        for i in user:
            await i.kick(reason = reason)
        await ctx.send(f"users: {user} have been kicked! with the reason of {reason}")
    @commands.command()
    @commands.has_permissions(administrator=True)
    # @commands.has_role(761976040355528715)
    async def createtxt(self,ctx,channelName):
            guild = ctx.guild

            em = discord.Embed(title='success', description='{} has been created' .format(channelName),color=discord.Colour.green())
            await guild.create_text_channel(name='{}'.format(channelName))
            await ctx.send(embed=em)

        # delete textcahnnel
    @commands.command()
    @commands.has_permissions(administrator=True)
    # @commands.has_role(761976040355528715)
    async def deletetxt(self,ctx,channel: discord.TextChannel):
            em = discord.Embed(title='success', description=f'channel: {channel} has been deleted' , color=discord.Colour.red())
            await ctx.send(embed=em)
            await channel.delete()    

        # create vc
    @commands.command()
    @commands.has_permissions(administrator=True)
    # @commands.has_role(761976040355528715)
    async def createvc(self,ctx,channelName):
            guild = ctx.guild

            em = discord.Embed(title='success', description=f'{channelName} Has Been Created',color=discord.Colour.green())
            await guild.create_voice_channel(name=channelName)
            await ctx.send(embed=em)

        # delete vccahnnel
    @commands.command()
    @commands.has_permissions(administrator=True)
    # @commands.has_role(761976040355528715)
    async def deletevc(self,ctx,vc: discord.VoiceChannel):
            em = discord.Embed(title='success', description=f'{vc} has been deleted' , color=discord.Colour.red())
            await ctx.send(embed=em)
            await vc.delete()

        # add role
    @commands.command()
    @commands.has_permissions(administrator=True)
    # @commands.has_role(761976040355528715)
    async def addrole(self,ctx,role: discord.Role, user:discord.Member):
            await user.add_roles(role)
            await ctx.send(f'Succefully Given {role.mention} To {user.mention}')

        # remove role
    @commands.command()
    @commands.has_permissions(administrator=True)
    # @commands.has_role(761976040355528715)
    async def removerole(self,ctx,role: discord.Role, user:discord.Member):
            await user.remove_roles(role)
            await ctx.send(f'Succefully Removed {role.mention} From {user.mention}')
        
        # warn
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def warn(self, ctx, member : discord.Member, *, reason="No Reason Provided"):
            try:
                await member.send(f"You Have Been Warned ⚠️ on **{ctx.guild.name}** for {reason}")
            except:
                await ctx.send('Cannot Send Dm To User Because They Has Their DM Closed')
            await ctx.send(f"{member.name} has been Warned ⚠️ for {reason}")

    @commands.command(aliases=['smon'])
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def slowmode_on(self, ctx, time):
            await ctx.channel.edit(slowmode_delay=time)
            await ctx.send(f'{time}s of slowmode was set on the current channel.')

    @commands.command(aliases=['smoff'])
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def slowmode_off(self, ctx):
            await ctx.channel.edit(slowmode_delay=0)
            await ctx.send(f'Slowmode removed.')   

def setup(bot):
    bot.add_cog(Moderation(bot))
