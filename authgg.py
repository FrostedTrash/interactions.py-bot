from discord.ext import commands
import PyAuthGG
import json
import discord

import interactions

global guild_id
global staff_role
global owner_role

guild_id = 921350023885758465
staff_role = 985243571630252107
owner_role = 922247919711711263

class mooncommands(interactions.Extension):
    def __init__(self, client):
        self.bot: interactions.Client = client

    @interactions.extension_command(
        name="getuser",
        description="Get Information about a Moon User"
    )
    async def getuser(self, ctx: commands.Context, User = ""):
      
      
      if User == "":
          await ctx.message.delete(delay=1)
          embed = discord.Embed(title=f"ERROR", description=f"Please specify a Username or E-Mail!", color=0xDC143C)
          await ctx.send(embed=embed, delete_after=5)
          return

      def writeJson(data, filename="auth.json"):
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
                
      print(PyAuthGG.Version)
      Admin = PyAuthGG.Administration("CIYENEGWDHQH")
      print(Admin.FetchUser(User))
      data = Admin.FetchUser(User)
      writeJson(data)

      with open("auth.json", "r") as f:
            data = json.load(f)

            if data['status'] == "failed":
                await ctx.message.delete(delay=1)
                embed = discord.Embed(title=f"ERROR", description=f"The User **{User}** doesn't exist!", color=0xDC143C)
                await ctx.send(embed=embed, delete_after=5)
                return
            print(data['username'])
            print(data['email'])
            print(data['hwid'])
            print(data['lastlogin'])
            print(data['lastip'])
            print(data['expiry'])

            embed = discord.Embed(title=f"Userinfo from {User}", color=0x4B0082)
            embed.add_field(name="**Username**", value=f"```{data['username']}```", inline= False)
            embed.add_field(name="**E-Mail**", value=f"```{data['email']}```", inline= False)
            embed.add_field(name="**HWID**", value=f"```{data['hwid']}```", inline= False)
            embed.add_field(name="**Last Login**", value=f"```{data['lastlogin']}```", inline= False)
            embed.add_field(name="**Last IP**", value=f"```{data['lastip']}```", inline= False)
            embed.add_field(name="**Expiry**", value=f"```{data['expiry']}```", inline= False)

            await ctx.message.delete(delay=1)
            await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @commands.has_role(983975830868860958)
    @commands.cooldown(rate=1, per=2)
    async def getusers(self, ctx: commands.Context, count = ""):

        def writeJson(data, filename="auth.json"):
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
        
        print(PyAuthGG.Version)
        Admin = PyAuthGG.Administration("CIYENEGWDHQH")
        #print(Admin.FetchUsers())
        data = Admin.FetchUsers()
        writeJson(data)
        

        with open("auth.json", "r") as f:
            data = json.load(f)
            print (len(data))
            usercount = len(data)

            await ctx.message.delete(delay=1)
            embed = discord.Embed(title=f"Total Users", description=f"We have **{usercount}** Users in total!", color=0x4B0082)
            await ctx.send(embed=embed)
            return


    @commands.command(pass_context=True)
    @commands.has_role(983975830868860958)
    @commands.cooldown(rate=1, per=2)
    async def moon(self, ctx: commands.Context, days):

        def writeJson(data, filename="auth.json"):
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
        days = int(days)

        if days == 0:
            await ctx.message.delete(delay=1)
            embed = discord.Embed(title=f"ERROR", description=f"Please make the key at least 1 Day valid!", color=0xDC143C)
            await ctx.send(embed=embed, delete_after=5)
            return
        
        print(PyAuthGG.Version)
        Admin = PyAuthGG.Administration("CIYENEGWDHQH")
        #print(Admin.FetchUsers())
        data = Admin.GenerateLicense(1, days, 1, 4, "DEMON", 10)
        writeJson(data)
        

        with open("auth.json", "r") as f:
            data = json.load(f)
            print (data["0"])
            key = data["0"]

            grammar = ""
            if days == 1:
              grammar = "Day"
            if days > 1:
              grammar = "Days"

            await ctx.message.delete(delay=1)
            embed = discord.Embed(title=f"Your {days} {grammar} Key", description=f"```{key}```", color=0x4B0082)
            await ctx.send(embed=embed)
            return

    @commands.command(pass_context=True)
    @commands.has_role(983975830868860958)
    @commands.cooldown(rate=1, per=2)
    async def getkey(self, ctx: commands.Context, key = ""):
      
      if key == "":
          await ctx.message.delete(delay=1)
          embed = discord.Embed(title=f"ERROR", description=f"Please specify a License!", color=0xDC143C)
          await ctx.send(embed=embed, delete_after=5)
          return

      def writeJson(data, filename="auth.json"):
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)

      print(PyAuthGG.Version)
      Admin = PyAuthGG.Administration("CIYENEGWDHQH")
      print(Admin.FetchLicense(f"{key}"))
      data = Admin.FetchLicense(f"{key}")
      writeJson(data)

      with open("auth.json", "r") as f:
            data = json.load(f)

            if data['status'] == "failed":
                await ctx.message.delete(delay=1)
                embed = discord.Embed(title=f"ERROR", description=f"The Key **{key}** doesn't exist!", color=0xDC143C)
                await ctx.send(embed=embed, delete_after=5)
                return
            print(data['license'])
            print(data['used'])
            print(data['used_by'])
            print(data['created'])

            embed = discord.Embed(title=f"Licenseinfo", color=0x4B0082)
            embed.add_field(name="**License**", value=f"```{data['license']}```", inline= False)
            embed.add_field(name="**Used?**", value=f"```{data['used']}```", inline= False)
            embed.add_field(name="**Used by?**", value=f"```{data['used_by']}```", inline= False)
            embed.add_field(name="**Creation**", value=f"```{data['created']}```", inline= False)

            await ctx.message.delete(delay=1)
            await ctx.send(embed=embed)


    @commands.command(pass_context=True)
    @commands.has_role(983975830868860958)
    @commands.cooldown(rate=1, per=2)
    async def getkeys(self, ctx: commands.Context):

        def writeJson(data, filename="auth.json"):
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
        
        print(PyAuthGG.Version)
        Admin = PyAuthGG.Administration("CIYENEGWDHQH")
        #print(Admin.FetchUsers())
        data = Admin.FetchLicenseCount()
        writeJson(data)
        

        with open("auth.json", "r") as f:
            data = json.load(f)
            print (data["value"])
            usercount = data["value"]

            await ctx.message.delete(delay=1)
            embed = discord.Embed(title=f"Total Keys", description=f"We have **{usercount}** Keys in total!", color=0x4B0082)
            await ctx.send(embed=embed)
            return


    @commands.command(pass_context=True)
    @commands.has_role(983975830868860958)
    @commands.cooldown(rate=1, per=2)
    async def reset(self, ctx: commands.Context, User = ""):
      
      if User == "":
          await ctx.message.delete(delay=1)
          embed = discord.Embed(title=f"ERROR", description=f"Please specify a Username!", color=0xDC143C)
          await ctx.send(embed=embed, delete_after=5)
          return

      def writeJson(data, filename="auth.json"):
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)

      print(PyAuthGG.Version)
      Admin = PyAuthGG.Administration("CIYENEGWDHQH")
      print(Admin.ResetHWID(User))
      data = Admin.ResetHWID(User)
      writeJson(data)

      with open("auth.json", "r") as f:
            data = json.load(f)

            if data['status'] == "failed":
                await ctx.message.delete(delay=1)
                embed = discord.Embed(title=f"ERROR", description=f"The User **{User}** doesn't exist!", color=0xDC143C)
                await ctx.send(embed=embed, delete_after=5)
                return

            embed = discord.Embed(title=f"HWID has been reset!", color=0x4B0082)

            await ctx.message.delete(delay=1)
            await ctx.send(embed=embed)

    

def setup(client):
    mooncommands(client)