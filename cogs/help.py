import discord
from discord.ext import commands

import json
import time

invite = "https://discord.com/oauth2/authorize?client_id=796735541101854740&scope=bot&permissions=66321471"


class HelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__(command_attrs={
            'cooldown': commands.Cooldown(1, 3.0, commands.BucketType.member),
            'help': 'Shows help about the bot, a command, or a category'
        })

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="BlackShadow Commands", colour=0xF1C27D, url = invite)
        description = self.context.bot.description
        if description:
            embed.description = description

        for cog, cmds in mapping.items():
            if cog is None:
                continue
            name = cog.qualified_name
            filtered = await self.filter_commands(cmds, sort=True)
            if filtered:
                value = "\u2002".join(f"`{c.name}`" for c in cmds)
                if cog and cog.description:
                    value = "{0}\n{1}".format(cog.description, value)

                embed.add_field(name=name, value=value, inline=False)

        await self.get_destination().send(embed=embed)

    async def on_help_command_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(str(error.original))

    def get_command_signature(self, command):
        parent = command.full_parent_name
        if len(command.aliases) > 0:
            fmt = f'[{command.name}]'
            if parent:
                fmt = f'{parent} {fmt}'
            alias = fmt
        else:
            alias = command.name if not parent else f'{parent} {command.name}'
        return f'{alias} {command.signature}'

    def common_command_formatting(self, embed_like, command):
        
        with open("./Config/config.json", "r") as f:
            config = json.load(f)

        embed_like.title = f"Help: {command.name.capitalize()}"
        embed_like.timestamp = self.context.message.created_at
        if command.description:
            embed_like.description = f"**Command Enabled:** {command.enabled}\n\n**Description:** {command.description}\n\n{command.help}"
        else:
            embed_like.description = f'{command.help}' or f'**Command Enabled:** {command.enabled}\n\nNo help found'
        embed_like.add_field(
            name="Command's Params:", value=f"```yaml\n{self.clean_prefix}{self.get_command_signature(command)}\n```" , inline = False)
        embed_like.add_field(name="Commands's Aliases:", value=" | ".join([f"`{alias}`" for alias in command.aliases]) if command.aliases else f"None!" , inline = False)
        embed_like.set_author(name = "BlackShadow Help" , icon_url=self.context.bot.user.avatar_url, url = config["invite"])
        embed_like.set_thumbnail(url  = self.context.bot.user.avatar_url)
        embed_like.set_footer(text = f"Requested By {self.context.author}" , icon_url = self.context.author.avatar_url)

    async def send_command_help(self, command):
        embed = discord.Embed(colour=discord.Colour(0xF1C27D))
        self.common_command_formatting(embed, command)
        await self.context.send(embed=embed)

    async def send_group_help(self, cmd):
        e = discord.Embed(color=discord.Colour(0xF1C27D))
        e.title = f"Category: **{cmd.name}**" + \
            (" | " + '-'.join(cmd.aliases) if cmd.aliases else "")
        e.set_author(name=self.context.guild.me.display_name,
                     url="https://discord.gg/q8aqtFPqum", icon_url=self.context.guild.me.avatar_url)
        e.set_footer(
            text=f"Type {self.clean_prefix}<command name> to get more information.")
        cmds = await self.filter_commands(cmd.commands, sort=True)
        for cmd in cmds:
            e.add_field(name=cmd.name.capitalize() + (" | " + ', '.join(
            [f"`{alias.capitalize()}`" for alias in cmd.aliases]) if cmd.aliases else f"None!"), value=(
                "- " + cmd.short_doc if cmd.short_doc else "No description.") + f"\n```yaml\n{self.get_command_signature(cmd)}\n```", inline=False)
        await self.context.send(embed=e)

class Meta(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.old_help_command = bot.help_command
        bot.help_command = HelpCommand()
        bot.help_command.cog = self

    def cog_unload(self):
        self.bot.help_command = self.old_help_command


def setup(bot):
    bot.add_cog(Meta(bot))