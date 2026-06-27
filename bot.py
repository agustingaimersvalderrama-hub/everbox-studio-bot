import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
from discord.ui import View, Button

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.tree.command(
    name="everbox",
    description="Información general sobre Everbox Studio"
)
async def everbox(interaction: discord.Interaction):

    embed = discord.Embed(
        title="Everbox Studio",
        description=(
            "Everbox Studio es un estudio dedicado al desarrollo y diseño para comunidades, servidores y proyectos digitales.\n\n"
            "Nuestro objetivo es ofrecer servicios profesionales, innovadores y de alta calidad."
        ),
        color=discord.Color.from_rgb(255, 255, 255)
    )

    embed.add_field(
        name="Servicios Principales",
        value="Bots • Liverys • Webs • Diseño • Videos • Servidores",
        inline=False
    )

    embed.set_footer(
        text="Everbox Studio © Todos los derechos reservados"
    )

    await interaction.response.send_message(embed=embed)


@bot.tree.command(
    name="servicios",
    description="Lista de servicios de Everbox Studio"
)
async def servicios(interaction: discord.Interaction):

    embed = discord.Embed(
        title="Servicios Disponibles",
        color=discord.Color.from_rgb(255, 255, 255)
    )

    embed.description = (
        "• Desarrollo de Bots Personalizados\n"
        "• Creación de Servidores\n"
        "• Diseño de Liverys\n"
        "• Diseño de Banners\n"
        "• Diseño de Fotos\n"
        "• Creación de Sitios Web\n"
        "• Edición y Producción de Videos"
    )

    await interaction.response.send_message(embed=embed)

@bot.tree.command(
    name="portafolio",
    description="Muestra el portafolio de Everbox Studio"
)
async def portafolio(interaction: discord.Interaction):

    embed = discord.Embed(
        title="Portafolio",
        description=(
            "Puedes revisar algunos de nuestros proyectos y trabajos realizados.\n\n"
            "• Bots personalizados\n"
            "• Liverys profesionales\n"
            "• Sitios web\n"
            "• Diseño gráfico\n"
            "• Servidores completos"
        ),
        color=discord.Color.blurple()
    )

    await interaction.response.send_message(embed=embed)


@bot.tree.command(
    name="equipo",
    description="Muestra el equipo de Everbox Studio"
)
async def equipo(interaction: discord.Interaction):

    embed = discord.Embed(
        title="Equipo de Everbox Studio",
        description=(
            "Nuestro equipo está conformado por desarrolladores, diseñadores y administradores dedicados a ofrecer el mejor servicio."
        ),
        color=discord.Color.gold()
    )

    await interaction.response.send_message(embed=embed)


@bot.tree.command(
    name="registrarcompra",
    description="Registrar una compra"
)
async def registrarcompra(
    interaction: discord.Interaction,
    cliente: discord.Member,
    servicio: str,
    precio: float
):

    if cliente.id not in compras:
        compras[cliente.id] = []

    compras[cliente.id].append({
        "servicio": servicio,
        "precio": precio
    })

    embed = discord.Embed(
        title="Compra Registrada",
        color=discord.Color.green()
    )

    embed.add_field(name="Cliente", value=cliente.mention)
    embed.add_field(name="Servicio", value=servicio)
    embed.add_field(name="Precio", value=f"${precio}")

    await interaction.response.send_message(embed=embed)


@bot.tree.command(
    name="vercompras",
    description="Ver compras de un cliente"
)
async def vercompras(
    interaction: discord.Interaction,
    cliente: discord.Member
):

    if cliente.id not in compras:
        await interaction.response.send_message(
            "Este cliente no tiene compras registradas."
        )
        return

    embed = discord.Embed(
        title=f"Compras de {cliente}",
        color=discord.Color.blue()
    )

    for compra in compras[cliente.id]:
        embed.add_field(
            name=compra["servicio"],
            value=f'Precio: ${compra["precio"]}',
            inline=False
        )

    await interaction.response.send_message(embed=embed)


@bot.tree.command(
    name="factura",
    description="Genera una factura"
)
async def factura(
    interaction: discord.Interaction,
    cliente: discord.Member,
    servicio: str,
    precio: float
):

    embed = discord.Embed(
        title="Factura Everbox Studio",
        color=discord.Color.dark_blue()
    )

    embed.add_field(name="Cliente", value=cliente.mention)
    embed.add_field(name="Servicio", value=servicio)
    embed.add_field(name="Monto", value=f"${precio}")
    embed.add_field(name="Estado", value="Pendiente de Pago")

    embed.set_footer(
        text="Gracias por confiar en Everbox Studio"
    )

    await interaction.response.send_message(embed=embed)


@bot.tree.command(
    name="cliente",
    description="Ver información de un cliente"
)
async def cliente(
    interaction: discord.Interaction,
    usuario: discord.Member
):

    embed = discord.Embed(
        title="Información del Cliente",
        color=discord.Color.orange()
    )

    embed.set_thumbnail(url=usuario.display_avatar.url)

    embed.add_field(
        name="Usuario",
        value=usuario.mention
    )

    embed.add_field(
        name="ID",
        value=usuario.id
    )

    embed.add_field(
        name="Cuenta creada",
        value=usuario.created_at.strftime("%d/%m/%Y")
    )

    await interaction.response.send_message(embed=embed)


@bot.tree.command(
    name="estadisticasventas",
    description="Ver estadísticas de ventas"
)
async def estadisticasventas(interaction: discord.Interaction):

    total_ventas = 0
    total_dinero = 0

    for lista in compras.values():
        total_ventas += len(lista)

        for compra in lista:
            total_dinero += compra["precio"]

    embed = discord.Embed(
        title="Estadísticas de Ventas",
        color=discord.Color.purple()
    )

    embed.add_field(
        name="Ventas Totales",
        value=str(total_ventas)
    )

    embed.add_field(
        name="Ingresos Totales",
        value=f"${total_dinero}"
    )

    await interaction.response.send_message(embed=embed)

@bot.tree.command(
    name="precios",
    description="Muestra la lista de precios de Everbox Studio"
)
async def precios(interaction: discord.Interaction):

    embed = discord.Embed(
        title="💰 | Lista de Precios - Everbox Studio",
        description=(
            "A continuación podrás visualizar los precios oficiales de nuestros servicios.\n\n"
            "⚠️ Los precios pueden variar dependiendo de la complejidad del pedido."
        ),
        color=discord.Color.from_rgb(255, 255, 255)
    )

    embed.add_field(
        name="🤖 Desarrollo de Bots",
        value=(
            "**Básico:** 80 Robux | $1.000 CLP\n"
            "**Intermedio:** 160 Robux | $1.000 CLP\n"
            "**Avanzado:** 320 Robux | $2.000 CLP"
        ),
        inline=False
    )

    embed.add_field(
        name="🎨 Diseño Gráfico",
        value=(
            "**Banner:** 30 Robux | $2.000 CLP\n"
            "**Foto/Logo:** 40 Robux | $3.000 CLP\n"
            "**Pack Completo:** 120 Robux | $8.000 CLP"
        ),
        inline=False
    )

    embed.add_field(
        name="🚓 Liverys",
        value=(
            "**Livery Simple:** 5/u Robux | $3.000 CLP\n"
            "**Livery Completa:** 10/u Robux | $6.000 CLP"
        ),
        inline=False
    )

    embed.add_field(
        name="🌐 Desarrollo Web",
        value=(
            "**Web Básica:** 200 Robux | $7.000 CLP\n"
            "**Web Profesional:** 300 Robux | $10.000 CLP"
        ),
        inline=False
    )

    embed.add_field(
        name="🎬 Edición de Video",
        value=(
            "**Video Básico:** 300 Robux | $5.000 CLP\n"
            "**Video Profesional:** 1.600 Robux | $10.000 CLP"
        ),
        inline=False
    )

    embed.set_footer(
        text="Everbox Studio © Todos los derechos reservados"
    )

    await interaction.response.send_message(embed=embed)

@bot.command(name="esperaticket")
async def esperaticket(ctx, cliente: discord.Member):

    await ctx.channel.edit(name="ticket-en-espera")

    embed = discord.Embed(
        title="⏳ | Ticket en Espera",
        description=(
            f"Gracias {cliente.mention} por contactar con **Everbox Studio**.\n\n"
            "Tu ticket ha sido colocado temporalmente en estado de **espera**.\n\n"
            "Nuestro equipo revisará tu solicitud lo antes posible.\n\n"
            "Agradecemos tu paciencia."
        ),
        color=discord.Color.orange()
    )

    embed.set_footer(
        text="Everbox Studio © Todos los derechos reservados"
    )

    await ctx.send(embed=embed)

import asyncio

@bot.command(name="cerrarticket")
@commands.has_permissions(manage_channels=True)
async def cerrarticket(ctx):

    embed = discord.Embed(
        title="🔒 | Cierre de Ticket",
        description=(
            "Este ticket ha sido marcado para ser cerrado.\n\n"
            "Gracias por contactar con **Everbox Studio**.\n\n"
            "Esperamos haber resuelto todas tus dudas o solicitudes.\n\n"
            "El canal será eliminado automáticamente en **10 segundos**."
        ),
        color=discord.Color.red()
    )

    embed.set_footer(
        text="Everbox Studio © Todos los derechos reservados"
    )

    await ctx.send(embed=embed)


@bot.command(name="ticketactivo")
@commands.has_permissions(manage_channels=True)
async def ticketactivo(ctx, usuario: discord.Member):

    try:
        # Cambiar nombre del canal
        await ctx.channel.edit(
            name=f"ticket-{usuario.name.lower()}"
        )

        embed = discord.Embed(
            title="🎫 | Ticket Tomado",
            description=(
                f"Hola {usuario.mention}, un miembro del equipo administrativo "
                f"ha tomado tu ticket.\n\n"
                "Por favor, ten paciencia mientras revisamos tu caso.\n\n"
                "Tu solicitud está siendo atendida por el equipo administrativo "
                "de Everbox Studio.\n\n"
                "Agradecemos tu paciencia y comprensión."
            ),
            color=discord.Color.green()
        )

        embed.add_field(
            name="👨‍💼 Staff Asignado",
            value=ctx.author.mention,
            inline=False
        )

        embed.set_footer(
            text="Everbox Studio © Todos los derechos reservados"
        )

        await ctx.send(
            content=usuario.mention,
            embed=embed
        )

    except Exception as e:
        await ctx.send(
            f"❌ Ocurrió un error: {e}"
        )

from discord.ui import View, Button

@bot.tree.command(
    name="postulaciones",
    description="Muestra las postulaciones al staff"
)
async def postulaciones(interaction: discord.Interaction):

    embed = discord.Embed(
        title="📋 | Postulaciones al Staff",
        description=(
            "Nos complace anunciar que las postulaciones para formar parte del equipo administrativo de Everbox Studio se encuentran oficialmente abiertas.\n\n"

            "Buscamos personas responsables, comprometidas y con ganas de contribuir al crecimiento de nuestra comunidad.\n\n"

            "**Requisitos:**\n"
            "• Buena ortografía y redacción.\n"
            "• Contar con madurez y responsabilidad.\n"
            "• Tener disponibilidad para atender tickets y usuarios.\n"
            "• Conocer las normativas del servidor.\n"
            "• Mantener una actitud respetuosa dentro y fuera de la comunidad.\n\n"

            "**¿Qué buscamos?**\n"
            "Personas activas, profesionales y comprometidas con ofrecer la mejor experiencia posible a nuestros clientes.\n\n"

            "¡Agradecemos tu interés en formar parte del equipo de Everbox Studio!"
        ),
        color=discord.Color.from_rgb(255, 255, 255)
    )

    embed.set_image(
        url="https://cdn.discordapp.com/attachments/1517939946219114657/1520463373198819389/Postulaciones.png?ex=6a41495d&is=6a3ff7dd&hm=a4eb7825438c11a0bb05ee94661f25676d83cfe1187ac04125e7bfa352cac9a1&"
    )

    embed.set_footer(
        text="Everbox Studio © Todos los derechos reservados"
    )

    # Botón
    view = View()

    boton = Button(
        label="Postula Aquí",
        url="https://docs.google.com/forms/d/e/1FAIpQLSe6oacPcluoI7rjeKjEfH36Y3BtIZPnjMSXTdADZBeFf6tzvw/viewform?usp=dialog"
    )

    view.add_item(boton)

    await interaction.response.send_message(
        embed=embed,
        view=view
    )

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

    try:
        synced = await bot.tree.sync()
        print(f"Se sincronizaron {len(synced)} comandos.")
    except Exception as e:
        print(f"Error al sincronizar: {e}")
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Se sincronizaron {len(synced)} comandos.")
    except Exception as e:
        print(e)
import os

bot.run(os.getenv("TOKEN"))
# prueba git